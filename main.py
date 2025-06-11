import sys
from stats import (
	get_num_words,
	get_num_characters,
	sort_dictionary,
)

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	book_path = sys.argv[1]

def get_book_text(filepath):
	with open(filepath) as f:
		return f.read()

	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {book_path}...")
	text = get_book_text(f"./{book_path}")
	print("----------- Word Count ----------")
	get_num_words(text)
	print(f"Found {get_num_words(text)} total words")
	print("--------- Character Count -------")
	result = sort_dictionary(get_num_characters(text))
	for item in result:
		if item['char'].isalpha():
			print(f"{item['char']}: {item['num']}")

	print("============= END ===============")

main()