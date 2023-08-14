import time
import board
import digitalio

red_led = digitalio.DigitalInOut(board.GP10)
red_led.direction = digitalio.Direction.OUTPUT
amber_led = digitalio.DigitalInOut(board.GP11)
amber_led.direction = digitalio.Direction.OUTPUT
green_led = digitalio.DigitalInOut(board.GP12)
green_led.direction = digitalio.Direction.OUTPUT

while True:
    green_led.value = False
    green_led.value = True
    time.sleep(3)
    amber_led.value = True
    amber_led.value = False
    time.sleep(5)
    red_led.value = True
    time.sleep(2)
    red_led.value = False


