from stats import get_num_words

def main():
	text = get_book_text("./books/frankenstein.txt")
	print(text)
	get_num_words(text)
	print(f"{get_num_words(text)} words found in the document")

def get_book_text(filepath):
	with open(filepath) as f:
		return f.read()

main()