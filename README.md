# Engineering_4_Notebook
This repository contains documentation of Engineering 4 assignments and projects.

Note to self: for each assignment's documentation, there should be the assignment description, evidence, wiring (if applicable), and reflection.


## Table of Contents
* [Python_Dice_Roller](#Python_Dice_Roller)
* [Python_Calculator](#Python_Calculator)
* [Quadratic_Solver](#Quadratic_Solver)
* [Strings_and_Loops](#Strings_and_Loops)
* [Hangman/MSP_Challenge](#Hangman/MSP_Challenge)
* [CAD_Skateboard](#CAD_Skateboard)
* [OnShape_Legos](#OnShape_Legos)
* [LED_Blink](#LED_Blink)
* [Safe_Shutdown_Button](#Safe_Shutdown_Button)
* [GPIO_Pins--I2C](#GPIO_Pins--I2C)
* [Headless_accelerometer](#Headless_accelerometer)
* [Pi_Camera](#Pi_Camera)
* [Copy_Pasta](#Copy_Pasta)
---


## Python_Dice_Roller

### Assignment Description

The Python Dice Roller assignment was the first Python assignment in Engineering IV besides the introductory Hello Python assignment. The purpose of the assignment was to create a Python program that could automatically roll dice. In addition, the program had to take user input of whether it would re-roll or exit the program after it had done its initial roll. For the spicy part of this assignment, the program had to also take user input on the number of sides that the dice should have and also how many dice were to be rolled. The spicy part also had to give the user the option of changing the settings in addition to choosing to either exit the prom or re-roll

### Evidence 

Vanilla version:

![Vanilla Dice Roller](/media/Engineering_IV-Vanilla_Dice_Roller.png)

Spicy version:

![Spicy Dice Roller](/media/Engineering_IV-Spicy_Dice_Roller.png)

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

![Vanilla Calculator](/media/Engineering_IV-Vanilla_Calculator.png)

Spicy version:

![Spicy Calculator](/media/Engineering_IV-Spicy_Calculator.png)

### Wiring

No wiring was required for this assignment. 

### Reflection

This assignment was initially confusing, but once I figured out that only one function was needed to perform the operations and that the operations could be simply called using if statements, it made more sense. Here were some lessons learned:

* In a print statement writing `\t` creates a tab in the print line, which is helpful for formatting consecutive print statements.

* A print function can incorporate a function by writing something like `print(str(doMath(a, b, 6)))`. Note that the 6 meant that the sixth if statement was being called, in this case, the 1st factorial.

* It's helpful to ask other students for help. By asking what somebody did for a certain aspect of the code, there's a chance to have a new perspective on the topic, which can then be modified and made original. In this case, asking for advice on how to create a factorial calculator was helpful.

* More information can be found in the code comments. 


## Quadratic_Solver

### Assignment Description

The quadratic solver assignment required code to be designed that could calculate the roots of a quadratic function (ax^2 + bx +c) when given user input for a, b, and c. 
Some algebra had to be recalled to remember how to calculate the discriminant ((-b +/- sqrt(b^2-4ac))/2a), and for the spicy section of the assignment, the greatest challenge was to write code that could print out the function in vertex form, as it was initially hard to algebraically convert from standard to vertex form. This assignment taught valuable lessons on how to represent algebraic equations in a coding environment.

### Evidence 

Vanilla version:

![Vanilla Quadratic Solver](/media/Engineering_IV-Quadratic_Solver.png)

Spicy version:

![Spicy Quadratic Solver Correct](/media/Engineering_IV-Quadratic_Solver_Spicy_Correct.png)

### Wiring

No wiring was required for this assignment. 

### Reflection

I had to remember some basic algebra terms like the discriminant and vertex form for this assignment. This wasn't difficult, but it was more challenging to convert from standard form to vertex form. Here are the lessons I learned:

* First of all, having a reliable code environment is helpful. I was using [this coding IDE](https://www.online-python.com/), but because it was randomly freezing on me, I switched to [this](https://www.onlinegdb.com/online_python_compiler) more reliable one. However, the spicy version of code was run on the [unreliable IE](https://www.online-python.com/) because the other was not registering f strings.

* Going off of that, f strings are a really helpful Python 3 tool that allows variables to be called in print statements without having to use `str()` each time. This made the printing of the vertex form and discriminant much easier.

* Make sure to read the assignment's requirements. I got functioning code the first time I did this assignment, but it didn't use f strings and functions like the assignment asked, so I re-did it.

* The assignment stated that because Python didn't have a built-in square root operator, the class `function` from the library `math` had to be used. However, I tested simply taking the exponent to the 1/2 or `**(1/2)`, and this worked just as well, suggesting that Python does in fact have a built-in square root operator.

* More lessons can be found in the code comments 


## Strings_and_Loops

### Assignment Description

The code for the Strings and Loops assignment had to make it so that when a sentence was typed from user input, the terminal would print out the sentence, one character at a time, with a dash between each word. In order to do this, nested for-loops had to be used. Also, for the spicy version of this assignment, the challenge was to make the code as condensed as possible. To do this, the code had to incorporate "list comprehension," which is a method of condensing nested for-loops in Python. 

### Evidence 

Vanilla version:

![Vanilla Strings and Loops](/media/Engineering_IV-Strings_And_Loops.png)

Spicy version:

![Spicy Strings and Loops](/media/Engineering_IV-Strings_And_Loops_Spicy.png)

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


## Hangman/MSP_Challenge

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


## CAD_Skateboard

### Assignment Description

The CAD Skateboard assignment was basically a tutorial on most of the basic OnShape features. It covered how to make a sketch and constrain it, how to make extrudes and revolves, how to link sketches to each other with the "use" feature and dimesnions, and how to assemble a part (skateboard) with nuts, bolts, and mate connectors. The goal of the assignent was to make a skateboard. To make it, the skateboard's deck, baseplate, hanger, bushing, an wheels. After this was done and the skateboard was assembled, there was also the option to curve the board, change the baseplate, and do other ad-onns.

### Evidence 

The basic skateboard's finished assembly:

![Configuration 1](/media/Engineering_IV-Basic_Skateboard_Top_View.png)

The lower part of the same part:

![Bottom skateboard original](/media/Engineering_IV-Bottom_Skateboard_Original.png)

The lower part of the advanced baseplate

![Bottom of advanced skateboard](/media/Engineering_IV-Bottom_Skateboard_Advanced.png)

The advanced skateboard's assembly:

![Top view advanced skateboard](/media/Engineering_IV-Skateboard_View_Isometric.png)

![Bottom view advanced skateboard](/media/Engineering_IV-Skateboard_Bottom_View.png)


### Part Link
[Skateboard Doc](https://cvilleschools.onshape.com/documents/22b030e3a14a54e0693551bc/w/bf8614f874c22e27b8822194/e/2df190b012d584e622d02173?renderMode=0&uiState=61717937cf0ba439faa7c38d)

### Reflection
The skateboard assignment was relatively straight-forward since it was set up like a walk through / tutorial, but there were some dificult aspects of it, especially for the advanced section. 

Here are some lessons learned:

* The "hole" feature is really conveiniant for making holes in a part that are the same size as commonly-used nuts, bolts, and other machine parts. When it's used, there's a menu with different brands, measurements, and features. 

* The "split" feature is useful for seperating a part into sections. It was used along with the "move face" feature to bend the edges of the skateboard deck.

* It's a lot easier to model a wheel or circular part with the revolve feature instead of an extrude. Also, multiple parts can be made based on one sketch, like how the wheel and bearing were made.

* Creating related parts in an assembly in a part studio is helpful for making them relative to each other, which saves time.


## OnShape_Legos

### Assignment Description

### Evidence 

### Wiring

### Reflection


## LED_Blink

### Assignment Description

### Evidence 

### Wiring

### Reflection


## GPIO_Pins--I2C

### Assignment Description

For the GPIO Pins-Asignment, the pi's GIPO pins were used along with an i2c device to rig up an LCD and accelerometer. The goal was to get the LCD to display the data that the accelerometer detected and update it as that data changed. In order to accomplish this, a library from the accelerometer (LSM303), simpletest.py and a library from the LCD (SSD1306), shapes.py, were combined into the file combined_i2c.py, which utilizied the libraries of both. 

### Evidence 

[Code](/python/Engineering_IV-combined_i2c_.py)

![GIF](/media/combined-i2c.gif)


### Wiring

![Wiring diagram](/media/Enginering-IV-gpio_and_headless_accel.jpg)

### Reflection

This asignment was intiially prettty dificult because I hadn't used an SSD106 LCD or acceleromter, but havng the example test code from the libraries of the two parts was really helpful. Calling both libraries in a different file also added uneccesary confusion, so combinging the to test libraries worked well to make the coding proccess smoother.

Notes:

* `sudo i2cdetect -y 1` is neccesary to find the working pins for the accelermotoer and LCD.

* Only the accel data from the accelerometer, not the mag data, was neccesary for the aignment.

* F strings like in the print statement `f"Accel X={accel_x}"` make it a lot easier to incoportate variables into prints.


## Safe_Shutdown_Button

### Assignment Description

For the GPIO Pins-Asignment, the pi's GIPO pins were used along with an i2c device to rig up an LCD and accelerometer. The goal was to get the LCD to display the data that the accelerometer detected and update it as that data changed. In order to accomplish this, a library from the accelerometer (LSM303), simpletest.py and a library from the LCD (SSD1306), shapes.py, were combined into the file combined_i2c.py, which utilizied the libraries of both. 

### Evidence 

[Code](/python/safe_restart_shutdown__int_interupt_Pi.py)


### Wiring

![Wiring diagram](/media/safe_shutdown_button.jpg)

### Reflection

This asignment was intiially prettty dificult because I hadn't used an SSD106 LCD or acceleromter, but havng the example test code from the libraries of the two parts was really helpful. Calling both libraries in a different file also added uneccesary confusion, so combinging the to test libraries worked well to make the coding proccess smoother.

Notes:

* First of all, using daemons (self-running programs that operate in the backgroud of the computer) makes life a lot easier. Having a manual shutdown button allows the pi to be able to safely power off when it's main power source is an external battery.

* I was having some trouble getting the shutdown button to work initially. I had tried re-creating the file using `python3 /home/pi/path-to-your-shutdown-file/your-shutdown-file.py &` (note that an & must be at the end of line for it to run automatically), but in the end when the command sudo shutdown -h now fixed the problem, so it never hurts to just try and reboot.

## Headless_accelerometer

### Assignment Description

The Headless accelerometer expanded on the GPIO pins-i2c asignment. The combined_i2c.py was the base code with the LCD displaying the accel data, but the add-on was that a shapes (square, triangle, or in my case a circle) had to be drawn on the LCD and have one of it's base axes linked to the accel data. For my code, the x-axis of the circle was linked to the x accel data that the accelerometer detected, meaning the circle would move back and forth based on the accelometer's orientation.

### Evidence 

[Code link](/python/Engineering_IV-combined_i2c_.py)

![GIF](/media/headless_accel.gif)


### Wiring

![Wiring diagram](/media/Engineering_IV-gpio_and_headless_accel.jpg)

### Reflection

This asignment was intiially prettty dificult because I hadn't used an SSD106 LCD or acceleromter, but havng the example test code from the libraries of the two parts was really helpful. Calling both libraries in a different file also added uneccesary confusion, so combinging the to test libraries worked well to make the coding proccess smoother.

Notes:

* `sudo i2cdetect -y 1` is neccesary to find the working pins for the accelermotoer and LCD.

* Only the accel data from the accelerometer, not the mag data, was neccesary for the aignment.

* F strings like in the print statement `f"Accel X={accel_x}"` make it a lot easier to incoportate variables into prints

* To draw an elipse, the function draw.elipse() makes the wok much easier, taking the co-verteces and verteces

* It's important to scale the accel values so that they do not cause the circle to move off the screen


## Pi_Camera

### Assignment Description

For the Pi Camera asignment, the raspberry pi's camera hardware was introduced. The goal was to, first, take a picture using the terminal; second, take a picture using python; third, take 5 pictures with python, each with a different effect.

### Evidence 

The first camera test worked to simply take one picture through python script.
[First camera test](/python/camera_test_01.py)

The second camera test expanded on the first and took 5 consecutive pictures, each with a different visual effect.
[Second camera test](/python/camera_test_02.py)

Note - no gif was needed for this assignment because the only hardware was the pi camera. 

### Wiring

![Wiring diagram](/media/Engineering_IV-pi_camera.jpg)

### Reflection

This asignment was not too challenging due to the fact that the links [1](https://picamera.readthedocs.io/en/release-1.10/recipes1.html) & [2](https://picamera.readthedocs.io/en/release-1.10/api_camera.html#picamera.camera.PiCamera.image_effect) provided helpful information about the camera functions, arguments, and parameters. The second camera test was a bit more challenging because I incorporated the f strings  `camera.capture(f"/home/pi/Engineering_4_Notebook/pics/test_02_{effect}.jpg")` & `print(f"Picture with {effect} effect taken")` into the code to make the naming process cleaner, but this still was not to challenging.

Notes:

*  `camera.start_preview()` creates a preview of the picture being taken, but it only works on devices like macs or PCs.

*  camera.capture() takes a picture.

*  effect = camera.image_effect = 'insert effect' is how an effect is used


## Copy_Pasta

### Assignment Description

### Evidence 

[Code link](/python/Engineering_IV-animation.py)

![GIF](/media/animation.gif)

### Wiring

![Wiring diagram](/media/Engineering_IV-animation.jpg)

### Reflection

The copypasta assignment was relatively straightforward as [this](https://www.raspberrypi.org/learning/push-button-stop-motion/) guide gave step-by-step 
instructions. However, below are some takeaways.

Notes:

* Writing `ffmpeg -r 10 -i animation/frame%03d.jpg -qscale 2 animation.mp4` converts a series of images, in this case labled as frame followed by a 3 digit number, into an mp4.

* The `mv` commands moves a file from one directory to another; the `mkdir` commands makes a directory; and the `rm` commands deletes a file. 

* To explain the `%03d` in the line `camera.capture('/home/pi/Engineering_4_Notebook/animation/frame%03d.jpg' % frame)`: the `%` inserts the variable frame, the `3d` creates 3 digits following the variable, and the `d` means digit.

*  I also found the command `sttty rows "" columns ""` to be helpful because it prevented lines from overwriting themselves.
