#INTERMEDIATE LEVEL - HANGMAN GAME
#Implement word guessing game.
import random

# List of words to guess from
word_list = ["python", "hangman", "program", "developer", "keyboard", "language"]
chosen_word = random.choice(word_list)

# Visuals for hangman progress
hangman_stages = [
    '''
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    ''',
    '''
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    ''',
    '''
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    ''',
    '''
     -----
     |   |
     O   |
    /|   |
         |
         |
    =========
    ''',
    '''
     -----
     |   |
     O   |
     |   |
         |
         |
    =========
    ''',
    '''
     -----
     |   |
     O   |
         |
         |
         |
    =========
    ''',
    '''
     -----
     |   |
         |
         |
         |
         |
    =========
    '''
]

lives = 6
display = ['_' for _ in chosen_word]
guessed_letters = []

# Game loop
print(" Welcome to Hangman!\n")

while lives > 0 and '_' in display:
    print(hangman_stages[6 - lives])
    print("Word: ", ' '.join(display))
    print(f"Guessed letters: {', '.join(guessed_letters)}")

    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print(" Please enter a single letter.\n")
        continue

    if guess in guessed_letters:
        print(" You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
        print("Good guess!\n")
    else:
        lives -= 1
        print(" Wrong guess! Lives left:", lives, "\n")

# Final result
if '_' not in display:
    print(" You won! The word was:", chosen_word)
else:
    print(hangman_stages[6 - lives])
    print(" You lost. The word was:", chosen_word)
    