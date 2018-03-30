import scipy, time, sys
from BinaryConverterFunctions import float_dec2bin, float_bin2dec
from packing import packaging, packaging4

print sys.argv
Content = sys.argv[1]
Samples = int(sys.argv[2])
#Bin = open("TSTestReceive", "rb")
check = 0
Pos = 0

while(check == 0):

	Bin = open(Content, "rb")
	Bin.seek(Pos, 0)
	checklist = packaging(Bin.read(8))

	j=0
	if checklist == '\xfe\xdc':
		print("here")
		#time.sleep(2)
		check = 1
		i=0
		List = []
		while(i<Samples):
			
			checklistcheck = Bin.read(8)
			
			
			#Check = open("Check", "ab")
			#Check.write(checklist + "\n")
			#print("writing...")
			#Check.close()

			if len(checklistcheck) < 8:
				print(i)
				i=Samples
				print(checklistcheck)
				
				print("End of file")
			else:
				checklist = packaging(checklistcheck)
			if checklist == '\xfe\xdc':
				#print("Gucci")
				#time.sleep(2)
				#print(j)
				if (j>0):
					Bin.seek(-1*(j+8), 1)
				
					#Check = open("Check", "wb")
					#Check.write(Bin.read(j))
					#print("writing...")
					#Check.close()

					#Bin.seek(-1*(j), 1)
					#print(Bin.tell())
					med = open("Medium", "wb")
					#print(j)
					for n in range(j/4):
						bite = packaging4(Bin.read(4))
						med.write(bite)
					med.close()
					

					point = Bin.tell()
					#print("j = " + str(j))

					with open("Medium", mode='rb') as file:
						#file.seek(point)
    						fileContent = file.read()
						file.close()
					#print(Bin.tell())
					TS = float_bin2dec(fileContent)
					#print(TS)
					List.append(TS)
					#print(List)
					i=i+1
					Bin.seek(8,1)
					j=0
				else:
					print("weird...")

			else:
				#print("Now Here")
				Bin.seek(-7,1)
				j=j+1
			
			

	else:
		Bin.seek(-7,1)
		Bin.close()
		Pos = Pos +1


#print(List)
PrevTime = 0
z=1
#firstone = 1

print(len(List))
for k in range(len(List)):
	Time = List[k]
	if (Time != PrevTime and Time != 0):
		print("Time Stamp: " + str(Time))
		print("Showed up " + str(z))
		z = 1
		PrevTime = Time
#	elif (Time != PrevTime and Time != 0 and firstone == 1):
#		PrevTime = Time
#		z = z+1
#		firstone = 0
	elif (Time != 0):
		z = z+1
	else:
		print("ERROR!")
print("Time Stamp: " + str(Time))
print("Showed up " + str(z))
Bin.close()
