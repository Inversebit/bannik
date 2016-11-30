# Copyright (c) 2016 Inversebit
#
# Licensed under The MIT License, please check the LICENSE file
# on the root of the project.
from flask import Blueprint, request, abort

from app.mod_access.utils import require_appkey
from app.mod_alerts.models import Alert
from app import db

mod_alerts = Blueprint('alerts', __name__, url_prefix='/alerts')


@mod_alerts.route('', methods=['GET'])
def list_alerts():
    return 'alerts'


@mod_alerts.route('', methods=['POST'])
@require_appkey
def add_alert():
    try:
        json_alert = request.get_json()
        alert = Alert(json_alert.get('content'),
                      json_alert.get('expiration'),
                      json_alert.get('alert_type'),
                      json_alert.get('alert_priority'))

        db.session.add(alert)
        db.session.commit()
    except Exception as ex:
        return ex

    return 'Added'
