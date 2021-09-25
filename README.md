# Engineering_4_Notebook
This repository contains documentation of Engineering 4 assignments and projects.

Note to self: for each assignment's documentation, there should be the assignment description, evidence, wiring (if applicable), and reflection.

## Python_Dice_Roller

### Assignment Description

The Python Dice Roller assignment was the first Python assignments in Engineering IV besides the introductory Hello Python assignment. The purpose of the assignment was to create a Python program that could automatically roll dice. In addition, the program had to take user input of whether it would re-roll or exit the program after it had done its initial roll. For the spicy part of this assignment, the program had to also take user input on the number of sides that the dice should have and also how many dice were to be rolled. The spicy part also had to give the user the option of changing the settings in addition to choosing to either exit the prom or re-roll

### Evidence 

Vanilla version:

![Vanilla Dice Roller](/Engineering_IV-Vanilla_Dice_Roller.png)

Spicy version:

![Spicy Dice Roller](/Engineering_IV-Spicy_Dice_Roller.png)

### Wiring

No wiring was required for this assignment. 

### Reflection

The Python Dice Roller assignment was a relatively simple assignment, being one of the first coding assignments of the school year. However, there were nuanced aspects of this assignment that had not been covered before in Engineering IV and lessons learned

* The 'input()' function allows a variable to be set to somethign a user types in. For example, `num_sides = input('Number of   sides: ') allowed users to choose how many sides they wanted their die to have. This variable was then called in the code later on.
  
* There is a difference between `==` and `=`. Using `==` asks "Is this equal to that?" whereas `=` says "This **is** equal to that.  

* More information can be found in the code  comments.


## Python_Calculator

### Assignment Description

The Python Calculator was a step more dificult than the Dice Roller assignment, incorpating what was learned in the Dice Roller asingment, such as the `input()` function. The assignment's nuanced element was that it required a function to be made that also have different if statements that performed different operations. The task was to design code to ask user input for two different numbers and then perofrm a series of operation on those numbers and print them. The operations were the sum, difference, product, quotient, modulo, and for the spicy section, factorials. 

### Evidence 

Vanilla version:

![Vanilla Calculator](/Engineering_IV-Vanilla_Calculator.png)

Spicy version:

![Spicy Calculator](/Engineering_IV-Spicy_Calculator.png)

### Wiring

No wiring was required for this assignment. 

### Reflection

This assignment was initially confusing, but once I figured out that only one function was needed to perform the operations and that the operations could be simply called using if statements, it made more sense. Here were some lessons learned:

* In a print statement writing `\t` creates a tab in the print line, which is helpful for formatting consecuitve print statements.

* A print function can incoporate a function by writing something like `print(str(doMath(a, b, 6)))`. Note that the 6 meant that the sixth if statement was being called, in this case the 1st factorial.

* It's helpful to ask other students for help. By asking what somebody did for a certain aspect of the code, there's a chance to have a new perspective on the topic, which can then be modified and made original. In this case, asking advice for how to create a factorial calculator was helpful.

* More information can be found in the code comments. 


## Quadratic Solver

### Assignment Description

The quadratic solver asignment required code to be designed that could calculate the roots of a quadratic function (ax^2 + bx +c) when given user input for a, b, and c. 
Some alebra had to be recalled to remember how to calculate the discriminant ((-b +/- sqrt(b^2-4ac))/2a), and for the spicy section of the assignment, the greatest challenge was to write code that could print out the function in vertex form, as it was initially hard to algebraically convert from standard to vertex form. This assignemnt taught valuble lessons of how to represent algebraic equations in a coding environment.

### Evidence 

Vanilla version:

![Vanilla Quadratic Solver](/Engineering_IV-Quadratic_Solver.png)

Spicy version:

![Spicy Quadratic Solver Correct](/Engineering_IV-Quadratic_Solver_Spicy_Correct.png)

### Wiring

No wiring was required for this assignment. 

### Reflection

I had to remember some basic algebra terms like the discriminant and vertex form for this assignment. This wasn't dificult, but it was more challenging to convert from standard from to vertex form. Here are the lessons I learned:

* First of all, having a reliable code environment is helpful. I was using [this coding IDE](https://www.online-python.com/), but because it was randomly freezing on me, I swithced to [this](https://www.onlinegdb.com/online_python_compiler) more reliable one. However, the spicy version of code was run on the [unreliable IE](https://www.online-python.com/) because the other was not registering f strings.

* Going off of that, f strings are a really helpful Python 3 tool that allows variables to be called in print statements without having to use `str()` each time. This made the printing of the vertex form and discriminant much easier.

* Make sure to read the assignment's requirements. I got functioning code the first time I did this assignment, but it didn't use f strings and functions like the assignment asked, so I re-did it.

* The assignment stated that because Python didn't have a built-in square root operator, the class `function` from the library `math` had to be used. However, I tested simply taking the exponent to the 1/2 or `**(1/2)`, and this worked just as well, suggesting that Python does in fact have a built-in square root operator.

* More lessons can be found in the code comments 


## Strings and Loops

### Assignment Description

The code for the Strings and Loops assignment had to make it so that when a sentence was typed from user input, the terminal would print out the sentence, one character at a time, with a dash between each word. In order to this, nested for-loops had to be used. Also, for the spicy version of this assignment, the challenege was to make the code as condensed as possible. To do this, the code had to incorporate "list comprehension," which is a method of condensing nested for-loops in Python. 

### Evidence 

Vanilla version:

![Vanilla Strings and Loops](/Engineering_IV-Strings_And_Loops.png)

Spicy version:

![Spicy Strings and Loops](/Engineering_IV-strings_and_loops_spicy.png)

### Wiring

No wiring was required for this assignment. 

### Reflection

This assignment took a while for me, but as a result of it I now understand list comprehension and ways to condense code much better. Here are some reflections:

* Google is your friend. When I was confused about list comprehension, I Googled it and found several pages explaining how it works. 

* GitHib is your friend. It doesn't hurt to draw inspiration from other people. 

* The `split()` function works to seperate a sentence into an index of words in str format. This was helpful to seperate the user input into an index that could be called with a for loop.
 
* The `len()` function is helpful for finding the length of a str. It's also helpful when making a for loop.

* Finally, list comprehension is a good tool for condensing nested for-loops, and it's something that's unique to Python. (Here)[https://www.w3schools.com/python/python_lists_comprehension.asp] is an article about list comprehension that I found helpful.

* Code comments have additional info.
