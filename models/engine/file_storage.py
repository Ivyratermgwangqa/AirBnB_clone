#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.review import Review
from models.city import City
import os.path

class FileStorage:
    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        # Import here to avoid circular dependency
        from models import storage
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj
        storage.save()

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as fl:
            json.dump(objdict, fl)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as fl:
                objdict = json.load(fl)
                for key, value in objdict.items():
                    class_name = value["__class__"]
                    del value["__class__"]
                    instance = eval(class_name)(**value)
                    key = "{}.{}".format(class_name, instance.id)
                    self.__objects[key] = instance
        except FileNotFoundError:
            return
