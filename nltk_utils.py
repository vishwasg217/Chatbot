from nltk import word_tokenize, PorterStemmer
import numpy as np

stemmer = PorterStemmer()


def tokenize(sentence):
    return word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word)

def bag_of_words(tokenized_sentence, words):
    sentence_words = [stem(word) for word in tokenized_sentence]
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words: 
            bag[idx] = 1

    return bag

# text = "India is a county with a population of 1.3 billion people."
# print(text)
# tokenized_text = tokenize(text)
# stemmed_text = [stem(word) for word in tokenized_text]
# print(stemmed_text)

# tokenize -> lowercase -> stem -> remove punctuation -> bag of words
