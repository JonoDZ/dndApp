import random
import sqlite3

#create the cursor and connection for the data DB
conn = sqlite3.connect('dnd.db')
c = conn.cursor()

#age of npc
#related to DB. dont change

buildings=[
'inn',
'alchemist',
'blacksmith',
'jeweler',
'enchanter',
'magicweps'
]

def generateBuilding(buildings=buildings):
	#reset variables
	
	firstNames =[]
	lastNames =[]
	listOfBuildings=[]
	for building in buildings:
		generatedBuilding = {}
		#get random race/gender
		for row in c.execute('SELECT '+building+"1"+' FROM buildings'):
			if row[0] != None:
				firstNames.insert(0,row[0])

		for row in c.execute('SELECT '+building+"2"+' FROM buildings'):
			if row[0] != None:
				lastNames.insert(0,row[0])
		generatedBuilding['type'] = building
		generatedBuilding['name'] = random.choice(firstNames) + " " + random.choice(lastNames)
		
		listOfBuildings.insert(0,generatedBuilding)
	return(listOfBuildings)