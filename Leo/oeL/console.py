#!/usr/bin/env python3
""" Defines a subclass that inherits from cmd.Cmd """
import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
