#!/bin/bash
# push-from-pc.sh : publish the working tree of this repository to bastiengaffet.fr right now,
# without going through GitHub. Run from the repository root:  bash deploy/push-from-pc.sh
# Only the files of deploy/rsync-allowlist are published; the release is atomic and reversible
# (ssh root@72.62.190.7 'sudo -u portfolio portfolio-deploy --rollback').
set -euo pipefail
VPS=root@72.62.190.7
TAR="${TMPDIR:-/tmp}/portfolio-push.tar.gz"
tar --force-local --exclude=.git --exclude=old --exclude=node_modules -czf "$TAR" .
scp -q "$TAR" "$VPS:/tmp/portfolio-push.tar.gz"
ssh "$VPS" 'chmod 644 /tmp/portfolio-push.tar.gz && sudo -u portfolio /usr/local/bin/portfolio-deploy --from-tar /tmp/portfolio-push.tar.gz && rm -f /tmp/portfolio-push.tar.gz'
echo "published: https://bastiengaffet.fr/"
