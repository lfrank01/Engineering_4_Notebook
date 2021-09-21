# Python Program 2 - Quadratic Solver (ENGR4)
# Written by Luke Frank
# 9/20/2

from math import sqrt
# This assignment stated that Python has no built-in operation for taking a 
# square root of something, meaning that a function had to be imported. 
# However, I found by experimenting that taking the exponent (**) of (1/2)
# does in fact act as taking the square root.

print('Quadratic Solver')
print('\nEnter the coefficients for ax^2 + bx + c = 0')

def get_discriminant(a, b, c):
    
    discriminant = b**2 - 4*a*c
    return discriminant

def get_roots(a, b, c):
    
    print('\nCalculating roots...')
        
    root_1 = ((-b+sqrt(b**2 - 4*a*c))/2*a)
    root_2 = ((-b-sqrt(b**2 - 4*a*c))/2*a)
    
    print('Root 1 = ' + str(root_1))
    print('Root 2 = ' + str(root_2))
    
def get_vertex_form(a, b, c):
    # Note that (c) must be called becuse get_discriminant() uses it.
    discriminant = get_discriminant(a, b, c)
    
    # This is how to calculate vertex form:
    print('\nVertex form formula is y = a(x-h)^2 + k')
    h = (-b/(2*a))
    k = (-(discriminant)/(4*a))
    print(f"Vertex form: y = {a}(x-{h})+{k}")

user_input = ""

while user_input != "x":
    
    a = int(input('Input for a: '))
    b = int(input('Input for b: '))
    c = int(input('Input for c: '))

    print(f"You entered {a}x^2 + {b}x + {c} = 0")
    
    if get_discriminant(a, b, c) < 0:
        print('Discriminant is less than 0. No real roots.')
    
    else:
        get_roots(a, b, c)
        get_vertex_form(a, b, c)
        
    user_input = input('\nNote - (enter) to run again, then (x) + (enter) to break: ')
    
print("Program has been exited.")
