from BusOnTime.Trip_Model import Trip_Model
from datetime import date


def date_cond(requested_date: str) -> bool:
    return Trip_Model.file_date == date.fromisoformat(requested_date)


def oper_cond(requested_oper: str) -> bool:
    return Trip_Model.agency_id == requested_oper


def line_cond(requested_line: str) -> bool:
    return Trip_Model.route_short_name == requested_line


def mkt_cond(requested_mkt: str) -> bool:
    return Trip_Model.route_mkt == requested_mkt


def direction_cond(requested_direction: str) -> bool:
    return Trip_Model.route_direction == requested_direction


def cluster_cond(requested_cluster: str) -> bool:
    return Trip_Model.cluster_id == requested_cluster