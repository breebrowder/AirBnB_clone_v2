#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, String
from os import getenv
import models
from models.city import City


class State(BaseModel, Base):
    """class for State inherited from BaseModel and Base"""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City",
        cascade="all,delete-orphan",
        backref=backref("state", cascade="all,delete"))
    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """gets Cities instances with state_id"""
            return [v for k, v in models.storage.all(City).items()
                    if v.state_id == self.id]