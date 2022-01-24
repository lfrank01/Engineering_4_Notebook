# Python Program 3 - Strings and Loops (ENGR4)
# Written by Luke Frank
# 9/23/21

# Program splits sentences into an array of words.
# Program uses for loop to print each letter of word.
# End of each word, program print (-).

# This code uses list comprehension to condense the number of lines.

# This looks pretty hard to read, so I will outline each part:

# 1: 
    # input('Type in your sentence: ').replace(" ", "-") + "-" takes the users input, 
    # which would be in a sentence, and replaces each space with a "-"
    
    # Then the "-" at the end adds a "-" to the end of the string.

# 2: 
    # print(char) for char is a condensed way of doing this:
        # for char in input():
            # print(char)

# 3: The [] outside of the code is what's necessary to do list comprehension.
    

[print(char) for char in input('Type in your sentence: ').replace(" ", "-") + "-"]


# Here is an alternative method, using 3 lines and the split() function

# for word in input('Type in your sentence: ').split():
    
#     for char in word:
#         print(char)
    