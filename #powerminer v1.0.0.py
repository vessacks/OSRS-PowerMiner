#powerminer
#powermines iron 

#todo: 
#1. figure out how to implement windmouse. I think it's better and more customizable than pyHM mouse. 

from calendar import c
import pyautogui
import time
import numpy as np
from pyHM import mouse


def countdown(t): #generic countdown function
    while t>0:
        time.sleep(1)
        print(t)
        t -= 1
    print("Now!")

class InventorySlot(object): #an inventory slot
    def __init__(self, centralTendency,numberRandWalks):
        self.centralTendency = centralTendency #this is the radius in pixels of each coords central tendency. A good value for an inventory spot on my thinkpad is ~7
        self.numberRandWalks = numberRandWalks #this is the number of one pixel random walks a click will take. A good value for an inventory spot on my thinkpad is 300. 
    
    def getcoords(self):
        input("position your mouse at coord 1 and press enter")
        coord1 = pyautogui.position()
        print("recorded coord 1 as "+ str(coord1))
        input("position your mouse at coord 2 and press enter")
        coord2 = pyautogui.position()
        print("recorded coord 2 as "+ str(coord2))
        input("position your mouse at coord 3 and press enter")
        coord3 = pyautogui.position()
        print("recorded coord 3 as "+ str(coord3))    
        self.coords = [coord1, coord2, coord3] 

    def dropclick(self): #randomizes a click location and clicks
        coordpick = np.random.randint(1,4) #selects which of the coords to start with
        #print("coordpick is "+str(coordpick))
        if coordpick == 1:
            x,y = self.coords[0]
        elif coordpick == 2:
            x,y = self.coords[1]
        else:
            x,y = self.coords[2]
        
        #this part shifts the coord a random, linearly distributed amount from coord to widen central tendency
        x += np.random.randint((self.centralTendency * -1), (self.centralTendency +1)) 
        y += np.random.randint((self.centralTendency * -1), (self.centralTendency +1)) 

        #this part shifts the coord again using a random walk (binomial distro?) to conceal the linear distribution
        xshift = 0
        yshift = 0 #these are the amounts that the click will be shifted
        
        for i in range(self.numberRandWalks): # adds numberRandWalks random +1s and -1s to xshift and y shift. change this value to increase the amount of random walk
            xshift += np.random.randint(-1,2) #resolves randomly to -1 or 1
            yshift += np.random.randint(-1,2) #resolves ramdonly to -1 or 1
        #print("xshift is %s and yshift is %s" %(str(xshift), str(yshift)))
        
        x += xshift
        y += yshift

        mouse.move(x,y, multiplier=.2) #this moves the mouse to the final point
        
        pyautogui.keyDown('shift')
        time.sleep(np.random.normal(loc=.2, scale=.03))
        pyautogui.click()
        time.sleep(np.random.normal(loc=.1, scale=.02))
        pyautogui.keyUp('shift')


       
