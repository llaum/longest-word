from flask import Flask, render_template
from game import Game

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello world!"
