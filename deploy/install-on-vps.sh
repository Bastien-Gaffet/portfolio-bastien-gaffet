#!/bin/bash
# install-on-vps.sh : one-time, idempotent setup of the portfolio hosting on the VPS (run as root).
# Expects the repo's deploy/ folder uploaded to /tmp/portfolio-deploy-files and, for the very
# first release, a tarball of the working tree at /tmp/portfolio-initial.tar.gz.
#
# Safe by construction: everything is backed up first, nginx is tested before reload and the
# previous configuration is restored automatically if the new one fails the checks.
set -euo pipefail

D=/tmp/portfolio-deploy-files
BK=/var/backups/portfolio-hosting-$(date +%Y%m%d-%H%M%S)
BASE=/var/www/portfolio
mkdir -p "$BK"

echo "== 1. backups in $BK"
cp -a /etc/nginx/sites-enabled/bastiengaffet.conf "$BK/bastiengaffet-enabled.conf"
cp -a /etc/nginx/sites-available/bastiengaffet.conf "$BK/bastiengaffet-available.conf" 2>/dev/null || true
tar -czf "$BK/old-webroot.tar.gz" -C /var/www portfolio-bastien-20261019
cp -a /etc/nginx/nginx.conf "$BK/nginx.conf"

echo "== 2. user and directories"
id portfolio >/dev/null 2>&1 || useradd --system --home-dir /var/lib/portfolio --create-home --shell /usr/sbin/nologin portfolio
mkdir -p "$BASE/releases" "$BASE/shared" /opt/portfolio-src
chown -R portfolio:portfolio "$BASE" /opt/portfolio-src
chmod 755 "$BASE" "$BASE/releases" "$BASE/shared"

echo "== 3. scripts and units"
install -m 755 "$D/portfolio-deploy.sh" /usr/local/bin/portfolio-deploy
install -m 755 "$D/portfolio-activity.py" /usr/local/bin/portfolio-activity
install -m 644 "$D"/systemd/*.service "$D"/systemd/*.timer /etc/systemd/system/
install -m 644 "$D/nginx/portfolio-security-headers.conf" /etc/nginx/snippets/portfolio-security-headers.conf
systemctl daemon-reload

echo "== 4. repository clone (public, read only)"
if [ ! -d /opt/portfolio-src/.git ]; then
  sudo -u portfolio git clone --quiet https://github.com/Bastien-Gaffet/portfolio-bastien-gaffet.git /opt/portfolio-src
fi

echo "== 5. first release from the uploaded working tree"
if [ -f /tmp/portfolio-initial.tar.gz ]; then
  REL="$BASE/releases/$(date -u +%Y%m%d-%H%M%S)-initial"
  TMP=$(mktemp -d)
  tar -xzf /tmp/portfolio-initial.tar.gz -C "$TMP"
  mkdir -p "$REL"
  rsync -a --prune-empty-dirs --filter=". $TMP/deploy/rsync-allowlist" "$TMP"/ "$REL"/
  [ -s "$REL/index.html" ] || { echo "index.html missing in release"; exit 1; }
  find "$REL" -type d -exec chmod 755 {} +
  find "$REL" -type f -exec chmod 644 {} +
  chown -R portfolio:portfolio "$REL"
  if find "$REL" -type f \( -name '*.md' -o -name '*.py' -o -name '*.sh' -o -name '*.toml' -o -name '*.zip' -o -name '*.webm' -o -name '.env*' \) | grep -q .; then
    echo "forbidden file type in release"; exit 1
  fi
  echo "release content:"; (cd "$REL" && find . -type f | sort | sed 's/^/  /')
  ln -sfn "$REL" "$BASE/current"
  chown -h portfolio:portfolio "$BASE/current"
  rm -rf "$TMP"
fi

echo "== 6. activity feed (first run)"
sudo -u portfolio /usr/bin/python3 /usr/local/bin/portfolio-activity || echo "activity: first run failed (will retry from the timer)"

echo "== 7. nginx"
# capture status codes of the apps that must not change
check() { curl -sk -o /dev/null -w "%{http_code}" --resolve bastiengaffet.fr:443:127.0.0.1 "https://bastiengaffet.fr$1"; }
AV=$(grep -o '/visio-[A-Za-z0-9]*/' /etc/nginx/snippets/auto-visio.conf | head -1)
BEFORE="drive=$(check /drive/) cours=$(check /cours/) visio=$(check "$AV")"
echo "before: $BEFORE"
install -m 644 "$D/nginx/bastiengaffet.conf" /etc/nginx/sites-available/bastiengaffet.conf
rm -f /etc/nginx/sites-enabled/bastiengaffet.conf
ln -s /etc/nginx/sites-available/bastiengaffet.conf /etc/nginx/sites-enabled/bastiengaffet.conf
rollback() {
  echo "!! rollback"
  rm -f /etc/nginx/sites-enabled/bastiengaffet.conf
  cp -a "$BK/bastiengaffet-enabled.conf" /etc/nginx/sites-enabled/bastiengaffet.conf
  nginx -t && systemctl reload nginx
  exit 1
}
nginx -t || rollback
systemctl reload nginx
sleep 1
AFTER="drive=$(check /drive/) cours=$(check /cours/) visio=$(check "$AV")"
echo "after:  $AFTER"
[ "$BEFORE" = "$AFTER" ] || { echo "drive/auto-visio status changed"; rollback; }
[ "$(check /)" = "200" ] || { echo "home is not 200"; rollback; }
echo "== done. Deploy timer is NOT enabled yet (it deploys the main branch)."
