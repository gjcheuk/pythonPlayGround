# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

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
    # FILL IN YOUR CODE HERE...
    word_unique = list(set(secretWord))
    correct = 0
    
    for char in word_unique:
        if char in lettersGuessed:
            correct += 1
        else:
            return False
    
    if correct == len(word_unique):
        return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    result = ''
    if len(lettersGuessed) == 0:
        return '_' * len(secretWord)
    
    
    for char in secretWord:
        if char in lettersGuessed:
            result += char
        else:
            result += '_ '
    return result
            



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    available_char = string.ascii_lowercase
    
    if len(lettersGuessed) == 0:
        return available_char
    else:
        for char in lettersGuessed:
            available_char = available_char.replace(char, '')
        return available_char

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
    # FILL IN YOUR CODE HERE...
    
    numberOfGuess = 8
    lettersGuessed = []
    repeat_tracker = []
    guessCorrect = False
    alphatbet = string.ascii_lowercase
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
    
    while numberOfGuess >= 0 or not guessCorrect:

        print("-----------")
        if numberOfGuess > 1:
            print("You have " + str(numberOfGuess) + " guesses left")
        elif numberOfGuess == 1:
            print("You have " + str(numberOfGuess) + " guess left")
        else:
            print("Sorry, you ran out of guesses. The word was " + secretWord + ".")
            break
        
        availableLetters = getAvailableLetters(lettersGuessed)
        print("Available Letters: " + availableLetters)
        guess_intitial = input("Please guess a letter: ")
        guess = guess_intitial.lower()
        if guess not in alphatbet:
            print("Please type in an alphabet and try again")
            continue
        
        lettersGuessed.append(guess)
        remainLetter = getGuessedWord(secretWord, lettersGuessed)
        if guess in repeat_tracker:
            print("Oops! You've already guessed that letter: " + remainLetter)
            continue
        else:
            if guess in secretWord:
                print("Good guess: " + remainLetter)
            else:
                print("Oops! That letter is not in my word: " + remainLetter)
                numberOfGuess -= 1
                
        repeat_tracker.append(guess)
        guessCorrect = isWordGuessed(secretWord, lettersGuessed)
        if guessCorrect:
            print("-----------")
            print("Congratulations, you won!")
            break
            



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
