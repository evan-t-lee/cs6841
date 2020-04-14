# library imports
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from joblib import load

# user imports
from shared import parse_features

nb_model = load('nb_model.joblib')

input_matrix = parse_features(['in.txt'])
input_result = nb_model.predict(input_matrix)

print('Phishy' if input_result else 'Not phishy')
