from flask import Flask, url_for
from flask import render_template
import dndGenerator



app = Flask(__name__)

@app.route('/')
def hello_world():
    characterList=(dndGenerator.genChar(10))
    return render_template('index.html', charList=characterList)



