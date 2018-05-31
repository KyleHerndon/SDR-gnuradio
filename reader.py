import time, struct, sys
import numpy as np
from scipy import stats
from packing import packaging, packaging4

if len(sys.argv) != 3:
    print("usage: python reader2.py filename <samples>")
    exit()

filenameFlag = sys.argv[1] # what file is it reading from?
samplesFlag = int(sys.argv[2]) # how many things should it try to read
RELATIVE = 1

samples = np.zeros(samplesFlag, dtype='float')

file = open(filenameFlag, "rb")
i = 0
while(i < samplesFlag):
    chksum = b''.join(packaging(file.read(8), file.read(8)))
    message = b''.join(packaging(file.read(8), file.read(8)))

    if len(chksum) < 4 or len(data) < 4:
        print(i)
        i = samplesFlag
        print("End of file")

    (data,) = struct.unpack('f', message)
    hash2 = hash(data)[-4:]

    if chksum == hash2:
        samples[i] = data
        i+=1
    else:
        file.seek(-31, RELATIVE)
file.close()

freqs = stats.itemfreq(samples)
errors = np.sum(samples[1:] < samples[:-1])
print("There were", errors, "relating to timestamps decreasing")

for k in freqs:
    print("Time Stamp", k[0])
    print("Showed up", int(k[1]), "times")

"""for k in range(len(samples)):
    Time = samples[k]
    if (Time != PrevTime and Time != 0):
        print("Time Stamp: " + str(Time))
        print("Showed up " + str(z))
        z = 1
        PrevTime = Time
#   elif (Time != PrevTime and Time != 0 and firstone == 1):
#       PrevTime = Time
#       z = z+1
#       firstone = 0
    elif (Time != 0):
        z = z+1
    else:
        print("ERROR!")
print("Time Stamp: " + str(Time))
print("Showed up " + str(z))
Bin.close()"""