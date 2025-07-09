#imports
from stats import get_word_count
from stats import get_char_occurance

#function delcarations
def get_book_text(book_filepath = ""):
    with open(book_filepath) as b:
        book_contents = b.read()
    return book_contents

def main():
    working_text = get_book_text("books/frankenstein.txt")
    #print(working_text)
    #print(f"{get_word_count(working_text)} words found in the document")
    print(f"{get_char_occurance(working_text)}")

#program
main()
