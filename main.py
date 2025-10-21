from machine import Pin, I2C
import time


i2c = I2C(1, sda=Pin(14), scl=Pin(15)) # will create i2c object that talks through channel 1.

devices = i2c.scan() # will scan the device address

for d in devices: # print the address of the devices that is loud.
    address = "0x{:02x}".format(d)
    #print(address)
print("found the address")


seconds = "x07"
i2c.writeto_mem(0x68, 0x00, seconds.encode()) # write to the address indicated. write in the memory 0x00

data = i2c.readfrom_mem(0x68, 0x00, 3) # address for device, which memory address to read from, how many bytes

for i in range(5): #loop through 5 times to see if the seconds increase.
    print(data)
    time.sleep(2)