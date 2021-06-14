#!/usr/bin/env python
# Jonathan Azpur
# Frst mapper simply outputs (key \t 1) = (word,filename     1)
# This is used as input for WordReduce which will aggregate and compute the # of occurences of W in D

import sys
import re
import os

# input comes from STDIN (standard input)
for line in sys.stdin:
    # get the file name of the book
    fName = os.environ['mapreduce_map_input_file']

    # remove leading and trailing whitespace
    line = line.strip()

    # split the line into words
    words = filter(None, re.split('[\W+_]', line))

    # write out word paired with count of 1
    for word in words:
        # write the results to STDOUT (standard output);
        # tab-delimited; the word + the file name as keys and as the value a count which is 1 for all
        word = re.sub('[^a-zA-Z0-9]+', '', word.lower())
        print('%s\t%s' % (word + ',' + fName , 1))

