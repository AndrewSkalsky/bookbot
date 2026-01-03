from stats import get_num_words, get_num_chars

def main():
    fileContent = get_book_text('./books/frankenstein.txt')
    numWords = get_num_words(fileContent)
    charDict = get_num_chars(fileContent)
    print(f"Found {numWords} total words")
    print(charDict)

def get_book_text(filePath):
    fileContent = ""
    with open(filePath) as file:
        fileContent = file.read()
    return fileContent

main()