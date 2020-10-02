from typing import Dict, Optional
from datetime import date

from flask import request  # ,current_app as app
from flask_restful import Resource
from sqlalchemy.orm import load_only
from sqlalchemy.sql import func
from sqlalchemy import desc


from werkzeug.datastructures import ImmutableMultiDict

from BusOnTime import db
from BusOnTime.Trip_Model import Trip_Model, trips_schema, stats_schema1  # , trips_schema2


def get_arguments(request_args: ImmutableMultiDict, *args: str) -> Dict[str, Optional[str]]:
    return {arg: request_args.get(arg) for arg in args}  # TODO Add error checking


def date_cond(requested_date: str) -> bool:
    return Trip_Model.file_date == date.fromisoformat(requested_date)


def oper_cond(requested_oper: str) -> bool:
    return Trip_Model.agency_id == requested_oper


def line_cond(requested_line: str) -> bool:
    return Trip_Model.route_short_name == requested_line


def cluster_cond(requested_cluster: str) -> bool:
    return Trip_Model.cluster_id == requested_cluster


class Test(Resource):

    def get(self):

        performance_measures = db.session.query(Trip_Model.agency_id)\
            .add_columns(func.avg(Trip_Model.departure_delay.in_(range(0, 6))).label("performance"))\
            .group_by(Trip_Model.agency_id).order_by(desc("performance"))#\
            #.all()

        # Parse results and return as json
        output = stats_schema1.dump(performance_measures)
        return {'Trips': output}
        #return {'Trips': [x for x in performance_measures]}
