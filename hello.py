from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Olá! Bem vindo ao seu Projeto Simple_Python_Flask</p>"
