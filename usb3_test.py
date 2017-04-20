import usb.core
import usb.util
from datetime import datetime

dev = usb.core.find(idVendor=0x04B4, idProduct=0x00F1)
print(dev)

ITERATIONS = 1000
BUFFER_SIZE = 65536

dev.set_configuration()

starttime = datetime.now()

for i in range(0, ITERATIONS):
    data = dev.read(0x81, BUFFER_SIZE, 200)

endtime = datetime.now()

delta = (endtime-starttime).total_seconds()

print("USB Time: {} seconds".format(delta))

speed_Bsec = (ITERATIONS*BUFFER_SIZE)/delta
speed_MBsec = speed_Bsec/(1024*1024)

print("Transfer speed: {} MB/Sec".format(speed_MBsec))
