# TF-IDF with Docker, Hadoop, and MapReduce:

I develop a MapReduce job for Hadoop to find the <a href="https://en.wikipedia.org/wiki/Tf%E2%80%93idf">tf-idf</a> of words in twenty books from The Project Gutenberg as text-file documents. I will be using a Docker container with an image distribution of Apache Hadoop for this project.

My goal is to develop an app capable of scaling to massive datasets (for example, 10+ million books). To do so, I have to avoid any unnecessary caching of key-value pairs and have a solution where mappers and reducers only have to look at one key-value pair at a time to generate their outputs. Therefore, I need to get the #docs (# of docs each word appears on) into the key-value stream so that it is available per word as necessary.

## Docker and Hadoop set up

I install Docker and once that's done I install the Hadoop image sequenceiq/hadoop-docker:2.7.1:
```
docker run -it --name Hadoop sequenceiq/hadoop-docker:2.7.1 /etc/bootstrap.sh -bash
```
I create a directory for my project:
```
docker cp tfidf Hadoop:/home/tfidf
```
I place the files I will be working with in Hadoop's HDFS filesystem:
```
cd /usr/local/hadoop
bin/hadoop fs -put /home/tfidf/Gutenberg Gutenberg
```
I created a <a href="https://github.com/jonaac/Hadoop-MapReduce-tfidf/blob/master/TF-IDF/Code/wct.sh">bash script</a> to execute all my code in Hadoop.

## First Map-Reducer:
For the first Map-Reducer I calculate the tf value for each word in each document"
```
<b>Input Mapper:</b>: 
/Gutenberg directory in my HDFS with 20 books in .txt format

<b>Output Mapper:</b>: 
⟨(word, document) , 1⟩

<b>Input Reducer:</b>: 
⟨(word, document) , 1⟩

<b>Output Reducer</b>: 
⟨(word, document) , tf score⟩
```

## Second Map-Reducer:
<b>Input Mapper</b>:
⟨(word, document) , tf⟩

<b>Output Mapper</b>:
⟨(word, document,tf) , 1⟩

<b>Input Reducer</b>:
⟨(word,document,tf) , 1⟩

<b>Output Reducer</b>:
⟨(word, document,tf) , dw⟩ s.t. dw is the number 

<b>dw</b> is a counter that will end up returning for each word the # of documents the word appears on. So let's say the word 'Hello' appears in doc1, doc2, doc5 and doc8. The second MapReduce will return:

⟨('Hello',doc1,tf) , 1⟩
⟨('Hello',doc2,tf) , 2⟩
⟨('Hello',doc5,tf) , 3⟩
⟨('Hello',doc8,tf) , 4⟩

So I have now the tf for each word and the # of books/documents each word appears in. This is done to avoid using any storage and running into any memory issues and allows the map/reducer to scale out. 

## Third Map-Reducer:
<b>Input Mapper</b>:
⟨(word, document,tf) , dw⟩ -> (word, document,tf) is sorted ascending and dw is sorted descending

<b>Output Mapper</b>:
⟨(word, document,tf) , dw⟩

<b>Input Reducer</b>:
⟨(word, document,tf) , dw⟩

<b>Output Reducer</b>:
⟨(word, document) , tf-idf⟩

In the Final Map-Reduce the keys are sorted ascending, values are sorted descending The largest dw value corresponding to the first entry of each respective word corresponds to the dw value I need which I use as I print the output. Once again no storage is being used so I avoid any memory/buffer issues.
