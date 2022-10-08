import RPi.GPIO as GPIO
import time
from songs import *

BuzzerPin = 23    # BCM numbering pin23 
SPEED = 1 
 
def setup():
    GPIO.setmode(GPIO.BCM) # BCM numbering
    GPIO.setup(BuzzerPin, GPIO.OUT)
 
def playTone(p,tone):
        # calculate duration based on speed and tone-length
    duration = (1./(tone[1]*0.25*SPEED))
 
    if tone[0] == "p": # p => pause
        time.sleep(duration)
    else: # let's rock n roll
        frequency = TONES[tone[0]]
        #change the freq
        p.start(0.5)
        time.sleep(duration)
        p.stop()
 
def run(song):
    #create pwm pin
    #start pwm pin
    print('Now playing: ', song)
    for t in SONGS[song]:
        playTone(p,t)
 
def destroy():
    GPIO.output(BuzzerPin, GPIO.LOW)
    GPIO.cleanup()                     # Release resource
 
if __name__ == '__main__':     # Program start from here
    setup()
    try:
        for song in SONGS.keys():
            run(song)
        GPIO.cleanup()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()

