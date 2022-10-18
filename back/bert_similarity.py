from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
model = SentenceTransformer('bert-base-nli-mean-tokens')

def similarity(text1, text2):
    sentences = []
    sentences.append(text1)
    sentences.append(text2)
    sentence_embeddings = model.encode(sentences)
    sentence_embeddings.shape
    
    res=cosine_similarity(
    [sentence_embeddings[0]],
    sentence_embeddings[1:]
    )
    return "The similarity between the articles is %0.6f" %res[0]