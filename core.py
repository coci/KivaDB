import os
import json


class ErrorException(Exception):
    pass


class KivaDB(object):
    """
        create instance :
        >>> my_db = KivaDB("~/Desktop/test.db")
        >>> my_db.set("foo","bar")
        >>> my_db.get("foo") ==> "bar"
    """
    def __init__(self,location):
        """
            os.path.expanduser("~/Desktop/test.db") =return=> /Users/example/Desktop/test.db
        """
        self.location = os.path.expanduser(location)
        self.load()

    def load(self):
        if os.path.exists(self.location):
            self._load() # load data from file
        else:
            self.db = {} # initial empty hash table

    def _load(self):
        self.db = json.load(open(self.location,"r")) # read and load pervious data from file

    def _dump(self):
        """
            write new edited data on file
        """
        try:
            json.dump(self.db,open(self.location,"w+"))
        except ErrorException:
            raise ErrorException("can't write on file .")

    def set(self,key,value):
        try:
            self.db[str(key)] = value
            self._dump() # insert new data on db
        except ErrorException:
            raise ErrorException("can't write on file .")

    def get(self,key):
        try:
            return self.db[str(key)]
        except ErrorException:
            raise ErrorException("invalid key .")
