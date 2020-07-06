## ==> GUI FILE
from main import *
import sqlite3

class AppFunctions(MainWindow):

    def initDBConnection(self):
        self.dbConnection = sqlite3.connect("database.db")
        self.cursor = self.dbConnection.cursor()

    def commitDB(self):
        self.dbConnection.commit()

    def closeDB(self):
        self.dbConnection.close()
        
    def executeQuery(self,query,data=""):  
        result = self.cursor.execute(query,data)
        return result

    def createDBTable(self):
        query = ''' CREATE TABLE IF NOT EXISTS "keywords" (
                    ID integer, IF text, DO text
                    );  '''
        AppFunctions.executeQuery(self,query)
        self.dbConnection.commit()

    def deleteDBtable(self):
        query = ''' DROP TABLE IF EXISTS "keywords" '''
        AppFunctions.executeQuery(self,query)
        self.dbConnection.commit()

    def insertRowInDB(self,rowData):
        query = ''' INSERT INTO keywords ('ID','IF','DO') VALUES (?,?,?) '''
        AppFunctions.executeQuery(self,query,rowData)
        self.dbConnection.commit()

