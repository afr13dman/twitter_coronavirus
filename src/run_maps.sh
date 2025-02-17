#!/usr/bin/sh

for file in '/data/Twitter dataset/'geoTwitter22-*.zip; do
	$(./src/map.py --input_path="$file") &
done
