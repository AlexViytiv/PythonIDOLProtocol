"""
	IDOL Protocol
"""

import sys

# Sign values used to detect receiver.
IVASYK_SIGN_VAL = 0
LESYA_SIGN_VAL = "end"

# List of receivers name.
names = ["Ivasyk.txt", "Dmytryk.txt", "Ostap.txt", "Lesya.txt"]

# Function dictToFile() used to write content of dictionary values
# to files with key as name of file.
def dictToFile(Dict):	
	for key in Dict:
		file = open(key, "w")
		# line - represents each packet
		for line in Dict[key]:
			file.write(line+"\n");
		file.close()	

# Function parsePacketReceiver() used to classify received packets.
# Packet represented by lines.
def parsePacketReceiver(lines, receivers):
	# line - represents each packets
	for line in lines:
		# remove newline symbols
		line = line.strip('\n')
		# drop empty packet as redudant
		if(len(line) == 0):
			continue
		
		# begins classification
		# if packet contain even number of symbols - it`s Ivasyk		
		if(len(line)%2 == IVASYK_SIGN_VAL):
			(receivers[names[0]]).append(line)
		# if packet first letter is capitalized and it`s not Ivasyk
		# - it`s Dmytryk
		elif(line[0].isupper()):
			(receivers[names[1]]).append(line)
		# if packet is not for Lesya && not for anyone - it`s Ostap		
		elif(line[-3:] != LESYA_SIGN_VAL):
			(receivers[names[2]]).append(line)
		
		# if packet last letters is LESYA_SIGN_VAL - it`s Lesya
		if(line[-3:] == LESYA_SIGN_VAL):
			(receivers[names[3]]).append(line)	
	
# Function openProtocolStack() used to open file that contain all 
# received packets. If something goes wrong, it caches excepion.
def openProtocolStack(filePath):
	try:
		file = open(filePath, "r")
	except FileNotFoundError:
		print(" [Problem] | File doesn`t exist. Please, check file name.")
		exit(1)	
	except Exception:
		print(""" [Problem] | Unknown type of problem. Please, send this information
				              to idolprotocol_support@gmail.com .""")
		exit(1)	

	lines = file.readlines()
	file.close()
	return lines

# Function main()
def main():
	receivers = {names[0]:[], names[1]:[], names[2]:[], names[3]:[]}	

	try:
		lines = openProtocolStack(sys.argv[1])
	except IndexError:	
		print(" [Problem] | You should enter name of file as argument of program.")
		exit(1)	

	parsePacketReceiver(lines, receivers)
	dictToFile(receivers)

	print(" Sucessfully sorted.")

if __name__ == "__main__":
	main()
