import RPi.GPIO as GPIO          
from time import sleep

def forward():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(2,GPIO.OUT)
    GPIO.setup(3,GPIO.OUT)
    GPIO.setup(17,GPIO.OUT)
    GPIO.setup(27,GPIO.OUT)
    GPIO.output(2,GPIO.LOW)
    GPIO.output(3,GPIO.HIGH)
    GPIO.output(17,GPIO.LOW)
    GPIO.output(27,GPIO.HIGH)
    sleep(1)
    GPIO.output(2,GPIO.LOW)
    GPIO.output(3,GPIO.LOW)
    GPIO.output(17,GPIO.LOW)
    GPIO.output(27,GPIO.LOW)



def back():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(2,GPIO.OUT)
    GPIO.setup(3,GPIO.OUT)
    GPIO.setup(17,GPIO.OUT)
    GPIO.setup(27,GPIO.OUT)
    GPIO.output(2,GPIO.HIGH)
    GPIO.output(3,GPIO.LOW)
    GPIO.output(17,GPIO.HIGH)
    GPIO.output(27,GPIO.LOW)
    sleep(1)
    GPIO.output(2,GPIO.LOW)
    GPIO.output(3,GPIO.LOW)
    GPIO.output(17,GPIO.LOW)
    GPIO.output(27,GPIO.LOW)

def right():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(2,GPIO.OUT)
    GPIO.setup(3,GPIO.OUT)
    GPIO.output(2,GPIO.LOW)
    GPIO.output(3,GPIO.HIGH)
    sleep(1)
    GPIO.output(2,GPIO.LOW)
    GPIO.output(3,GPIO.LOW)

def left():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17,GPIO.OUT)
    GPIO.setup(27,GPIO.OUT)
    GPIO.output(17,GPIO.LOW)
    GPIO.output(27,GPIO.HIGH)
    sleep(1)
    GPIO.output(17,GPIO.LOW)
    GPIO.output(27,GPIO.LOW)
