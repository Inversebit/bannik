# Copyright (c) 2016 Inversebit
#
# Licensed under The MIT License, please check the LICENSE file
# on the root of the project.
from flask import Blueprint, request, jsonify, make_response

from app.mod_hw import refresh_alerts

from app.mod_access.utils import require_appkey
from app.mod_alerts.models import Alert

mod_alerts = Blueprint('alerts', __name__, url_prefix='/alerts')


@mod_alerts.route('', methods=['GET'])
def list_alerts():
    alert_id = request.args.get('id')
    if alert_id is None:
        response = list_all_alerts()
    else:
        response = Alert.query.filter_by(id=alert_id).first().serialize

    return jsonify(response)


def list_all_alerts():
    alert_list = Alert.query.all()
    return [al.serialize for al in alert_list]


@mod_alerts.route('', methods=['POST'])
@require_appkey
def add_alert():
    try:
        json_alert = request.get_json()
        alert = Alert(json_alert.get('content'),
                      json_alert.get('expiration'),
                      json_alert.get('alert_type'),
                      json_alert.get('alert_priority'))

        alert.add_to_db()
    except Exception as ex:
        return ex

    refresh_alerts()

    return 'Added'


@mod_alerts.route('', methods=['DELETE'])
@require_appkey
def remove_alert():
    alert_id = request.args.get('id')
    if alert_id is not None:
        alert = Alert.query.filter_by(id=alert_id).first()
        if alert is not None:
            alert.remove_from_db()
            refresh_alerts()
            return "Alert " + alert_id + " successfully removed"
        else:
            return make_response("Non-existent alert", 500)
    else:
        return make_response("Must provide an id", 400)
