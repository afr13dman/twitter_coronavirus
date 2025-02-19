#!/usr/bin/sh

for file in '/data/Twitter dataset/'geoTwitter22-*.zip; do
    #echo $file
    nohup ./src/map.py --input_path="$file" > nohup/$(basename "$file") &
done

for file in '/data/Twitter dataset/'tweets-2022*.zip; do
	#echo $file
    nohup ./src/map.py --input_path="$file" > nohup/$(basename "$file") &
done
