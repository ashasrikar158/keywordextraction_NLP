# keywordextraction_NLP
In this NLP-based Keyword Extraction project, the goal is to automatically identify and extract key terms or phrases from a given text, document, or dataset. The project involves leveraging Natural Language Processing (NLP) techniques to analyze the content and identify words or phrases that best represent the document's main topics.

The dataset we used : "https://www.kaggle.com/code/akhatova/extract-keywords/input"

In this we used TF-IDF algorithm. TF-IDF is a numerical statistic used in Natural Language Processing (NLP) and information retrieval to evaluate the importance of a term in a document relative to its occurrence in a collection of documents (corpus). It is a widely used technique for extracting meaningful features from text data. 

Limitations:

1.Lack of Context Understanding: TF-IDF does not consider the context of words within a document. It treats each word independently, which can lead to limitations in capturing the true meaning or significance of a word within a specific context.

2.Sensitivity to Document Length: TF-IDF is sensitive to document length. Longer documents tend to have higher term frequencies, which can impact the TF-IDF scores. This sensitivity may lead to bias towards longer documents, and it might be necessary to normalize the scores.

3.Difficulty with Rare Terms: Rare terms may not be well-represented in a TF-IDF model. If a term occurs infrequently in the corpus, its IDF value can be high, making the TF-IDF score sensitive to small changes in term frequency.
