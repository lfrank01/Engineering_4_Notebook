# Python Calculator
# Written by Luke Frank 
# 9/14/21

# This code will run return the sum, difference, quotient, and modulo 
# of two numbers inputed to the system. 

print("Calculator Program \n")


def doMath(first_num, second_num, option):
    
    if option == 1:
        # This is sum.
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
        # This is modulo.
        return(first_num % second_num)
        
    if option == 6:
        # This is first factorial.
        
        factorial = 1
        
        for i in range(1, first_num + 1):
            factorial = factorial * i 
            
        # The factorial is calculated by using a "for i in range()"" loop.
        # The parameters of range are set to 1 and the inputed number + 1
        # becuse if the range began at zero, the factorial would be multiplied by 
        # 0, and the inputed number is added to by 1 so that the correct range of 
        # numbers will be used. Because python ranges begin with 0, if 0 is added to by 1,
        # so should the inputed number to preserve the correct range.
        
        return(str(factorial))
        
    if option == 7:
        # This is second factorial.
        
        factorial = 1
        
        for i in range(1, second_num + 1):
            factorial = factorial * i 
        
        return(str(factorial))
    
a = int(input('Input your first number: '))
b = int(input('Input your second number: '))

# It's necessary to convert to an integer because the input wil come 
# in a string/str format, which cannot do math operations.

# print("Sum:\t\t" + str(doMath(a, b, 1)))
# print("Difference:\t" + str(doMath(a, b, 2)))
# print("Product:\t" + str(doMath(a, b, 3)))
# print("Quotient:\t" + str(doMath(a, b, 4)))
# print("Modulo:\t\t" + str(doMath(a, b, 5)))
print("1st Factorial:\t\t" + str(doMath(a, b, 6)))
print("2nd Factorial:\t\t" + str(doMath(a, b, 7)))
    