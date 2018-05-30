import time, sys;
import struct
from BinaryConverterFunctions import float_dec2bin, float_bin2dec

fileName = sys.argv[1]
waitTime = float(sys.argv[2])
open("TSTestReceive", 'w').close()
ts = time.time()
time.sleep(0)
i=1
#while(time.time()<ts+.01):
f = open(fileName, "wb")
while(True):
    s=(time.time()*1000-ts*1000)
    data = struct.pack('f', s)

    print(s)

    f.write(b'\xFE\xDC')
    f.write(data)

    time.sleep(waitTime)
f.close()


