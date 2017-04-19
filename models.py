import datetime
import os
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy import (DECIMAL, Boolean, Column, DateTime, Date, ForeignKey, Index,
                        Integer, MetaData, Table, Text, UniqueConstraint,
                        Float, CheckConstraint, event, BigInteger)
from database import Base

class Result(Base):
    __tablename__ = 'results'
    id = Column(Integer, primary_key=True)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    budgets = Column(JSON)
    transactions = Column(JSON)

    def __repr__(self):
        return '<id {}>'.format(self.id)
