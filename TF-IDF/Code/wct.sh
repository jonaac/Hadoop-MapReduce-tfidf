#!/bin/bash

WCDIR=/home/tfidf/Code
STREAMINGJAR=share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar

bin/hadoop jar $STREAMINGJAR                        \
    -files   $WCDIR/wordMap.py,$WCDIR/wordReduce.py \
    -mapper  $WCDIR/wordMap.py                      \
    -reducer $WCDIR/wordReduce.py                   \
    -input   Gutenberg/'*'                          \
    -output  Output1

printf "\nMAPPER-REDUCER #2\n\n"
bin/hadoop jar $STREAMINGJAR                        \
    -files   $WCDIR/mapper2.py,$WCDIR/reducer2.py 	\
    -mapper  $WCDIR/mapper2.py						\
    -reducer $WCDIR/reducer2.py                     \
    -input   Output1/'*'							\
    -output  Output2


printf "\nMAPPER-REDUCER #3\n\n"
bin/hadoop jar $STREAMINGJAR                                                                            \
    -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator   \
    -D stream.num.map.output.key.fields=2                                                               \
    -D mapreduce.partition.keycomparator.options="-k1,1 -k2,2"                                          \
    -D mapreduce.partition.keypartitioner.options="-k1,1"                                               \
    -files   $WCDIR/mapper3.py,$WCDIR/reducer3.py                                                       \
    -mapper  $WCDIR/mapper3.py                                                                          \
    -reducer $WCDIR/reducer3.py                                                                         \
    -input   Output2/'*'                                                                                \
    -output  Output3
