"""
	IDOL Protocol classification util.

	Require : python3
	Syntax of run command : 
		python3 <name_of_program> <name_of_packets_stack>	
"""

import sys

# Receivers
IVASYK  = "Ivasyk.txt"
DMYTRYK = "Dmytryk.txt"
OSTAP   = "Ostap.txt"
LESYA   = "Lesya.txt"
# Sign values used to detect receiver.
IVASYK_SIGN_VAL = 0
LESYA_SIGN_VAL = "end"

# Function dictToFile() used to write content of dictionary values
# to files with key as name of file.
def dictToFile(Dict):	
	for key in Dict:
		file = open(key+".txt", "w")
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
			(receivers[IVASYK]).append(line)
		# if packet first letter is capitalized and it`s not Ivasyk
		# - it`s Dmytryk
		elif(line[0].isupper()):
			(receivers[DMYTRYK]).append(line)
		# if packet is not for Lesya && not for anyone - it`s Ostap		
		elif(line[-3:] != LESYA_SIGN_VAL):
			(receivers[OSTAP]).append(line)
		
		# if packet last letters is LESYA_SIGN_VAL - it`s Lesya
		if(line[-len(LESYA_SIGN_VAL):] == LESYA_SIGN_VAL):
			(receivers[LESYA]).append(line)	
	
# Function openPacketsStack() used to open file that contain all 
# received packets. If something goes wrong, it print message to inform
# user about possible problem.
def openPacketsStack(filePath):
	try:
		# attemp to open stack of IDOL packets
		file = open(filePath, "r")
	except FileNotFoundError:
		print(" [Problem] | File doesn`t exist. Please, check file name.")
		exit(1)	
	except Exception:
		print(""" [Problem] | Unknown type of problem. Please, send this information
				              to idolprotocol_support@gmail.com .""")
		exit(1)	

	# temporary save all packets in list. 
	# TIP : it would be better to directly return file.readlines(),
	#       but we need to close file =(
	lines = file.readlines()
	file.close()
	return lines

# Function main() realize calls of all functions.
def main():
	# dictionary of possible receivers
	receivers = {IVASYK:[], DMYTRYK:[], OSTAP:[], LESYA:[]}	

	# check availability of first argument & call openPacketsStack()
	try: 
		lines = openPacketsStack(sys.argv[1])
	except IndexError:	
		print(" [Problem] | You should enter name of file as argument of program.")
		exit(1)	

	# call parsing packets
	parsePacketReceiver(lines, receivers)
	# saves data to files	
	dictToFile(receivers)

	# unnecessary information. Just to see some result.
	print(" Sucessfully sorted.")

if __name__ == "__main__":
	main()
