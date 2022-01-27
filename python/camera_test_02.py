# Luke Frank 
# Engineering IV 
# 1/27/21

# This is the first camera test for the pi camera assignment. 
# This code has to do:

# A program that, when run, takes 5 pictures, each using a different effect.  

import time
import picamera

with picamera.PiCamera() as camera:


	camera.resolution = (1024, 768)
	# Default resolution is 2592 x 1944. The higher the number, the 
        # higher the resolution but also higher the file size.


	# Effect #1:
	effect = camera.image_effect = 'cartoon'
	# Create variable of effect to add to specific picture name

	camera.start_preview()
	# Preview isn't neccesary for pictures with pi. If the pi was hooked up to
	# some external camera, then preview would allow a preview of the picture, 
	# but it's not applicable to this. 

	# Camera warm-up time. Brings the camera onto its default settings
	# brightness, exposure, contrast, etc...

	print("Camera running")

	time.sleep(2)

	camera.capture(f"/home/pi/Engineering_4_Notebook/pics/test_02_{effect}.jpg")
	# Specify path for the picture to go into.

	print(f"Picture with {effect} effect taken")

	camera.stop_preview()


	# Effect #2:
	effect = camera.image_effect = 'watercolor'

	camera.start_preview()

	print("Camera running")

	time.sleep(2)

	camera.capture(f"/home/pi/Engineering_4_Notebook/pics/test_02_{effect}.jpg")
	
	print(f"Picture with {effect} effect taken")
	
	camera.stop_preview()


	# Effect #3:
	effect = camera.image_effect = 'solarize'
	  
	camera.start_preview()

	print("Camera running")

	time.sleep(2)

	camera.capture(f"/home/pi/Engineering_4_Notebook/pics/test_02_{effect}.jpg")

	print(f"Picture with {effect} effect taken")
	
	camera.stop_preview()
	

	# Effect #4:
	effect = camera.image_effect = 'sketch'
	  
	camera.start_preview()

	print("Camera running")

	time.sleep(2)

	camera.capture(f"/home/pi/Engineering_4_Notebook/pics/test_02_{effect}.jpg")

	print(f"Picture with {effect} effect taken")
	
	camera.stop_preview()


	# Effect #5:
	effect = camera.image_effect = 'negative'
	  
	camera.start_preview()

	print("Camera running")

	time.sleep(2)

	camera.capture(f"/home/pi/Engineering_4_Notebook/pics/test_02_{effect}.jpg")
	
	print(f"Picture with {effect} effect taken")

	camera.stop_preview()


	print("All 5 pictures taken...")
