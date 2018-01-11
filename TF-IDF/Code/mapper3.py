#!/usr/bin/env python
# Rami Abou-Nassar
# Jonathan Azpur
# Third Mapper:
# Input from second reducer (previous reducer):
#   (word,filename,count    dw)
#
# Outputs:
#   (word,filename,count    dw)
#
# Here as explained from the previous reducer step the keys are sorted ascending, values are sorted descending
# The largest dw value corresponding to the first entry of each respective word corresponds to the dw value we
# need which we use as we print the output. Once again no storage is being used so we avoid any memory/buffer issues


import sys
import re

currWord = None
currCount = None
currFile = None
currWordCount =None
actualDW = 0

# input comes from STDIN (standard input)
for line in sys.stdin:
    
    #remove leading and trailing whitespace
    line = line.strip()
    
    #split line into different components
    wFwc, dw = line.split()
    
    #split into respective components
    word, fileName, wordCount = wFwc.split(',' ,2)
    
    # parse the line which will be used as print output
    parseLine = word + ',' + fileName + '\t' + wordCount
    
    #Start by setting the word and count
    if currWord == None:
        currWord = word
        
        #here we set the actual DW value for the respective word (this will not change till we hit a new word)
        actualDW = int(dw)     
        
        print(parseLine + ',' + str(actualDW))
     # same word simply print using the actual DW value stored from the intial entry
    elif currWord == word:        
        print(parseLine + ',' + str(actualDW))
    #hit a new word        
    else:
        #set to new word
        currWord = word       
        
        #new word means we have to once again set the proper DW value which will be used for all occurrences of this word
        actualDW = int(dw)
        
        print(parseLine + ',' + str(actualDW))    