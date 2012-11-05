import operator

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def findWords(letters, wordlist):
    '''
    Given a string of letters, compiles a list of words that can be constructed using those letters.

    input:
        - a string of letters, without spaces
    output:
        - a list with all words that can be constructed from the given letters
    '''
    letters = letters.lower()
    result = []
    for word in wordList:
        add = True
        lettersCopy = letters[:]
        for char in word:
            if char not in lettersCopy:
                add = False
                break
            else:
                lettersCopy = lettersCopy.replace(char,"",1)
        if add == True:
            result.append(word)
    return result

def sortWords(wList, compare = operator.lt):
    '''
    Sorts a list of words by the words' length.

    input:
        - a word list
        - optionally - a comparison operator (lt/gt)
    output:
        - a sorted word list
    '''
    if len(wList) < 2:
        return wList[:]
    else:
        midpoint = int(len(wList) / 2)
        listOne = sortWords(wList[:midpoint], compare)
        listTwo = sortWords(wList[midpoint:], compare)
        return merge(listOne, listTwo, compare)

def merge(listOne, listTwo, compare):
    '''
    Merges lists.

    input:
        - two sorted lists
        - a comparison operator (lt/gt)
    output:
        - a merged sorted list
    '''
    result = []
    i = 0
    j = 0
    while i < len(listOne) and j < len(listTwo):
        if compare(len(listOne[i]), len(listTwo[j])):
            result.append(listOne[i])
            i += 1
        else:
            result.append(listTwo[j])
            j += 1
    while i < len(listOne):
        result.append(listOne[i])
        i += 1
    while j < len(listTwo):
        result.append(listTwo[j])
        j += 1
    return result

def display(sortedList):
    '''
    Assumes the list is sorted by word length, prints them out in groups.

    input:
        - a word list sorted by word length
    output:
        - None
    '''
    lastWord = ""
    for word in sortedList:
        if len(word) != len(lastWord):
            print
            print("----------------------------------------")
            print("Words that are " + str(len(word)) + " letters long:")
            print("----------------------------------------")
        print(word),
        lastWord = word

def solve(letters):
    '''
    Gives possible solutions for a Letterpress game.

    input:
        - a string of letters, w/o spaces
    output:
        - displays solutions, returns None
    '''
    display(sortWords(findWords(letters, wordList)))

if __name__ == '__main__':
    wordList = loadWords()
    solve(raw_input("Enter a string of letters: "))
