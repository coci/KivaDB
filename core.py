import os
import json

class ErrorException(Exception):
    pass


class KivaDB(object):
    """
        create instance :
        my_db = KivaDB("~/Desktop/test.db")
    """
    def __init__(self,location):
        self.location = os.path.expanduser(location)
        self.load()

    def load(self):
        if os.path.exists(self.location):
            self._load()
        else:
            self.db = {}

    def _load(self):
        self.db = json.load(open(self.location,"r"))

    def _dump(self):
        try:
            json.dump(self.db,open(self.location,"w+"))
        except ErrorException:
            raise ErrorException("can't write on file .")

    def set(self,key,value):
        try:
            self.db[str(key)] = value
            self._dump()
        except ErrorException:
            raise ErrorException("can't write on file .")

    def get(self,key):
        try:
            return self.db[str(key)]
        except ErrorException:
            raise ErrorException("invalid key .")
