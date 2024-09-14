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
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """ makes the best match amongst language options
    """
    locale = request.args.get('locale')
    if locale is not None:
        if locale in app.config['LANGUAGES']:
            return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """ Return the index page
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(debug=True)
