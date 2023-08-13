#!/usr/bin/env python3
""" A module that defines a subclass Review """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Defines the class Review that inherits from BaseModel """
    place_id = ""
    user_id = ""
    text = ""
