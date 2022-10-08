import RPi.GPIO as GPIO
import time
import #module for getting online requests
 
ledPin = # define ledPin
 
def setup():
    GPIO.setmode(GPIO.BCM)       # use PHYSICAL GPIO Numbering
    GPIO.setup(ledPin, GPIO.OUT)   # set the ledPin to OUTPUT mode
    GPIO.output(ledPin, GPIO.LOW)  # make ledPin output LOW level 
    print ('Using pin%d'%ledPin)
 
def destroy():
    GPIO.cleanup()                      # Release all GPIO

modelID = #enter your model ID here
baseURL = 'https://aicode101.com'
api = '{base}/api/model/{model}/predict'.format( base = baseURL, model = modelID)
    
def classify_text(term):
    terms = [term]

    httpResponse = #create a get HTTP request
    
    response = httpResponse.json()
    
    prediction = #get the prediction from the response
    label = #get the highest prediction label
    confidence = prediction['confidences'][label]
    return #label and the confidence
 

def loop():
    while True:
        print('Type something')
        x = # read keyboard input
        label, confidence = classify_text(x)
        print(x + ';classify to: ' + label + ' with ' + str(confidence) + '% confidence')
        
        if label == 'Happy':
            #turn on the LED
        else:
            #turn off the LED

if __name__ == '__main__':    # Program entrance
    print ('Program is starting ... \n')
    setup()
    try:
        loop()
    except KeyboardInterrupt:   # Press ctrl-c to end the program.
        destroy()
