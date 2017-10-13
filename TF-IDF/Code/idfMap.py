#!/usr/bin/env python
# Rami Abou-Nassar
# Jonathan Azpur
# First Reducer

import sys
import re

#input comes from STDIN (standard input)
for line in sys.stdin:

	#remove leading and trailing whitespace
	line = line.strip()

	#split line into different components
	key, count = line.split('\t', 1)

	#split futher key into corresponding word and document name
	word, filename = key.split(',', 1)

	#print word [] doc, count to second reducer
	print('%s\t%s' % (word, filename + ',' + count))
	
	
