from struct import *

def middleStep(place, bitList):
	return ((bitList[place+1] % 16) + ((bitList[place+1] - (bitList[place+1] % 16))/16)*2 + (bitList[place] % 16)*4 + ((bitList[place] - (bitList[place] % 16))/16)*8)
def packaging(bits):
	#This function takes a block of 8 bytes for which each hexadecimal character is either 0 or 1
#and, reinterpreting this block of 16 binary numbers as 2 big-endian bytes and returning them
#in such a packed form
	
	bitListing = unpack('bbbbbbbb', bits)
	#print(bitListing)
	
	sixteensPlace = middleStep(0, bitListing)
	onesPlace = middleStep(2, bitListing)

	firstByte = 16 * sixteensPlace + onesPlace

	sixteensPlace2 = middleStep(4, bitListing)
	onesPlace2 = middleStep(6, bitListing)
	secondByte = 16 * sixteensPlace2 + onesPlace2


	

	#print(firstByte)
	#print(secondByte)

	return pack('BB', firstByte, secondByte)


def packaging4(bits):
	#Similar, but packs 4 bytes into 1 byte instead of 8 bytes into 2 bytes

	bitListing = unpack('bbbb', bits)
	#print(bitListing)
	
	sixteensPlace = middleStep(0, bitListing)
	onesPlace = middleStep(2, bitListing)

	firstByte = 16*sixteensPlace + onesPlace

	return pack('B', firstByte)



#packaging(b'\x11\x11\x11\x10\x11\x01\x11\x00')
#print(X)