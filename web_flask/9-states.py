#!/usr/bin/python3
""" Start a Flask web application """
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/states")
def states():
    """
    List states: display a HTML page: (inside the tag BODY)
    Returns:
        html: template that lists all states sort by name A->Z
    """
    states = storage.all("State").values()
    return render_template("7-states_list.html", states=states)


@app.route("/states/<id>", stric_slashes=False)
def state_with_id(num_id):
    """
    Get a state by id
    Returns:
        html: template that lists cities of state sort by name A->Z
    """
    state = None
    for s in storage.all("State").values():
        if s.id == num_id:
            state = s
            break
    return render_template("9-states.html", state=state)


@app.teardown_appcontext
def close_db(err=None):
    """this is the close db"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
