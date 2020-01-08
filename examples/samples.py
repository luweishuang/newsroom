#! -*- coding: utf-8 -*-

from __future__ import print_function
import random

from newsroom import jsonl
from newsroom.analyze import Fragments


# Extraction Analysis
# Read file entry by entry:
# with open("../data/Newsroom/train.label.info.jsonl", "r+", encoding="utf8") as f:
#     for item in jsonlines.Reader(f):

with jsonl.open("../../data/Newsroom/train.label.info.jsonl") as train_file:
    for entry in train_file:
        print(entry["summary"], entry["text"])

        # Compute stats on random training example:
        summary, text = entry["summary"], entry["text"]
        fragments = Fragments("".join(summary), "\n".join(text))

        # Print paper metrics:
        print("Coverage:",    fragments.coverage())
        print("Density:",     fragments.density())
        print("Compression:", fragments.compression())

        # Extractive fragments oracle:
        print("List of extractive fragments:")
        print(fragments.strings())