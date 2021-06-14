#!/usr/bin/env python
# Rami Abou-Nassar
# Jonathan Azpur
# Secoond Reducer:
# Input from second mapper (previous mapper):
#   (word,filename,count    1)
#
# Outputs:
#   (word,filename,count    dw)
#
# *********** Important****************************
# count is the tf value (ie the # of occurences of W in D)
# 
# dw (currCount) in this case is simply outputing an increasing value as it printse ach line from the 
# first occurence of the word, till a new occurence of word at which point dw gets reset and starts
# incrementing again. 
#
# This is done to avoid using any storage and running into any memory issues and allows the map/reducer
# to scale out. 
#
# The trick is in the final map step we simply will sort the keys ascending AMD VALUES DESCENDING
# Since the values are descending we simply need the first occurrence of this dw value (ie the largest value)
# which corresponds to all remaining dw values for the respective word. 

import sys

currWord  = None
currCount = 0     #represents dw value  
#currWordCount = 0

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
    #hit a new word        
    else:        
        #set to new word
        currWord = word
        
        #reset count
        currCount = count
        
        print(parseLine + '\t' + str(currCount))   
