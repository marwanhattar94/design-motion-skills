#!/bin/sh
# Builds one .zip per skill in dist/ for uploading to claude.ai (Settings > Capabilities > Skills).
set -e
cd "$(dirname "$0")/.."
rm -rf dist && mkdir dist
for d in skills/*/; do n=$(basename "$d"); (cd skills && zip -qr "../dist/$n.zip" "$n"); done
echo "Built $(ls dist | wc -l) zips in dist/"
