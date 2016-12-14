# Copyright (c) 2016 Inversebit
#
# Licensed under The MIT License, please check the LICENSE file
# on the root of the project.

from functools import wraps
from flask import request, make_response

from app.mod_access.models import AccessKey

QUERYSTRING_KEY_VAR = 'api_key'


# The actual decorator function
def require_appkey(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        if request.headers.get(QUERYSTRING_KEY_VAR):
            if AccessKey.is_authorized(request.headers.get(QUERYSTRING_KEY_VAR)):
                return view_function(*args, **kwargs)
            else:
                return make_response("API key not authorized", 401)
        else:
            return make_response("Must provide an API key", 401)
    return decorated_function
