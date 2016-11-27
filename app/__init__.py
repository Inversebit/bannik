# Copyright (c) 2016 Inversebit
#
# Licensed under The MIT License, please check the LICENSE file
# on the root of the project.

# Import flask and template operators
from flask import Flask, abort

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    abort(404)

# Import a module / component using its blueprint handler variable (mod_auth)
from app.mod_alerts.controllers import mod_alerts
from app.mod_access.controllers import mod_access

# Register blueprint(s)
app.register_blueprint(mod_alerts)
app.register_blueprint(mod_access)

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()
