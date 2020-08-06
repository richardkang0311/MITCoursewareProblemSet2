# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
from builtins import True

WORDLIST_FILENAME = "words.txt"


def load_words():
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



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''

    length = len(secret_word)
    for c in letters_guessed:
        for x in range(len(secret_word)):
            if c == secret_word[x]:
                length -= 1
    return length == 0



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    return_word = ""
    for c in range(len(secret_word)):
        return_word += "_ "


    for c in letters_guessed:
        for x in range(len(secret_word)):
            if c == secret_word[x]:
                return_word = return_word[0:2 * x] + c + return_word[(2 * x) + 1:]
    return return_word



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    all_letters = string.ascii_lowercase
    for c in letters_guessed:
        for x in range(len(all_letters)):
            if (c == all_letters[x]):
                all_letters = all_letters[0:x] + all_letters[x+1:]
                break;
    return all_letters

def is_letter_present(word, letter):
    '''
    secret_word: string, the secret word to guess.
    letter: letter guessed by the user
    returns: True if the letter is in secret_word
    '''
    for c in word:
        if letter ==  c:
            return True
    return False

def is_vowel(letter):
    vowels = ["a", "e", "i", "o", "u"]
    for c in vowels:
        if c == letter:
            return True
    return False

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    remaining_guesses = 6
    warnings = 3
    unique_letters = 0
    list_of_guessed_letters = []
    current_state = get_guessed_word(secret_word, list_of_guessed_letters)
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("You have", warnings, "warnings.")
    print("--------------")
    print("You have", remaining_guesses, "guesses left.")

    while (not(is_word_guessed(secret_word, list_of_guessed_letters)) and remaining_guesses > 0):

        # list of all available letters without guessed letters
        available_letters = get_available_letters(list_of_guessed_letters)
        print("Available letters:", available_letters, end = '')

        # get user guessed_letter input and convert it to a lower case
        guessed_letter = str.lower(input("Please guess a letter: "))

        # if they entered a letter already guessed, or a non-letter, ask them to retry
        # handle warning cases here
        while (is_letter_present(list_of_guessed_letters, guessed_letter) or not str.isalpha(guessed_letter)):
            warnings -= 1
            if (is_letter_present(list_of_guessed_letters, guessed_letter)):
                print("Oops! You already guessed that letter. ", end = '')
            elif (not str.isalpha(guessed_letter)):
                print("Oops! That is not a valid letter. ", end = '')
            if warnings == 0:
                print("You have no warnings left so you lose a guess. Warnings are reset to 3.")
                remaining_guesses -= 1
                warnings = 3
            print("You have", warnings, "warnings left:", current_state)
            print("---------------------")
            print("You have", remaining_guesses, "guesses left.")
            print("Available letters:", available_letters, end = '')
            guessed_letter = input("Try again. Please guess a letter: ")

        # add guessed_letter to list of guessed letters
        list_of_guessed_letters += guessed_letter

        # get the state of the secret_word
        current_state = get_guessed_word(secret_word, list_of_guessed_letters)

        # check if the word is present in secret_word
        if (is_letter_present(secret_word, guessed_letter)):
            print("Good guess:", current_state)
            unique_letters += 1
        else:
            print("Oops! That letter is not in my word:", current_state)
            if is_vowel(guessed_letter):
                remaining_guesses -= 2
            else:
                remaining_guesses -= 1
        print("---------------------")
        print("You have", remaining_guesses, "guesses left.")

    if (is_word_guessed(secret_word, list_of_guessed_letters)):
        print("Well played! You guessed", secret_word)
        print("Your total score for this game is:", remaining_guesses * unique_letters)
    else:
        print("You lost! The secret word was", secret_word)

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)
# -----------------------------------

def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    if not(len(my_word) / 2 == len(other_word)):
        return False

    other_word_occurances = {}
    my_word_occurances = {}
    for c in other_word:
        if c in other_word_occurances:
            other_word_occurances[c] = other_word_occurances[c] + 1
        else:
            other_word_occurances[c] = 1
    for c in my_word:
        if c in my_word_occurances:
            my_word_occurances[c] = my_word_occurances[c] + 1
        else:
            my_word_occurances[c] = 1
    my_word_occurances.pop(" ", None)
    my_word_occurances.pop("_", None)

    for c in my_word_occurances:
        if not(c in other_word_occurances and other_word_occurances[c] == my_word_occurances[c]):
            return False

    for x in range(len(other_word)):
        if not(my_word[2 * x] == other_word[x] or my_word[2 * x] == "_"):
            return False
    return True

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for word in wordlist:
        if (match_with_gaps(my_word, word)):
            print(word, "", end = '')

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    remaining_guesses = 6
    warnings = 3
    unique_letters = 0
    list_of_guessed_letters = []
    current_state = get_guessed_word(secret_word, list_of_guessed_letters)
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("You have", warnings, "warnings.")
    print("--------------")
    print("You have", remaining_guesses, "guesses left.")

    while (not(is_word_guessed(secret_word, list_of_guessed_letters)) and remaining_guesses > 0):

        # list of all available letters without guessed letters
        available_letters = get_available_letters(list_of_guessed_letters)
        print("Available letters:", available_letters, end = '')

        # get user guessed_letter input and convert it to a lower case
        guessed_letter = str.lower(input("Please guess a letter: "))

        # if they entered a letter already guessed, or a non-letter, ask them to retry
        # handle warning cases here
        while (is_letter_present(list_of_guessed_letters, guessed_letter) or not str.isalpha(guessed_letter) or guessed_letter == "*"):
            if (guessed_letter == "*"):
                show_possible_matches(current_state)
            else:
                warnings -= 1
                if (is_letter_present(list_of_guessed_letters, guessed_letter)):
                    print("Oops! You already guessed that letter. ", end = '')
                elif (not str.isalpha(guessed_letter)):
                    print("Oops! That is not a valid letter. ", end = '')
                if warnings == 0:
                    print("You have no warnings left so you lose a guess. Warnings are reset to 3.")
                    remaining_guesses -= 1
                    warnings = 3
            print("\nYou have", warnings, "warnings left:", current_state)
            print("---------------------")
            print("You have", remaining_guesses, "guesses left.")
            print("Available letters:", available_letters, end = '')
            guessed_letter = input("Try again. Please guess a letter: ")

        # add guessed_letter to list of guessed letters
        list_of_guessed_letters += guessed_letter

        # get the state of the secret_word
        current_state = get_guessed_word(secret_word, list_of_guessed_letters)

        # check if the word is present in secret_word
        if (is_letter_present(secret_word, guessed_letter)):
            print("Good guess:", current_state)
            unique_letters += 1
        else:
            print("Oops! That letter is not in my word:", current_state)
            if is_vowel(guessed_letter):
                remaining_guesses -= 2
            else:
                remaining_guesses -= 1
        print("---------------------")
        print("You have", remaining_guesses, "guesses left.")

    if (is_word_guessed(secret_word, list_of_guessed_letters)):
        print("Well played! You guessed", secret_word)
        print("Your total score for this game is:", remaining_guesses * unique_letters)
    else:
        print("You lost! The secret word was", secret_word)

# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.

if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
    
    testtest = True
    if testtest:
        x = 1
    else:
        y = 1
        
    
    
    
    
