# library imports
import os
import re
from collections import Counter
from numpy import zeros
from joblib import dump, load

MAX_KEYWORDS = 3000

def collate_directory(directory):
    return [os.path.join(directory, filename) for filename in os.listdir(directory)]

def count_frequency(files, has_custom):
    all_words = []
    for filename in files:
        with open(filename) as text:
            for i, line in enumerate(text):
                if i < 2: # content starts from 3rd line
                    continue
                sentence = re.sub(r'[^a-zA-Z ]+', '', line.strip())
                sentence = re.sub(r'\b[a-zA-Z]\b', '', sentence)
                all_words += sentence.split()

    if has_custom:
        custom_words = [(line.strip(), MAX_KEYWORDS)for line in open('keywords.txt')]
        word_amount = MAX_KEYWORDS - len(custom_words)
        word_freq = custom_words + Counter(all_words).most_common(word_amount)
    else:
        word_freq = Counter(all_words).most_common(MAX_KEYWORDS)
    dump(word_freq, 'word_freq.joblib')

def parse_features(files):
    word_freq = load('word_freq.joblib')
    features_matrix = zeros((len(files), MAX_KEYWORDS))
    for i, filename in enumerate(files):
        with open(filename) as text:
            for j, line in enumerate(text):
                if j < 2: # content starts from 3rd line
                    continue
                words = line.strip().split()
                for word in words:
                    for k, count in enumerate(word_freq):
                        if count[0] == word:
                            features_matrix[i, k] = words.count(word)
    return features_matrix
