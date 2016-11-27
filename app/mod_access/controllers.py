# Copyright (c) 2016 Inversebit
#
# Licensed under The MIT License, please check the LICENSE file
# on the root of the project.

from flask import Blueprint

mod_access = Blueprint('access', __name__, url_prefix='/access')

@mod_access.route('/', methods=['GET'])
def list_access_keys():
    return 'access'
