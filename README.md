# MapReduce Project:

TF-IDF: write a MapReduce job for Hadoop to find the tf-idf of words in twenty books from The Project Gutenberg as text-file documents. I will use the stream library in Hadoop. A Docker container image distribution of Apache Hadoop for the project, using Hadoop commands I can copy files into (-put) and out of (get) HDFS, which I will need to run a MapReducer.

tf-idf(W,D)=tf(W,D)⋅idf(W) s.t. tf(W,D)=<occurrences of W in D> ∧ idf(W)=ln(N/d(W))

## Second Reducer:
Input: /Gutenberg directory in my HDFS with 20 books in .txt format
Output: for each word in each document, ⟨(word, document) , tf-idf score⟩

## Second Reducer:
Input from second mapper (previous mapper):
(word,filename,count    1)

Outputs:
(word,filename,count    dw)

*********** Important****************************
count is the tf value (ie the  of occurences of W in D)

dw (currCount) in this case is simply outputing an increasing value as it printse ach line from the 
first occurence of the word, till a new occurence of word at which point dw gets reset and starts
incrementing again. 

This is done to avoid using any storage and running into any memory issues and allows the map/reducer
to scale out. 

The trick is in the final map step we simply will sort the keys ascending AMD VALUES DESCENDING
Since the values are descending we simply need the first occurrence of this dw value (ie the largest value)
which corresponds to all remaining dw values for the respective word. 


## Third Mapper:
Input from second reducer (previous reducer):
(word,filename,count    dw)

Outputs:
(word,filename,count    dw)

Here as explained from the previous reducer step the keys are sorted ascending, values are sorted descending
The largest dw value corresponding to the first entry of each respective word corresponds to the dw value we
need which we use as we print the output. Once again no storage is being used so we avoid any memory/buffer issues
