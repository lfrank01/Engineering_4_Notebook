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
    accel, mag = lsm303.read()
    accel_x, accel_y, accel_z = accel
    mag_x, mag_y, mag_z = mag
    print(
        "Accel X: "
        + str(accel_x)
        + " | Accel Y: "
        + str(accel_y)
        + " | Accel Z: "
        + str(accel_z)
    )

    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    # Display X, Y and Z acceleration values
    draw.text((0, 0), f"X={accel_x}", font=font, fill=255)
    draw.text((55, 0), f"Y={accel_y}", font=font, fill=255)
    draw.text((100, 0), f"Z={accel_z}", font=font, fill=255)

    # Calculate position of shape
    y_margin = 10  # we need some space for the text above the shape

    # Calculate the zero position
    x_center = int(width / 2)
    # Divide width by 2 to get center of LCD
    y_center = int((height + y_margin) / 2)

    # Calculate the movement caused by X and Y values
    x_move = int(accel_x / 2000 * width)
    y_move = int(accel_y / 2000 * height)
    # Sale the x/y movement so that the circle will not move off the screen

    x_position = x_center + x_move
    y_position = y_center - y_move

    # Draw a circle
    circle_radius = 10
    draw.ellipse(
        (
            x_position - circle_radius,
            y_position - circle_radius,
            x_position + circle_radius,
            y_position + circle_radius,
        ),
        outline=255,
        fill=0,
    )

    # display image on OLED
    disp.image(image)
    disp.display()
