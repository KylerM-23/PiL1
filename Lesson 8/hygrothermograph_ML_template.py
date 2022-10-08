import RPi.GPIO as GPIO
import time, requests
import Freenove_DHT as DHT
from predict import *

modelID = #set your model id

DHTPin = #set the pin number

error_messages = {0: "DHT OK",
                  -1: "Checksum error",
                  -2: "Timeout error"}
                  
def testModel():
    #create the DHT object
    prediction = None
    #set the modelID
    
    while True:
        #get the humidity and temp and place it into a list with humidity and then temp
        print("Humidity:", data[0], "Temperature:", data[1])
        #call the classify function with our data and then access the first index in predictions

        if answer == 0:
            prediction =
        elif answer == 1:
            prediction = 
        elif answer == 2:
            prediction = 
        #output the prediction and add a wait

def get_reading(dht, logging=False):
    while True:
        chk = dht.readDHT11()     #read DHT11 and get a return value. Then determine whether data read is normal according to the return value.
        if (chk is dht.DHTLIB_OK and not(dht.temperature == 0 and dht.humidity == 0)):      #read DHT11 and get a return value. Then determine whether data read is normal according to the return value.
            return (dht.humidity, dht.temperature)
        else:
            if logging:
                print(error_messages[chk])
            time.sleep(2)
    
        
if __name__ == '__main__':
    print ('Program is starting ... ')
    try:
        testModel()
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit()
