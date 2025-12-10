#!/usr/bin/env python3

def how_many_words(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        num_words = len(file_contents.split())
        print(f"Found {num_words} total words")
    return

def character_count(path_to_file):
    letter_count = {}
    with open(path_to_file) as f:
        file_contents = f.read()
        file_lowercase = file_contents.lower()
        for char in file_lowercase:
            if char not in letter_count:
                letter_count.update({char: file_lowercase.count(char)})
        print(letter_count)
    return
