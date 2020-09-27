from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api


db = SQLAlchemy()
ma = Marshmallow()
api = Api()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    ma.init_app(app)

    with app.app_context():
        from BusOnTime.Trip import Trip

    api.add_resource(Trip, '/trips')

    @app.route('/')
    def hello_world():
        return 'Hello World!'

    api.init_app(app)  # This init must be placed after resources additions

    return app
