#!/usr/bin/python3
""" Create a unique FileStorage instance for my application. """


from models.engine import file_storage


storage = file_storage.FileStorage()
storage.reload()
