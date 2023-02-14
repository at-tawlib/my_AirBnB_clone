#!/usr/bin/python3
"""Entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City 
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
import re


class HBNBCommand(cmd.Cmd):
    """Command processor for the HBNB"""

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """end the program"""
        print()
        return True

    def emptyline(self):
        """Does nothing when Enter is hit"""
        pass

    def precmd(self, line):
        """Intercepts commands to test for Class.all()"""
        # use RE to check if line is in the format 'String.all()'
        match = re.search(r'^\w+[.]\w+\(\)$', line)
        if not match:
            return line
        
        # split the line to return formated command
        split = line.split(".")
        command = f"all {split[0]}"
        return command


    def do_create(self, line):
        """creates a new instance of base model, saves it and prints the id"""
        class_dict = {
                "BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Place": Place,
                "Review": Review
                }

        if line == "" or line is None:
            print("** class name missing **")
        else:
            if line in class_dict:
                obj = class_dict[line]()
            else:
                print("** class doesn't exist **")
                return

            obj.save()
            print(obj.id)

    def do_show(self, line):
        """Prints the string representation of an instance based on the class name and id"""
        class_dict = {
                "BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Place": Place,
                "Review": Review
                }

        args = line.split(' ')
        if line == "" or line is None:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            base = args[0]
            obj_id = args[1]
            data = storage.all()
            key = "{}.{}".format(base, obj_id)

            if base in class_dict:
                if key in data:
                    print(data[key])
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")

    
    def do_destroy(self, line):
        """Deletes an instance based on the class name and id (save the change into the JSON file)."""
        class_list = ["BaseModel", "User", "City", "State", "Amenity", "Review", "Place"]
        commands = line.split(" ")
        if line == "" or line is None:
            print("** class name missing **")
        elif len(commands) < 2:
            print("** instance id missing **")
        elif commands[0] not in class_list:
            print("** class doesn't exist **")
        else:
            data = storage.all()
            key = "{}.{}".format(commands[0], commands[1])
            if key not in data:
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()


    def do_all(self, line):
        """Prints all string representation of all instances based or not on the class name"""
        class_dict = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
            }

        if line == "" or line is None:
            data_list = [str(value) for key, value in storage.all().items()]
            print(data_list)
        elif line not in class_dict:
            print("** class doesn't exist **")
        else:
            data = storage.all()
            data_list = []
            obj_class = class_dict[line]
            for key, value in data.items():
                if type(value) == obj_class:
                    data_list.append(str(value))
            print(data_list)

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)"""

        class_dict = {
                "BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Place": Place,
                "Review": Review
            }

        ex = line.split(" ")
        if line == "" or line is None:
            print("** class name missing **")
        else:
            if ex[0] not in class_dict:
                print("** class doesn't exist **")
            else:
                if len(ex) == 1:
                    print("** instance id missing **")
                else:
                    key = "{}.{}".format(ex[0], ex[1])
                    data = storage.all()
                    if key not in data:
                        print("** no instance found **")
                    else:
                        if len(ex) == 2:
                            print("** attribute name missing **")
                        elif len(ex) == 3:
                            print("** value missing **")
                        else:
                            # get the data
                            obj = data[key]
                            obj_dict = obj.to_dict()

                            # cast value to string, int or float
                            try:
                                if not re.search('^".*"$', ex[3]):
                                    if '.' in ex[3]:
                                        value = float(ex[3])
                                    else:
                                        value = int(ex[3])
                                else:
                                    value = ex[3].replace('"', '')

                                    obj_dict[ex[2]] = value
                                    obj_obj = class_dict[ex[0]](**obj_dict)

                                    obj_obj.save()
                                    storage.all()[key] = obj_obj
                                    storage.save()
                            except ValueError:
                                print("Data not Updated")
    
    def do_count(self, line):
        """Retrieves the number of instances of a class"""
        class_dict = {
                "BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Place": Place,
                "Review": Review
                }

        if line == "" or line is None:
            print(len(storage.all().items()))
        elif line in class_dict:
            obj_class = class_dict[line]
            count_items = []
            for key, value in storage.all().items():
                if type(value) == obj_class:
                    count_items.append(storage.all()[key])
            print(len(count_items))
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
