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

def get_num_chars_stand(bookContent):
    charDict = get_num_chars(bookContent)
    charList = []
    for k in charDict.keys():
        chartElement = {
            "char": k,
            "num": charDict[k],
            "isAlpha": k.isalpha()
        }
        charList.append(chartElement)
    charList.sort(reverse=True, key= lambda item: item["num"])
    return charList
    