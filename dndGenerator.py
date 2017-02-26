import charGen

def genChar(toGen=1):
	charlist =[]
	npcsToGen = 10

	for i in range(0,npcsToGen):
		charlist.insert(0,(charGen.generateRace()))
	return charlist
#(genChar(10))