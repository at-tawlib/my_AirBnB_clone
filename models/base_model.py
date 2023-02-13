#!/usr/bin/python3
"""Base class"""
import uuid
from datetime import datetime

class BaseModel():
    """Base class for all other classess"""

    def __init__(self, *args, **kwargs):
        """constructor function"""
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    
    def __str__(self):
        """returns human readable format of object"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"


    def save(self):
        """updates updated_at with the current datetime"""
        self.updated_at = datetime.today()

    def to_dict(self):
        """returns  a dictionary containing all keys/values of __dict__ of the instance
        Return:
            dictionary of instance
        """
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
