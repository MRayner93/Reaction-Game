import random
import time
from machine import Pin

led1 = Pin(2, Pin.OUT)
led2 = Pin(9, Pin.OUT)
led3 = Pin(8, Pin.OUT)
switch1 = Pin(21, Pin.IN, Pin.PULL_UP)
switch2 = Pin(20, Pin.IN, Pin.PULL_UP)
switch3 = Pin(7, Pin.IN, Pin.PULL_UP)

### Functions ####

# light up LED2
def light_led2():
    led2.value(1)

# random delay
def random_delay():
    delay = random.randint(3, 10)
    for i in range(delay):
        light_led2()

# Activation of LED1 or LED3 based on the selected switch
def activate_led(switch, led):
    if not switch.value():
        led.value(1)

### Loop ###

# Start Game
while True:
    if not switch3.value():
        # LED2 lights up for a random delay
        random_delay()
        
        # Waiting for input from switch1 or switch2
        start_time = time.time()
        while True:
            if not switch1.value():
                activate_led(switch1, led1)
                print("Switch 1 pressed")
                break
            elif not switch2.value():
                activate_led(switch2, led3)
                print("Switch 2 pressed")
                break
                
            # Checking if time has elapsed
            current_time = time.time()
            if current_time - start_time > 5:  # Timelimit of 5 Seconds
                print("Time's up!")
                break
                
        # Checking which switch was pressed first
        if led1.value():
            print("Switch 1 wins!")
            time.sleep(5)
        elif led3.value():
            print("Switch 2 wins!")
            time.sleep(5)
        # Game ends
        led1.value(0)
        led3.value(0)
        time.sleep(1)
