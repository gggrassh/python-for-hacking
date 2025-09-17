# create am empty list
# for each letter in the secret_word add a "_" that will be
# printed to the console
# example if the word is Hacker "_" "_" "_" "_" "_" "_"
# loop through each of the letters in the chosen word
# if the letter is in the word replace the "_" with the letter
# it should look like this "_" "_" "c" "_" "_" "_"

import random
print('Hello! Welcome to hangman!')
words = ['what','fight','dante']
display = []
secret_word = random.choice(words).lower()
for letter in secret_word:
    display += "_"
print(display)
game_over = False
num = 0
while not game_over:
    guess = input('Guess a letter: ').lower()
    for position in range(len(secret_word)):
        if guess == secret_word[position]:
            display[position] = guess
    if guess not in secret_word:
        num += 1
        guess_left = 5 - num
        print(f'you guessed wrong, you have {guess_left} guesses left')
        if num >= 5:
            print('You lose!')
            game_over = True
    print(display)

    if "_" not in display:
        print('You win!')
        game_over = True