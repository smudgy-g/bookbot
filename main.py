import sys
from stats import get_num_words, get_num_chars, sort_char_counts


def get_book_text(file_path: str):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents


def main():
    try:
        book_path = sys.argv[1]
        book = get_book_text(book_path)
        num_words = get_num_words(book)
        num_chars = get_num_chars(book)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for i in sort_char_counts(num_chars):
            print(f"{i['char']}: {i['count']}")
        print("============= END ===============")

    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)


main()
