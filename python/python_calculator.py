# Python Calculator
# Written by Luke Frank 
# 9/14/21

# This code will run return the sum, difference, quotient, and modulo 
# of two numbers inputed to the system. 

print("Calculator Program \n")


def doMath(first_num, second_num, option):
    
    if option == 1:
        # This is.
        return (first_num + second_num)
        
    if option == 2:
        # This is difference.
        return (first_num - second_num)
        
    if option == 3:
        # This is product.
        return (first_num * second_num)
        # An aserisk indicates multiplication.
        
    if option == 4:
        # This is quotient
        return round((first_num / second_num), 2)
        
    if option == 5:
        # This is modulo
        return(first_num % second_num)
    
a = int(input('Input your first number: '))
b = int(input('Input your second number: '))

# It's neccesary to convert to an integer because the input wil come 
# in a string/str format, which cannot do math operations.

print("Sum:\t\t" + str(doMath(a, b, 1)))
print("Difference:\t" + str(doMath(a, b, 2)))
print("Product:\t" + str(doMath(a, b, 3)))
print("Quotient:\t" + str(doMath(a, b, 4)))
print("Modulo:\t\t" + str(doMath(a, b, 5)))
    