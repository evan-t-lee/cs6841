# library imports
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix
from joblib import dump, load

# user imports
from parse import collate_directory, determine_outcomes, parse_features, count_frequency

mode = int(input('Choose mode - Both(1)/Train(2)/Test(3): '))

# train model
if mode % 3:
    has_custom = input('Do you have custom keywords (y/n)? ')
    has_custom = True if has_custom == 'y' else False

    text_prompt = '\nTraining model'
    if has_custom:
        text_prompt += ' with custom keywords'
    print(text_prompt + '...')

    count_frequency(collate_directory('training_dataset'), has_custom)

    # identify legit/phishing emails
    training_outcomes = determine_outcomes('training_dataset')

    training_features = parse_features(collate_directory('training_dataset'))

    nb_model = MultinomialNB()
    nb_model.fit(training_features, training_outcomes)

    dump(nb_model, 'nb_model.joblib')

    print('Model trained.')

# test model
if mode % 2:
    print('\nTesting model...')

    nb_model = load('nb_model.joblib')

    testing_features = parse_features(collate_directory('testing_dataset'))

    # identify legit/phishing emails
    testing_outcomes = determine_outcomes('testing_dataset')

    result = nb_model.predict(testing_features)
    result_features = confusion_matrix(testing_outcomes, result)

    print('---------------\nTest results:')
    print(f'Passed (P|N): {result_features[0][0]} | {result_features[1][1]}')
    print(f'Failed (P|N): {result_features[1][0]} | {result_features[0][1]}')
    print('---------------\nModel tested.')
