# library imports
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from joblib import load

# user imports
from parse import parse_features

show_email = input('Would you like the input email to be shown (y/n)? ')
show_email = True if show_email == 'y' else False

nb_model = load('nb_model.joblib')

input_matrix = parse_features(['in.txt'])
input_result = nb_model.predict(input_matrix)

if show_email:
	email = open('in.txt').read()
	print('\n------------------------------')
	print(email)
	print('------------------------------')

email_result = 'phishy' if input_result else 'not phishy'
print(f'\nAccording to our analysis, it is likely that this email is {email_result}.')
