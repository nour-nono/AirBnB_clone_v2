#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
from models.state import State


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ """
        s = State(name="abc")
        s.save()
        new = self.value(name="abc")
        new.save()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        s = State(name="abc")
        s.save()
        new = self.value(name="abc")
        new.save()
        self.assertEqual(type(new.name), str)
