from typing import Dict, Optional
from datetime import date

from flask import request  # ,current_app as app
from flask_restful import Resource
from sqlalchemy.sql import func
from sqlalchemy import desc


from werkzeug.datastructures import ImmutableMultiDict

from BusOnTime import db
from BusOnTime.Trip_Model import Trip_Model, stats_schema
from BusOnTime.conditions import date_cond, oper_cond, line_cond, cluster_cond


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


class StatsByLine(Resource):

    def get(self):

        params = get_arguments(request.args, "date", "oper", "cluster", "desc", "ignoreRareTrips")

        conditions = []
        filters = [True]  # if nothing to filter by... will use 'True' as filter to return all

        ignore_terms = [None, 'all']

        if params['date'] not in ignore_terms:
            conditions.append(date_cond(params['date']))

        if params['oper'] not in ignore_terms:
            conditions.append(oper_cond(params['oper']))

        if params['cluster'] not in ignore_terms:
            conditions.append(cluster_cond(params['cluster']))

        if params['ignoreRareTrips'] in ['false']:
            conditions.append(Trip_Model.num_trips >= 15)

        if params['desc'] not in ['false']:
            performance_sort_order = desc("performance")
        else:
            performance_sort_order = "performance"

        if conditions:
            filters = conditions

        # Query the DB
        select_cols = [Trip_Model.agency_id, Trip_Model.route_short_name,
                       Trip_Model.route_mkt, Trip_Model.route_long_name]

        performance_measures = db.session.query(*select_cols) \
            .add_columns(func.avg(Trip_Model.departure_delay.in_(range(0, 6))).label("performance")) \
            .filter(*filters) \
            .group_by(Trip_Model.route_mkt)\
            .order_by(performance_sort_order)\
            .limit(50)

        # Parse results and return as json
        output = stats_schema.dump(performance_measures)
        return {'Performance': output}
