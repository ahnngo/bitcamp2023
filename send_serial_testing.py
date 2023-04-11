import serial
import sys

arduino = serial.Serial('COM10', baudrate=9600, timeout=1)

def flash_light(label):
    arduino.write(1)
    #arduino.close()

