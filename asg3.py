#!/usr/bin/env python
"""NLP Preprocessing Library"""

from nltk.tokenize import TweetTokenizer

def clean_text(raw_text):
    """Remove url, tokens"""

def tokenize_text(tweet_str):
    """convert string to chunks of text"""

def replace_token_with_index(tokenized_tweet, max_length_dictionary, file_path="./Glove_dict.txt"):
    """convert each text to dictionary index"""

    # should be replacing each token in a list of tokens by their corresponding index
    # Source: https://github.com/stanfordnlp/GloVe
    # Source: https://towardsdatascience.com/word-embeddings-for-sentiment-analysis-65f42ea5d26e

    file = open(file_path, "r")
    corpus = [""]*max_length_dictionary
    idx = 0
    for word in file:
        corpus[idx] = word.rstrip()
        idx += 1

    for idx, word in enumerate(tokenized_tweet):
        if word not in tokenized_tweet:
            tokenized_tweet[idx] = "<unk>"

    return [corpus.index(x) for x in tokenized_tweet]


def pad_sequence(arr, max_length_tweet):
    """add 0 padding to the trail until max_length_tweet"""

def get_glove_dictionary(file_path="./glove.twitter.27B.25d.txt"):
    """output a glove dictionary"""
    file = open(file_path, "r")
    dictionary = {}
    keys = []
    for word_vector in file:
        dictionary[word_vector.split()[0]] = word_vector.split()[1:]
        keys.append(word_vector.split()[0])
    file.close()

    file = open("Glove_dict.txt", "a")
    for word in keys:
        file.write(word + '\n')
    file.close()


def preprocess(input_text, max_length_tweet=100000, max_length_dictionary=1193515):
    """a general method to call, convert string to vectorized representation"""
    input_text = clean_text(input_text)
    text_list = tokenize_text(input_text)
    index_list = replace_token_with_index(text_list, max_length_dictionary)
    index_list = pad_sequence(index_list, max_length_tweet)
    return index_list
    """a general method to call, convert string to vectorized representation"""
