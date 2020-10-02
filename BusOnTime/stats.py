from typing import Dict, Optional
from datetime import date

from flask import request  # ,current_app as app
from flask_restful import Resource
from sqlalchemy.orm import load_only
from sqlalchemy.sql import func
from sqlalchemy import desc


from werkzeug.datastructures import ImmutableMultiDict

from BusOnTime import db
from BusOnTime.Trip_Model import Trip_Model, trips_schema, stats_schema  # , trips_schema2
from BusOnTime.conditions import *


def get_arguments(request_args: ImmutableMultiDict, *args: str) -> Dict[str, Optional[str]]:
    return {arg: request_args.get(arg) for arg in args}  # TODO Add error checking


class GeneralStats(Resource):

    def get(self):

        params = get_arguments(request.args, "date", "by")

        if params['date'] in [None, 'all']:
            date_filter = True  # Ignore filtering by sending 'True' as condition)
        else:
            date_filter = date_cond(params['date'])

        if params['by'] in [None, 'oper']:
            measure_type = Trip_Model.agency_id
        else:
            measure_type = Trip_Model.cluster_id

        performance_measures = db.session.query(measure_type)\
            .add_columns(func.avg(Trip_Model.departure_delay.in_(range(0, 6))).label("performance"))\
            .filter(date_filter)\
            .group_by(measure_type).order_by(desc("performance"))

        # Parse results and return as json
        output = stats_schema.dump(performance_measures)
        return {'Performance': output}


# class GeneralStats(Resource):
#
#     def get(self):
#
#         params = get_arguments(request.args, "date", "by")
#
#         if params['date'] in [None, 'all']:
#             date_filter = True  # Ignore filtering by sending 'True' as condition)
#         else:
#             date_filter = date_cond(params['date'])
#
#         if params['by'] in [None, 'oper']:
#             measure_type = Trip_Model.agency_id
#         else:
#             measure_type = Trip_Model.cluster_id
#
#         performance_measures = db.session.query(measure_type) \
#             .add_columns(func.avg(Trip_Model.departure_delay.in_(range(0, 6))).label("performance")) \
#             .filter(date_filter) \
#             .group_by(measure_type).order_by(desc("performance"))
#
#         # Parse results and return as json
#         output = stats_schema.dump(performance_measures)
#         return {'Trips': output}
