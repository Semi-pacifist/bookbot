#imports
from stats import get_word_count
from stats import get_char_occurance
from stats import dict_sort
import sys

#function delcarations
def get_book_text(book_filepath = ""):
    with open(book_filepath) as b:
        book_contents = b.read()
    return book_contents

def generate_report(text_path = ""):
    working_text = get_book_text(text_path)
    word_count = get_word_count(working_text)
    char_occurance = get_char_occurance(working_text)
    sorted_occurance = dict_sort(char_occurance)

    print("========BOOKBOT========")
    print(f"Analyzing book found at {text_path}...")
    print("--------Word Count--------")
    print(f"Found {word_count} total words")
    print("--------Character Count --------")
    for i in sorted_occurance:
        print(i)
    print("======== END ========")

def main(user_text = []):
    if len(user_text) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        generate_report(user_text[1])

#program
main(sys.argv)
