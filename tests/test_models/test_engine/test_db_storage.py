#!/usr/bin/python3
"""test db"""
import unittest
from models.engine.db_storage import DBStorage
import os


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                 "this test just for db")
class test_dbStorage(unittest.TestCase):
    def test_documentation(self):
        self.assertIsNotNone(DBStorage.__doc__)
