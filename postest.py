# Purpose is to train a model. Output should be a file with features. Then call cmd to output trained model. 
#Then other script will read from inputfile.txt and produce pos_output.txt.

import sys
import os,re
import pdb

testFile = open(sys.argv[1],"r")
testLines = testFile.readlines()

outputFeature =  open ('posoutputfeaturestest',"wb")

arkfile = open ('posdatalist','r')
arklines = arkfile.readlines()
arkfile.close()

dic = {}
for i in range (0,len(arklines)):
	sent = arklines[i]
	sent = sent.split ()
	for j in sent:
		dic[j.split("_")[0]] = j.split("_")[1]

nerlistfile = open ('nerdatalist','r')
nerlistlines = nerlistfile.readlines()
nerlistfile.close()

dicner = {}
for i in range (0,len(nerlistlines)):
	#print nerlistlines[i]
	dicner[nerlistlines[i].split()[1]] = nerlistlines[i].split()[0]


def punct (word):
	if(')' in word):
		return 'true'
	if('(' in word):
		return 'true'
	if('_' in word):
		return 'true'
	if('>' in word):
		return 'true'
	if('=' in word):
		return 'true'
	return 'false'

for i in range(0,len(testLines)):
	line = testLines[i]
	
	if line == '\n':
		outputFeature.write('\n')	
		continue
	
	feature = line.split()[0]
	word = line.split()[0]
	#sentence.append(word)
	prefix3 = 'prefix3'+word[0:3]
	prefix2 = 'prefix2'+word[0:2]
	suffix3 = 'suffix3'+word[-3:]
	suffix2 = 'suffix2'+word[-2:]
	
	prevword = 'prevword_'
	if(i!=0):
		if(testLines[i-1] == '\n'):
			prevword = prevword + ''
		else:
			prevword = prevword + testLines[i-1].split()[0]

	nextword = 'nextword_'
	if(i!=len(testLines)-1):
		if(testLines[i+1] == '\n'):
			nextword = nextword + ''
		else:
			nextword = nextword + testLines[i+1].split()[0]
	
	capital = "CAP_"+ str(word[0].isupper())

	haspunctuation = "Haspunct_" + punct (word)

	hasat = "Has@_" + str('@' in word)
	hashash = "Has#_" + str ('#' in word)
	hascolon = "Has:_" + str(':' in word)
	hasurl = "httpurlpresent_" + str('http' in word)
	hastil = "has~_"+ str("~" in word)
	lengtheq1 = 'lengtheq1_'+str(len(word)==1)


	arknum = ''
	if(dic.has_key(word)):
		arknum = "arknum_" + str( dic[word])
	nernum = ''
	if(dicner.has_key(word)):
		nernum = "nernum_" + str( dicner[word])


	feature = feature + ' '+ prefix3 + ' ' + prefix2 + ' ' +suffix3 + ' ' +suffix2 + ' ' +prevword + ' ' +nextword + ' ' +capital + ' ' +haspunctuation + ' ' +hasat + ' ' + hascolon + ' ' + hashash + ' ' + hastil + ' ' + hasurl + ' ' + lengtheq1 + ' ' + arknum + ' ' + nernum
	
	outputFeature.write(feature + '\n')	

outputFeature.close()


