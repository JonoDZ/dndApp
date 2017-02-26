import charGen
import buildingGen

def genChar(toGen=10):
	charlist =[]

	for i in range(0,toGen):
		charlist.insert(0,(charGen.generateRace()))
	return charlist

def genBuilding(buildings=0):
	buildingList =[]
	if buildings == 0:
		buildingList = buildingGen.generateBuilding()
	elif not buildings:
		buildingList = buildingGen.generateBuilding()
	else:
		buildingList = buildingGen.generateBuilding(buildings)
	return buildingList