import time, sys;
from BinaryConverterFunctions import float_dec2bin, float_bin2dec

fileName = sys.argv[1]
waitTime = float(sys.argv[2])
open("TSTestReceive", 'w').close()
ts = time.time()
time.sleep(0)
i=1
#while(time.time()<ts+.01):
open(fileName, "wb").close()
while(True):
	f = open(fileName, "wb")
	s=(time.time()*1000-ts*1000)
	print(s)
	#print(s)
	t = float_dec2bin(s)
	f.write("\xFE\xDC")
	f.write(t)
	#f.write("\xFE\xDC")
	f.close()
	#if((i % 10) == 0):
		#f = open("TSTestReceive", "ab")
		#s=(time.time()*1000-ts*1000)
		#print("Check: " + str(s))
		#t = float_dec2bin(s)
		#f.write("\xFE\xDC")
		#f.write(t)
		#f.write("\xFE\xDC")
		#f.close()
	#i += 1
	time.sleep(waitTime)



