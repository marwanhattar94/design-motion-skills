#!/bin/sh
# Re-clone each upstream repo into .upstream/ and print what changed; copy changes in by hand or re-run the build.
set -e
cd "$(dirname "$0")/.."
mkdir -p .upstream
cut -d'|' -f2 .sources | sort -u | while read s; do
  d=".upstream/$(echo "$s" | tr / _)"
  if [ -d "$d" ]; then git -C "$d" pull -q; else git clone -q --depth 1 "https://github.com/$s.git" "$d"; fi
  echo "$s @ $(git -C "$d" log -1 --format='%h %cs')"
done
