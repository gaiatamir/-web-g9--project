# noinspection PyUnresolvedReferences
from utilities.db.db_manager import dbManager


# New Class for interact with DB
class DBint:
    def __init__(self):
        pass

    # Get - Gallery images src
    def getImges(self):
        query = "Select * From gallery"
        return dbManager.fetch(query)

    @staticmethod
    def getRecommends():
        query = "Select * From recommends where image !=''"
        return dbManager.fetch(query)


# Creates an instance for the interactDB class for export.
DBint = DBint()
