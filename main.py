from stats import get_num_words
from stats import get_num_characters
from stats import sort_dictionary

def main():
	print("============ BOOKBOT ============")
	print("Analyzing book found at books/frankenstein.txt...")
	text = get_book_text("./books/frankenstein.txt")
	# print(text)
	print("----------- Word Count ----------")
	get_num_words(text)
	print(f"Found {get_num_words(text)} total words")
	print("--------- Character Count -------")
	result = sort_dictionary(get_num_characters(text))
	for item in result:
		if item['char'].isalpha():
			print(f"{item['char']}: {item['num']}")
	print("============= END ===============")

def get_book_text(filepath):
	with open(filepath) as f:
		return f.read()

main()