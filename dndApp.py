from flask import Flask, url_for, request, jsonify
from flask import render_template
import dndGenerator



app = Flask(__name__)


@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)


@app.route('/')
def hello_world():
    characterList=dndGenerator.genChar(10)
    buildingList=dndGenerator.genBuilding()
    return render_template('index.html', charList=characterList, buildingList=buildingList)



