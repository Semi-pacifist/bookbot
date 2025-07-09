#imports
from stats import get_word_count
from stats import get_char_occurance
from stats import dict_sort

#function delcarations
def get_book_text(book_filepath = ""):
    with open(book_filepath) as b:
        book_contents = b.read()
    return book_contents

def generate_report(text_path = ""):
    working_text = get_book_text(text_path)
    word_count = get_word_count(working_text)
    char_occurance = get_char_occurance(working_text)
    print("========BOOKBOT========")
    print(f"Analyzing book found at {text_path}...")
    print("--------Word Count--------")
    print(f"Found {word_count} total words")
    print("--------Character Count --------")
    print(f"{dict_sort(char_occurance)}")
    print("======== END ========")

def main():
    generate_report("books/frankenstein.txt")

#program
main()
