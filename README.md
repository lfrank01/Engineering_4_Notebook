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
 
