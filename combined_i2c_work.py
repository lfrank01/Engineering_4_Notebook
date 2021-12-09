# Setup

# Accelerometer -----

import time

# Import the LSM303 module -- Accelerometer
import Adafruit_LSM303

# Import the LSM303 module -- Accelerometer
import Adafruit_LSM303

# Import other Accelerometer libraries
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306 -- Screen

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Set up Raspberry Pi

# Raspberry Pi pin configuration:
RST = 24
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0



# Create a LSM303 (accelerometer) instance.
lsm303 = Adafruit_LSM303.LSM303()

# Set up SSD1306 display 
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)

# Initialize process - not really sure what it means...

disp.begin()
font = ImageFont.load_default()





# Clear display.
disp.clear()
disp.display()
# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# -------------
print('Printing accelerometer & magnetometer X, Y, Z axis values, press Ctrl-C to quit...')

# Write two lines of text.
draw.text((x, top),    'Hello',  font=font, fill=255)
draw.text((x, top+20), 'World!', font=font, fill=255)

# Display image.
disp.image(image)
disp.display()

# Test run





# disp.clear()
# disp.display()
# # Create blank image for drawing.
# # Make sure to create image with mode '1' for 1-bit color.
# width = disp.width
# height = disp.height
# image = Image.new('1', (width, height))

# # Read the X, Y, Z axis acceleration values and print them.
# accel, mag = lsm303.read()

# # Grab the X, Y, Z components from the reading and print them out.
# accel_x, accel_y, accel_z = accel
# mag_x, mag_y, mag_z = mag
    
    
    
# print('Accel X={0}, Accel Y={1}, Accel Z={2}, Mag X={3}, Mag Y={4}, Mag Z={5}'.format(
# accel_x, accel_y, accel_z, mag_x, mag_y, mag_z))


# # Wait half a second and repeat.
# time.sleep(0.5)

    
  

  
  
  
  
  
  





# Load default font.
font = ImageFont.load_default()

# Alternatively load a TTF font.  Make sure the .ttf font file is in the same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
#font = ImageFont.truetype('Minecraftia.ttf', 8)

# Write two lines of text.
draw.text((x, top),    'Hello',  font=font, fill=255)
draw.text((x, top+20), 'World!', font=font, fill=255)

# Display image.
disp.image(image)
disp.display()

#----------------------

#Setup stuff

# while true:
  read accel values
  clear screen
  draw.text for x, y ,z accel
  #display image stuff
  #delay
