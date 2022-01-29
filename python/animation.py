# Luke Frank
# Engineering 4 - Copypasta
# 1/29/21


from picamera import PiCamera
from time import sleep
from gpiozero import Button
# Import manual button to take pictures

# Define button and camera
button = Button(17)
camera = PiCamera()

camera.start_preview()

# Create variable to be used in loop. It'll be factored into the file name
# of each picture taken
frame = 1

# This code will create an animation.
while True:

	try:
		# Wait for button press
		print("Waiting for button press")
		button.wait_for_press()

		print('Taking in 3 seconds')
		sleep(3)

		# Take picture
		print(f"Taking picture {frame}")

		camera.capture('/home/pi/Engineering_4_Notebook/animation/frame%03d.jpg' % frame)
		# Writing frame%03d means that each pic/file will be saved as "fra$
		# followed by a 3-digit number with leading zeros (ex: 001). This
		# makes it a lot easier to keep track of pictures
		
		# The % takes the variable and puts into the print statement
		# The 03 means use 3 digits and d means decimal

		frame += 1

	except KeyboardInterrupt:

		print("Breaking loop")
		camera.stop_preview()
		break
