#!/usr/bin/env python3
""" Defines a subclass that inherits from cmd.Cmd """
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


allClasses = [
                "BaseModel", "User", "Place", "State",
                "City", "Amenity", "Review"
            ]


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
            storage.save()  # Why do this have to be here!?

    def do_all(self, cmd):
        """ Prints all string representation of all instances
            based or not on the class name.
            Ex: $ all BaseModel or $ all<F5>
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
        args = cmd.split()

        if len(args) == 0:
            print(f"** class name missing **")
        elif args[0] not in allClasses:
            print(f"** class doesn't exist **")
        elif len(args) == 1:
            print(f"** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key in storage.all():
                if len(args) < 3:
                    print(f"** attribute name missing **")
                elif len(args) < 4:
                    print(f"** value missing **")
                else:
                    obj = storage.all()[key]
                    try:
                        setattr(obj, args[2], eval(args[3]))
                    except NameError:
                        setattr(obj, args[2], args[3])
                    obj.save()
            else:
                print(f"** no instance found **")

    def default(self, cmd):
        """ Handles Unknown Commands
            Ex. <class name>.<method>().
        """
        args = cmd.split(".")

        if args[0] in allClasses:
            if args[1][0:-2] == "all":
                self.do_all(args[0])
            elif args[1][0:-2] == "count":
                count = 0
                for k in storage.all().keys():
                    if k.startswith(args[0]):
                        count += 1
                print(count)
            elif args[1].startswith("show"):
                class_id = eval(args[1].strip("show()"))
                self.do_show(f"{args[0]} {class_id}")
            elif args[1].startswith("destroy"):
                class_id = eval(args[1].strip("destroy()"))
                self.do_destroy(f"{args[0]} {class_id}")
            elif args[1].startswith("update"):
                """check if it starts with update
                    strip off the update
                    eval it and it becomes a tuple
                    index the dictionary part and itrratr
                """
                if args[1].endswith("})"):
                    arg = eval(args[1].strip("update"))
                    idd = arg[0]
                    for k, v in arg[1].items():
                        cmd = f"{args[0]} {idd} {k} {v}"
                        self.do_update(cmd)
                else:
                    test = args[1].strip("update()").split(", ")
                    idd = eval(test[0])
                    attribute = eval(test[1])
                    cmd = f"{args[0]} {idd} {attribute} {test[2]}"
                    self.do_update(cmd)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
