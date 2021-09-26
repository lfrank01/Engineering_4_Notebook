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

def hangman_builder(option):
    
    # Max number of turns before complete hang man = 7
    
    if option == 1: 
        print("|----")
        print("    |")
        print("    0")
    
def ask_guess():
    pass

secret_word = input("Player 1 choose your word: ")

hangman_builder(1) 

print("Missed Letters: ")
print("Secret Word = " + ("-" * len(secret_word)))
print("Guess a letter: ")    
    