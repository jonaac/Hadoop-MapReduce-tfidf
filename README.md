# MapReduce Project:

I develop a MapReduce job for Hadoop to find the tf-idf of words in twenty books from The Project Gutenberg as text-file documents. 
I use the stream library in Hadoop.
A Docker container image distribution of Apache Hadoop for the project, using Hadoop commands so I can copy files into (-put) and out of (get) HDFS, which I will need to run a MapReducer.

tf-idf(W,D)=tf(W,D)⋅idf(W) s.t. tf(W,D)=<occurrences of W in D> ∧ idf(W)=ln(N/d(W))

## First Map-Reducer:
<b>Input Mapper:</b>: 
/Gutenberg directory in my HDFS with 20 books in .txt format

<b>Output Mapper:</b>: 
⟨(word, document) , 1⟩

<b>Input Reducer:</b>: 
⟨(word, document) , 1⟩

<b>Output Reducer</b>: 
⟨(word, document) , tf-idf score⟩

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
