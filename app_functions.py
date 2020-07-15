## ==> GUI FILE
#from main import *

# Bibliotecas nativas
import sqlite3, os, shutil
# Bibliotecas externas
from PyPDF2 import PdfFileWriter, PdfFileReader
from PIL import Image
from pdf2image import convert_from_path 
import pytesseract

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
        counterFiles = 0
        for path in paths:
            pdf_reader = PdfFileReader(path)
            counterFiles+= 1
            for page in range(pdf_reader.getNumPages()):
                # Add each page to the writer object
                pdf_writer.addPage(pdf_reader.getPage(page))
        # Write out the merged PDF
        PDFfunctions.createDirectory(self,os.path.split(output)[0])
        with open(output, 'wb') as out:
            pdf_writer.write(out)

    def mergeBatch(self,rootDirectory,outputDirectory,suffix):
        counterFiles = 0
        ext = ".pdf"
        listPdfFiles = (os.listdir(rootDirectory))
        for subdir in listPdfFiles:
            counterFiles = 0
            files = []
            path = os.path.join(rootDirectory,subdir)
            for file in os.listdir(path):
                if file.endswith(ext):
                    counterFiles+=1
                    files.append(os.path.join(path,file))
            if counterFiles != 0:
                output = os.path.join(outputDirectory,subdir) + suffix + ext
                PDFfunctions.merge(self,files,output)

    def ocrPDF(self,paths,output,suffix):
        print("Carregando...")
        ext = ".pdf"
        counterFiles = 0
        pytesseract.pytesseract.tesseract_cmd = "tesseract\\tesseract"
        for path in paths:
            counterPages = 1
            splitext = os.path.splitext(path)[0]
            basename = os.path.basename(splitext)
            finalName = output + "\\" + basename + suffix
            pages = convert_from_path(path,150,poppler_path="poppler\\bin")
            counterFiles+=1
            for page in pages:
                print("Convertendo página {}/{} do arquivo {}/{}.".format(counterPages,len(pages),counterFiles,len(paths)))
                if counterPages == 1:
                    fileName = finalName
                else:
                    fileName = output + "\\." + basename + "-page" +str(counterPages)
                page.save(fileName + '.jpg') 
                pdfOcr = pytesseract.image_to_pdf_or_hocr(fileName + '.jpg', lang = "por")
                with open(fileName + ext,"w+b") as f:
                    f.write(pdfOcr)
                os.remove(fileName + ".jpg")
                if counterPages !=1:
                    PDFfunctions.merge(self,[finalName + ext, fileName + ext],finalName + ext)
                    os.remove(fileName + ext)
                counterPages += 1