#!/usr/bin/python3
""" Link Basemodel to FileStorage by using storage """

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
