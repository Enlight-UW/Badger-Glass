# Enlight UW Badger Glass
import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


# Raspberry Pi pin configuration:
RST = 24
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

# 128x64 display with hardware SPI:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000))

colorBlack = 0
colorWhite = 255

invert = False

bgColor = 0
fntColor = 0

if(invert):

    bgColor = colorWhite
    fntColor = colorBlack

else:

    bgColor = colorWhite
    fntColor = colorBlack
    

def writeToScreen(msg, x, y, draw, fnt ):

    draw.text((3+x, 13+y), msg, font=fnt, fill=fntColor)

    return


def updateScreen(disp, image):
    disp.image(image)
    disp.display()
    return


def clearScreen(draw):
    draw.rectangle((0,11,width,height), outline=bgColor, fill=bgColor)
    return

# Initialize library.
disp.begin()

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

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = 3
shape_width = 20
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
#x = padding
# Draw an ellipse.
#draw.ellipse((x, top , x+shape_width, bottom), outline=255, fill=0)
#x += shape_width+padding
# Draw a rectangle.
#draw.rectangle((x, top, x+shape_width, bottom), outline=255, fill=0)
#x += shape_width+padding
# Draw a triangle.
#draw.polygon([(x, bottom), (x+shape_width/2, top), (x+shape_width, bottom)], outline=255, fill=0)
#x += shape_width+padding
# Draw an X.
#draw.line((x, bottom, x+shape_width, top), fill=255)
#draw.line((x, top, x+shape_width, bottom), fill=255)
#x += shape_width+padding

# Load default font.
font = ImageFont.load_default()

###
##
#THE ACTUAL PROGRAM BEGINS HERE!!!!
##
###

hP = 10

#draw.rectangle((0,0,width,height), outline=0, fill=0)
clearScreen(draw)

draw.line((0,top,0,hP), fill=fntColor)
draw.line((width-1,top,width-1,hP), fill=fntColor)
draw.line((0,top,width,top), fill=fntColor)
draw.line((0,10,width,hP), fill=fntColor)
draw.line((width-25,top,width-25,hP), fill=fntColor)

#draw.text((padding, top), "Colonel, do you read?", font=font, fill=255)
writeToScreen("Colonel, do you read?", 0,0, draw, font)
updateScreen(disp, image)
time.sleep(2)


#draw.text((padding, top+10), "This is Snake", font=font, fill=255)
writeToScreen("This is Solid Snake.", 0,10,draw,font)
updateScreen(disp, image)
time.sleep(1)


writeToScreen("METAL GEAR", 0,20, draw, font)
updateScreen(disp, image)


time.sleep(2)


for i in range(0, 100):
    clearScreen(draw)
    writeToScreen(str(i), 15,15, draw, font)
    updateScreen(disp, image)
    #time.sleep(.001)



