import random
import sqlite3

#create the cursor and connection for the data DB
conn = sqlite3.connect('dnd.db')
c = conn.cursor()

#
#VARIABLES
#

#possible builds in the town. 
#non-db related
buildings =[
"Inn"
"general Store"
"Alchemy"
"blacksmith"
"jeweler"
"enchanter"
"magic weapons"
"holysite"
"animal keeper"
]
#possible jobs in the town
#non-db related
jobs = [
"innkeep"
"Alchemist"
"blacksmith"
"jeweler"
"enchanter"
"Magic Weapons"
"General Store"
"Guard Captain"
"Holy person"
"town master"
"animal keeper"
"random1"
"random2"
"random3"
"random4"
"random5"
]
#possible genders
#related to DB. dont change
gender=[
'male',
'female'
]
#age of npc
#non-db related
age = [
'young',
'middle aged',
'old',
'very old',
'is he dead?'
]

#get all items from alist in DB
def getItemsFromDb(item, table, connCursor=c):
	returnList = []
	for row in connCursor.execute('SELECT '+item+' FROM '+table+''):
			if row[0] != None:
				returnList.insert(0,row[0])
	return returnList
def generateRace(requestedRace=0):
	#reset variables
	character = {}
	firstName =[]
	lastName =[]
	personality=[]
	charRace =[]
	#if user has specified a race
	if (requestedRace == 0):
		character['race'] = random.choice(getItemsFromDb('race', 'race'))
	else:
		character['race'] = random.choice(requestedRace)

	#build character details
	character['gender'] = random.choice(gender)
	character['lastName'] = random.choice(getItemsFromDb('last', character['race']))
	character['firstName'] = random.choice(getItemsFromDb(character['gender'],character['race']))
	character['personality1'] = random.choice(getItemsFromDb('personality1', 'commonTraits'))
	character['personality2'] = random.choice(getItemsFromDb('personality2', 'commonTraits'))
	character['age'] = random.choice(age)
	#get all personality 1 types
	#get all personality 2 tyoes
	#a random data from generated lists, apply to character.

	return(character)


