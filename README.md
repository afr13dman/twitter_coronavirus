# Coronavirus twitter analysis

The goal of this assignment was to scan all geotagged tweets sent in 2020 to monitor for the spread of the coronavirus on social media.

<!--
**Learning Objectives:**

1. work with large scale datasets
1. work with multilingual text
1. use the MapReduce divide-and-conquer paradigm to create parallel code
-->

## Background

**About the Data:**

The lambda server's `/data/Twitter dataset` folder contains all geotagged tweets that were sent in 2020.
That is, tweets that includes the user location from where it was sent.
In total, the dataset includes about 1.1 billion tweets.

The tweets for each day are stored in a zip file `geoTwitterYY-MM-DD.zip`, 
and inside this zip file are 24 text files, one for each hour of the day.
Each text file contains a single tweet per line in JSON format, a popular format for storing data that is closely related to python dictionaries.

## The Project and Programming Steps

I used a [MapReduce](https://en.wikipedia.org/wiki/MapReduce) procedure to analyze these tweets.

The file `map.py` processed all of the tweets within each inputed zip file while tracking the usage of of the hashtags on both a language and country level.
For each day it outputs two files (a `.lang` and a `.country`) that contain a dictionary of dictionaries.
The outermost dictionary has hashtags as the keys, and the innermost dictionary has languages or country as the keys, respectively. 

Since there are 366 days, or files, worth of data, I created a shell script to loop over each in the dataset and run the map.py command on that file.
```
for file in '/data/Twitter dataset/'geoTwitter20-*.zip; do
	$(./src/map.py --input_path="$file") &
done
```

Then, I merged the outputs generated by the `map.py` file to combine all of the .lang files into a single file, and all of the .country files into a different file.
```
$ ./src/reduce.py --input_paths outputs/geoTwitter*.lang --output_path=reduced.lang
```
and
```
$ ./src/reduce.py --input_paths outputs/geoTwitter*.country --output_path=reduced.country
```

Next, in the `visualize.py` file, I used the matplotlib library to generate bar graphs of the results and store them as a png file.
For each graph, the horizontal axis was the top 10 keys of the input file, and the vertical axis were the values of the input file.
The results were sorted from low to high.

I generated four plots using the following command four times:
```
$ ./src/visualize.py --input_path=PATH --key=HASHTAG
```
where `--input_path` equaled either the country or lang files created in the reduce phase,
and the `--key` was set to either `#coronavirus` or `#코로나바이러스`.

## Plots

Tweets Using #coronavirus by Country

![](https://github.com/afr13dman/twitter_coronavirus/blob/master/country%23coronavirus.png)
<img src='country#coronavirus.png' width=100% /> 

Tweets Using #coronavirus by Language

<img src="lang#coronavirus.png" width=100% /> 

Tweets Using #코로나바이러스 by Country

<img src='country#코로나바이러스.png' width=100% /> 

Tweets Using #코로나바이러스 by Language

<img src='lang#코로나바이러스'.png width=100% /> 

## Alternative Reduce

In addition to the normal map reduce, I did an alternative reduce process where I took as input on the command line a list of hashtags,
and output a line plot where:
1. There is one line per input hashtag.
1. The x-axis is the day of the year.
1. The y-axis is the number of tweets that use that hashtag during the year.

The `alternative_reduce.py` file combines parts of `reduce.py` and `visualize.py`.
First, the file scans through the data in the `outputs` folder to construct a dataset from which to plot the data.

I plotted the frequency of tweets including `#flu`, `#cough`, and `#sick` during 2020.

<img src=year_hashtag_graph.png width=100% />
