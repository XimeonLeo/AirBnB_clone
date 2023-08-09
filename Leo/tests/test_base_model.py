#!/usr/bin/env python3
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_instance(self):
        model = BaseModel()
        self.assertIsInstance(model.id, str) 
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
