# Engineering_4_Notebook
This repository contains documentation of Engineering 4 assignments and projects.

Note to self: for each assignment's documentation, there should be the assignment description, evidence, wiring (if applicable), and reflection.

## Python_Dice_Roller

### Assignment Description

The Python Dice Roller assignment was the first Python assignment in Engineering IV besides the introductory Hello Python assignment. The purpose of the assignment was to create a Python program that could automatically roll dice. In addition, the program had to take user input of whether it would re-roll or exit the program after it had done its initial roll. For the spicy part of this assignment, the program had to also take user input on the number of sides that the dice should have and also how many dice were to be rolled. The spicy part also had to give the user the option of changing the settings in addition to choosing to either exit the prom or re-roll

### Evidence 

Vanilla version:

![Vanilla Dice Roller](/Engineering_IV-Vanilla_Dice_Roller.png)

Spicy version:

![Spicy Dice Roller](/Engineering_IV-Spicy_Dice_Roller.png)

### Wiring

No wiring was required for this assignment. 

### Reflection

The Python Dice Roller assignment was a relatively simple assignment, being one of the first coding assignments of the school year. However, there were nuanced aspects of this assignment that had not been covered before in Engineering IV and lessons learned

* The 'input()' function allows a variable to be set to something a user types in. For example, `num_sides = input('Number of sides: ') allowed users to choose how many sides they wanted their die to have. This variable was then called in the code later on.
  
* There is a difference between `==` and `=`. Using `==` asks "Is this equal to that?" whereas `=` says "This **is** equal to that.  

* More information can be found in the code comments.


## Python_Calculator

### Assignment Description

The Python Calculator was a step more difficult than the Dice Roller assignment, incorporating what was learned in the Dice Roller assignment, such as the `input()` function. The assignment's nuanced element was that it required a function to be made that also have different if statements that performed different operations. The task was to design code to ask user input for two different numbers and then perform a series of operations on those numbers and print them. The operations were the sum, difference, product, quotient, modulo, and for the spicy section, factorials. 

### Evidence 

Vanilla version:

![Vanilla Calculator](/Engineering_IV-Vanilla_Calculator.png)

Spicy version:

![Spicy Calculator](/Engineering_IV-Spicy_Calculator.png)

### Wiring

No wiring was required for this assignment. 

### Reflection

This assignment was initially confusing, but once I figured out that only one function was needed to perform the operations and that the operations could be simply called using if statements, it made more sense. Here were some lessons learned:

* In a print statement writing `\t` creates a tab in the print line, which is helpful for formatting consecutive print statements.

* A print function can incorporate a function by writing something like `print(str(doMath(a, b, 6)))`. Note that the 6 meant that the sixth if statement was being called, in this case, the 1st factorial.

* It's helpful to ask other students for help. By asking what somebody did for a certain aspect of the code, there's a chance to have a new perspective on the topic, which can then be modified and made original. In this case, asking for advice on how to create a factorial calculator was helpful.

* More information can be found in the code comments. 


## Quadratic Solver

### Assignment Description

The quadratic solver assignment required code to be designed that could calculate the roots of a quadratic function (ax^2 + bx +c) when given user input for a, b, and c. 
Some algebra had to be recalled to remember how to calculate the discriminant ((-b +/- sqrt(b^2-4ac))/2a), and for the spicy section of the assignment, the greatest challenge was to write code that could print out the function in vertex form, as it was initially hard to algebraically convert from standard to vertex form. This assignment taught valuable lessons on how to represent algebraic equations in a coding environment.

### Evidence 

Vanilla version:

![Vanilla Quadratic Solver](/Engineering_IV-Quadratic_Solver.png)

Spicy version:

![Spicy Quadratic Solver Correct](/Engineering_IV-Quadratic_Solver_Spicy_Correct.png)

### Wiring

No wiring was required for this assignment. 

### Reflection

I had to remember some basic algebra terms like the discriminant and vertex form for this assignment. This wasn't difficult, but it was more challenging to convert from standard form to vertex form. Here are the lessons I learned:

* First of all, having a reliable code environment is helpful. I was using [this coding IDE](https://www.online-python.com/), but because it was randomly freezing on me, I switched to [this](https://www.onlinegdb.com/online_python_compiler) more reliable one. However, the spicy version of code was run on the [unreliable IE](https://www.online-python.com/) because the other was not registering f strings.

* Going off of that, f strings are a really helpful Python 3 tool that allows variables to be called in print statements without having to use `str()` each time. This made the printing of the vertex form and discriminant much easier.

* Make sure to read the assignment's requirements. I got functioning code the first time I did this assignment, but it didn't use f strings and functions like the assignment asked, so I re-did it.

* The assignment stated that because Python didn't have a built-in square root operator, the class `function` from the library `math` had to be used. However, I tested simply taking the exponent to the 1/2 or `**(1/2)`, and this worked just as well, suggesting that Python does in fact have a built-in square root operator.

* More lessons can be found in the code comments 


## Strings and Loops

### Assignment Description

The code for the Strings and Loops assignment had to make it so that when a sentence was typed from user input, the terminal would print out the sentence, one character at a time, with a dash between each word. In order to do this, nested for-loops had to be used. Also, for the spicy version of this assignment, the challenge was to make the code as condensed as possible. To do this, the code had to incorporate "list comprehension," which is a method of condensing nested for-loops in Python. 

### Evidence 

Vanilla version:

![Vanilla Strings and Loops](/Engineering_IV-Strings_And_Loops.png)

Spicy version:

![Spicy Strings and Loops](/Engineering_IV-Strings_And_Loops_Spicy.png)

### Wiring

No wiring was required for this assignment. 

### Reflection

This assignment took a while for me, but as a result of it I now understand list comprehension and ways to condense code much better. Here are some reflections:

* Google is your friend. When I was confused about list comprehension, I Googled it and found several pages explaining how it works. 

* GitHub is your friend. It doesn't hurt to draw inspiration from other people. 

* The `split()` function works to separate a sentence into an index of words in str format. This was helpful to separate the user input into an index that could be called with a for loop.
 
* The `len()` function is helpful for finding the length of a str. It's also helpful when making a for loop.

* Finally, list comprehension is a good tool for condensing nested for-loops, and it's something that's unique to Python. [Here](https://www.w3schools.com/python/python_lists_comprehension.asp) is an article about list comprehension that I found helpful.

* Code comments have additional info.


## Hangman/MSP Challenge

### Assignment Description

For the MSP Challenge assignment, the goal was to create a functioning hangman game. To do this, several functions had to be created that divided up the tasks, since the assignment as a whole was relatively complicated. The basis of the code was to create a function that generated the hangman image and a function that checked user input of a guessed letter and determined whether it was part or not part of the secret word. 

### Evidence 

Vanilla / Some Spice version:

![MSP Challenge](/Engineering_IV-MSP_Challenge_1.png)

### Wiring

No wiring was required for this assignment. 

### Reflection

The MSP Challenge was a good example of how it's really helpful to divide up sections of code into functions. Doing this makes the organization of the code easier and the workload less intimidating. Here are some lessons learned:

* The `.join()` function is really helpful for converting an index into string. Whatever precedes the functions, like `"".join()` or `", ".join()` will be what goes in between each item in the index when it's converted to a string.

* The `enumerate()` function will convert a string into a list. It's kind of the opposite of the `.join()` function. 

* In a for loop, if, for example, `for position, character in list` was written, what goes before the comma will represent the place/position in the list, and what goes after the comma will represent the value of whatever place in the list. 

* More info in the code comments.


## CAD_Swing_Arm 

### Assignment Description

This assignment asked me to replicate a swing arm part from a set of drawings. The assignment was set up in a way that was similar to how an OnShape certification test would be, so that the structure of how it works would be more familiar.

### Evidence 

Configuration #1

![Configuration 1](https://user-images.githubusercontent.com/89222808/137238893-1fb00671-a56e-4945-a0b9-d2524f2dbd67.png)

Configuration #2

![Configuration 2](https://user-images.githubusercontent.com/89222808/137238944-1d552151-7784-423e-88ad-8f4976325d97.png)

### Part Link
[Swing Arm Part](https://cvilleschools.onshape.com/documents/3a036d7d27feee6e965d0f59/w/c94159d42a85942668a71f24/e/de84f3e5f3246241c71112dd?configuration=List_egCNsovqerewr9%3DDefault&renderMode=0&uiState=6171739679c5e6291e6e5569)

### Reflection
The CAD Swing Arm assignment was more difficult than I had expected. The main challenge was to create a part based on different drawings with their corresponding measurements, which were from different view points. It took me several tries to get the basis for the swing arm down, but once I had the basic structure of it, adding fillets and cuts was easier.

Here are some lessons learned:

* When there are a bunch of drawings that a parts supposed to be mae from, it's helpful to start with just one and to create a rough sketch of it. The sketch doesn't have to be fully defined, but just creating some geometry to work off of can be a big help.

* It's useful to create variables in sketches if multiple configurations of a part are going to be made. Doing this made it easier to create a second configuration of the swing arm once the first had been made. 

* Fillets should usually come last in a part since they can interfere with other sketches and extrusions if they're made early on.  

* There're lots of ways to build a part, like doing a bunch of sketches or doing fewer and more complicated sketch. Usually, it's easier to do multiple sketches and then base them off of each other with features like "use," but doing a more complicated sketch--what I did for my part--can work decently, just as long as it's done well since there're more things that can go wrong.


## CAD Skateboard

### Assignment Description

The CAD Skateboard assignment was basically a tutorial on most of the basic OnShape features. It covered how to make a sketch and constrain it, how to make extrudes and revolves, how to link sketches to each other with the "use" feature and dimesnions, and how to assemble a part (skateboard) with nuts, bolts, and mate connectors. The goal of the assignent was to make a skateboard. To make it, the skateboard's deck, baseplate, hanger, bushing, an wheels. After this was done and the skateboard was assembled, there was also the option to curve the board, change the baseplate, and do other ad-onns.

### Evidence 

Basic skateboard assembly

![Configuration 1](/Engineering_IV-Basic_Skateboard_Top_View.png)

Bottom of advanced skateboard

![Bottom of advanced skateboard](/Engineering_IV-Bottom_Skateboard_Advanced.png)

Bottom skateboard original

![Bottom skateboard original](/Engineering_IV-Bottom_Skateboard_Original.png)

Bottom view advanced skateboard

![Bottom view advanced skateboard](/Engineering_IV-Skateboard_Bottom_View.png)

Top view advanced skateboard

![Top view advanced skateboard](/Engineering_IV-Skateboard_View_Isometric.png)


### Part Link
[Skateboard Doc](https://cvilleschools.onshape.com/documents/22b030e3a14a54e0693551bc/w/bf8614f874c22e27b8822194/e/2df190b012d584e622d02173?renderMode=0&uiState=61717937cf0ba439faa7c38d)

### Reflection
The skateboard assignment was relatively straight-forward since it was set up like a walk through / tutorial, but there were some dificult aspects of it, especially for the advanced section. 

Here are some lessons learned:

* The "hole" feature is really conveiniant for making holes in a part that are the same size as commonly-used nuts, bolts, and other machine parts. When it's used, there's a menu with different brands, measurements, and features. 

* The "split" feature is useful for seperating a part into sections. It was used along with the "move face" feature to bend the edges of the skateboard deck.

* It's a lot easier to model a wheel or circular part with the revolve feature instead of an extrude. Also, multiple parts can be made based on one sketch, like how the wheel and bearing were made.

* Creating related parts in an assembly in a part studio is helpful for making them relative to each other, which saves time.
