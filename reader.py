import time, struct, sys
import numpy as np
from scipy import stats
#from BinaryConverterFunctions import float_dec2bin, float_bin2dec
from packing import packaging, packaging4

if len(sys.argv) != 3:
    print("usage: python reader2.py filename <samples>")
    exit()

filenameFlag = sys.argv[1] # what file is it reading from?
samplesFlag = int(sys.argv[2]) # how many things should it try to read
RELATIVE = 1

samples = np.zeros(samplesFlag, dtype='float')

file = open(filenameFlag, "rb")
file.seek(0, 0)
#checklist = packaging(file.read(8))
i = 0
while(i < samplesFlag):
    checklistcheck = file.read(8)
    #checklistcheck = file.read(2)

    if len(checklistcheck) < 8:
    #if len(checklistcheck) < 2:
        print(i)
        i = samplesFlag
        print(checklistcheck)
        print("End of file")
    else:
        checklist = packaging(checklistcheck)
        #checklist = checklistcheck

    if checklist == b'\xFE\xDC':
        a = packaging(file.read(8))
        b = packaging(file.read(8))
        c = b''.join([a,b])
        (f,) = struct.unpack('f', c)
        #(f,) = struct.unpack('f', file.read(4))
        samples[i] = f
        i+=1
    else:
        file.seek(-7, RELATIVE)
        #file.seek(-1, RELATIVE)
file.close()

freqs = stats.itemfreq(samples)
errors = np.sum(samples[1:] < samples[:-1])
print("There were", errors, "relating to timestamps decreasing")

for k in freqs:
    print("Time Stamp", k[0])
    print("Showed up", int(k[1]), "times")
