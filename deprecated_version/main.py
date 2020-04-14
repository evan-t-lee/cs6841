# library imports
import re

# user files
import data
import parse

filename = input('Enter name of the file you\'d like to check: ')
raw_email = open('in.txt').read()
email = parse.email(raw_email)

# evaluate salutation
print(parse.salutation(email['content']))

# evaluate signature
