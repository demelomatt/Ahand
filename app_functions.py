## ==> GUI FILE
#from main import *

# Bibliotecas nativas
import sqlite3, os, shutil
# Bibliotecas externas
from PyPDF2 import PdfFileWriter, PdfFileReader
from PIL import Image
from pdf2image import convert_from_path 
import pytesseract

from io import StringIO
import re
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

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

    def moveFiles(fromPath,toPath): # Mover arquivos
        if not os.path.exists(toPath):    
            shutil.move(fromPath,toPath)
        if os.path.exists(fromPath):
            os.remove(fromPath)

    def createDirectory(path): # Criar diretórios se não existirem
        if not os.path.exists(path):
            os.makedirs(path)

    def merge(paths, outputFile):
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
        PDFfunctions.createDirectory(os.path.split(outputFile)[0])
        with open(outputFile, 'wb') as out:
            pdf_writer.write(out)
            out.close()

    def mergeBatch(rootDirectory,outputDirectory,suffix):
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
                outputDirectory = os.path.join(outputDirectory,subdir) + suffix + ext
                PDFfunctions.merge(files,outputDirectory)


    def ocrPDF(paths,outputDirectory,suffix,dpi=200):
        print("Carregando...")
        counterFiles = 0
        ext = ".pdf"
        pytesseract.pytesseract.tesseract_cmd = "tesseract\\tesseract"
        for path in paths:
            counterPages = 1
            splitext = os.path.splitext(path)[0]
            basename = os.path.basename(splitext)
            finalName = outputDirectory + "\\" + basename + suffix
            pages = convert_from_path(path,dpi,poppler_path="poppler\\bin")
            counterFiles+=1
            for page in pages:
                print("Convertendo página {}/{} do arquivo {}/{}.".format(counterPages,len(pages),counterFiles,len(paths)))
                if counterPages == 1:
                    fileName = finalName
                else:
                    fileName = outputDirectory + "\\." + basename + "-page" +str(counterPages)
                pdfName = fileName + ext
                imgName = fileName + '.jpg'
                page.save(imgName,'JPEG') 
                pdfOcr = pytesseract.image_to_pdf_or_hocr(imgName, lang = "por")
                with open(pdfName,"w+b") as f:
                    f.write(pdfOcr)
                    f.close()
                os.remove(imgName)
                if counterPages !=1:
                    PDFfunctions.merge([finalName + ext, fileName + ext],finalName + ext)
                    os.remove(pdfName)
                counterPages += 1

    def regex(string,ascii=False,ignoreSpaces=False):
        pass

    def searchPattern(paths,outputDirectory,moveFullFile=False,folderNotFound=True):
        keywords = ["Campinas","Ribeirão Preto","São José do Rio Preto"]
        output_string = None
        for path in paths:
            with open(path, 'rb') as in_file:
                parser = PDFParser(in_file)
                doc = PDFDocument(parser)
                rsrcmgr = PDFResourceManager()
                device = None
                interpreter = None
                for page in PDFPage.create_pages(doc):
                    output_string = StringIO()
                    device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
                    interpreter = PDFPageInterpreter(rsrcmgr, device)
                    interpreter.process_page(page)
                    text = output_string.getvalue()
                    for keyword in keywords:
                        if re.search(keyword,text,re.IGNORECASE):
                            print("Palavra {} encontrada.".format(keyword))
                        else:
                            print("Palavra {} não encontrada.".format(keyword))
                    output_string.close()
                    device.close()
                in_file.close()