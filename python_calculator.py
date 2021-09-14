# Python Calculator
# Written by Luke Frank 
# 9/14/21

# This code will run return the sum, difference, quotient, and modulo 
# of two numbers inputed to the system. 

print("Calculator Program")

def doMath(first_num, second_num, option):
    if option == 1:
        return str(int(first_num) + int(second_num))
    
first_num = input('Input your first number: ')
second_num = input('Input your second number: ')

doMath(first_num, second_num, option)
# Work in progress currently.

# Note - Make sure quotient is rounded to 2 digits.
# Note - Modulo = remainder after division

# Last 5 lines of code should be:
    # print("Sum:\t\t" + doMath(a,b,1))
    # print("Difference:\t" + doMath(a,b,2))
    # print("Product:\t" + doMath(a,b,3))
    # print("Quotient:\t" + doMath(a,b,4))
    # print("Modulo:\t\t" + doMath(a,b,5))