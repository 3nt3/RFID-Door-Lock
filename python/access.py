# Copyrght Niels Schlegel 2018
# My romm user access database

import datetime
import time

users = {
	# Data-Structure:
	
	# "name": ["UUID", "name", "o/d", "perm", blocked],
	
	# Permissions:
	# A - root; Create and remove tags.  
	# B - normal; Open x times per day. 0 means unlimited access.
	
    "root": ["0001", "root", 0, "A", False],
	"niels": ["0002", "niels", 0, "B", False],
	"ps": ["0003", "eltern", 0, "B", False],
	"jan": ["0004", "jan", 2, "B", True]
    }

now = datetime.datetime.now()

if now.isoweekday() == 5:
    cleaningDay = True
else:
    cleaningDay = False
    
def closeDoor():
    doorOpened = False

def openDoor(sleep, time):
    doorOpened = True
    
    if sleep == True:
        time.sleep(time)
        closeDoor()
    
    
if cleaningDay != True:
    eingabe = input("Insert name: ").lower()
    print(users[eingabe])
    
    if eingabe in users:
            
        print("Checking if you're blocked.")
        
        if users[eingabe][4] != True:
            blocked = False
        else:
            blocked = True
            
        if blocked != True:
            print("Access Granted!")
            openDoor(False, 0)
            
        else:
            print("Acces Blocked")
        
    else:
        print("Invalid Name")
        
else:
    print("It's cleaning day. The door already is unlocked!")
    openDoor(False, 0)