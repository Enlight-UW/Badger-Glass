# Enlight UW Badger Glass
import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import sys
from fbchat import Client
from fbchat.models import *

#Messenger class stuff
class MessageListener(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
      print(message_object.text)
      clearScreen(draw)
      writeToScreen(message_object.text, 0,0, draw, font)
      updateScreen(disp, image)

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
    
#set text to be written to screen
def writeToScreen(msg, x, y, draw, fnt ):

    draw.text((3+x, 13+y), msg, font=fnt, fill=fntColor)

    return

#Setup screen with ui
def initScreen():
  clearScreen(draw)
  draw.line((0,top,0,hP), fill=fntColor)
  draw.line((width-1,top,width-1,hP), fill=fntColor)
  draw.line((0,top,width,top), fill=fntColor)
  draw.line((0,10,width,hP), fill=fntColor)
  draw.line((width-25,top,width-25,hP), fill=fntColor)


#update screen with new text
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

# First define some constants to allow easy resizing of shapes.
padding = 3
shape_width = 20
top = padding
bottom = height-padding

# Load default font.
font = ImageFont.load_default()

###
##
#THE ACTUAL PROGRAM BEGINS HERE!!!!
##
###

if(len(sys.argv) >= 3):
    uname = sys.argv[1]
    pword = sys.argv[2]
    #client = Client(uname, pword)
    client = MessageListener(uname, pword)

    if not client.isLoggedIn():
        print "Login Failed!"
    else:
        print('My ID: ' + client.uid)
        threads = client.fetchThreadList()
        initScreen()
        client.listen()
        
        

        

else:
    print "Invalid Username or Passowrd!"
#####

hP = 10


