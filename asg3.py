#!/usr/bin/env python
"""NLP Preprocessing Library"""

from nltk.tokenize import TweetTokenizer

def clean_text(raw_text):
    """Remove url, tokens"""

def tokenize_text(tweet_str):
    """convert string to chunks of text"""

def replace_token_with_index(tokenized_tweet, max_length_dictionary, file_path="./Glove_dict.txt"):
    """convert each text to dictionary index"""


def pad_sequence(arr, max_length_tweet):
    """add 0 padding to the trail until max_length_tweet"""

def get_glove_dictionary(file_path="./glove.twitter.27B.25d.txt"):
    """output a glove dictionary"""


def preprocess(input_text, max_length_tweet=100000, max_length_dictionary=1193515):
    """a general method to call, convert string to vectorized representation"""
