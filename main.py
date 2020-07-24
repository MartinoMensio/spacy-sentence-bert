import spacy
import numpy as np
from sentence_transformers import SentenceTransformer

def vectorise(sent):
    return model.encode([sent.text])[0]

def overwrite_vectors(doc):
    doc.user_hooks['vector'] = vectorise
    doc.user_span_hooks['vector'] = vectorise
    doc.user_token_hooks['vector'] = vectorise
    return doc


nlp = spacy.blank('en')
nlp.add_pipe(overwrite_vectors)



# https://github.com/UKPLab/sentence-transformers
model = SentenceTransformer('bert-base-nli-mean-tokens') # 768
model = SentenceTransformer('roberta-large-nli-stsb-mean-tokens') # 1024


sentences = ['This framework generates embeddings for each input sentence',
    'Sentences are passed as a list of string.', 
    'The quick brown fox jumps over the lazy dog.',
    'Sentences are given as a list of strings']
docs = [nlp(s) for s in sentences]

print(docs[0].vector.shape)

m = np.zeros((len(docs), len(docs)))
for i, d_i in enumerate(docs):
    for j, d_j in enumerate(docs):
        m[i,j] = d_i.similarity(d_j)

print(m)