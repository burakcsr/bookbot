def get_book_text(path):
    with open(path) as content:
        text = content.read()
    return text



def main():
    text = get_book_text('books/frankenstein.txt')
    num_words = count_words(text)
    print(f"Found {num_words} total words")
    print(char_count(text))

from stats import count_words
from stats import char_count



main()