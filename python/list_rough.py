# Python Program 3 - Strings and Loops (ENGR4)
# Written by Luke Frank
# 9/21/21

# Program splits sentence into array of words.
# Program uses for loop to print each letter of word.
# End of each word, program print (-).
 

# word = 'hi'

# newlist = []

# for char in word:
#     print(char)






# Method 1:
    # fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    # newlist = []
    
    # for x in fruits:
    #   if "a" in x:
    #     newlist.append(x)
    
    # print(newlist)

# Method 2:

    # fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    
    # newlist = [x for x in fruits if "a" in x]
    
    # print(newlist)

   
user_input = (input('Your sentence: '))

sentence = user_input.split()

for i in sentence:
    


    
    letters = list(i)
    
    print(letters)
    
    # for test in range(0, len(letters)):
        
    #     letter = letters[test]
    #     print(letter)
    
    # print("-")
        
        
        
