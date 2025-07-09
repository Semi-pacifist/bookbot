# Contains functions for analyzing text

def get_word_count(book_text = ""):
    text_words = book_text.split()
    word_count = len(text_words)
    return word_count
