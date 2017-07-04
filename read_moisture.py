#!/usr/bin/python
import time

#import ADC code
import Adafruit_ADS1x15

#import numpy for median
import numpy

#import Raspberry Pi GPIO
import RPi.GPIO as GPIO

#create a function to reutrn the soil moisture; x = channel
def read_moisture(x):
    #Create an ADS1015 ADC (12-bit) instance
    adc = Adafruit_ADS1x15.ADS1015()

    GAIN = 1

    readings = []

    #take 5 readings .5 seconds apart and store in list
    for i in range(5):
        readings.append(adc.read_adc(x, gain=GAIN))
        time.sleep(0.5)

    soil = numpy.median(readings)

    return soil

#print read_moisture(0)

#set GPIO numbering
GPIO.setmode(GPIO.BCM)
#set pin 17 as output and default of off
GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW)


while True:
    if read_moisture(0) > 1000:
        GPIO.output(17, True) #turn on water
        time.sleep(5)
        GPIO.output(17, False)  #turn off water
        localtime = time.asctime( time.localtime(time.time()) )
        print "Plant watered at:", localtime
    else:
        localtime = time.asctime( time.localtime(time.time()) )
        print "Plant did not need water:", localtime


    time.sleep(3600)
