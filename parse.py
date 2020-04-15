# library imports
import os
import re
from collections import Counter
from numpy import zeros
from joblib import dump, load

MAX_WORDS = 3000

def collate_directory(directory):
    return [os.path.join(directory, filename) for filename in os.listdir(directory)]

def normalise_words(line):
    return re.sub(r'[^a-zA-Z ]+', '', line.lower().strip())

def count_frequency(files, has_custom):
    words = []
    for filename in files:
        with open(filename) as text:
            for i, line in enumerate(text):
                if i < 2: # content starts from 3rd line
                    continue
                words += normalise_words(line).split()

    custom_words = [(line.strip(), MAX_WORDS) for line in open('custom.txt')] if has_custom else []
    word_freq = custom_words + Counter(words).most_common(MAX_WORDS - len(custom_words))
    dump(word_freq, 'word_freq.joblib')

def parse_features(files):
    word_freq = load('word_freq.joblib')
    features_matrix = zeros((len(files), MAX_WORDS))
    for i, filename in enumerate(files):
        with open(filename) as text:
            for j, line in enumerate(text):
                if j < 2: # content starts from 3rd line
                    continue
                words = line.split()
                for word in words:
                    for k, word_count in enumerate(word_freq):
                        if word_count[0] == word:
                            features_matrix[i, k] = words.count(word)
    return features_matrix
