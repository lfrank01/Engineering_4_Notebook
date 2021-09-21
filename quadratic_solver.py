# Python Program 2 - Quadratic Sover (ENGR4)
# Written by Luke Frank
# 9/20/2

from math import sqrt
# This assignent stated that Python has no built-in operation for taking a 
# square root of something, meaning that a function had to be imported. 
# However, I found by experimenting that taking the exponent (**) of (1/2)
# does in fact act as taking the square root.

print('Quadratic Solver')
print('\nEnter the coefficients for ax^2 + bx + c = 0')

a = int(input('Input for a: '))
b = int(input('Input for b: '))
c = int(input('Input for c: '))

while True:
    
    print('\nCalculating discriminant...')

    discriminant = b**2 - 4*a*c
    # A double asterisk (**) is used for an exponent.
    
    if discriminant < 0:
        print('Negative discriminant: no real roots.')
        
    # A negative discriminant means that there aren't any roots.
    
    else:
        print('Dicriminant is: ' + str(discriminant))
        print('\nCalculating roots...')
        
        root_1 = (-b+sqrt(b**2 - 4*a*c))/2*a
        root_2 = (-b-sqrt(b**2 - 4*a*c))/2*a
        
        print('Root 1 = ' + str(root_1))
        print('Root 2 = ' + str(root_2))
        
    answer = input('Note - (enter) to run again, then (x) + (enter) to break: ')
    
    if answer == "":
        a = int(input('Input for a: '))
        b = int(input('Input for b: '))
        c = int(input('Input for c: '))
        
    if answer == "x":
        print('Exit')
        break
