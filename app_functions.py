## ==> GUI FILE
from main import *
import sqlite3

class DataBase():

    def __init__(self,path,tableName):
        self.dbConnection = sqlite3.connect(path)
        self.cursor = self.dbConnection.cursor()
        self.tableName = tableName

    def commitDB(self):
        self.dbConnection.commit()

    def closeDB(self):
        self.dbConnection.close()
        
    def executeQuery(self,query,data=""):  
        result = self.cursor.execute(query,data)
        return result

    def createDBTable(self):
        query = ''' CREATE TABLE IF NOT EXISTS {} (
                    ID integer, IF text, DO text
                    );  '''.format(self.tableName)
        self.executeQuery(query)
        self.dbConnection.commit()

    def deleteDBtable(self):
        query = ''' DROP TABLE IF EXISTS {} '''.format(self.tableName)
        self.executeQuery(query)
        self.dbConnection.commit()

    def insertRowInDB(self,rowData):
        query = ''' INSERT INTO {} ('ID','IF','DO') VALUES (?,?,?) '''.format(self.tableName)
        self.executeQuery(query,rowData)
        self.dbConnection.commit()