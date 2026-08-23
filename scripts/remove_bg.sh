#!/usr/bin/env bash
# Remove a solid (near-white) background from an image and resize it,
# preserving aspect ratio, then write the result to a PNG.
#
# usage: remove_bg.sh <input> <size> [output]
#   input   image to process
#   size    max width/height in pixels (e.g. 256)
#   output  destination PNG (default: <input>_nobg_<size>.png)

set -euo pipefail

usage() {
	grep '^#' "$0" | cut -c 3- | sed -n '2,7p'
	exit 1
}

[[ $# -ge 2 && $# -le 3 ]] || usage

input=$1
size=$2
output=${3:-"${input%.*}_nobg_${size}.png"}

convert "$input" -alpha set -fuzz 15% -transparent white \
	-resize "${size}x${size}" \
	"$output"

echo "wrote $output"
