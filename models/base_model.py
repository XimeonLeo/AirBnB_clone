#!/usr/bin/env python3
""" Defines the BaseModel """
import uuid
from datetime import datetime
import models


class BaseModel():
    """ Defines all attribute/methods for other classes """
    def __init__(self, *args, **kwargs):
        if len(kwargs):
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.fromisoformat(value)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ Prints out the classname, id and dict of the class
        [<class name>] (<self.id>) <self.__dict__>
        """
        className = self.__class__.__name__
        instanceId = self.id
        instanceDict = self.__dict__
        return f"[{className}] ({instanceId}) {instanceDict}"

    def save(self):
        """ updates attribute <updated_at> with cuerent DT """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all
            keys/values of __dict__ """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict
