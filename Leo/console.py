#!/usr/bin/env python3
""" Defines a subclass that inherits from cmd.Cmd """
import cmd
from models.base_model import BaseModel
from models import storage


allClasses = ["BaseModel"]


class HBNBCommand(cmd.Cmd):
    """ The entry point of the command interpreter """
    prompt = "(hbnb) "

    def do_quit(self, cmd):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, cmd):
        """An EOF signal that quits the program
        """
        return True

    def emptyline(self):
        pass

    def do_create(self, cmd):
        """Creates a new instance of BaseModel, saves it
            (to the JSON file) and prints the id..
            Ex: $ create BaseModel
        """
        args = cmd.split()

        if len(args) == 0:
            print(f"** class name missing **")
        elif args[0] not in allClasses:
            print(f"** class doesn't exist **")
        else:
            MyModel = eval(args[0])()
            MyModel.save()
            print(MyModel.id)

    def do_show(self, cmd):
        """Prints the string representation of an instance
            based on the class name and id.
            Ex: $ show BaseModel 1234-1234-1234.
        """
        args = cmd.split()

        if len(args) == 0:
            print(f"** class name missing **")
        elif args[0] not in allClasses:
            print(f"** class doesn't exist **")
        elif len(args) == 1:
            print(f"** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key not in storage.all():
                print(f"** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, cmd):
        """Deletes an instance based on the class name and id
            (save the change into the JSON file).
            Ex: $ destroy BaseModel 1234-1234-1234.
        """
        args = cmd.split()

        if len(args) == 0:
            print(f"** class name missing **")
        elif args[0] not in allClasses:
            print(f"** class doesn't exist **")
        elif len(args) == 1:
            print(f"** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key not in storage.all():
                print(f"** no instance found **")
            else:
                del(storage.all()[key])

    def do_all(self, cmd):
        """ Prints all string representation of all instances
            based or not on the class name.
            Ex: $ all BaseModel or $ all
        """
        args = cmd.split()

        if len(args) == 0:
            print([str(v) for v in storage.all().values()])
        elif args[0] not in allClasses:
            print(f"** class doesn't exist **")
        else:
            lst = []
            for k, v in storage.all().items():
                if k.startswith(args[0]):
                    lst.append(str(v))
            print(lst)
        # print([str(v) for k, v in storage.all().items()
        # if k.startswith(args[0])])

    def do_update(self, cmd):
        """ Updates an instance based on the class name and id
        by adding or updating attribute
        (save the change into the JSON file).

        Ex: $ update BaseModel 1234-1234-1234 email
            "aibnb@mail.com".
        """




if __name__ == '__main__':
    HBNBCommand().cmdloop()
