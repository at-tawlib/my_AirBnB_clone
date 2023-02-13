#!/usr/bin/python3
"""Module for FileStorage class"""
import json
import os
import datetime

class FileStorage:

    """serializes instances to a JSON file and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects
        Return:
            dictionary objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """sets objects
        Args:
            obj : object to set 
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj


    def save(self):
        """serializes __objects to JSON file"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            dict_objs = {}
            for key, value in FileStorage.__objects.items():
                dict_objs[key] = value.to_dict()
            json.dump(dict_objs, file)


    def reload(self):
        """deserializes the JSON file to __objects"""
        from models.base_model import BaseModel
        classes = {
                'BaseModel': BaseModel
                }
        if not os.path.exists(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
            obj_dict = json.load(file)
            final_obj = {key: classes[value["__class__"]](**value) for key, value in obj_dict.items()}
        FileStorage.__objects = final_obj 
