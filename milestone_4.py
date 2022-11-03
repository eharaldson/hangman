import random

class Hangman:

    # Class constructor
    def __init__(self, word_list, num_lives=5):

        self.word = random.choice(word_list)                # Random word from the list to be guessed.
        self.word_guessed = ['_' for x in self.word]        # List of letters guessd. _ if not been guessed yet.
        self.num_letters = len(set(self.word))              # Number of unique letters in the word to be guessed.
        self.num_lives = num_lives                          # Number of lives left.
        self.word_list = word_list                          # List of words to pick from.
        self.list_of_guesses = []                           # Letters that have been guessed by player.

    # Methods
    def check_guess(self, guess):
        guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

        self.list_of_guesses.append(guess)

    def ask_for_input(self):
        while True:
            guess = input("Enter a letter: ")
            if len(guess) != 1 or guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                break

game1 = Hangman(['apple', 'banana'])
print(game1.num_letters)
game1.ask_for_input()
print(game1.word_guessed)
print(game1.num_letters)
print(game1.list_of_guesses)