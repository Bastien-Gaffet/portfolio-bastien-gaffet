#!/bin/bash
# portfolio-deploy.sh : atomic, pull-based deployment of bastiengaffet.fr on the VPS.
#
# Runs as the unprivileged user "portfolio" (see systemd/portfolio-deploy.service).
# It never needs a secret: the repository is public and is only read.
#
#   /opt/portfolio-src                  clone of the GitHub repository
#   /var/www/portfolio/releases/<id>    one directory per deployment (allowlist only)
#   /var/www/portfolio/current          symlink to the live release (nginx root)
#   /var/www/portfolio/shared           data written by timers (activity.json)
#
# Usage:  portfolio-deploy.sh [branch]      (default: main)
#         FORCE=1 portfolio-deploy.sh       redeploy even if nothing changed
#         portfolio-deploy.sh --rollback    go back to the previous release
#         portfolio-deploy.sh --from-tar f  deploy a tarball of a working tree (see push-from-pc.sh)
set -euo pipefail
cd /tmp

SRC=/opt/portfolio-src
BASE=/var/www/portfolio
KEEP=6

if [ "${1:-}" = "--rollback" ]; then
  cur=$(readlink -f "$BASE/current")
  prev=$(ls -1d "$BASE"/releases/*/ | sed 's:/$::' | sort | grep -B1 -x "$cur" | head -n1 || true)
  if [ -z "$prev" ] || [ "$prev" = "$cur" ]; then echo "no previous release"; exit 1; fi
  ln -sfn "$prev" "$BASE/current.new" && mv -T "$BASE/current.new" "$BASE/current"
  echo "rolled back to $prev"; exit 0
fi

if [ "${1:-}" = "--from-tar" ]; then
  # manual deployment of a working tree (used before a change is merged into main)
  TARFILE="${2:?usage: portfolio-deploy --from-tar file.tar.gz}"
  NEW="manual-$(date -u +%Y%m%d%H%M%S)"
  SHORT="manual"
  FROM_TAR=1
else
  FROM_TAR=0
  BRANCH="${1:-main}"
  cd "$SRC"
  git fetch --quiet origin "$BRANCH"
  NEW=$(git rev-parse "origin/$BRANCH")
  SHORT="${NEW:0:7}"
  CUR=$(cat "$BASE/.deployed-commit" 2>/dev/null || true)
  if [ "$NEW" = "$CUR" ] && [ "${FORCE:-0}" != "1" ]; then exit 0; fi
fi

REL="$BASE/releases/$(date -u +%Y%m%d-%H%M%S)-$SHORT"
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT
mkdir -p "$REL"

if [ "$FROM_TAR" = "1" ]; then tar -xzf "$TARFILE" -C "$TMP"; else git archive "$NEW" | tar -x -C "$TMP"; fi
rsync -a --prune-empty-dirs --filter=". $TMP/deploy/rsync-allowlist" "$TMP"/ "$REL"/

# sanity checks before going live
[ -s "$REL/index.html" ] || { echo "index.html missing, abort"; rm -rf "$REL"; exit 1; }
[ "$(find "$REL" -type f | wc -l)" -ge 20 ] || { echo "too few files, abort"; rm -rf "$REL"; exit 1; }
if find "$REL" -type f \( -name '*.md' -o -name '*.py' -o -name '*.sh' -o -name '*.toml' -o -name '*.zip' -o -name '*.webm' -o -name '.env*' \) | grep -q .; then
  echo "forbidden file type in release, abort"; rm -rf "$REL"; exit 1
fi

# normal permissions: owner writes, everybody reads, nobody writes the web root
find "$REL" -type d -exec chmod 755 {} +
find "$REL" -type f -exec chmod 644 {} +

ln -sfn "$REL" "$BASE/current.new"
mv -T "$BASE/current.new" "$BASE/current"
echo "$NEW" > "$BASE/.deployed-commit"
echo "deployed $NEW to $REL"

# keep the last $KEEP releases
ls -1d "$BASE"/releases/*/ | sed 's:/$::' | sort | head -n -"$KEEP" | xargs -r rm -rf
