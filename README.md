# MapReduce
MapReduce Projects:

(0) TF-IDF: write a MapReduce job for Hadoop to find the tf-idf of words in twenty books from The Project Gutenberg as text-file documents. I will use the stream library in Hadoop. A Docker container image distribution of Apache Hadoop for the project, using Hadoop commands I can copy files into (-put) and out of (get) HDFS, which I will need to run a MapReducer.

tf-idf(W,D)=tf(W,D)⋅idf(W) s.t. tf(W,D)=<#occurrences of W in D> ∧ idf(W)=ln(N/d(W))

Input: /Gutenberg directory in my HDFS with 20 books in .txt format
Output: for each word in each document, ⟨(word, document) , tf-idf score⟩

(1)