from stats import number_of_words, character_count, sorted_characters
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]

    text = get_book_text(path)
    dict = character_count(text)
    word_count = number_of_words(text)
    sorted_list = sorted_characters(dict)
    
    #report
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in sorted_list:
        if char["character"].isalpha():
            print(f"{char['character']}: {char['count']}")
        else:
            pass
    print("============= END ===============")

main()