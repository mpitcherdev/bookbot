
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def number_of_words(booktext):
    words = booktext.split()
    return len(words)
    
def main():
    words = number_of_words(get_book_text("books/frankenstein.txt"))
    print(f"{words} words found in the document")

main()