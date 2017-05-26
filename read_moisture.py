#!/usr/bin/python
import time

import Adafruit_ADS1x15

import numpy

def read_moisture():
    #Create an ADS1015 ADC (12-bit) instance
    adc = Adafruit_ADS1x15.ADS1015()

    GAIN = 1

    readings = []

    for i in range(5):
        readings.append(adc.read_adc(0, gain=GAIN))
        time.sleep(0.5)

    soil = numpy.median(readings)

    return soil

print read_moisture()