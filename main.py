import sys
from stats import get_num_words, get_num_chars_stand

def main():
    try:
        bookPath = sys.argv[1]
    except Exception:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    fileContent = get_book_text(bookPath)
    numWords = get_num_words(fileContent)
    charList = get_num_chars_stand(fileContent)
    print('============ BOOKBOT ============')
    print(f"Analyzing book found at {bookPath}...")
    print('----------- Word Count ----------')
    print(f"Found {numWords} total words")
    print('--------- Character Count -------')
    for elem in charList:
        if elem["isAlpha"]:
            print(f"{elem["char"]}: {elem["num"]}")
    print('============= END ===============')

def get_book_text(filePath):
    fileContent = ""
    with open(filePath) as file:
        fileContent = file.read()
    return fileContent

main()