# Copyright (c) 2016 Inversebit
#
# Licensed under The MIT License, please check the LICENSE file
# on the root of the project.

from functools import wraps
from flask import request, abort

from app.mod_access.models import AccessKey

QUERYSTRING_KEY_VAR = 'key'


# The actual decorator function
def require_appkey(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        if request.args.get(QUERYSTRING_KEY_VAR):
            if AccessKey.is_authorized(request.args.get(QUERYSTRING_KEY_VAR)):
                return view_function(*args, **kwargs)
        else:
            abort(401)
    return decorated_function
