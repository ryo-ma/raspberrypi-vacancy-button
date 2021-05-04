# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from time import sleep

RED_LED_GPIO = 4
RED_TACT_GPIO = 17

BLUE_LED_GPIO = 27
BLUE_TACT_GPIO = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_LED_GPIO, GPIO.OUT)
GPIO.setup(RED_TACT_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(BLUE_LED_GPIO, GPIO.OUT)
GPIO.setup(BLUE_TACT_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

is_vacant = False


try:
    print('--- start program ---')
    while True:
        if GPIO.input(RED_TACT_GPIO) == GPIO.HIGH:
            is_vacant = False
            print("red switch on")
            GPIO.output(RED_LED_GPIO, GPIO.HIGH)
            GPIO.output(BLUE_LED_GPIO, GPIO.LOW)
            sleep(0.1)
        elif GPIO.input(BLUE_TACT_GPIO) == GPIO.HIGH:
            is_vacant = True
            print("blue switch on")
            GPIO.output(BLUE_LED_GPIO, GPIO.HIGH)
            GPIO.output(RED_LED_GPIO, GPIO.LOW)
            sleep(0.1)
        sleep(0.01)
except KeyboardInterrupt:
    pass
finally:
    GPIO.output(RED_LED_GPIO, GPIO.LOW)
    GPIO.output(BLUE_LED_GPIO, GPIO.LOW)
    GPIO.cleanup()
    print('--- stop program ---')
