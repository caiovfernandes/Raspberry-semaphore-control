import RPi.GPIO as GPIO
from time import sleep

def config_gpio():
    GPIO.setmode(GPIO.BCM)

def gpio_setup_out(port):
    GPIO.setup(port, GPIO.OUT)

def gpio_setup_in(port):
    GPIO.setup(port, GPIO.IN)

def output_high(port):
    GPIO.output(port, 1)

def output_low(port):
    GPIO.output(port, 0)

def gpio_toggle(port, time):
    gpio_high(port)
    sleep(time)
    gpio_low(port)

def set_gpio_event_detection(channel, bouncetime, callback):
    GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=bouncetime, callback=callback)