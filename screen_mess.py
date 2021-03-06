# Enlight UW Badger Glass
import time

import os

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
      
      cleanMessage = message_object.text.strip()
      cleanMessage = cleanMessage.encode('ascii', 'ignore')
        
      print(author_id + " " + cleanMessage)
      clearScreen(draw)
      writeToScreen(cleanMessage, 0,0, draw, font)
      updateScreen(disp, image)

# Raspberry Pi pin configuration:
RST = 24
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

# 128x64 display with hardware SPI:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000))


#Screen colors
colorBlack = 0
colorWhite = 255

invert = False

bgColor = 0
fntColor = 0

maxLineString = 20

if(invert):

    bgColor = colorWhite
    fntColor = colorBlack

else:

    bgColor = colorWhite
    fntColor = colorBlack
    
#set text to be written to screen
def writeToScreen(msg, x, y, draw, fnt ):

    splitString = msg.split()
    tmpString = ""
    lines = 0

    #draw.text((3+x, 13+y), msg, font=fnt, fill=fntColor)

    
    #For each word in this String
    for i in range(0,len(splitString)):

            #if the current string and the next word are less than the max length
            if((len(splitString[i]) + len(tmpString))<maxLineString):
                tmpString = tmpString + splitString[i] + " "
            else:
                #if the next word wont fit on this line, print the string as is
                draw.text((3+x, 3+y+(lines*10)), tmpString, font=fnt, fill=fntColor)
                tmpString = splitString[i] + " "
                lines+=1
    
    if(len(tmpString) != 0):
        draw.text((3+x, 3+y+(lines*10)), tmpString, font=fnt, fill=fntColor)

    return

#Setup screen with ui
def initScreen():
  clearScreen(draw)
  '''
  draw.line((0,top,0,hP), fill=fntColor)
  draw.line((width-1,top,width-1,hP), fill=fntColor)
  draw.line((0,top,width,top), fill=fntColor)
  draw.line((0,10,width,hP), fill=fntColor)
  draw.line((width-25,top,width-25,hP), fill=fntColor)
    '''

#update screen with new text
def updateScreen(disp, image):
    disp.image(image)
    disp.display()
    return


def clearScreen(draw):
    draw.rectangle((0,0,width,height), outline=bgColor, fill=bgColor)
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

hP = 10
if(len(sys.argv) >= 3):
    os.system('clear')
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
        
        #Listen for new messages
        client.listen()
        
        

        

else:
    print "python <progname> <messenger username> <messenger password>"
#####

hP = 10


