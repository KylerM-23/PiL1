import #import GPIO module
import time
 
ledPin = #define ledPin with pin value
 
def setup():
    #add code here
    
def loop():
    while True:
        #add code here
 
def destroy():
    #add code here
 
if __name__ == '__main__':    # Program entrance
    print ('Program is starting ... \n')
    setup()
    try:
        loop()
    except KeyboardInterrupt:   # Press ctrl-c to end the program.
        destroy()

