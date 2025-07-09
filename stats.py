# Contains functions for analyzing text

def sort_on(items):
    return items["num"]

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
    unsorted_list = []
    sorted_list = []
# remove non-alpha characters from dictionary
    for c in working_dict:
        if not c.isalpha():
            delete_dict[c] = 1
    for d in delete_dict:
        del working_dict[d]
# create list of dictionaries then sort list
    for c, n in working_dict.items():
        list_entry = {"char": c, "num": n}
        unsorted_list.append(list_entry)
    unsorted_list.sort(reverse=True, key=sort_on)
    for i in unsorted_list:
        sorted_list.append(f"{i["char"]}: {i["num"]}")
    return sorted_list
