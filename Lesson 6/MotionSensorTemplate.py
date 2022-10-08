import RPi.GPIO as GPIO
 
ledPin =    #board pin for the LED
sensorPin = #board pin for the IR sensor
 
def setup():
    GPIO.setmode(GPIO.BOARD)        # use PHYSICAL GPIO Numbering
    GPIO.setup(ledPin, )    # set ledPin to OUTPUT mode
    GPIO.setup(sensorPin, ) # set sensorPin to INPUT mode
 
def loop():
    while True:
        if GPIO.input(sensorPin)==GPIO.HIGH:
            #Turn on the LED and create a message to display
        else :
            #Turn off the LED and create a message to display
 
def destroy():
    GPIO.cleanup()                     # Release GPIO resource
 
if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()  

