#imports
from stats import get_word_count

#function delcarations
def get_book_text(book_filepath = ""):
    with open(book_filepath) as b:
        book_contents = b.read()
    return book_contents

def main():
    print(get_book_text("books/frankenstein.txt"))
    print(f"{get_word_count(get_book_text("books/frankenstein.txt"))} words found in the document")

#program
main()
