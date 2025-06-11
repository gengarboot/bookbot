from stats import get_num_words
from stats import get_num_characters

def main():
	text = get_book_text("./books/frankenstein.txt")
	print(text)
	get_num_words(text)
	print(f"{get_num_words(text)} words found in the document")
	print(f"{get_num_characters(text)}")

def get_book_text(filepath):
	with open(filepath) as f:
		return f.read()

main()