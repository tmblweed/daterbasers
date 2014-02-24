from __future__ import absolute_import

from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, Unicode

from playtime.models import Base


class ItemType(Base):
    ''' Names of types of items, like books, shoes etc. '''

    __tablename__ = 'item_types'

    __auditing_enabled__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Unicode, unique=True)
