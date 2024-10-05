from flask import Flask


def create_app():
    """Function for create init of app."""
    flask_app = Flask(__name__)

    return flask_app


if __name__ == '__main__':
    app = create_app()
    app.run()
