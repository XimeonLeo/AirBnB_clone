#!/usr/bin/python3
"""
Module that defines the class BaseModel
"""

from datetime import datetime
import uuid


class BaseModel:
    """ This class defines all common attributes/methods for other classes """

    def __init__(self, *args, **kwargs):
        if (kwargs is not None):
            for k, v in kwargs.items():
                if (k != "__class__"):
                    if (k == "created_at") or (k == "updated_at"):
                        kwargs[k] = datetime.fromisoformat(v)
                    setattr(self.__class__, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dt = self.__dict__
        dt["__class__"] = self.__class__.__name__
        for k, v in dt.items():
            if (k == "created_at"):
                dt[k] = v.isoformat()
            if (k == "updated_at"):
                dt[k] = v.isoformat()
        return (dt)
"""    def to_dict(self):
        dt = datetime.now()
        self.created_at = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.updated_at = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.__dict__ = {
                "__class__": self.__class__.__name__,
                "id": self.id,
                "created_at": self.created_at,
                "updated_at": self.updated_at
                }
        return (self.__dict__)
"""
