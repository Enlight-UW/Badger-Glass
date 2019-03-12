import sys
from fbchat import Client
from fbchat.models import *


if(len(sys.argv) >= 3):
    uname = sys.argv[1]
    pword = sys.argv[2]
    client = Client(uname, pword)

    if not client.isLoggedIn():
        print "Login Failed!"

else:
    print "Invalid Username or Passowrd!"

