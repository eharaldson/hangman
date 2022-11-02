import random

def num_unique(ls):
    ls_set = set(ls)
    return len(ls_set)

class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)                # Random word from the list to be guessed.
        self.word_guessed = ['_' for x in self.word]        # List of letters guessd. _ if not been guessed yet.
        self.num_letters = num_unique(self.word)            # Number of unique letters in the word to be guessed.
        self.num_lives = num_lives                          # Number of lives left.
        self.word_list = word_list                          # List of words to pick from.
        self.list_of_guesses = []                           # Letters that have been guessed by player.

    
