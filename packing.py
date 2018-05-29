from struct import *

def middleStep(place, bitList):
	return ((bitList[place+1] % 16) + ((bitList[place+1] - (bitList[place+1] % 16))/16)*2 + (bitList[place] % 16)*4 + ((bitList[place] - (bitList[place] % 16))/16)*8)
def packaging(bits):
	
	
	bitListing = unpack('bbbbbbbb', bits)
	#print(bitListing)
	
	sixteensPlace = middleStep(0, bitListing)
	onesPlace = middleStep(2, bitListing)

	firstByte = 16*sixteensPlace + onesPlace

	sixteensPlace2 = middleStep(4, bitListing)
	onesPlace2 = middleStep(6, bitListing)
	secondByte = 16*sixteensPlace2 + onesPlace2


	

	#print(firstByte)
	#print(secondByte)

	return pack('BB', firstByte, secondByte)


def packaging4(bits):

	bitListing = unpack('bbbb', bits)
	#print(bitListing)
	
	sixteensPlace = middleStep(0, bitListing)
	onesPlace = middleStep(2, bitListing)

	firstByte = 16*sixteensPlace + onesPlace

	return pack('B', firstByte)



packaging("\x11\x11\x11\x10\x11\x01\x11\x00")
#print(X)
