#!/usr/bin/python3
"""
    `Base` class Module
"""
import json


class Base:
    """
        Defines Base class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
            Initialization attributes for Base class
            Args:
                id: public instance attribute
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            Returns JSON string representation of list_dictionaries
        """
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
            Writes the JSON string representation of list_objs into file
        """
        obj_arr = []
        if list_objs is not None:
            for obj in list_objs:
                obj_arr.append(cls.to_dictionary(obj))
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(obj_arr))

    @staticmethod
    def from_json_string(json_string):
        """
            Returns the list of the JSON string representation json_string
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
            Returns an instance with attributes already set
        """
        if cls.__name__ == "Square":
            dummy = cls(1)
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
            Returns a list of instances
        """
        filename = cls.__name__ + ".json"
        obj_arr = []
        try:
            with open(filename, "r") as f:
                instances = cls.from_json_string(f.read())
            for i, instance in enumerate(instances):
                obj_arr.append(cls.create(**instances[i]))
        except FileNotFoundError:
            pass
        return obj_arr
