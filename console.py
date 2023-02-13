#!/usr/bin/python3
"""Entry point of the command interpreter"""
import cmd

class HBNBCommand(cmd.Cmd):
    """Command processor for the HBNB"""

    prompt = "(hbnb) "
    def do_quit(self, line):
        return True

    def help_quit(self):
        print("Quit command to exit the program\n")

    def help_EOF(self):
        print("end program")

    def do_EOF(self, line):
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
