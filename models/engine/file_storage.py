#!/usr/bin/env python3
""" A module that defines a class FileStorage """
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage():
    """ Serialize instance of JSON file and deserialize
        JSON file to an instance """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dict __objects """
        return self.__objects

    def new(self, obj):
        """ sets the key and value for the dict __objects
             key:
                <obj class name>.id
             value:
                obj
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """ serialize dict(__objects) and store
            in __file"""
        with open(self.__file_path, "w", encoding="utf-8") as j_file:
            str_dict = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(str_dict, j_file)

    def reload(self):
        """ Deserializes the JSON file to __objects
            provided that <__file_path> exists"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as j_file:
                p_file = json.load(j_file)
                for v in p_file.values():
                    self.new(eval(v["__class__"])(**v))
        except FileNotFoundError:
            pass
