import pickle
from rank_bm25 import BM25Okapi
class Results:
    def __init__(self, obj):
        self.bm25 = obj
        
def getDocs():
    return
    
def getAudio():
    return


corpusText = {}

with open('corpusText.pkl', 'rb') as f:
    corpusText = pickle.load(f)

tokenized_corpus_text = [doc.split(" ") for doc in corpusText.keys()]

bm25 = Results(BM25Okapi(tokenized_corpus_text))
bm25 = bm25.bm25

with open('bm25text.pkl', 'wb') as f:
    pickle.dump(bm25, f)


with open('corpusImg.pkl', 'rb') as f:
    corpusText = pickle.load(f)

tokenized_corpus_text = [doc.split(" ") for doc in corpusText.keys()]

bm25 = Results(BM25Okapi(tokenized_corpus_text))
bm25 = bm25.bm25

with open('bm25img.pkl', 'wb') as f:
    pickle.dump(bm25, f)
