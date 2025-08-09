import sys


from stats import get_num_words, get_chars_dict, chars_dict_to_sorted_list
def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
        return contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    actual_words = get_num_words(book_text)
    print(f"Found {actual_words} total words")
    main_char  = get_chars_dict(book_text)
    main_dict = chars_dict_to_sorted_list(main_char)
    for i in main_dict:
        print(f"{i['char']}: {i['num']}")

if __name__ == "__main__":
    main()

