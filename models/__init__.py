#!/usr/bin/python3
"""Initialization module for the models package."""
from models.engine.file_storage import FileStorage

"""A var storage, an interger for fileStorage."""
storage = FileStorage()
storage.reload()
