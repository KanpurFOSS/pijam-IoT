#pip install Flask
#export FLASK_APP=pilab.py
#python -m flask run--host=0.0.0.0  for intranet
#http://0.0.0.0:5000/on
#http://0.0.0.0:5000/off

import time
import RPi.GPIO as GPIO
from flask import Flask

app = Flask(__name__)
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
ledPin = 20 # Broadcom pin 40
rPin=26
GPIO.setup(ledPin,GPIO.OUT)
GPIO.setup(rPin,GPIO.OUT)
GPIO.output(ledPin,GPIO.LOW)
GPIO.output(rPin,GPIO.LOW)
GPIO.output(ledPin,GPIO.HIGH)
GPIO.output(rPin,GPIO.HIGH)

@app.route('/')
def hello_world():

        GPIO.output(ledPin, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(ledPin, GPIO.LOW)
        time.sleep(1)
        return 'Hello blink!'

@app.route('/off')
def on():
    GPIO.output(ledPin, GPIO.HIGH)
    time.sleep(3)
    GPIO.output(rPin, GPIO.HIGH)
    time.sleep(5)

    #GPIO.cleanup()
    return 'of.....'

@app.route('/on')
def off():
    GPIO.output(ledPin, GPIO.LOW)
    time.sleep(2)
    GPIO.output(rPin, GPIO.LOW)
    time.sleep(2)


    #GPIO.cleanup()
    return 'on....'

if __name__ == '__main__':
    app.run()

