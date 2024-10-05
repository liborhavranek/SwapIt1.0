"""
Module Name: app.py
Author: Made with love by Libor Raven
Date: 05.10.2024
"""
from flask import Flask
from blueprints.base.base import base_bp


def create_app() -> Flask:
    """Function for create init of app."""
    flask_app = Flask(__name__)

    flask_app.register_blueprint(base_bp)

    return flask_app


if __name__ == '__main__':   # pragma: no cover
    app = create_app()
    app.run()
