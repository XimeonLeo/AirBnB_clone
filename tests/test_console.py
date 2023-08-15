#!/usr/bin/python3
""" Test Module for the console """

import sys
import unittest
from unittest.mock import patch
from console import HBNBCommand
from io import StringIO


class TestConsole(unittest.TestCase):
    def test_show(self):
        h = ("Prints the string representation of an instance\n      based on"
             "the class name and id.\n  Ex: $ show BaseModel 1234-1234-1234.")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(h, output.getvalue().strip())

    def test_prompt_string(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_line(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
