# Contains functions for analyzing text

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
    delete_dict = {}
    for c in working_dict:
        if not c.isalpha():
            delete_dict[c] = 1
    for d in delete_dict:
        del working_dict[d]
    #working_dict.sort(reverse=True)
    return working_dict
