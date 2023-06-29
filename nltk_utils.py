from nltk import word_tokenize, PorterStemmer

stemmer = PorterStemmer()


def tokenize(sentence):
    return word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, all_words):
    pass

text = "India is a county with a population of 1.3 billion people."
print(text)
tokenized_text = tokenize(text)
stemmed_text = [stem(word) for word in tokenized_text]
print(stemmed_text)

# tokenize -> lowercase -> stem -> remove punctuation -> bag of words
