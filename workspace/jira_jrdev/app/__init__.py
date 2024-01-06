from flask import Flask


def create_app():
    app = Flask(__name__)

    # Import the ping blueprint
    from .ping import ping_blueprint
    app.register_blueprint(ping_blueprint)

    return app
