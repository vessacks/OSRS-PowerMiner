#powerminer 2.0.0
#note: needs breakRoller and clickableEntity

from calendar import c
import pyautogui
import time
import numpy as np
from pyHM import mouse

import breakRoller
import clickableEntity



#gets the coords for everything
#decent parameters are (2,10) for slots and (5,30) for rocks on samsung monitor
#decent parameters are (7,300) for slots and unknown for rocks on samsumg monitor

slot1 = clickableEntity.clickableEntity(2,10)
print("we will now take coords for inventory slot 1" )
slot1.getcoords()

slot2 = clickableEntity.clickableEntity(2,10)
print("we will now take coords for inventory slot 2" )
slot2.getcoords()

slot3 = clickableEntity.clickableEntity(2,10)
print("we will now take coords for inventory slot 3" )
slot3.getcoords()

Rock1 = clickableEntity.clickableEntity(5,30)
print("we will now take coords for rock 1")
Rock1.getcoords()

Rock2 = clickableEntity.clickableEntity(5,30)
print("we will now take coords for rock 2")
Rock2.getcoords()

Rock3 = clickableEntity.clickableEntity(5,30)
print("we will now take coords for rock 3")
Rock3.getcoords()


#this determines how long to run for
count = 0
startTime = time.time()

countOrSecond = input('would you like to run for #seconds or #counts? (s/c)')
if countOrSecond == 's':
    durationSeconds = float(input('please input number of seconds to run (1h= 3600, 6h=21600'))
    
elif countOrSecond == 'c':
    durationCount = int(input('please enter the number of counts to perform'))
    
else:
    print('you\'ve messed something up, quitting program now' )



def normdistwait(mean, standarddev):
    #normal distribution determines how long to wait between rock clicks
    time.sleep(np.random.normal(loc=mean,scale=standarddev))
count = 0
startTime = time.time()

while True: #run loop 
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
   
    #breakroller
    breakRoller.breaktime()

    #this is the count/seconds section
    count += 1
    runTime = round(time.time() - startTime,0)
    countSec = round(count/runTime,2)
    print('count = %s | runTime = %s seconds | count/sec = %s | cycletime = %s'%(count, runTime, countSec, waitTotal))

    #termination conditions
    if pyautogui.position() == pyautogui.Point(0,0):
        print('quitting program')
        quit()
    if countOrSecond == 's' and runTime > durationSeconds:
        print('quitting program')
        quit()
    if countOrSecond == 'c' and count > durationCount:
        print('quitting program')
        quit()
    


