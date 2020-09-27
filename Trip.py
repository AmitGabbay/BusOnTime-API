from flask import request#, current_app as app
from flask_restful import Resource
from sqlalchemy.ext.automap import automap_base
from datetime import date

from data_tools import ma, db



# def init_mapping():
#     Base = automap_base()
#     Base.prepare(db.engine, reflect=True)
#     global Trip_model
#     Trip_model = Base.classes.trips


from app_test import app

Base = automap_base()
with app.app_context():
    Base.prepare(db.engine, reflect=True)
Trip_model = Base.classes.trips


class TripSchema(ma.SQLAlchemySchema):  # use SQLAlchemyAutoSchema to return all fields
    class Meta:
        model = Trip_model
        load_instance = True

    service_id = ma.auto_field()
    # agency_id = ma.auto_field()
    route_id = ma.auto_field()
    # route_short_name = ma.auto_field()
    planned_start_date = ma.auto_field()
    planned_start_time = ma.auto_field()
    bus_id = ma.auto_field()
    # predicted_end_date = ma.auto_field()
    # predicted_end_time = ma.auto_field()
    # agency_name = ma.auto_field()
    route_long_name = ma.auto_field()
    route_type = ma.auto_field()  # ?
    route_mkt = ma.auto_field()  # ?
    # route_direction = ma.auto_field()
    route_alternative = ma.auto_field()
    num_trips = ma.auto_field()
    start_stop_id = ma.auto_field()
    start_stop_name = ma.auto_field()
    start_stop_city = ma.auto_field()
    # end_stop_city = ma.auto_field()
    num_stops = ma.auto_field()
    line_type_desc = ma.auto_field()  # ?
    # cluster_id = ma.auto_field()
    cluster_name = ma.auto_field()
    cluster_sub_desc = ma.auto_field()
    departed = ma.auto_field()
    departure_delay = ma.auto_field()
    notes = ma.auto_field()
    file_date = ma.auto_field()
    # full_srv_id = ma.auto_field()


class Trip(Resource):

    def get(self):
        # item = next(filter(lambda i: i['name'] == name, items), None)
        # return {'item:': item}, 200 if item else 404
        # trips = Trip.query.filter(route_id == route_id).all() // not working :(

        route_id = request.args['routeID']
        date_str = request.args['date']
        cond1 = Trip_model.route_id == route_id
        cond2 = Trip_model.file_date == date.fromisoformat(date_str)
        trips = db.session.query(Trip_model).filter(cond1, cond2)
        output = trips_schema.dump(trips)
        return {'Trips:': output}


trips_schema = TripSchema(many=True)
