def get_num_words(bookContent):
    return len(bookContent.split())

def get_num_chars(bookContent):
    charStats = {}
    standarContent = bookContent.lower()
    for c in standarContent:
        if c in charStats:
            charStats[c] += 1
        else:
            charStats[c] = 1
    return charStats
