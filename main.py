import sys
from stats import get_num_words
from stats import get_num_characters
from stats import sort_dictionary

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {sys.argv[1]}...")
	text = get_book_text(f"./{sys.argv[1]}")
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