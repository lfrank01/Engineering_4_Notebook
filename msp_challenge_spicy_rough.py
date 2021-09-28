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
    # Create hangman steps. \n used to condense lines. 
    
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
    
    # In a for loop, if there is a variable, comma, then a variable, the first variable will represent
    # the index number and the second will represent the character that is that number in the string.
    
    for position, character in enumerate(secret_word):
        if character == guessed_letter:  # we found a match
            answer[position] = guessed_letter
            
    joined_answer = ''.join(answer)  # this joins the list of characters into a string
    
    return joined_answer

def clear_screen(num_times: int):
    print('\n' * num_times)

def wrong_letter_bank(incorrect_letters):
    word_bank = ', '.join(incorrect_letters)
    
    return word_bank

play_again = ""


while play_again != "x":

    secret_word = input("Player 1 choose your word: ")

    incorrect_letters = []
    word_before_guess = "-" * len(secret_word)
    wrong_guesses = 1
    
    clear_screen(50)
    
    # Print starting hangman
    print(hangman_string(wrong_guesses))

    while wrong_guesses < 7:
        
        clear_screen(1)
        
        # Print guessed secret word
        print('The word is: ' + word_before_guess)
        
        clear_screen(1)
        
        guessed_letter = input('Player 2: enter your guessed letter: ')
        
        clear_screen(50)
        
        word_after_guess = check_letter(
            guessed_letter, 
            word_before_guess, 
            secret_word
            )
        
        if word_after_guess == word_before_guess:
            wrong_guesses = wrong_guesses + 1
            incorrect_letters.append(guessed_letter)
            print("Wrong! One step closer to hanging..")
            
            word_bank = wrong_letter_bank(incorrect_letters)
            
            
        else:
            print("You got a letter correct!")
            word_before_guess = word_after_guess
            
            if word_after_guess == secret_word:
                clear_screen(1)
                print("Hooray! You did it!")
                print("The word was: ", secret_word)
                print("You escaped the hangman.")
                break
        
        clear_screen(1)
        
        print(hangman_string(wrong_guesses))
        
        clear_screen(1)
        
        print('Missed letters: ' + word_bank)
        
    play_again = input('enter to go again, x + enter to quit')
    
    if play_again == "":
        wrong_guesses = 1
    
print('Thanks for playing')