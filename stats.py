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

def sort_on(dict):
	return dict["num"]

def sort_dictionary(dictionary):
	sorted_items = []	

	# dictionary.items gives a list of touples where each index in touple is key / value
	for key in dictionary:
		sorted_items.append({"char": key, "num": dictionary[key]})
		
	sorted_items.sort(reverse=True, key=sort_on)
	return sorted_items
	

	