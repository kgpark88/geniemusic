import re
import pandas as pd
from gensim.models import Word2Vec
from sklearn.feature_extraction.text import CountVectorizer

df = pd.read_csv('geniemusic_review.csv',sep=',',encoding="cp949")
