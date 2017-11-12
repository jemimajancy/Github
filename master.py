#!/usr/bin/env python2

import serial
import sys

def config():
        ser = serial.Serial("/tmp/ttyS0")
        return ser

def writeToSerial(ser):
        while True:
                input = raw_input("CMD: ")
                ser.write(input + "\n")
                ser.flush()
                print ser.readline()

if __name__ == "__main__":
        ser = config()
        writeToSerial(ser)
