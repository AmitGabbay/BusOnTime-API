from flask import request  # , current_app as app
from flask_restful import Resource
from datetime import date
from sqlalchemy.orm import load_only

from BusOnTime import db
from BusOnTime.Trip_Model import Trip_Model, trips_schema  # , trips_schema2


class Trip(Resource):

    def get(self):
        # trips = Trip.query.filter(route_id == route_id).all() // not working :(

        route_id = request.args['routeID']
        date_str = request.args['date']
        cond1 = Trip_Model.route_id == route_id
        cond2 = Trip_Model.file_date == date.fromisoformat(date_str)
        # is the lazy load necessary?
        trips = db.session.query(Trip_Model).filter(cond1, cond2).options(load_only("route_id", "file_date"))
        output = trips_schema.dump(trips)
        return {'Trips': output}


class Lines(Resource):

    def get(self):
        date_str = request.args['date']
        operator = request.args['operator']

        cond1 = Trip_Model.file_date == date.fromisoformat(date_str)
        cond2 = Trip_Model.agency_id == operator
        lines = db.session.query(Trip_Model.route_short_name).filter(cond1, cond2).distinct()
        # output = trips_schema2.dump(lines)
        # return {'Lines': output}
        return {'Lines': [x.route_short_name for x in lines]}


class RoutesMkt(Resource):

    def get(self):
        date_str = request.args['date']
        operator = request.args['operator']
        line_num = request.args['line']

        cond1 = Trip_Model.file_date == date.fromisoformat(date_str)
        cond2 = Trip_Model.agency_id == operator
        cond3 = Trip_Model.route_short_name == line_num
        routes_mkts = db.session.query(Trip_Model.route_mkt).filter(cond1, cond2, cond3).distinct()
        return {'Routes for this line': [x.route_mkt for x in routes_mkts]}
