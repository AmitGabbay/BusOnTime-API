from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api
from flask_cors import CORS


db = SQLAlchemy()
ma = Marshmallow()
api = Api()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    CORS(app)

    db.init_app(app)
    ma.init_app(app)

    with app.app_context():  # Necessary for trip model loading via SQLAlchemy
        from BusOnTime.endpoints import Trip, Lines, RoutesMKTs, Directions

    api.add_resource(Trip, '/trips')
    api.add_resource(Lines, '/lines')
    api.add_resource(RoutesMKTs, '/mkts')
    api.add_resource(Directions, '/directions')

    @app.route('/')
    def hello_world():
        return 'Hello World!'

    api.init_app(app)  # This init must be placed after resources additions

    return app
