#!/usr/bin/env python
# Rami Abou-Nassar
# Jonathan Azpur

import sys
import math

currWord  = None
currCount = 0
word      = None
currFile  = None
dwcounter = 0
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input
    word, fc = line.split('\t', 1)
    file, count = fc.split(',', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number,
        # so silently ignore this line
        continue

    if currWord == None:
        currWord = word
        currFile = file
        dwcounter += 1
    elif currWord != word:
        # ------- calculate IDF ---------- #
        idf = math.log(float(20) / float(dwcounter))
        # -------    print IDF  ---------- #
        print('%s\t%s' % (currWord, idf))
        currFile = file
        currWord = word
        dwcounter = 1
    else:
        dwcounter += 1

idf = math.log(float(20) / float(dwcounter))
print('%s\t%s' % (currWord, idf))