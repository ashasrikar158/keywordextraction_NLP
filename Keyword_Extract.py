import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
nltk.download('stopwords')
nltk.download('wordnet')
import numpy as np
import pandas as pd 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import pickle



#Stopwords
stop_words = set(stopwords.words('english'))
##Creating a list of custom stopwords
new_words = ["fig","figure","image","sample","using", 
            "show", "result", "large", 
            "also", "one", "two", "three", 
            "four", "five", "seven","eight","nine"]
stop_words = list(stop_words.union(new_words))


def pre_process(text):
    
    # lowercase
    text=text.lower()
    
    #remove tags
    text=re.sub("&lt;/?.*?&gt;"," &lt;&gt; ",text)
    
    # remove special characters and digits
    text=re.sub("(\\d|\\W)+"," ",text)
    
    ##Convert to list from string
    text = text.split()
    
    # remove stopwords
    text = [word for word in text if word not in stop_words]

    # remove words less than three letters
    text = [word for word in text if len(word) >= 3]

    # lemmatize
    lmtzr = WordNetLemmatizer()
    text = [lmtzr.lemmatize(word) for word in text]
    
    return ' '.join(text)

def calculate_tfidf(docs,text):
    tf_idf_vector=tfidf_transformer.transform(cv.transform([text]))

    #sort the tf-idf vectors by descending order of scores
    sorted_items=sort_coo(tf_idf_vector.tocoo())

    #extract only the top n; n here is 10
    keywords=extract_topn_from_vector(feature_names,sorted_items,10)
    
    return keywords

def sort_coo(coo_matrix):
  tuples = zip(coo_matrix.col, coo_matrix.data)
  return sorted(tuples, key=lambda x: (x[1], x[0]), reverse=True)



def extract_topn_from_vector(feature_names, sorted_items, topn=10):
    """get the feature names and tf-idf score of top n items"""
    
    #use only topn items from vector
    sorted_items = sorted_items[:topn]

    score_vals = []
    feature_vals = []

    for idx, score in sorted_items:
        fname = feature_names[idx]
        
        #keep track of feature name and its corresponding score
        score_vals.append(round(score, 3))
        feature_vals.append(feature_names[idx])

    #create a tuples of feature,score
    #results = zip(feature_vals,score_vals)
    results= {}
    for idx in range(len(feature_vals)):
        results[feature_vals[idx]]=score_vals[idx]
    
    return results
 

def extract_words(text):
    
    keywords_text = calculate_tfidf(docs,text)
    for k in keywords_text:
        print(k, keywords_text[k])
    return keywords_text


df = pd.read_csv(r'./data/papers.csv')   #Reading CSV file of texts
docs = df['paper_text'].iloc[:1000].apply(lambda x:pre_process(x))  #preprocessing of training data
# Using TF-IDF
#docs = docs.tolist()
#create a vocabulary of words, 
cv=CountVectorizer(max_df=0.85,         # ignore words that appear in 85% of documents
                max_features=1500,  # the size of the vocabulary
                ngram_range=(1,3)    # vocabulary contains single words, bigrams, trigrams
                )
cv.fit(docs)
word_count_vector= cv.transform(docs)
# Saving our class objects used for feature engineering:
pickle.dump(cv, open(r'./data/DataScience-Pianalytix-Models/keywords-count-vectorizer.pkl', 'wb'))
tfidf_transformer=TfidfTransformer(smooth_idf=True,use_idf=True)
tfidf_transformer.fit(word_count_vector)
pickle.dump(tfidf_transformer, open(r'./data/DataScience-Pianalytix-Models/keywords-tfidf-model.pkl', 'wb'))
# get feature names
feature_names=cv.get_feature_names_out()
pickle.dump(feature_names, open(r'./data/DataScience-Pianalytix-Models/keywords-feature-names.pkl', 'wb'))
#generate tf-idf for the given document