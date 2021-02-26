# A very simple Flask Hello World app for you to get started with...
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask <br /> <b> HOLA!!!! </b>'