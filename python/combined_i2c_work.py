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
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3D)

# Initialize display
disp.begin()
disp.clear()
disp.display()

# Image settings
width = disp.width
height = disp.height
print("Width: " + str(width) + " Height: " + str(height))

# Create blank image for drawing with mode '1' for 1-bit color.
image = Image.new("1", (width, height))

# Create font
font = ImageFont.load_default()

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

print("Reading accelerometer data...")


while True:
    # Read accel and mag values and print them
    # Need to convert accel data from milli g's to m/s^2. To do this
    # the z-value can be scaled from its millli g valu (~1016) to the 
    # resting force of gravity (9.8 m/s/s)

    CONVERSION_FACTOR = 1016/9.8 

    accel, mag = lsm303.read()
    accel_x, accel_y, accel_z = accel
    mag_x, mag_y, mag_z = mag

#    print(
#        "Accel X: "
#        + str(accel_x)
#        + " | Accel Y: "
#        + str(accel_y)
#       + " | Accel Z: "
#        + str(accel_z)
#    )

    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    # Display X, Y and Z acceleration values
    draw.text((20, 50), f"Accel X={accel_x/CONVERSION_FACTOR}", font=font, fill=255)
    draw.text((20, 40), f"Accel Y={accel_y/CONVERSION_FACTOR}", font=font, fill=255)
    draw.text((20, 30), f"Accel Z={accel_z/CONVERSION_FACTOR}", font=font, fill=255)

    # display image stuff
    disp.image(image)
    disp.display()

    # delay
    time.sleep(1)
