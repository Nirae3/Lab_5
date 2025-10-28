from machine import I2C, Pin
import time

i2c = I2C(1, sda=Pin(14), scl=Pin(15)) # will create i2c object that talks through channel 1.

led=Pin(16, Pin.OUT) # innitialise led
sw5 = Pin(22, Pin.IN, Pin.PULL_DOWN) # initialise button
devices = i2c.scan() # will scan the device address
date = "\x00\x00"

i2c.writeto_mem(0x68, 0x00, date.encode()) # write to the address indicated. write in the memory 0x00

def convert_from_bcd_to_decimal(bcd): # convert from bcd to decimal to understand the time
    return ((bcd >> 4) * 10) + (bcd & 0x0F) # taken from chatGPT

def button_pressed():
    # Button starts LOW (unpressed)
    if sw5.value() == 0:
        time.sleep(0.1)
        if sw5.value() == 1: # When the button is pressed...
            return True
    return False

def count_seconds():
    data = i2c.readfrom_mem(0x68, 0x00, 7)
    seconds = convert_from_bcd_to_decimal(data[0])
    minutes = convert_from_bcd_to_decimal(data[1])
    print("{:02d}:{:02d}".format(minutes, seconds))
    time.sleep(1)

while True:
    if button_pressed():
        print("Button pressed!")
        led.on()
        count_seconds()
    else:
        led.off()