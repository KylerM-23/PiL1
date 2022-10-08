import RPi.GPIO as GPIO
import time
OFFSET_DUTY = #define pulse offset of servo
SERVO_MIN_DUTY = #define pulse duty cycle for minimum angle of servo
SERVO_MAX_DUTY = #define pulse duty cycle for maximum angle of servo
servoPin = #pin for servo communication
 
def mapNum( value, fromLow, fromHigh, toLow, toHigh):  # map a value from one range to another range
    return (toHigh-toLow)*(value-fromLow) / (fromHigh-fromLow) + toLow
 
def setup():
    global p
    GPIO.setmode(GPIO.BOARD)         # use PHYSICAL GPIO Numbering
    GPIO.setup(servoPin, GPIO.OUT)   # Set servoPin to OUTPUT mode
    GPIO.output(servoPin, GPIO.LOW)  # Make servoPin output LOW level
 
    p = # Create PWM pin for the servo and set Freq. to 50Hz
    # Set initial Duty Cycle to 0
    
def servoWrite(angle):      # make the servo rotate to specific angle, 0-180 
    if(angle<0):
        angle = 0
    elif(angle > 180):
        angle = 180
    # map the angle to duty cycle and output it
    
def loop():
    while True:
        for dc in range(,,):   # make servo rotate from 0 to 180 deg
            servoWrite(dc)     # Write dc value to servo
            time.sleep(0.001)
        time.sleep(0.5)
        for dc in range(, , ): # make servo rotate from 180 to 0 deg
            servoWrite(dc)
            time.sleep(0.001)
        time.sleep(0.5)
 
def destroy():
    p.stop()
    GPIO.cleanup()
 
if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
