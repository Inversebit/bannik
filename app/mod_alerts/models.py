# Copyright (c) 2016 Inversebit
#
# Licensed under The MIT License, please check the LICENSE file
# on the root of the project.

from app import db
from app.db_base import Base

import datetime


class Alert(Base):

    __tablename__ = 'Alerts'

    content         = db.Column(db.String(512), nullable=False)
    expiration      = db.Column(db.DateTime, nullable=False)
    alert_type      = db.Column(db.Integer, nullable=False)
    alert_priority  = db.Column(db.Integer, nullable=False)

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
        return '\n<<Alert\n\tId: {}\n\tContent: {}\n\tExpiration: {}\n\tType: {}\n\tPriority:{}\n>>\n'.format(
            self.id, self.content, self.expiration, self.alert_type, self.alert_priority)

    @property
    def serialize(self):
        return{
                'id': self.id,
                'content': self.content,
                'expiration': Alert.dump_datetime(self.expiration),
                'type': self.alert_type,
                'priority': self.alert_priority
        }

    @staticmethod
    def dump_datetime(value):
        if value is None:
            return None
        else:
            return value.strftime('%Y-%m-%dT%H:%M:%S.%fZ')


    def add_to_db(self):
        db.session.add(self)
        db.session.commit()

    def remove_from_db(self):
        db.session.delete(self)
        db.session.commit()
