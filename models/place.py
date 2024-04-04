#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship

place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column(
        'place_id',
        String(60),
        ForeignKey('places.id'),
        nullable=False,
        primary_key=True
    ),
    Column(
        'amenity_id',
        String(60),
        ForeignKey('amenities.id'),
        nullable=False,
        primary_key=True
    )
)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False,
                                 back_populates="place_amenities")
        reviews = relationship('Review', back_populates='place',
                               cascade='all, delete-orphan')
        user = relationship('User', back_populates='places')
        cities = relationship('City', back_populates='places')

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """getter funtion to get reviews of certain place"""
            from models import storage
            reviews_dict = storage.all('Review')
            place_reviews = []
            for value in reviews_dict.values():
                if value.place_id == self.id:
                    place_reviews.append(value)
            return place_reviews

        @property
        def amenities(self):
            """getter funtion to get reviews of certain place"""
            from models import storage
            all_amenities = []
            stored = storage.all(Amenity).values()
            for amenity in stored:
                if amenity.id in self.amenity_ids:
                    all_amenities.append(amenity)
            return all_amenities

        @amenities.setter
        def amenities(self, obj):
            """getter funtion to get reviews of certain place"""
            if isinstance(obj, Amenity) and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
