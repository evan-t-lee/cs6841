# library imports
import os
import re
import numpy as np
from collections import Counter
from joblib import dump, load

MAX_KEYWORDS = 3000

def collate_directory(directory):
    return [os.path.join(directory, file) for file in os.listdir(directory)]

def parse_features(files): 
    word_freq = load('word_freq.joblib')
    features_matrix = np.zeros((len(files), MAX_KEYWORDS))
    for i in range(len(files)):
        with open(files[i]) as file:
            for j, line in enumerate(file):
                if j < 2: # content starts from 3rd line
                    continue
                words = line.strip().split()
                for word in words:
                    for k, count in enumerate(word_freq):
                        if count[0] == word:
                            features_matrix[i, k] = words.count(word)
    return features_matrix

def count_frequency(directory, has_custom):
    emails = [os.path.join(directory,f) for f in os.listdir(directory)]    
    all_words = []       
    for mail in emails:    
        with open(mail) as m:
            for i,line in enumerate(m):
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
