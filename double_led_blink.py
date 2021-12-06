import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM) # sets up numbering scheme as BCM 

# Goal: when 1 led goes high, the other goes off. 
# Print state of each LED
# Blinking continues until user inputs "CTRL + c"

GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(19, GPIO.OUT, initial=GPIO.HIGH)
print("Starting Up")

while True:
	print("Switch Lights")
	GPIO.output(19, GPIO.LOW)
	GPIO.output(21, GPIO.HIGH)
	print("Wait a second")
	sleep(1)
	print("Switch Lights")
	GPIO.output(19, GPIO.HIGH)
	GPIO.output(21, GPIO.LOW)
	print("Wait a second")
	sleep(1)






