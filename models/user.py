#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = "users"

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
        reviews = relationship('Review', back_populates='user',
                               cascade='all, delete-orphan')
        places = relationship('Place',
                              cascade="all, delete, delete-orphan",
                              back_populates='user')
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
