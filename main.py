#!/usr/bin/env python3

from stats import how_many_words, character_count

book_loc = "books/frankenstein.txt"

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        print(file_contents)
    return

def main():
    how_many_words(book_loc)
    character_count(book_loc)
    return

main()