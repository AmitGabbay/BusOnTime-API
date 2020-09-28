from flask import request  # , current_app as app
from flask_restful import Resource
from sqlalchemy.orm import load_only

# noinspection PyUnresolvedReferences
from datetime import date

from BusOnTime import db
from BusOnTime.Trip_Model import Trip_Model, trips_schema  # , trips_schema2


routeID_cond = "Trip_Model.route_id == route_id"
date_cond = "Trip_Model.file_date == date.fromisoformat(date_str)"
oper_cond = "Trip_Model.agency_id == operator"
line_cond = "Trip_Model.route_short_name == line_num"
mkt_cond = "Trip_Model.route_mkt == mkt"


def get_arguments(request_args, *args):

    arguments = [request_args['operator'], request_args['date']]

    if "line" in args:
        line = request_args['line']
        arguments.append(line)

    if "mkt" in args:
        mkt = request_args.get('mkt')
        arguments.append(mkt)

    if "direction" in args:
        direction = request_args.get('direction')
        arguments.append(direction)

    return arguments


class Trip(Resource):

    def get(self):

        # noinspection PyUnusedLocal
        route_id, date_str = request.args.values()

        '''
        # code for unordered query string treatment
        route_id = request.args['routeID']
        date_str = request.args['date']
        '''
        # trips = Trip.query.filter(route_id == route_id).all() // not working :(

        trips = db.session.query(Trip_Model)\
            .filter(eval(routeID_cond), eval(date_cond))\
            .options(load_only("route_id", "file_date"))  # is the lazy load necessary?
        output = trips_schema.dump(trips)
        return {'Trips': output}


class Lines(Resource):

    def get(self):
        # noinspection PyUnusedLocal
        operator, date_str = request.args.values()

        '''
        # code for unordered query string treatment
        operator = request.args['operator']
        date_str = request.args['date']
        '''

        lines = db.session.query(Trip_Model.route_short_name)\
            .filter(eval(date_cond), eval(oper_cond)).distinct()

        return {'Lines': [x.route_short_name for x in lines]}


class RoutesMkt(Resource):

    def get(self):
        # noinspection PyUnusedLocal
        operator, date_str, line_num = request.args.values()

        '''
        # code for unordered query string treatment
        operator = request.args['operator']
        date_str = request.args['date']
        line_num = request.args['line']
        '''

        routes_mkts = db.session.query(Trip_Model.route_mkt)\
            .filter(eval(date_cond), eval(oper_cond), eval(line_cond)).distinct()

        return {'Routes for this line': [x.route_mkt for x in routes_mkts]}


class Directions(Resource):

    def get(self):

        operator, date_str, line_num, mkt = get_arguments(request.args, "line", "mkt")

        '''
        # code for unordered query string treatment
        operator = request.args['operator']
        date_str = request.args['date']
        line_num = request.args['line']
        mkt = request.args['mkt']
        '''

        conditions = [eval(date_cond), eval(oper_cond), eval(line_cond)]

        if mkt:
            conditions.append(eval(mkt_cond))

        directions = db.session.query(Trip_Model.route_direction).filter(*conditions).distinct()

        return {'Routes for this line': [x.route_direction for x in directions]}
