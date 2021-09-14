# Automatic Dice Roller
# Written by Luke Frank 

# This code will generate a random integer between 1 and 6 when the 
# user writes enter. In addition, when the user types "x" into the
# terminal the program will cancel. 

from random import randint
# Import from the library "random" the class "randint"
# Randint wil accept argument (start value, end value), and it 
# will then choose a pseudo random integer in between the two values.

print ("Automatic Dice Roller")

# Create loop
while True:
    # Note that "=" is equivalnt to "is," setting one value or 
    # variable to another, while "==" is a comparison operator, asking 
    # "is this equal to that."
    
    answer = input('Enter to roll: ')
    
    if answer == "":
        dice_roll = randint(1, 6)
        print(dice_roll)
        
    if  answer == "x":
        break






    