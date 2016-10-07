from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    ForeignKey,
    Boolean,
)

from .meta import Base
from .build_site import BuildSite

from sqlalchemy.orm import backref, relation

class BuildServer(Base):
    __tablename__ = 'build_server'
    id = Column(Integer, primary_key=True)

    site_id = Column(Integer, ForeignKey("build_site.id"), nullable =False)
    build_site = relation("BuildSite", backref=backref('site', order_by=id))

    server_name = Column(Text)
    instance_user = Column(Text)
    batch = Column(Integer)
    start_app = Column(Boolean)
    property_file = Column(Text)

