#!/usr/bin/python3
"""
Module that defines the class BaseModel
"""

from datetime import datetime
import uuid
import models

class BaseModel:
    """ This class defines all common attributes/methods for other classes """

    def __init__(self, *args, **kwargs):
        if len(kwargs):
            for k, v in kwargs.items():
                if (k != "__class__"):
                    if (k == "created_at") or (k == "updated_at"):
                        self.__dict__[k] = datetime.fromisoformat(v)
                    setattr(self.__class__, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        dt = self.__dict__.copy()
        dt["__class__"] = self.__class__.__name__
        for k, v in dt.items():
            if (k == "created_at"):
                dt[k] = v.isoformat()
            if (k == "updated_at"):
                dt[k] = v.isoformat()
        return (dt)
