from sqlalchemy.ext.automap import automap_base

from BusOnTime import ma, db


Base = automap_base()
Base.prepare(db.engine, reflect=True)
Trip_Model = Base.classes.trips

# old init pattern:
# with app.app_context():
#     Base.prepare(db.engine, reflect=True)


class TripSchema(ma.SQLAlchemySchema):  # use SQLAlchemyAutoSchema instead to return all fields
    class Meta:
        model = Trip_Model
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


trips_schema = TripSchema(many=True)
