#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
import os
import shlex


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship('City', back_populates='state',
                              cascade='all, delete, delete-orphan')
    else:
        name = ''

        @property
        def cities(self):
            from models import storage
            var = storage.all()
            lista = []
            result = []
            for key in var:
                city = key.replace('.', ' ')
                city = shlex.split(city)
                if (city[0] == 'City'):
                    lista.append(var[key])
            for elem in lista:
                if (elem.state_id == self.id):
                    result.append(elem)
            return result
