def main():
	text = get_book_text("./books/frankenstein.txt")
	print(text)
	num_of_words(text)
	print(f"{num_of_words(text)} words found in the document")

def num_of_words(text):
	word_count = text.split()
	return len(word_count)

def get_book_text(filepath):
	with open(filepath) as f:
		return f.read()

main()