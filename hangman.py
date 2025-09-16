# create a greeting
# create your word list
# randomly choose a word from the list you have created
# ask the user to guess a letter
# bonus make the program take the input from the user and make it lowercase
# check if the letter is in the word

import random
print('Hello! Welcome to hangman!')
words = ['what','fight','dante']
secret_word = random.choice(words)
guess = input('Please guess a letter: ').lower()
for letter in secret_word:
    if letter == guess:
        print('RIGHT!')
    else:
        print('wrong')