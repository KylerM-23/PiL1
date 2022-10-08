import RPi.GPIO as GPIO
import time
 
LedPin = #Enter the board number for the pin GPIO 18
 
def setup():
    global p
    #setup the GPIO for board mode
    #setup the pin for output and turn it off
 
    #create PWM pin and set to 500Hz
    #start PWM pin at 0% duty cycle
 
def loop():
    while True:
        #Set the range to chnage the duty cycle from 0 to 100 at steps of 1
        for dc in range(X, Y, S):   # make the led brighter
            #change duty cycle
            time.sleep(0.01)
        time.sleep(1)
        #Set the range to chnage the duty cycle from 100 to 0 at steps of 1
        for dc in range(X, Y, S):
            #change the duty cycle
            time.sleep(0.01)
        time.sleep(1)
 
def destroy():
    #Stop PWM
    GPIO.cleanup() # Release all GPIO
 
if __name__ == '__main__':     # Program entrance
    print ('Program is starting ... ')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy() 

