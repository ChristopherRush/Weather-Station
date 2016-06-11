#!/usr/bin/env python


# Chris Rush
# Initial Date: 01 June 2016
# Last Updated: 11 June 2016

import sys
import time
import math
import struct

debug =0
millimeters =0

if sys.version_info<(3,0):
	p_version=2
else:
	p_version=3

if sys.platform == 'uwp':
	import winrt_smbus as smbus
	bus = smbus.SMBus(1)
else:
	import smbus
	import RPi.GPIO as GPIO
	rev = GPIO.RPI_REVISION
	if rev == 2 or rev == 3:
		bus = smbus.SMBus(1)
	else:
		bus = smbus.SMBus(0)

# I2C Address of Arduino
address = 0x04

# Command Format
# digitalRead() command format header
dRead_cmd = [1]
# digitalWrite() command format header
dWrite_cmd = [2]
# analogRead() command format header
aRead_cmd = [3]
# analogWrite() command format header
aWrite_cmd = [4]
# pinMode() command format header
pMode_cmd = [5]
# Rain gauge
rain_cmd = [6]
# Anenometer read
aa_cmd = [7]

# This allows us to be more specific about which commands contain unused bytes
unused = 0

# Function declarations of the various functions used for encoding and sending
# data from RPi to Arduino


# Write I2C block
def write_i2c_block(address, block):
	try:
		return bus.write_i2c_block_data(address, 1, block)
	except IOError:
		if debug:
			print ("IOError")
		return -1

# Read I2C byte
def read_i2c_byte(address):
	try:
		return bus.read_byte(address)
	except IOError:
		if debug:
			print ("IOError")
		return -1


# Read I2C block
def read_i2c_block(address):
	try:
		return bus.read_i2c_block_data(address, 1)
	except IOError:
		if debug:
			print ("IOError")
		return -1

# Arduino Digital Read
def digitalRead(pin):
	write_i2c_block(address, dRead_cmd + [pin, unused, unused])
	time.sleep(.1)
	n = read_i2c_byte(address)
	return n

# Arduino Digital Write
def digitalWrite(pin, value):
	write_i2c_block(address, dWrite_cmd + [pin, value, unused])
	return 1


# Setting Up Pin mode on Arduino
def pinMode(pin, mode):
	if mode == "OUTPUT":
		write_i2c_block(address, pMode_cmd + [pin, 1, unused])
	elif mode == "INPUT":
		write_i2c_block(address, pMode_cmd + [pin, 0, unused])
	return 1


# Read analog value from Pin
def analogRead(pin):
	bus.write_i2c_block_data(address, 1, aRead_cmd + [pin, unused, unused])
	time.sleep(.2)
	bus.read_byte(address)
	number = bus.read_i2c_block_data(address, 1)
	time.sleep(.2)
	return number[1] * 256 + number[2]


# Write PWM
def analogWrite(pin, value):
	write_i2c_block(address, aWrite_cmd + [pin, value, unused])
	return 1

# Read the value of the Rain Gauge
def rain_gauge(pin):
	write_i2c_block(address, rain_cmd + [unused, unused, unused])
	time.sleep(.2)
	val = read_i2c_byte(address)
	mm = val * 0.3
	return mm



# Read temp in Celsius from Grove Temperature Sensor
def temp36(pin):

	a = analogRead(pin)
	volts = a * 5.0 / 1024
	t = (volts - 0.5) * 100
	return t

# Read value from Grove Ultrasonic
def anenometerRead():
	write_i2c_block(address, aa_cmd + [unused, unused, unused])
	time.sleep(.2)
	number = read_i2c_byte(address)
	rpm = number * 60
	mph = 0.7 * 3.14 * rpm * 60 / 5280

	mph = round(mph, 2)
	return mph
