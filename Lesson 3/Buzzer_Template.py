import RPi.GPIO as GPIO
import time
 
buzzer_pin = #enter buzzer pin
 
def setup():
    # add code to disable warnings
 
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(buzzer_pin, GPIO.OUT)
 
def loop():
    while True:
        GPIO.output(buzzer_pin, GPIO.HIGH)  # make buzzer_Pin output HIGH level to turn on buzzer
        print ('buzzer turned on >>>')     # print information on terminal
        time.sleep(1)                   # Wait for 1 second
        GPIO.output(buzzer_pin, GPIO.LOW)   # make buzzer_pin output LOW level to turn off buzzer
        print ('buzzer turned off <<<')
        time.sleep(1)                   # Wait for 1 second
 
def destroy():
    GPIO.cleanup()                      # Release all GPIO
 
if __name__ == '__main__':    # Program entrance
    print ('Program is starting ... \n')
    setup()
    try:
        loop()
    except KeyboardInterrupt:   # Press ctrl-c to end the program.
        destroy() 

