#breakroller
import numpy as np
import time

def breaktime():
#this guy determines if it should take a break
    breakroller = np.random.randint(0,450)
    hibernation_time = (np.random.randint(10,140)) #breaktime random time between 10-140 seconds
    if breakroller == 1:
        print("Breakroll! hibernating for "+ str(hibernation_time)+ " seconds")
        time.sleep(hibernation_time)
        
    #else:
        #print("breakroller was "+ str(breakroller)+ ". I would have hibernated for "+ str(hibernation_time) + " seconds.")