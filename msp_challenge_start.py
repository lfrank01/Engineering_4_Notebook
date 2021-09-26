# Python Challenge - MSP (ENGR4)
# Written by Luke Frank
# 9/26/21

# This code is for the MSP Engineering 4 assignment. The goal is to develop a program
# that can simulate a game of hang man. 

# 3 functions should probably be used:
# (1) A function that requests a guess from the user. 
# (2) A function that generates the hangman graphic, the letters guessed, and the blank letters. 
# (3) A function that asks if the user wants to play again. It is not necessary 
# to use the same function structure as I did, but I thought it might help some of you to get started.

print('Hangman Game')

    
def hangman_string(number: int):
    characters = [
        "",                     # 0
        "|----\n    |\n    0",  # 1
        "|----\n    |\n    0\n    |\n", # 2
        "|----\n    |\n    0\n   \|\n", # 3
        "|----\n    |\n    0\n   \|/\n", # 4
        "|----\n    |\n    0\n   \|/\n    |\n", # 5
        "|----\n    |\n    0\n   \|/\n    |\n   /\n", # 6
        "|----\n    |\n    0\n   \|/\n    |\n   / \ \n", # 7
        ]
    return characters[number]
    
def check_letter(guessed_letter, word_before_guess, secret_word):
    answer = list(word_before_guess)  # convert existing word to a list of characters
    for position, character in enumerate(secret_word):
        if character == guessed_letter:  # we found a match
            answer[position] = guessed_letter
    joined_answer = ''.join(answer)  # this joins the list of characters into a string
    return joined_answer

secret_word = input("Player 1 choose your word: ")
word_before_guess = "-" * len(secret_word)
wrong_guesses = 0

while wrong_guesses < 7:
    print("The word you have to guess is: ", word_before_guess)
    guessed_letter = input("Player 2: enter your guessed letter: ")
    word_after_guess = check_letter(
        guessed_letter, 
        word_before_guess, 
        secret_word
        )
    
    if word_after_guess == word_before_guess:
        wrong_guesses = wrong_guesses + 1
        print ("Wrong! One step closer to hanging..")
        print(hangman_string(wrong_guesses))
    else:
        print("You got a letter correct!")
        print(word_after_guess)
        word_before_guess = word_after_guess
        if word_after_guess == secret_word:
            print("Hooray! You did it!")
            print("The word was: ", secret_word)
            print("Your word was: ", word_after_guess)
            print("You escaped the hangman.")
            break
