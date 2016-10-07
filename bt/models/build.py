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
from .build_site import BuildSite

from sqlalchemy.orm import backref, relation

class Build(Base):
    __tablename__ = 'build'
    id = Column(Integer, primary_key=True)

    site_id = Column(Integer, ForeignKey("build_site.id"), nullable =False)
    build_site = relation("BuildSite", backref=backref('build_site', order_by =id))

    build_time = Column(DateTime(timezone=True))
    scheduled_time = Column(DateTime(timezone=True))
    qa_approved = Column(Boolean)
    vetoed_by = Column(Text)
    sprint_link = Column(Text)
    auto_start = Column(Boolean, default=False)

