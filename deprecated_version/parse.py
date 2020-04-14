def email(raw_email):
	sections = raw_email.split('-----')
	return {
		'header': get_header(sections[0]),
		'content': sections[1].strip()
	}

def salutation(text):
	sentences = re.split('\\. |, ', text, 1)
	print(sentences)
	if len(sentences) > 1:
		salutation = sentences[0]
		# a salutation should never be more than 5 words
		if len(salutation.split()) < 5:
			return salutation
	return None

# private functions

def get_header(text):
	text = text.split('\n')
	return {
		'sender email': get_value(text[0]),
		'sender name': get_value(text[1]),
		'recipient name': get_value(text[2]),
		'subject': get_value(text[3])
	}

def get_value(text):
	return text.split(': ')[1].strip()