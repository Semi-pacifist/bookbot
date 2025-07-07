def get_book_text(book_filepath = ""):
    with open(book_filepath) as b:
        book_contents = b.read()
    return book_contents

def get_text_words(book_text = ""):
    text_words = book_text.split()
    word_count = len(text_words)
    return word_count

def main():
    print(get_book_text("books/frankenstein.txt"))
    print(f"{get_text_words(get_book_text("books/frankenstein.txt"))} words found in the document")

main()
