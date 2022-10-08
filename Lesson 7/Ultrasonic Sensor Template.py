import RPi.GPIO as GPIO
import time
 
trigPin = 
echoPin = 
MAX_DISTANCE =           # define the maximum measuring distance, unit: cm
timeOut = MAX_DISTANCE*   # calculate timeout according to the maximum measuring distance
 
def pulseIn(pin,level,timeOut): # obtain pulse time of a pin under timeOut
    t0 = #take the refrence time
    while(GPIO.input(pin) != level):
        #check if a time out occured
    t0 = #take a refrence time
    while(GPIO.input(pin) == level):
        #check if a time out occured
    pulseTime #calculate the pulse time
    return pulseTime
    
def getSonar():     # get the measurement results of ultrasonic module,with unit: cm
    # make trigPin output 10us HIGH level 
    # make trigPin output LOW level 
    pingTime = pulseIn(echoPin,GPIO.HIGH,timeOut)   # read plus time of echoPin
    distance = # calculate distance with sound speed 340m/s 
    return distance
    
def setup():
    GPIO.setmode(GPIO.BOARD)      # use PHYSICAL GPIO Numbering
    # set trigPin to OUTPUT mode
    # set echoPin to INPUT mode
 
def loop():
    while(True):
        distance = getSonar() # get distance
        print ("The distance is : %.2f cm"%(distance))
        time.sleep(1)
        
if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        GPIO.cleanup()         # release GPIO resource

