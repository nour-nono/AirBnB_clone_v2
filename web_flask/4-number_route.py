#!/usr/bin/python3
"""ths is the first flask app"""
from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """this is the index page"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """this is the hbnb page"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """this is the c page"""
    return f"C {text.replace('_', ' ')}"


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """this is the python page"""
    return f"Python {escape(text).replace('_', ' ')}"


@app.route('/number/<int:n>', strict_slashes=False)
def number_page(n):
    """this is the number page"""
    return f"{escape(n)} is a number"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