class ClickableEntity(object): #same as inventory slot except the central tendency size and random walk count are modifiable
    def __init__(self, centralTendency,numberRandWalks):
        self.centralTendency = centralTendency #this is the radius in pixels of each coords central tendency. A good value for an inventory spot on my thinkpad is ~7
        self.numberRandWalks = numberRandWalks #this is the number of one pixel random walks a click will take. A good value for an inventory spot on my thinkpad is 300. 
    
    def getcoords(self):
        input("position your mouse at coord 1 and press enter")
        coord1 = pyautogui.position()
        print("recorded coord 1 as "+ str(coord1))
        input("position your mouse at coord 2 and press enter")
        coord2 = pyautogui.position()
        print("recorded coord 2 as "+ str(coord2))
        input("position your mouse at coord 3 and press enter")
        coord3 = pyautogui.position()
        print("recorded coord 3 as "+ str(coord3))    
        self.coords = [coord1, coord2, coord3] 

    def genclick(self): #randomizes a click location and clicks
        coordpick = np.random.randint(1,4) #selects which of the coords to start with
        #print("coordpick is "+str(coordpick))
        if coordpick == 1:
            x,y = self.coords[0]
        elif coordpick == 2:
            x,y = self.coords[1]
        else:
            x,y = self.coords[2]
        
        #this part shifts the coord a random, linearly distributed amount from coord to widen central tendency
        x += np.random.randint((self.centralTendency * -1), (self.centralTendency +1)) 
        y += np.random.randint((self.centralTendency * -1), (self.centralTendency +1)) 

        #this part shifts the coord again using a random walk (binomial distro?) to conceal the linear distribution
        xshift = 0
        yshift = 0 #these are the amounts that the click will be shifted
        
        for i in range(self.numberRandWalks): # adds numberRandWalks random +1s and -1s to xshift and y shift. change this value to increase the amount of random walk
            xshift += np.random.randint(-1,2) #resolves randomly to -1 or 1
            yshift += np.random.randint(-1,2) #resolves ramdonly to -1 or 1
        #print("xshift is %s and yshift is %s" %(str(xshift), str(yshift)))
        
        x += xshift
        y += yshift

        mouse.move(x,y, multiplier=.2) #this moves the mouse to the final point
        
        time.sleep(np.random.normal(loc=.2, scale=.03))
        pyautogui.click()
        time.sleep(np.random.normal(loc=.1, scale=.02))
        
    def dropclick(self): #randomizes a click location and drop clicks
        coordpick = np.random.randint(1,4) #selects which of the coords to start with
        #print("coordpick is "+str(coordpick))
        if coordpick == 1:
            x,y = self.coords[0]
        elif coordpick == 2:
            x,y = self.coords[1]
        else:
            x,y = self.coords[2]
        
        #this part shifts the coord a random, linearly distributed amount from coord to widen central tendency
        x += np.random.randint((self.centralTendency * -1), (self.centralTendency +1)) 
        y += np.random.randint((self.centralTendency * -1), (self.centralTendency +1)) 

        #this part shifts the coord again using a random walk (binomial distro?) to conceal the linear distribution
        xshift = 0
        yshift = 0 #these are the amounts that the click will be shifted
        
        for i in range(self.numberRandWalks): # adds numberRandWalks random +1s and -1s to xshift and y shift. change this value to increase the amount of random walk
            xshift += np.random.randint(-1,2) #resolves randomly to -1 or 1
            yshift += np.random.randint(-1,2) #resolves ramdonly to -1 or 1
        #print("xshift is %s and yshift is %s" %(str(xshift), str(yshift)))
        
        x += xshift
        y += yshift

        mouse.move(x,y, multiplier=.2) #this moves the mouse to the final point
        
        pyautogui.keyDown('shift')
        time.sleep(np.random.normal(loc=.2, scale=.03))
        pyautogui.click()
        time.sleep(np.random.normal(loc=.1, scale=.02))
        pyautogui.keyUp('shift')

def breaktime():
#this guy determines if it should take a break
    breakroller = np.random.randint(0,450)
    hibernation_time = (np.random.randint(10,140)) #breaktime random time between 10-140 seconds
    if breakroller == 1:
        print("breakroller was " + str(breakroller)+ ". hibernating for "+ str(hibernation_time)+ " seconds")
        time.sleep(hibernation_time)
        
    else:
        print("breakroller was "+ str(breakroller)+ ". I would have hibernated for "+ str(hibernation_time) + " seconds.")


def normdistwait(mean, standarddev):
    #normal distribution determines how long to wait between rock clicks
    time.sleep(np.random.normal(loc=mean,scale=standarddev))


slot1 = ClickableEntity(2,10)
print("we will now take coords for inventory slot 1" )
slot1.getcoords()

slot2 = ClickableEntity(2,10)
print("we will now take coords for inventory slot 2" )
slot2.getcoords()

slot3 = ClickableEntity(2,10)
print("we will now take coords for inventory slot 3" )
slot3.getcoords()

Rock1 = ClickableEntity(5,30)
print("we will now take coords for rock 1")
Rock1.getcoords()

Rock2 = ClickableEntity(5,30)
print("we will now take coords for rock 2")
Rock2.getcoords()

Rock3 = ClickableEntity(5,30)
print("we will now take coords for rock 3")
Rock3.getcoords()





for i in range(2000): #sets number of repititions 

    
    Rock1.genclick()
    normdistwait(1.45,.1)
    Rock2.genclick()
    normdistwait(1.45,.1)
    Rock3.genclick()
    normdistwait(1.2,.1)

    slot1.dropclick()
    normdistwait(.02,.002)
    slot2.dropclick()
    normdistwait(.02,.002)
    slot3.dropclick()
    normdistwait(.02,.002)
    breaktime()


print("bubba")
