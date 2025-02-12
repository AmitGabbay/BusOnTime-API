import os
import pyodbc
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api
from flask_cors import CORS
from urllib import parse

db = SQLAlchemy()
ma = Marshmallow()
api = Api()


def create_app():
    app = Flask(__name__)

    pyodbc.pooling = False

    conn = os.environ['DATABASE_CONN_STR']
    params = parse.quote_plus(conn)
    conn_str = 'mssql+pyodbc:///?odbc_connect={}'.format(params)
    app.config['SQLALCHEMY_DATABASE_URI'] = conn_str

    engine_options = {'pool_recycle': 1800}
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = engine_options

    #app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data_small.db'

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    CORS(app)

    db.init_app(app)
    ma.init_app(app)

    with app.app_context():  # Necessary for trip model loading via SQLAlchemy
        from BusOnTime.search import Trips, Lines, RoutesMKTs, Directions, Trip2
        from BusOnTime.stats import GeneralStats, StatsByLine, DelayDistribution

    api.add_resource(Trips, '/trips')
    api.add_resource(Trip2, '/trips2')
    api.add_resource(Lines, '/lines')
    api.add_resource(RoutesMKTs, '/mkts')
    api.add_resource(Directions, '/directions')
    api.add_resource(GeneralStats, '/stats/main/')
    api.add_resource(StatsByLine, '/stats/byLine/')
    api.add_resource(DelayDistribution, '/stats/delays/')

    @app.route('/')
    def hello():
        return 'BusOnTime API'

    api.init_app(app)  # This init must be placed after resources additions

    return app
