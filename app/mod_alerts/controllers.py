# Copyright (c) 2016 Inversebit
#
# Licensed under The MIT License, please check the LICENSE file
# on the root of the project.

from flask import Blueprint

mod_alerts = Blueprint('alerts', __name__, url_prefix='/alerts')

@mod_alerts.route('/', methods=['GET'])
def list_alerts():
    return 'alerts'
