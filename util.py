import csv
import json

import nltk


def word_tokenize(text):
    return nltk.word_tokenize(text)


def stem(word):
    return nltk.SnowballStemmer("english").stem(word)


def read_json(file):
    with open(file) as f:
        return json.load(f)


def write_json(file, obj):
    with open(file, 'w') as f:
        json.dump(obj, f)


def csv2dict(file):
    dic = {}
    with open(file, newline='') as f:
        reader = csv.DictReader(f)
        for idx, row in enumerate(reader):
            dic[idx] = dict(row)
    return dic
