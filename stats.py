def get_num_words(text):
	word_count = text.split()
	return len(word_count)

def get_num_characters(text):
	dict = {}
	for character in text:
		char = character.lower()
		if char not in dict:
			dict[char] = 1
		else:
			dict[char] +=1
			
	return dict