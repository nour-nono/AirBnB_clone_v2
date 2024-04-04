#!/usr/bin/python3
"""db_storage module"""
import os
from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """
    A class to handle database storage operations.
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Initializes the database connection using environment variables.
        """
        user = os.getenv("HBNB_MYSQL_USER")
        password = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db_name = os.getenv("HBNB_MYSQL_DB")
        mode = os.getenv("HBNB_ENV")
        db_url = "mysql+mysqldb://{}:{}@{}/{}".format(
            user, password, host, db_name)
        self.__engine = create_engine(db_url, pool_pre_ping=True)
        if mode == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Retrieves all objects of a given class from the database,
        or all objects if no class is specified.
        """
        all_classes = {'State': State, 'City': City, 'Amenity': Amenity,
                       'Place': Place, 'User': User, 'Review': Review}
        all_obj = []
        new_dict = {}
        if cls is None:
            for value in all_classes.values():
                all_obj.extend(self.__session.query(value).all())
        else:
            all_obj = self.__session.query(cls).all()
        for obj in all_obj:
            new_dict[f"{obj.__class__.__name__}.{obj.id}"] = obj
        return new_dict

    def new(self, obj):
        """
        Adds a new object to the database session.
        """
        if obj is not None:
            self.__session.add(obj)

    def save(self):
        """
        Commits the current database session,
        saving all new and changed objects.
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes an object from the database session.
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        Recreates the database session, useful for test environments.
        """
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()

    def close(self):
        """
        close session.
        """
        self.__session.close()
