import sys
from fbchat import Client
from fbchat.models import *

class MessageListener(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        print(message_object.text)



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
        client.listen()

        

else:
    print "Invalid Username or Passowrd!"

