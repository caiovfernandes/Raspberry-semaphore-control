import RPi.GPIO as GPIO
from gpio import set_gpio_event_detection, gpio_setup_in
from utils import get_pedestrian_sensors_pinout

def button_is_pressed_event(callback):
    channel = 7
    bouncetime = 400

    pedestrian_sensors_pinout = get_pedestrian_sensors_pinout()

    for pedestrian in pedestrian_sensors_pinout.values():
        for channel in pedestrian.values():
            gpio_setup_in(channel)
            set_gpio_event_detection(channel, bouncetime, callback)

