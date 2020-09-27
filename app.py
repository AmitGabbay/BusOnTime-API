from flask import Flask, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from flask_marshmallow import Marshmallow
from datetime import date

from app_test import app
from data_tools import db, ma
# from Trip import Trip  # init_mapping


# app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
ma.init_app(app)

from Trip import Trip

api = Api(app)
api.add_resource(Trip, '/trips')


@app.route('/')
def hello_world():
    return 'Hello World!'


# @app.before_first_request
# def create_tables():
#     init_mapping()


if __name__ == '__main__':
    # db.init_app(app)
    # ma.init_app(app)
    app.run(debug=True, port=4999)  # Port and debug are set in the run configurations
