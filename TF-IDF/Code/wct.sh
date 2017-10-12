#!/bin/bash

WCDIR=/home/tfidf/Code
STREAMINGJAR=share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar

bin/hadoop jar $STREAMINGJAR                        \
    -files   $WCDIR/wordMap.py,$WCDIR/wordReduce.py \
    -mapper  $WCDIR/wordMap.py                      \
    -reducer $WCDIR/wordReduce.py                   \
    -input   Gutenberg/'*'                          \
    -output  Gutenberg-out

