from flask import Flask, url_for, request, jsonify
from flask import render_template
import dndGenerator

app = Flask(__name__)

#### variables #####
requestedNpcs = 10

@app.route('/redo')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    characterList=dndGenerator.genChar(a)
    return jsonify(render_template('npctable.html', charList=characterList))


@app.route('/')
def hello_world():
    characterList=dndGenerator.genChar(10)
    buildingList=dndGenerator.genBuilding()
    return render_template('index.html', charList=characterList, buildingList=buildingList)



