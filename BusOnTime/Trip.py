from flask import request  # , current_app as app
from flask_restful import Resource
from datetime import date

from BusOnTime import db
from BusOnTime.Trip_Model import Trip_Model, trips_schema


class Trip(Resource):

    def get(self):

        # trips = Trip.query.filter(route_id == route_id).all() // not working :(

        route_id = request.args['routeID']
        date_str = request.args['date']
        cond1 = Trip_Model.route_id == route_id
        cond2 = Trip_Model.file_date == date.fromisoformat(date_str)
        trips = db.session.query(Trip_Model).filter(cond1, cond2)
        output = trips_schema.dump(trips)
        return {'Trips:': output}



