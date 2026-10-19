#!/usr/bin/env python3
"""portfolio-activity.py : writes /var/www/portfolio/shared/activity.json

Reads the PUBLIC GitHub events of the account (no token, public data only) and keeps
the latest commits of an allowlist of repositories, so the "Now" page can show what
changed recently without being rebuilt by hand. Run by portfolio-activity.timer.

Only repositories listed in ALLOWED_REPOS can appear: a public repository that is not
meant to be presented on the portfolio never shows up. The page renders the text with
textContent, never as HTML.
"""
import json
import os
import re
import sys
import tempfile
import urllib.request
from datetime import datetime, timezone

USER = "Bastien-Gaffet"
OUT = os.environ.get("ACTIVITY_OUT", "/var/www/portfolio/shared/activity.json")
ALLOWED_REPOS = {
    "portfolio-bastien-gaffet", "equiliz", "krino", "kairoo", "tourny", "glacify",
    "PrepaTrack", "Robot_J4", "cdp-scraper", "toolbox-py",
}
MAX_ITEMS = 8


def fetch(url):
    req = urllib.request.Request(url, headers={
        "User-Agent": "bastiengaffet.fr-activity/1.0",
        "Accept": "application/vnd.github+json",
    })
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.load(r)


def clean(msg):
    first = (msg or "").strip().split("\n")[0]
    first = re.sub(r"\s+", " ", first)
    return first[:110]


def main():
    events = fetch(f"https://api.github.com/users/{USER}/events/public?per_page=100")
    items = []
    for ev in events:
        if ev.get("type") != "PushEvent":
            continue
        repo = ev["repo"]["name"].split("/", 1)[-1]
        if repo not in ALLOWED_REPOS:
            continue
        when = ev.get("created_at")
        for c in reversed(ev["payload"].get("commits", [])):
            msg = clean(c.get("message"))
            if not msg or msg.lower().startswith("merge"):
                continue
            items.append({
                "repo": repo,
                "message": msg,
                "date": when,
                "url": f"https://github.com/{USER}/{repo}/commit/{c['sha']}",
            })
    items.sort(key=lambda i: i["date"], reverse=True)
    data = {
        "generated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source": f"https://github.com/{USER}",
        "items": items[:MAX_ITEMS],
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(OUT), suffix=".tmp")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    os.chmod(tmp, 0o644)
    os.replace(tmp, OUT)  # atomic: the old file stays if anything above fails
    print(f"wrote {len(data['items'])} items")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # keep the previous file on any network or API error
        print("activity update failed:", e, file=sys.stderr)
        sys.exit(1)
