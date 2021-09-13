# -*- coding: utf-8 -*-

from sqlalchemy import Column, Time, Integer, Boolean, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQL statements and expressions API
# cf. http://docs.sqlalchemy.org/en/rel_0_7/core/expression_api.html
from sqlalchemy import and_, extract

import datetime

engine = create_engine('sqlite:///:memory:')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class WakeupTimer(Base):
    __tablename__ = 'WakeupTimer'
    id = Column(Integer, primary_key=True)
    time = Column(Time(), nullable=False,
                  doc='naive time')
    everyday = Column(Boolean(), default=True)

    def __init__(self, time, everyday=True):
        self.time = time
        self.everyday = everyday


Base.metadata.create_all(engine)

timers = [
    WakeupTimer(datetime.time(7, 0)),
    WakeupTimer(datetime.time(7, 10))
]
session.add_all(timers)
session.commit()


# querying
now = datetime.time(7, 0)
timer_from_db = session.query(WakeupTimer).filter(
        and_(now.hour == extract('hour', WakeupTimer.time),
             now.minute == extract('minute', WakeupTimer.time))).first()

assert hasattr(timer_from_db, 'time')
assert timer_from_db.time == now
