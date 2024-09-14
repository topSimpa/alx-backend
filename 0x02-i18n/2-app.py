#!/usr/bin/env python3
""" Module for Basic babel setup
"""


from flask import (
    Flask,
    render_template,
    request
)

from flask_babel import Babel

app = Flask(__name__)


class Config:
    """ Config for babel
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


def get_locale() -> str:
    """ makes the best match amongst language options
    """

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """ Return the index page
    """
    return render_template('2-index.html')


babel = Babel(app, locale_selector=get_locale)

if __name__ == '__main__':
    app.run(debug=True)
