import charGen
import buildingGen
def genChar(toGen=1):
	charlist =[]
	npcsToGen = 10

	for i in range(0,npcsToGen):
		charlist.insert(0,(charGen.generateRace()))
	return charlist

def genBuilding():
	buildingList =[]
	buildingList = buildingGen.generateBuilding()
	return buildingList