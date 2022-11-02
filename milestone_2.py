# Task 1
# %%
word_list = ['Watermelon', 'Apple', 'Mango', 'Banana', 'Raspberry']

print(word_list)

# Task 2
# %%
import random

word = random.choice(word_list)

print(word)

# Task 3
# %%
guess = input("Enter a letter: ")

# Task 4
# %%
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    "Oops! That is not a valid input."
