#!/usr/bin/python3
"""Starts a Flask web application."""
from flask import Flask, render_template
from models import storage
from markupsafe import escape

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ Display HTML page: (inside the tag BODY) """
    states = storage.all("State").values()
    return render_template("8-cities_by_states.html",
                           states=states)


@app.teardown_appcontext
def close_db(err=None):
    """this is the close db"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
