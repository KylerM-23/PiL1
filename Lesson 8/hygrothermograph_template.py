import RPi.GPIO as GPIO
import time, requests
import Freenove_DHT as DHT

DHTPin = #pin number for the DHT pin

error_messages = {0: "DHT OK",
                  -1: "Checksum error",
                  -2: "Timeout error"}
                  
def get_reading(dht, logging=False):
    while True:
        chk = dht.readDHT11()
        if #check is ok and temp and humidity not 0):
            #return the temp and humidity
        else:
            if logging:
                print(error_messages[chk])
            time.sleep(2)

def loop():
    #create an instance of the DHT   
    while True:
        #save the humidity and temperature from the DHT
        print("Humidity : %.2f, \t Temperature : %.2f \n"%(humidity,temp))
        #sleep for a period of time       
        
if __name__ == '__main__':
    print ('Program is starting ... ')
    try:
        loop()
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit()
