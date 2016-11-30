# Copyright (c) 2016 Inversebit
#
# Licensed under The MIT License, please check the LICENSE file
# on the root of the project.

from app import db
from app.db_base import Base

import datetime

class Alert(Base):

    __tablename__ = 'Alerts'

    content     = db.Column(db.String(512), nullable=False)
    expiration  = db.Column(db.DateTime, nullable=False)
    alert_type        = db.Column(db.Integer, nullable=False)
    alert_priority    = db.Column(db.Integer, nullable=False)

    def __init__(self, content, expiration=None, alert_type=None, alert_priority=None):

        if content is None:
            raise TypeError('Alert content must not be None')

        if expiration is None:
            expiration = datetime.date.today() + datetime.timedelta(hours=18)

        if alert_type is None:
            alert_type = 0

        if alert_priority is None:
            alert_priority = 1

        self.content = content
        self.expiration = datetime.datetime.strptime(expiration, '%Y-%m-%dT%H:%M:%S.%fZ')
        self.alert_type = alert_type
        self.alert_priority = alert_priority

    def __repr__(self):
        return '<Alert\n\tId: {}\n\tContent: {}\n\tExpiration: {}\n\tType: {}\n\tPriority:{}>'.format(
            super(Alert, self).id, self.content, self.expiration, self.alert_type, self.alert_priority)
