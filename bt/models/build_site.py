from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
)

from .meta import Base


class BuildSite(Base):
    __tablename__ = 'build_site'
    id = Column(Integer, primary_key=True)
    site_name = Column(Text)

