#!/usr/bin/env python3
""" Module for Basic babel setup
"""


from flask import Flask, render_template
from flask_babel import Babel

app = flask(__name__)


class Config:
    """ Config for babel
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel: Babel = Babel(app)


@app.route('/')
def index() -> str:
    """ Return the index page
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
