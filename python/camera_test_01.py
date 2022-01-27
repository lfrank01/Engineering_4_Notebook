# Luke Frank 
# Engineering IV 
# 1/27/21

# This is the first camera test for the pi camera assignment. 
# This code has to do:

# A program that, when run, prints a message to the screen (like "running"), 
# takes a picture, and then prints another message to the screen (like "done")


import time
import picamera

with picamera.PiCamera() as camera:

    camera.resolution = (1024, 768)
    # Default resolution is 2592 x 1944. The higher the number, the higher the 
    # resolution but also higher the file size.

    camera.start_preview()
    # Preview isn't neccesary for pictures with pi. If the pi was hooked up to
    # some external camera, then preview would allow a preview of the picture, 
    # but it's not applicable to this. 

    # Camera warm-up time. Brings the camera onto its default settings
    # brightness, exposure, contrast, etc...
    
    print("Camera running")

    time.sleep(2)

    camera.capture("/home/pi/Engineering_4_Notebook/media/test_01.jpg")
    # Specify path for the picture to go into.

    print("Picture taken")

    camera.stop_preview()
