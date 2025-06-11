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
	for item in dictionary.items():
		new_dictionary = {}
		new_dictionary["char"] = item[0]
		new_dictionary["num"] = item[1]
		sorted_items.append(new_dictionary)

	sorted_items.sort(reverse=True, key=sort_on)
	return sorted_items
	

	