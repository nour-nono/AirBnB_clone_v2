#!/usr/bin/python3
"""this is flask app"""
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/states")
def states():
    states_s = storage.all('States').values()
    states_s = sorted(states_s, key=lambda s: s.name)
    return render_template('9-states.html', states=states_s)


@app.route("/states/<id>", stric_slashes=False)
def state_with_id(num_id):
    states_s = storage.all('States').values()
    filtered_states = [state for state in states_s if state.id == num_id]
    cities = storage.all('City').values()
    filtered_cities = [city for city in cities if city.state_id == num_id]
    filtered_cities = sorted(filtered_cities, key=lambda s: s.name)
    return render_template('9-states.html', states=filtered_states,
                           num_id=num_id, cities=filtered_cities)


app.run(host="0.0.0.0", port=5000)
