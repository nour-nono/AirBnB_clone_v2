#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from markupsafe import escape

app = Flask(__name__)

@app.route('/cities_by_states')
def cities_by_states():
	pass
