from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    ForeignKey,
    DateTime,
    Boolean,
)

from .meta import Base
from .build import Build
from .build_server import BuildServer

from sqlalchemy.orm import backref, relation


class BuildFlow(Base):
    __tablename__ = 'build_flow'
    id = Column(Integer, primary_key=True)

    build_id = Column(Integer, ForeignKey("build.id"), nullable =False)
    build = relation("Build", backref=backref('build', order_by=id))

    build_server_id = Column(Integer, ForeignKey("build_server.id"), nullable =False)
    server = relation("BuildServer", backref=backref('build_server', order_by=id))

    timestamp = Column(DateTime(timezone=True))
    lb_status = Column(Boolean)
    nginx_status = Column(Boolean)
    git_status = Column(Boolean)
    pre_compile_status = Column(Boolean)
    compile_status = Column(Boolean)
    bounce_status = Column(Boolean)
    verify_status = Column(Boolean)
    compile_jsp_status = Column(Boolean)
    final_status = Column(Boolean)

Index('build_idx', BuildFlow.build_id, unique=True, mysql_length=255)
