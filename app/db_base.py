# Copyright (c) 2016 Inversebit
#
# Licensed under The MIT License, please check the LICENSE file
# on the root of the project.

from app import db


class Base(db.Model):

    __abstract__ = True

    id              = db.Column(db.Integer, primary_key=True)
    date_created    = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified   = db.Column(db.DateTime,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
