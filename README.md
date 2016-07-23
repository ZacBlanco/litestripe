# Litestripe

A library and web interface that can be run off of a Raspberry Pi to control a strip of RGB LEDs.

## Pre-Requisites

- [pigio](http://abyz.co.uk/rpi/pigpio/index.html) daemon installed and running on your pi
  - You should be able to run `sudo apt-get install pigpio`
- You'll also need the [pigpio python library](http://abyz.co.uk/rpi/pigpio/python.html). 

	git clone https://github.com/joan2937/pigpio.git
	cd pigpio/
	sudo python setup.py install

## Litestripe-core

The core library provides a host of user-friendly functions for controlling the colors of the LED's of the raspberry pi. [See the docs for more info]()

## Litestripe-server

The server module provides an http server which hosts a pre-made user interface to control your lights off of something as simple as your phone!

More information about litestripe server [can be found in the docs]()
