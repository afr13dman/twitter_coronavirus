#!/usr/bin/env python3

import matplotlib.pyplot as plt

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
    print(k,':',v)

# plot bar graphs
x_axis = [item[0] for item in items[:9]]
y_axis = [item[1] for item in items[:9]]
plt.bar(x_axis, y_axis)
plt.ylabel("Count")
if args.input_path == "reduced.country":
    plt.xlabel("Countries (Top 10)")
    plt.title("Number of Times" + args.key + "Appear in Tweets by Country")
elif args.input_path == "reduced.lang":
    plt.xlabel("Languages (Top 10)")
    plt.title("Number of Times" + args.key + "Appear in Tweets by Language")
plt.savefig('plot'+args.input_path+args.key, dpi='figure', format='PNG')
