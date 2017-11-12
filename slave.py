#!/usr/bin/env python2

import serial
import sys
import datetime


def config():
        ser = serial.Serial("/tmp/ttyS1")
        return ser

def readFromSerial(ser):
        while True:
                ret = ser.readline().strip("\n")
                cur = datetime.datetime.now()
                if ret == "date":
                        val = cur.strftime("%Y-%m-%d")
                        ser.write(val + "\n")

                elif ret == "time":
                        val = cur.strftime("%H:%M")
                        ser.write(val + "\n")

                elif ret == "hey Siri":
                        ser.write("hi how can I help you!\n")
		
		else:
                        ser.write("ERROR\n")

if __name__ == "__main__":
        ser = config()
        readFromSerial(ser)
