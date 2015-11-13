# Purpose is to train a model. Output should be a file with features. Then call cmd to output trained model. 
#Then other script will read from inputfile.txt and produce pos_output.txt.

import sys
import os,re
import pdb

outputFile = open(sys.argv[1],"r")#'neroutput'
outputLines = outputFile.readlines()
outputFile.close()

testFile = open(sys.argv[2],'r')#'nertest'
testLines = testFile.readlines()
testFile.close()
outputFile =  open (sys.argv[1],"wb")#'neroutput'

for i in range(0,len(outputLines)):
	line = outputLines[i]
	line = line.strip(' ')
	if line == '\n':
		outputFile.write('\n')	
		continue
	
	output = line.split()[0]
	linet = testLines[i].strip()

	outputFile.write(linet + ' ' + output + '\n')

outputFile.close()
testFile.close()


