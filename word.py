import random
import string

WORDLIST_FILENAME = "words.txt"

class Word:

    def __init__(self, inputFile = str):
        self.__inputFile = str(inputFile)
        self.__readingParam = str
        self.__lineReader = str
        self.__wordlist = list

    def loadWords(self):
        """
        Depending on the size of the word list, this function may
        take a while to finish.
        """
        print "Loading word list from file..."

        __readingParam = 'r'
        __inputFile = open(WORDLIST_FILENAME, readingParam)

        __lineReader = inputFile.readline()
        __wordlist = string.split(lineReader)

        print "  ", len(wordlist), "words loaded."

        return random.choice(wordlist)
