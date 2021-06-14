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
I created a <a href="https://github.com/jonaac/Hadoop-MapReduce-tfidf/tree/master/src">bash script</a> to execute all my code in Hadoop.

## First MapReduce process:
For the first MapReducer I calculate the tf value for each word in each document"
```
Input Mapper: /Gutenberg files in .txt
Output Mapper: ⟨(word, document) , 1⟩
Input Reducer: ⟨(word, document) , 1⟩
Output Reducer: ⟨(word, document) , tf⟩
```

## Second MapReduce process:
For the second MapReduce process I calculate a <b>dw</b> counter. <b>dw</b> is a counter whose last iteration for each word will be the # of documents the word appears on. So let's say the word 'Hello' appears in doc1, doc2, doc5 and doc8. The second MapReduce will return:

⟨('Hello',doc1,tf) , dw = 1⟩
⟨('Hello',doc2,tf) , dw = 2⟩
⟨('Hello',doc5,tf) , dw = 3⟩
⟨('Hello',doc8,tf) , dw = 4⟩

So I have now the tf for each word and the # of books/documents each word appears in. This is done to avoid using any storage and running into any memory issues and allows the map/reducer to scale out. 

```
Input Mapper: ⟨(word, document) , tf⟩
Output Mapper: ⟨(word, document,tf) , 1⟩
Input Reducer: ⟨(word,document,tf) , 1⟩
Output Reducer: ⟨(word, document,tf) , dw⟩
```

## Third MapReduce process:
For the third and last MapReduce process the input will have the keys are sorted ascending, and the values are sorted descending. The largest dw value corresponds to the #docs value for each word that I need to calculate the tf-idf. Once again no storage is being used so I avoid any memory/buffer issues.
```
Input Mapper: ⟨(word, document,tf) , dw⟩ -> key is sorted ascending and (dw) is sorted descending
Output Mapper: ⟨(word, document,tf) , #docs⟩
Input Reducer: ⟨(word, document,tf) , #docs⟩
Output Reducer: ⟨(word, document,tf) , tf-idf⟩
```
