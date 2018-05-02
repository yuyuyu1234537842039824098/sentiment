#File: sentiment_mod.py

import nltk
import random
#from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier
import pickle
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from nltk.classify import ClassifierI
from nltk.tokenize import word_tokenize



documents_f = open("documents.pickle", "r")
documents = pickle.load(documents_f)
documents_f.close()




word_features5k_f = open("word_features5k.pickle", "r")
word_features = pickle.load(word_features5k_f)
word_features5k_f.close()


def find_features(document):
    words = word_tokenize(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features

open_file = open("BernoulliNB_classifier5k.pickle", "r")
BernoulliNB_classifier = pickle.load(open_file)
open_file.close()



def sentiment(text):
    feats = find_features(text)
    return BernoulliNB_classifier.classify(feats)