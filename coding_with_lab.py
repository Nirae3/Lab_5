from machine import Pin, I2C
import time


i2c = I2C(1, sda=Pin(14), scl=Pin(15)) # will create i2c object that talks through channel 1.
devices = i2c.scan() # will scan the device address

for d in devices: # print the address of the devices that is loud.
    address = "0x{:02x}".format(d)
    #print(address)
print("found the address")


date = "\x15\x14\x03\x02\x10\x10\x23"
i2c.writeto_mem(0x68, 0x00, date.encode()) # write to the address indicated. write in the memory 0x00

def bcd2dec(bcd): 
    return ((bcd >> 4) * 10) + (bcd & 0x0F)

for i in range(15):
    data = i2c.readfrom_mem(0x68, 0x00, 7)
    seconds = bcd2dec(data[0])
    minutes = bcd2dec(data[1])
    hours   = bcd2dec(data[2])
    
    print("{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds))
    time.sleep(1)

# open and write to the log file
try:
    log = open("log.txt", "w")
    log.write("Hello World!\n")
    log.write("hiiii\n")
    log.flush()
finally:
    log.close()

