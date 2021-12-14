
import time

# Import the LSM303 module -- Accelerometer
import Adafruit_LSM303

# Import screen libraries
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306 

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

# Initialize process
disp.begin()

# Image settings
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Create font
font = ImageFont.load_default()

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

x = 0
top = 2
while True:
	  
  # Read acel values
  accel, mag = lsm303.read()
  accel_x, accel_y, accel_z = accel
  mag_x, mag_y, mag_z = mag

      
  # clear screen
  disp.clear()
  disp.display()
  # Create blank image for drawing.
  # Make sure to create image with mode '1' for 1-bit color.
  width = disp.width
  height = disp.height
  image = Image.new('1', (width, height))
  # Draw a black filled box to clear the image.
  draw.rectangle((0,0,width,height), outline=0, fill=0)



  # draw.text for x, y ,z accel - Not done
  

  # print('Accel X={0}, Accel Y={1}, Accel Z={2}, Mag X={3}, Mag Y={4}, Mag Z={5}'.format(
  # accel_x, accel_y, accel_z, mag_x, mag_y, mag_z))
  draw.text((x, top),    'Accel X={0}',  font=font, fill=255)
  # draw.text((x, top+20), 'World!', font=font, fill=255)
    
 

  # display image stuff

  disp.image(image)
  disp.display()

  # delay

  time.sleep(5)
