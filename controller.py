import pyfirmata
from serial import Serial, SerialException
import serial.tools.list_ports as list_ports
from pyfirmata import Arduino
import time

comPort = 'COM3'
board = pyfirmata.Arduino(comPort)
print("Version -",board.get_firmata_version())

led_1 = board.get_pin('d:8:o')
led_2 = board.get_pin('d:9:o')
led_3 = board.get_pin('d:10:o')
# led_3 = board.get_pin('d:13:o')

def ledLight(val):
    if val['c_red'] == 1:
        led_1.write(1)
    if val['c_blue'] == 1:
        led_2.write(1)
    if val['c_green'] == 1:
        led_3.write(1)
    # if val['c_orange'] == 1:
    #     led_3.write(1)
    # if val['c_yellow'] == 1:
    #     led_3.write(1)
    if val['c_red'] == 0:
        led_1.write(0)
    if val['c_blue'] == 0:
        led_2.write(0)
    if val['c_green'] == 0:
        led_3.write(0)
    # if val['c_orange'] == 0:
    #     led_3.write(0)
    # if val['c_yellow'] == 0:
    #     led_3.write(0)
#Serial.close()