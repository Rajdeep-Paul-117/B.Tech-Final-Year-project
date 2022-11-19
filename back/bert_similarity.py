from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
model = SentenceTransformer('bert-base-nli-mean-tokens')

def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    sent=""
    for w in word_tokens:
        if w not in stop_words:
            sent+=" "+w
    return sent

def similarity(text1, text2):
    sentences = []
    sentences.append(remove_stopwords(text1))
    sentences.append(remove_stopwords(text2))
    
    sentence_embeddings = model.encode(sentences)
    sentence_embeddings.shape
    res=cosine_similarity(
    [sentence_embeddings[0]],
    sentence_embeddings[1:]
    )
    return "%0.6f" %res[0]

from sentence_transformers import SentenceTransformer, util
import numpy as np
model = SentenceTransformer('stsb-roberta-large')

def roberta_similarity(text1, text2):
    
    sentence_embeddings1 = model.encode(remove_stopwords(text1))
    sentence_embeddings2 = model.encode(remove_stopwords(text2))
    

    res=cosine_scores = util.pytorch_cos_sim(sentence_embeddings1, sentence_embeddings2)
    return "%0.6f" %res.item()
