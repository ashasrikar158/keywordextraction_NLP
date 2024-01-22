# keywordextraction_NLP
In this NLP-based Keyword Extraction project, the goal is to automatically identify and extract key terms or phrases from a given text, document, or dataset. The project involves leveraging Natural Language Processing (NLP) techniques to analyze the content and identify words or phrases that best represent the document's main topics.

The dataset we used : "https://www.kaggle.com/code/akhatova/extract-keywords/input"

TF-IDF is a more sophisticated approach that considers not only term frequency but also the importance of terms across a collection of documents. It is calculated using the following steps:

Term Frequency (TF): Measures how often a term appears in a document.
TF
(
�
,
�
)
=
Number of times term t appears in document d
Total number of terms in document d
TF(t,d)= 
Total number of terms in document d
Number of times term t appears in document d
​
 

Inverse Document Frequency (IDF): Measures the importance of a term across the entire document collection.
IDF
(
�
,
�
)
=
log
⁡
(
Total number of documents in the collection D
Number of documents containing term t in D
+
1
)
IDF(t,D)=log( 
Number of documents containing term t in D+1
Total number of documents in the collection D
​
 )

TF-IDF Score: The product of TF and IDF.
TF-IDF
(
�
,
�
,
�
)
=
TF
(
�
,
�
)
×
IDF
(
�
,
�
)
TF-IDF(t,d,D)=TF(t,d)×IDF(t,D)
