#!/usr/bin/env python3

# This file should take as input on the command line a list of hashtags, and output a line plot where:
# 1. There is one line per input hashtag.
# 2. The x-axis is the day of the year.
# 3. The y-axis is the number of tweets that use that hashtag during the year.

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_paths',nargs='+',required=True)  # can i have this as an input path or am i supposed to hard code so that it looks at the outputs folder that end in LANG (we are doing that)
parser.add_argument('--keys',nargs='+',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
import re
import matplotlib.pyplot as plt

# load each of the input paths
total = defaultdict(lambda: Counter())
for path in args.input_paths:
    date = re.search(r'\d{2}-\d{2}-\d{2}', path).group()[3:]
    with open(path) as f:
        tmp = json.load(f)
        for k in args.keys:
            counts = 0
            if k in tmp:
                for i in tmp[k]:
                    counts += tmp[k][i]
            total[k][date] = counts

# creates readable dictionary
data = json.dumps(total)
data = json.loads(data)

# normalize the data by the total values
if args.percent:
    for k in data[args.key]:
        data[args.key][k] /= data['_all'][k]

# plot graph
for k in args.keys:
    items = list(data[k].items())
    x_axis = [item[0] for item in items]
    y_axis = [item[1] for item in items]
    plt.plot(x_axis, y_axis, label = k)
plt.legend()
plt.ylabel("Count")
plt.xlabel("Day of the Year in 2020")
plt.title("Number of Tweets Using COVID-19 Related Hashtags in 2020")
plt.savefig("test_alt_reduce7.png")
