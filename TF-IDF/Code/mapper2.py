#!/usr/bin/env python
# Rami Abou-Nassar
# Jonathan Azpur
# Second Mapper:
# Input from wordReduce (previous reducer):
#   (word,filename    tf(W,D))
#   (Note tf(W,D) is simply count in the code)
#
# Outputs:
#   (word,filename,count    1)
#
# This is used as input for the second reducer
 
import sys
import re

# input comes from STDIN (standard input)
for line in sys.stdin:
    
    #remove leading and trailing whitespace
    line = line.strip()
    
    #split line into different components
    key, count = line.split('\t', 1)
    
    #split futher key into corresponding word and document components
    word, fileName = key.split(',', 1)
    
    #print word,fileName,count + '\t' + 1 which will be input for the second reducer
    print('%s\t%s' % (word + ',' + fileName + ',' + count, 1))
    