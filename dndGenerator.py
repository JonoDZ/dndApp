import charGen
import buildingGen

def genChar(toGen=10):
	charlist =[]

	for i in range(0,toGen):
		charlist.insert(0,(charGen.generateRace()))
	return charlist

def genBuilding():
	buildingList =[]
	buildingList = buildingGen.generateBuilding()
	return buildingList