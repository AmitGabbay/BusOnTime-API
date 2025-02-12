from typing import Dict, Optional
from datetime import date

from flask import request  # ,current_app as app
from flask_restful import Resource
from sqlalchemy.orm import load_only
from werkzeug.datastructures import ImmutableMultiDict

from BusOnTime import db
from BusOnTime.trip_model import Trip_Model, trips_schema
from BusOnTime.conditions import date_cond, oper_cond, mkt_cond, direction_cond, line_cond


def get_arguments(request_args: ImmutableMultiDict, *args: str) -> Dict[str, Optional[str]]:

    error_cond = ('operator' not in request_args)\
                 or ('date' not in request_args)\
                 or ('line' in args and 'line' not in request_args)

    if error_cond:
        raise KeyError("Missing required query string params")

    params = {arg: request_args.get(arg) for arg in args}
    return params


class Trips(Resource):

    def get(self):

        # Get params and conditions to filter the DB with:
        params = get_arguments(request.args, "operator", "date", "line", "mkt", "direction")

        conditions = [oper_cond(params['operator']), date_cond(params['date']), line_cond(params['line'])]

        if params['mkt']:
            conditions.append(mkt_cond(params['mkt']))

        direction_ignore_terms = [None, 'all']
        if params['direction'] not in direction_ignore_terms:
            conditions.append(direction_cond(params['direction']))

        # Query the DB
        cols_to_load = ["route_id", "file_date", "route_short_name", "route_mkt",
                        "route_direction", "planned_start_time"]

        trips = db.session.query(Trip_Model).filter(*conditions) \
            .order_by(Trip_Model.planned_start_time) #\
            #.options(load_only(*cols_to_load))  # is the lazy load necessary?

        # Parse results and return as json
        output = trips_schema.dump(trips)
        return {'Trips': output}


class Lines(Resource):

    def get(self):

        # Get params and conditions to filter the DB with:
        params = get_arguments(request.args, "operator", "date")
        conditions = [oper_cond(params['operator']), date_cond(params['date'])]

        # Query the DB and return the results as json
        lines = db.session.query(Trip_Model.route_short_name).filter(*conditions).distinct()
        lines_list = [x.route_short_name for x in lines]
        return {'Lines': sorted(lines_list)}


class RoutesMKTs(Resource):

    def get(self):
        # Get params and conditions to filter the DB with:
        params = get_arguments(request.args, "operator", "date", "line")
        conditions = [oper_cond(params['operator']), date_cond(params['date']), line_cond(params['line'])]

        # Query the DB and return the results as json
        routes_mkts = db.session.query(Trip_Model.route_mkt).filter(*conditions).distinct()
        return {'MKTs': [x.route_mkt for x in routes_mkts]}


class Directions(Resource):

    def get(self):
        # Get params and conditions to filter the DB with:
        params = get_arguments(request.args, "operator", "date", "line", "mkt")
        conditions = [oper_cond(params['operator']), date_cond(params['date']), line_cond(params['line'])]

        if params['mkt']:
            conditions.append(mkt_cond(params['mkt']))

        # Query the DB and return the results as json
        directions = db.session.query(Trip_Model.route_direction).filter(*conditions).distinct()
        return {'Directions': [x.route_direction for x in directions]}


# Old endpoint for testing
class Trip2(Resource):

    def get(self):

        route_id, date_str = request.args.values()

        '''
        # code for unordered query string treatment
        route_id = request.args['routeID']
        date_str = request.args['date']
        '''
        # trips = Trip.query.filter(route_id == route_id).all() // not working :(

        cond1 = Trip_Model.route_id == route_id
        cond2 = Trip_Model.file_date == date.fromisoformat(date_str)

        trips = db.session.query(Trip_Model).filter(cond1, cond2)\
            .options(load_only("route_id", "file_date"))  # is the lazy load necessary?
        output = trips_schema.dump(trips)
        return {'Trips': output}
