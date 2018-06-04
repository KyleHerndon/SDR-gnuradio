import time, sys;
import struct
from BinaryConverterFunctions import float_dec2bin, float_bin2dec
from hashlib import md5

fileName = sys.argv[1]
waitTime = float(sys.argv[2])
open("TSTestReceive", 'w').close()
ts = time.time()
time.sleep(0)
i=1
#while(time.time()<ts+.01):
f = open(fileName, "wb", 0)
while(True):
    s=(time.time()*1000-ts*1000)
    data = struct.pack('f', s)
    (data2,) = struct.unpack('f',data)

    h = md5.new()
    h.update(data2)
    h.digest()
    
    chksum = struct.pack('l', h[-4:])

    print(s)

    f.write(chksum)
    f.write(data)

    time.sleep(waitTime)
f.close()


