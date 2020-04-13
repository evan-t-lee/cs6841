import re

filename = input('Enter name of the file you\'d like to check: ')

for line in open(filename):
	line.strip()
	if line.startswith('From:'):
		email = line.split()[1]		

match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)

if match == None:
	print('Bad Syntax')
else:
	print('valid email')