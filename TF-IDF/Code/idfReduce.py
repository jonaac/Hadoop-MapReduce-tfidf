#!/usr/bin/env python
# Rami Abou-Nassar
# Jonathan Azpur

import sys

currWord  = None
currCount = 0     #represents dw value  

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    #parse the line into its different components
    key, count = line.split('\t', 1)

    #furhter parse value into seperate word, fileName and wordCount components
    word, fileName, wordCount = key.split(',',2)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number,
        # so silently ignore this line
        continue

    # parse the line which will be used as print output
    parseLine = word + ',' + fileName + ',' + wordCount

    #Start by setting the word and count
    if currWord == None:
        currWord = word
        currCount = count
        print(parseLine + '\t' + str(currCount))
    # same word means it appeared in another book so we must increment the conuter which represents the dw value
    elif currWord == word:
        currCount += count
        print(parseLine + '\t' + str(currCount))
    else:
        #set to new word
        currWord = word
        
        #reset count
        currCount = count
        
        print(parseLine + '\t' + str(currCount))
