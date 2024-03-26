# Reaction Game

This project was developed as part of a training program for certified technicians. The challenge was to create a "Pocket Game" that fits within a casing measuring 2.5 cm x 4 cm x 6 cm (H x W x D).


## Table of Contents

1. [Features](#features)
2. [Gameplay](#gameplay)
3. [Technical Details](#technicaldetails)
4. [Pictures](#pictures)
5. [Usage](#Usage)
6. [License](#license)

## Features

The Pocket Game is a Reaction Game with three LEDs, three switches, and an ON/OFF switch. The casing was designed using 3D printing and Autodesk Fusion 360. The circuit board was created with EasyEDA. Inside the casing, there's a lithium-polymer battery providing several hours of runtime, which can be charged via USB-C.

## Gameplay

The game operates as follows: Upon pressing the START button, the middle white LED illuminates continuously. After a random period, the LED goes out, and Player 1 and Player 2 must attempt to press their switches as quickly as possible. The player who reacts the fastest will have their LED light up for one second, and the game restarts.

## Technical Details

    Casing: 3D-printed casing
    Circuit Board: Designed using EasyEDA
    Switches: 3x 12v/DC 50mA
    LEDs: 2x 5mm LED in Green, 1x 5mm LED in White
    Microcontroller: Beetle ESP32 with USB-C charging capability
    Power Supply: EEMB 3.7V 150mAh Lithium Polymer Battery

## Pictures

<img src="/images/case.png" alt="Image of the reaction game case." width="400" height="300">
<img src="/images/case_measuring.png" alt="Image of the reaction game case." width="800" height="300">

## Usage

    1. Turn on the game using the ON/OFF switch.
    2. Press the START button to begin the game.
    3. React quickly to press the switch when the middle LED goes out.
    4. The player with the fastest reaction wins.

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute the code.
