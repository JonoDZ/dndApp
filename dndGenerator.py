import charGen
import buildingGen

def genChar(chars=0, toGen=10):
	charlist =[]
	if chars == 0:
		for i in range(0,toGen):
			charlist.insert(0,(charGen.generateRace()))
	elif not chars:
		for i in range(0,toGen):
			charlist.insert(0,(charGen.generateRace()))
	else:	
		for i in range(0,toGen):
			charlist.insert(0,(charGen.generateRace(chars)))
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