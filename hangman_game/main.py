import random
import hangman_art
from hangman_words import word_list
import os

chosen_word = random.choice(word_list)
word_lenght = len(chosen_word)
end_of_game = False
lives = 6

print(hangman_art.logo)

# testing code
#print(f"Pssst, the solution is {chosen_word}.")

# create a function to clear terminal after each guess
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# create blanks
display = []
for letter in range(word_lenght):
    display.append("_")

while not end_of_game:
    # Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Guess a letter:\n").lower()
    clear()
    # let a user know they guessed a letter already
    if guess in display:
        print(f"You've already guessed \"{guess}\".")
    #check guessed letter
    for letter in range(word_lenght):
        if chosen_word[letter] == guess:
            display[letter] = guess
    # check if user is wrong
    if guess not in chosen_word:
        # if the letter is not in chosen_word, print out a letter and let them know it's not in the word
        print(f"You guessed \"{guess}\", it's not in word. You lose a life!")
        lives -= 1

     #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")


    # check if user has got all letters
    if "_" not in display:
        end_of_game = True
        print("\nYou won!")
    elif lives == 0:
        end_of_game = True
        print("\nYou lose!")

    # print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(hangman_art.stages[lives])
    

