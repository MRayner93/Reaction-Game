import random
import time
from machine import Pin

led1 = Pin(2, Pin.OUT)
led2 = Pin(9, Pin.OUT)
led3 = Pin(8, Pin.OUT)
switch1 = Pin(21, Pin.IN, Pin.PULL_UP)
switch2 = Pin(20, Pin.IN, Pin.PULL_UP)
switch3 = Pin(7, Pin.IN, Pin.PULL_UP)

# LED2 leuchtet konstant
def light_led2():
    led2.value(1)

# Zufällige Verzögerung
def random_delay():
    delay = random.randint(3, 10)
    for i in range(delay):
        light_led2()

# Aktivierung von LED1 oder LED3 basierend auf dem gewählten Schalter
def activate_led(switch, led):
    if not switch.value():
        led.value(1)

# Spielstart
while True:
    if not switch3.value():
        # LED2 leuchtet konstant für eine zufällige Verzögerung
        random_delay()
        
        # Warten auf Eingabe von switch1 oder switch2
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
                
            # Überprüfen, ob Zeit abgelaufen ist
            current_time = time.time()
            if current_time - start_time > 5:  # Zeitlimit von 5 Sekunden
                print("Time's up!")
                break
                
        # Überprüfen, welcher Schalter zuerst gedrückt wurde
        if led1.value():
            print("Switch 1 wins!")
            time.sleep(5)
        elif led3.value():
            print("Switch 2 wins!")
            time.sleep(5)
        # Spielende
        led1.value(0)
        led2.value(0)
        led3.value(0)
        time.sleep(1)
