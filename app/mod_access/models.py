# Copyright (c) 2016 Inversebit
#
# Licensed under The MIT License, please check the LICENSE file
# on the root of the project.

from app import db
from app.db_base import Base

import os
import binascii


class AccessKey(Base):

    __tablename__ = 'AccessKeys'

    key = db.Column(db.String(64), nullable=False)
    creator = db.Column(db.String(64), nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False)

    def __init__(self, creator, is_admin):

        if creator is None:
            raise TypeError('Key creator must not be None')

        if is_admin is None:
            is_admin = False

        self.key = str(binascii.hexlify(os.urandom(32)), 'utf-8')
        self.creator = creator
        self.is_admin = is_admin

    def __repr__(self):
        return '<AccessKey\n\tId: {}\n\tKey: {},\n\tCreator:{},\n\tAdmin: {}>'.format(
            super(AccessKey, self).id, self.key, self.creator, self.is_admin)

    @staticmethod
    def is_authorized(app_key):
        res = AccessKey.query.filter_by(key=app_key).first()
        return not (res is None)
