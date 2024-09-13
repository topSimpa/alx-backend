#!/usr/bin/env/python3
""" Module for Basic Flask app
"""

from flask import Flask


app = Flask(__name__)

@app.route('/")
def index():
    """ root page of web application
    """
    return render_template("templates/0-index.html")

