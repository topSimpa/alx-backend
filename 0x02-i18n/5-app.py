#!/usr/bin/env python3
""" Module for Basic babel setup
"""


from flask import (
    Flask,
    g,
    render_template,
    request
)

from flask_babel import Babel

app = Flask(__name__)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> dict:
    """ get the appropriate user by id
    """
    user_id = int(request.args.get('login_as'))
    if users.get(user_id):
        print(users.get(user_id))
        return users.get(user_id)
    return None


@app.before_request
def before_request():
    """ get_user before request is handled
    """
    if get_user:
        g.user = get_user()


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
    user_name = None
    if g.user:
        user_name = g.user.get('name')
    return render_template('5-index.html', username=user_name)


if __name__ == '__main__':
    app.run(debug=True)
