#!/usr/bin/env python3
""" A module that creates a sub class User from BaseModel """
from models.base_model import BaseModel


class User(BaseModel):
    """ Defining a class User """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
