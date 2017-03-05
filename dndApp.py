from flask import Flask, url_for, request, jsonify
from flask import render_template
import dndGenerator

app = Flask(__name__)

#### variables #####

@app.route('/regenNpcs')
def regenNpcs():
    npcQuant = request.args.get('npcQuant', 0, type=int)
    charList = request.args.get('charList', 0)
    charList = charList.split(",")
    charList.remove("")
    characterList=dndGenerator.genChar(charList, npcQuant)
    return jsonify(render_template('npctable.html', charList=characterList))

@app.route('/regenBuildings')
def regenBuildings():
    a = request.args.get('a',0)
    a = a.split(",")
    a.remove("")
    buildingList=dndGenerator.genBuilding(a)
    return jsonify(render_template('buildingstable.html', buildingList=buildingList))

@app.route('/')
def hello_world():
    characterList=dndGenerator.genChar(0,10)
    buildingList=dndGenerator.genBuilding()
    return render_template('index.html', charList=characterList, buildingList=buildingList)
