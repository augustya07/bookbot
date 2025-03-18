def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    print(f"{word_count} words found in the document")

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    

def count_words(text):
    words = text.split()
    return len(words)


    

main()