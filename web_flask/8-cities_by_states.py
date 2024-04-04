#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from markupsafe import escape

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Display HTML page: (inside the tag BODY) """
    states = storage.all("State").values()
    states = sorted(states, key=lambda v: v.name)
    return render_template("7-states_list.html", states=states)


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    """ Display HTML page: (inside the tag BODY) """
    cities = storage.all("City").values()
    cities = sorted(cities, key=lambda v: v.name)
    return render_template("8-cities_by_states.html"
                           , states=states, cities=cities)


@app.teardown_appcontext
def close_db(err=None):
    """this is the close db"""
    storage.close()
