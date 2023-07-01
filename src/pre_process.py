from nltk import word_tokenize, PorterStemmer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import re
import json

def process_json(intents):
    pass


def pre_process(intents):

    stemmer = PorterStemmer()
    X_train = []
    tags = []
    y_train = []

    for intent in intents['intents']:
        tag = intent['tag']
        tags.append(tag)
        for pattern in intent['patterns']:
            pattern = re.sub(r'[^a-zA-Z0-9\s]', '', pattern)
            pattern = pattern.lower()
            pattern = word_tokenize(pattern)
            pattern = [stemmer.stem(word) for word in pattern if word not in stopwords.words('english')]
            pattern = ' '.join(pattern)
            X_train.append(pattern)
            y_train.append(tag)
            

    cv = CountVectorizer(max_features=5000)
    X_train = cv.fit_transform(X_train).toarray()

    for i, tag in enumerate(y_train):
        y_train[i] = tags.index(tag)

    return X_train, y_train


intents = json.load(open('intents.json'))
X_train, y_train = pre_process(intents)
print(X_train)
print(y_train)