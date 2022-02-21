# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import string
import random

WORDLIST_FILENAME = "problem_set_3/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    secretWord = set(secretWord)
    lettersGuessed = set(lettersGuessed)

    return secretWord.issubset(lettersGuessed)


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    output = ['_ ' for _ in secretWord]

    def getIndex(word, letter):
        indeces = []
        for index, char in enumerate(word):
            if char == letter:
                indeces.append(index)
        return indeces

    for letter in lettersGuessed:
        if letter in secretWord:
            indeces = getIndex(secretWord, letter)
        else:
            continue
    
        for index in indeces:
            output[index] = letter
        
    guessedWord = ''.join([x for x in output])
    return guessedWord



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''

    letters = set(string.ascii_lowercase)

    lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
    lettersGuessed = set(lettersGuessed)

    complementIntersection = letters ^ lettersGuessed

    return ''.join([x for x in sorted(complementIntersection)])
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is",str(len(secretWord)),"letters long.")
    print("-------------")

    guessesAvailable = 8
    lettersGuessed = []

    while guessesAvailable > 0:
        print("You have",str(guessesAvailable),"left")
        print("Available letters:",getAvailableLetters(lettersGuessed))
        guess = (input("Please guess a letter: ")).lower()
        if guess not in lettersGuessed:
            lettersGuessed.append(guess)
            if guess in secretWord:
                print("Good guess:",getGuessedWord(secretWord,lettersGuessed))
            else:
                print("Oops! That letter is not in my word:",getGuessedWord(secretWord,lettersGuessed))
                guessesAvailable -= 1
        else:
            print("Oops! You've already guessed that letter:",getGuessedWord(secretWord,lettersGuessed))
        print("-------------")
        if isWordGuessed(secretWord,lettersGuessed):
            print("Congratulations, you won!")
            return None

    print("Sorry, you ran out of guesses. The word was", secretWord)
    return None


wordlist = loadWords()
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)



