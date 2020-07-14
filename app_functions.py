## ==> GUI FILE
#from main import *
import sqlite3
from PyPDF2 import PdfFileWriter, PdfFileReader
import os
import shutil

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

class PDFfunctions():

    def moveFiles(self,fromPath,toPath): # Mover arquivos
        if not os.path.exists(toPath):    
            shutil.move(fromPath,toPath)
        if os.path.exists(fromPath):
            os.remove(fromPath)

    def createDirectory(self,path): # Criar diretórios se não existirem
        if not os.path.exists(path):
            os.makedirs(path)

    def merge(self,paths, output):
        pdf_writer = PdfFileWriter()
        #outputDir = os.path.dirname(paths[0])
        #outputFile = os.path.basename(paths[0])
        #output = outputPath = os.path.join(outputDir,outputFile)
        counter = 0
        for path in paths:
            pdf_reader = PdfFileReader(path)
            counter+= 1
            for page in range(pdf_reader.getNumPages()):
                # Add each page to the writer object
                pdf_writer.addPage(pdf_reader.getPage(page))

        # Write out the merged PDF
        PDFfunctions.createDirectory(self,os.path.split(output)[0])
        with open(output, 'wb') as out:
            pdf_writer.write(out)

    def mergeBatch(self,rootDirectory,outputDirectory,suffix):
        counter = 0
        ext = ".pdf"
        listPdfFiles = (os.listdir(rootDirectory))
        for subdir in listPdfFiles:
            counter = 0
            files = []
            path = os.path.join(rootDirectory,subdir)
            for file in os.listdir(path):
                if file.endswith(".pdf"):
                    counter+=1
                    files.append(os.path.join(path,file))
            if counter != 0:
                output = os.path.join(outputDirectory,subdir) + suffix + ext
                PDFfunctions.merge(self,files,output)

PDF = PDFfunctions
#PDF.mergeBatch(PDFfunctions,"E:\\OneDrive\\Documentos\\GitHub\\Ahand\\root","E:\\OneDrive\\Documentos\\GitHub\\Ahand\\output"," - MERGED")
        
    



    
