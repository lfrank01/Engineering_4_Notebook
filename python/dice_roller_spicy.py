# Automatic Dice Roller
# Written by Luke Frank 

# This code will generate a random integer between 1 and 6 when the 
# user writes enter. In addition, when the user types "x" into the
# terminal the program will cancel. 

from random import randint
# Import from the library "random" the class "randint"
# Randint wil accept argument (start value, end value), and it 
# will then choose a pseudo random integer in between the two values.

print("Automatic Dice Roller")
print("(enter)=run, (c)=change settings, (x)=exit")

num_sides = input('Number of sides: ')
num_rolls = input('Number of rolls: ')

# Create loop
while True:
    # Note that "=" is equivalnt to "is," setting one value or 
    # variable to another, while "==" is a comparison operator, asking 
    # "is this equal to that."
    
    answer = input('Enter to roll: ')
    
    if answer == "":
        for i in range(int(num_rolls)):
            dice_roll = randint(1, int(num_sides))
            print(dice_roll)
            # num_sides and num_rolls must be converted to integers from being strings.
    
    if answer == "c":
        num_sides = input('Number of sides: ')
        num_rolls = input('Number of rolls: ')
    
    if  answer == "x":
        break
        # The "break" statement exits out of a loop.
    