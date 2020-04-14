for line in open('keyphrases.txt'):
	line = line.strip()
	if line:
		print(line.lower())