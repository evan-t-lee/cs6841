# library imports
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix
from joblib import dump, load

# user imports
from parse import count_frequency, parse_features

mode = int(input('Choose mode - Both(1)/Train(2)/Test(3): '))

if mode % 3:
    has_custom = input('Do you have custom keywords (y/n)? ')
    has_custom = True if has_custom == 'y' else False

    text_prompt = '\nTraining model'
    if has_custom:
        text_prompt += ' with custom keywords'
    print(text_prompt + '...')

    count_frequency('train_data', has_custom)

    # label legit emails
    train_outcomes = np.zeros(704)
    # label phishing emails 
    train_outcomes[353:703] = 1

    train_matrix = parse_features('train_data')

    nb_model = MultinomialNB()
    nb_model.fit(train_matrix, train_outcomes)

    dump(nb_model, 'nb_model.joblib')

    print('Model trained.')

if mode % 2:
    print('\nTesting model...')

    nb_model = load('nb_model.joblib')

    test_matrix = parse_features('test_data')

    # label legit emails
    test_outcomes = np.zeros(260)
    # label phishing emails
    test_outcomes[130:260] = 1

    result = nb_model.predict(test_matrix)
    result_matrix = confusion_matrix(test_outcomes, result)

    print('---------------\nTest results:')
    print(f'Passed (P|N): {result_matrix[0][0]} | {result_matrix[1][1]}')
    print(f'Failed (P|N): {result_matrix[1][0]} | {result_matrix[0][1]}')

    print('---------------\nModel tested.')
