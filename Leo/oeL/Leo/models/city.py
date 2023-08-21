#!/usr/bin/env python3
""" A module that defines a subclass City """
from models.base_model import BaseModel


class City(BaseModel):
    """ Defines the class City that inherits from BaseModel """
    state_id = ""
    name = ""
