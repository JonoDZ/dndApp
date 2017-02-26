import random
import sqlite3

#create the cursor and connection for the data DB
conn = sqlite3.connect('dnd.db')
c = conn.cursor()

#####################
##### VARIABLES #####
#####################

### LISTS ###
#all races exactly as listed in DB. 
#related to DB. dont change
races = [
"human",
"dragonborn",
"dwarf",
"halforc",
"gnome",
"elf",
"halfling",
"tiefling",
"halfelf"
]
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
"temple"
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

#####################
##### FUNCTIONS #####
#####################

def generateRace(requestedRace=0):
	#reset variables
	character = {}
	firstName =[]
	lastName =[]
	#if user has specified a race
	if (requestedRace == 0):
		#get random race/gender
		character['race'] = random.choice(races)
		character['gender'] = random.choice(gender)
		#variables for DB looks ups
		g = character['gender']
		r = character['race']
		#get all race and gender first names from db
		for row in c.execute('SELECT '+g+' FROM '+r+''):
			if row[0] != None:
				firstName.insert(0,row[0])
		#get all race last names from db
		for row in c.execute('SELECT last FROM '+r+''):
			if row[0] != None:
				lastName.insert(0,row[0])
		#a random data from generated lists, apply to character.
		character['firstName'] = random.choice(firstName)
		character['lastName'] = random.choice(lastName)
		character['age'] = random.choice(age)
		return(character)


