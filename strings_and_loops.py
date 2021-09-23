# Python Program 3 - Strings and Loops (ENGR4)
# Written by Luke Frank
# 9/21/21

# Program splits sentence into array of words.
# Program uses for loop to print each letter of word.
# End of each word, program print (-).
 

user_input = input('Type in your sentence: ')

sentence = user_input.split()
# split() creates index with each sentence seperaate.

for word in sentence:
    # No need to use range() becaue Python recognizes an index and so will set 
    # run "word" through each word in the setence index. 
        
    for char in word:
    # Python recognizes "word" as a str and will set char to each character in it.
        print(char)
    
        
    print("-")
    # Seperate each word with a (-) 
    
# Note that another way to seperate a word into an array of characters 
# is to use the list() function. 
    