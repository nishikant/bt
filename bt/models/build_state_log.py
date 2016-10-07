from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    ForeignKey,
)

from .meta import Base
from .build_flow import BuildFlow

from sqlalchemy.orm import backref, relation

class BuildStateLog(Base):
    __tablename__ = 'build_state_log'
    id = Column(Integer, primary_key=True)
    build_flow_id = Column(Integer, ForeignKey("build_flow.id"), nullable =False)
    build_flow = relation("BuildFlow", backref=backref('build_flow', order_by=id))


    build_state_log = Column(Text)

