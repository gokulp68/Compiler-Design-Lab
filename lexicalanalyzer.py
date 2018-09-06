import numpy as np
f = open("input.txt", "r")
lines = f.read().splitlines()
keywords = ["for","while","if","else","int","main","void","float","printf","scanf"]
operators = ["+","-","*","/","=","<"]
seperators = [",",";","{","}","(",")"]
numbers = ["1","2","3","4","5","6","7","8","9","0"]
#print lines
prkeywords = []
prseperator = []
pridentifier = []
properator = []
prliteral = []
def iskeyword(buffer):
	if buffer in keywords:
		return True
	else:
		return False
def isseperator(buffer):
	if buffer in seperators:
		return True
	else:
		return False
def isoperator(buffer):
	if buffer in operators:
		return True
	else:
		return False
def exceptions(part):
	#print part
	buffe = ""
	if part == "" or part[0] == "#":
		return
	else:
		for i in range(0,len(part)):
			if part[i].isalnum() or part[i]==".":
				buffe+=part[i]
			else:
				if iskeyword(buffe):
					prkeywords.append(buffe)
				else:
					if buffe != "":
						if buffe.isalpha():
							pridentifier.append(buffe)
						else:
							prliteral.append(buffe)

				
				if isseperator(part[i]):
					prseperator.append(part[i])
				elif isoperator(part[i]):
					if isoperator(part[i+1]):
						properator.append(part[i:i+2])
						i = i + 1
					else:
						properator.append(part[i])
				elif part[i]==('\"'):
					printf = part[i:]
					#print printf
					prliteral.append(printf[:printf[1:].index('\"')+2])
					#print printf[:printf[1:].index('\"')+2]
					i = i + 2 + printf[1:].index('\"')

				exceptions(part[i+1:])
				break

for line in lines:
	linpart = line.split()
	for linepart in linpart:
		if iskeyword(linepart):
			prkeywords.append(linepart)
		elif isseperator(linepart):
			prseperator.append(linepart)
		else:
			exceptions(linepart)





print "keywords are :",
print np.unique(prkeywords)
print "seperators are :",
print np.unique(prseperator)
print "identifiers are :",
print np.unique(pridentifier)
print "operators are :",
print np.unique(properator)
print "literals are :",
print np.unique(prliteral)

f.close()