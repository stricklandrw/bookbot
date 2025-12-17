#!/usr/bin/env python3

def how_many_words(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        num_words = len(file_contents.split())
    return num_words

def character_count(path_to_file):
    letter_count = {}
    with open(path_to_file) as f:
        file_contents = f.read()
        file_lowercase = file_contents.lower()
        for char in file_lowercase:
            if char not in letter_count:
                letter_count.update({char: file_lowercase.count(char)})
    return letter_count

def pretty_report(path_to_file):
    char_dict = character_count(path_to_file)
    chars_list = []
    sorted_list = []
    for char in char_dict:
        if not char.isalpha():
            continue
        chars_list.append({"char": char, "num": char_dict[char]})
#    print(chars_list)
    sorted_list = sorted(chars_list, reverse=True, key=lambda x: x["num"])
#    print(sorted_list)
    return sorted_list