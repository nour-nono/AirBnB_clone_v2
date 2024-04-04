#!/usr/bin/python3
"""ths is the first flask app"""
from flask import Flask, render_template
from models import storage
from markupsafe import escape


app = Flask(__name__, instance_relative_config=True, static_folder='static')
app.jinja_env.line_statement_prefix = '#'


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
def number_no_page(n):
    """this is the number page"""
    return f"{escape(n)} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_page(n):
    """this is the number page"""
    return render_template('5-number.html', n=escape(n))


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    return render_template('6-number_odd_or_even.html', n=int(escape(n)))


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Display HTML page: (inside the tag BODY) """
    states = storage.all("State").values()
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def close_db():
    """this is the close db"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
