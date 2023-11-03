import random
import os

word_list = ['good', 'night', 'anxiety', 'depression']
word = random.choice(word_list)
attempts = 5
guessed_letters = []
display_word = ['_'] * len(word)

while attempts > 0:
    print(f'Lives left: {attempts}')
    print(' '.join(display_word))
    letter = input('Guess a letter: ').lower()
    os.system('cls')

    if letter in guessed_letters:
        print('You already guessed that letter!')
        attempts -= 1
    else:
        guessed_letters.append(letter)
        if letter in word:
            for index, char in enumerate(word):
                if char == letter:
                    display_word[index] = letter
        else:
            print('No match...')
            attempts -= 1

    if ''.join(display_word) == word:
        print(f'You WON...!\nThe word was "{word}"')
        break


if attempts == 0:
    print(f'Ran out of moves...\nGAME OVER!\nThe word was "{word}"')

print('Thanks for playing!')
