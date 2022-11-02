# Task 1 & 2 & 3
# %%
import random

word_list = ['Watermelon', 'Apple', 'Mango', 'Banana', 'Raspberry']

word = random.choice(word_list)

def check_guess(guess):
    '''
    DOCSTRING: Checks if the guessed letter is in the word
    INPUT: guess (str)
    OUTPUT: N/A
    '''

    guess = guess.lower()

    if guess in word:
        print("Good guess! " + guess + " is in the word.")
    else:
        print("Sorry, " + guess + " is not in the word. Try again.")

def ask_for_input():
    '''
    DOCSTRING: Asks for input letter from user and checks if it is in the word
    INPUT: N/A
    OUTPUT: N/A
    '''

    while True:

        guess = input("Enter a letter: ")

        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

    check_guess(guess)

ask_for_input()
