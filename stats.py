# Contains functions for analyzing text
from curses.ascii import isalpha

def get_word_count(book_text = ""):
    text_words = book_text.split()
    word_count = len(text_words)
    return word_count

def get_char_occurance(book_text = ""):
    char_dict = {}
    book_text = book_text.lower()
    for c in book_text:
        if c in char_dict:
            char_dict[c] += 1
        if c not in char_dict:
            char_dict[c] = 1
    return char_dict

def dict_sort(working_dict = {}):
    working_dict = working_dict.isalpha()
    working_dict.sort(reverse=True)
    return working_dict
