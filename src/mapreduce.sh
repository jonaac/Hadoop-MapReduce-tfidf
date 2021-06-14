#!/bin/bash

WCDIR=/home/tfidf/Code
STREAMINGJAR=share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar

bin/hadoop jar $STREAMINGJAR                                            \
    -files   $WCDIR/MapReduce1/mapper.py,$WCDIR/MapReduce1/reducer.py   \
    -mapper  $WCDIR/MapReduce1/mapper1.py                               \
    -reducer $WCDIR/MapReduce1/reducer1.py                              \
    -input   Gutenberg/'*'                                              \
    -output  Output1

printf "\nMAPPER-REDUCER #2\n\n"
bin/hadoop jar $STREAMINGJAR                                            \
    -files   $WCDIR/MapReduce2/mapper.py,$WCDIR/MapReduce2/reducer.py   \
    -mapper  $WCDIR/MapReduce2/mapper2.py                               \
    -reducer $WCDIR/MapReduce2/reducer2.py                              \
    -input   Output1/'*'                                                \
    -output  Output2


printf "\nMAPPER-REDUCER #3\n\n"
bin/hadoop jar $STREAMINGJAR                                                                            \
    -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator   \
    -D stream.num.map.output.key.fields=2                                                               \
    -D mapreduce.partition.keycomparator.options="-k1,1 -k2,2"                                          \
    -D mapreduce.partition.keypartitioner.options="-k1,1"                                               \
    -files   $WCDIR/MapReduce3/mapper.py,$WCDIR/MapReduce3/reducer.py                                   \
    -mapper  $WCDIR/MapReduce3/mapper3.py                                                               \
    -reducer $WCDIR/MapReduce3/reducer3.py                                                              \
    -input   Output2/'*'                                                                                \
    -output  Output3
