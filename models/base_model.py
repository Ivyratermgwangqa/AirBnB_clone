#!/usr/bin/python3
"""Defines the BaseModel class."""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """Represents the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Additional key/value pairs of attributes.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for i, j in kwargs.items():
                if i == "created_at" or i == "updated_at":
                    setattr(self, i, datetime.strptime(j, tform))
                else:
                    setattr(self, i, j)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.today()
            storage.new(self)

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()
        storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.

        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)

    @classmethod
    def from_dict(cls, adict):
        """Create a BaseModel instance from a dictionary representation."""
        instance = cls(**adict)
        return instance
