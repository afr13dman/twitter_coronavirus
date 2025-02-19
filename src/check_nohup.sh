#!/usr/bin/sh

for file in nohup/*.zip; do
    # Counts the number of lines in the output file
    line_count=$(cat "$file" | wc -l)
    # echo $line_count

    # Check if line count is not equal to 26
    if [ "$line_count" != 26 ]; then
        echo "$file" >> nohup/days_with_issues 
    fi
done
