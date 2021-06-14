#!/usr/bin/env python
# Rami Abou-Nassar
# Jonathan Azpur
# Third Reducer:
# Input from third mapper:
#   (word,filename,count    dw)
#
# Outputs:
#   (word,filename,     tfidf)

import sys
import math

currWord  = None
currCount = 0
word      = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    
    #split line into different components
    wF, wcC = line.split()
    
    #split into respective components
    word, fileName = wF.split(',',1 )
    wordCount, count = wcC.split(',', 1) 
    
    #calculate and print tf-idf(W,D) = tf(W,D) X idf(W)
    idf = math.log(float(20) / float(count))
    tf = (float(wordCount))
    tfidf = (tf * idf)
    
    print('%s\t%f' % (word + ',' + fileName, tfidf))