#!/usr/bin/python3
""" Defines the FileStorage class that serializes and deserializes """
import json
from models.base import BaseModel


class FileStorage:
    """ serializes and deserializes an instance to a file and vice versa """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, mode="w", encoding="utf-8") as f:
            obj_ = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(obj_, f)

    def reload(self):
        try:
            with open(self.__file_path, mode="r") as fh:
                load = json.load(fh)
                for v in load.values():
                    self.new(eval(v["__class__"])(**v))
        except FileNotFoundError:
            pass
