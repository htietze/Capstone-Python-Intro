# I guessss I should learn to use functions again..
# main function is just getting the input and splitting it to get formatted by the other function
def main():
    sentence = input('Enter your sentence: ')
    # Kathryn let me know this existed, then went to read up on it, 
    # splits strings into a list, using white space by default
    words = sentence.split()
    # Then that list gets sent to the other function to get processed
    editedList = camelCase(words)
    # and finally printed on return
    print(''.join(editedList))

def camelCase(wordList):
    # next function, takes in wordList as argument, then using .lower() on the first index
    wordList[0] = wordList[0].lower()
    # for the rest, looping through the index based on the length of the list
    for x in range(1, len(wordList)):
        # and capitalizing each list entry *except the first*
        wordList[x] = wordList[x].capitalize()
    # Finally returning that edited word list to be joined and printed
    return wordList

main()