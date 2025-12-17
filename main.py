#!/usr/bin/env python3

from stats import how_many_words, character_count, pretty_report

book_loc = "books/frankenstein.txt"

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        print(file_contents)
    return

def main():
    wordcount = how_many_words(book_loc)
    charcount = character_count(book_loc)
    charcount_report = pretty_report(book_loc)
    print(f"============ BOOKBOT ============\r\nAnalyzing book found at {book_loc}...\r\n----------- Word Count ----------")
    print(f"Found {wordcount} total words")
    print("--------- Character Count -------")
    for char in charcount_report:
        print(f"{char['char']}: {char['num']}")
    print("============= END ===============")
    return

main()