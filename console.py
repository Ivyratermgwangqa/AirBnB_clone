#!/usr/bin/python3
"""Command interpreter module."""
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit on end-of-file (EOF)."""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty line."""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel and save it."""
        

    def do_show(self, arg):
        """Show the string representation of an instance."""
        args = arg.split()
        

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id."""
        args = arg.split()
        

    def do_all(self, arg):
        """Print all string representations of all instances."""
        args = arg.split()
        obj_list = []
       

    def do_update(self, arg):
        """Update an instance based on the class name and id."""
        args = arg.split()
       


if __name__ == '__main__':
    HBNBCommand().cmdloop()
