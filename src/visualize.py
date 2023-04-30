#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib.pyplot as plt

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
for k,v in items:
    pass
    # print(k,':',v)

# set up font that works with chinese characters
font_name = "STKaiti"
plt.rcParams['font.family']=font_name
plt.rcParams['axes.unicode_minus']=False

# plot bar graphs
items = items[0:10]
items.reverse()

x_axis = [item[0] for item in items]
y_axis = [item[1] for item in items]
x_axis2 = range(len(x_axis))

plt.bar(x_axis2, y_axis)
plt.xticks(x_axis2, x_axis)
plt.ylabel("Count")

if args.input_path == "reduced.country":
    plt.xlabel("Countries (Top 10)")
    plt.title("Number of Times " + args.key + " Appears in Tweets from 2020 by Country")
    plt.savefig('country' + args.key + '.png')
elif args.input_path == "reduced.lang":
    plt.xlabel("Languages (Top 10)")
    plt.title("Number of Times " + args.key + " Appears in Tweets from 2020 by Language")
    plt.savefig('lang' + args.key + '.png')
# install font that works with asian characters for title issue or just put it the readme
