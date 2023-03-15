from machine import Pin
import time
import random

# LED-Pins initialisieren
led1_pin = Pin(5, Pin.OUT)
led2_pin = Pin(18, Pin.OUT)
led3_pin = Pin(19, Pin.OUT)

# Schalter-Pins initialisieren
switch1_pin = Pin(21, Pin.IN, Pin.PULL_UP)
switch2_pin = Pin(22, Pin.IN, Pin.PULL_UP)

# Zufällige Zeit auswählen, bis die LED blinkt
blink_time = random.uniform(5, 10)

# Warten, bis beide Schalter gleichzeitig gedrückt werden
while switch1_pin.value() == 1 or switch2_pin.value() == 1:
    pass

# LED blinkt
led1_pin.on()
time.sleep(blink_time)
led1_pin.off()

# Warten, bis einer der beiden Schalter gedrückt wird
while switch1_pin.value() == 1 and switch2_pin.value() == 1:
    pass

# Überprüfen, welcher Schalter gedrückt wurde und entsprechende LED einschalten
if switch1_pin.value() == 0:
    led2_pin.on()
else:
    led3_pin.on()