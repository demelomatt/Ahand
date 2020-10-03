# Importar arquivos
from ui_main import Ui_MainWindow
from ui_functions import UIFunctions

# Bibliotecas nativas
import os, shutil, datetime, time, re, unicodedata, csv, codecs, zipfile, json
from io import StringIO

# Bibliotecas externas
from PyPDF2 import PdfFileWriter, PdfFileReader # PDF
from PIL import Image # IMAGE
from pdf2image import convert_from_path # PDF2IMAGE
import pytesseract, winsound

    #pdfminer

from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import *

    #pyside
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class PDFfunctions(QThread):
# Classe para agrupar as funções dos arquivos PDF.

    def __init__(self,parent=None):
        QThread.__init__(self)
        self.ui = Ui_MainWindow()

    sender = None
    
    def __del__(self):
        self.wait()

    def run(self):
        # Executar uma função da classe PDFFunctions

        functionValue = 0

        try:
            if self.sender == 'pushButton_run_ocr':
                inputPdfPaths = UIFunctions.inputPdfPaths_ocr
                lineEdit_outputPath = self.ui.lineEdit_outputPath_ocr.text()

                goForward = self.emptyData(inputPdfPaths,lineEdit_outputPath)
                if goForward:
                    functionValue = PDFfunctions.ocrPDF(self,inputPdfPaths,lineEdit_outputPath,self.ui.lineEdit_filename_ocr.text(),self.ui.lineEdit_intDpi_ocr.text())

            elif self.sender == 'pushButton_run_merge':
                inputPdfPaths = UIFunctions.inputPdfPaths_merge
                lineEdit_outputPath = self.ui.lineEdit_outputPath_merge.text()

                goForward = self.emptyData(inputPdfPaths,lineEdit_outputPath,2)
                if goForward:
                    functionValue = PDFfunctions.merge(self,inputPdfPaths,lineEdit_outputPath,self.ui.lineEdit_filename_merge.text())

            elif self.sender == 'pushButton_run_extract':
                inputPdfPaths = UIFunctions.inputPdfPaths_extract
                lineEdit_outputPath = self.ui.lineEdit_outputPath_extract.text()
                pages = self.ui.lineEdit_intPages_extract.text()

                goForward = self.emptyData(inputPdfPaths,lineEdit_outputPath,pages=pages)
                if goForward:
                    functionValue = PDFfunctions.extractOrSplit(self,inputPdfPaths,pages,lineEdit_outputPath,self.ui.lineEdit_filename_extract.text())

            elif self.sender == 'pushButton_run_zip':
                inputPdfPaths = self.ui.lineEdit_rootDirectory_zip.text()
                lineEdit_outputPath = self.ui.lineEdit_outputPath_zip.text()

                goForward = self.emptyData(inputPdfPaths,lineEdit_outputPath)
                if goForward:
                    functionValue = PDFfunctions.zipCompress(self,inputPdfPaths,lineEdit_outputPath,self.ui.lineEdit_filename_zip.text())
                
            elif self.sender == 'pushButton_run_export':
                inputPdfPaths = UIFunctions.inputPdfPaths_export
                lineEdit_outputPath = self.ui.lineEdit_outputPath_export.text()

                goForward = self.emptyData(inputPdfPaths,lineEdit_outputPath)
                if goForward:
                    functionValue = PDFfunctions.getTableNames(self,inputPdfPaths,lineEdit_outputPath,self.ui.lineEdit_filename_export.text())
            
            else:
                inputPdfPaths = UIFunctions.inputPdfPaths_search
                lineEdit_outputPath = self.ui.lineEdit_outputPath_search.text()

                lineEdit_keywords_search = self.ui.lineEdit_keywords_search.text().lstrip().rstrip()
                lineEdit_moveto_search = self.ui.lineEdit_moveto_search.text().lstrip().rstrip()

                goForward = self.emptyData(inputPdfPaths,lineEdit_outputPath,keywords=lineEdit_keywords_search)
                if goForward:
                    functionValue = PDFfunctions.searchPattern(self,inputPdfPaths,lineEdit_outputPath,self.ui.lineEdit_filename_search.text())
            
        except Exception as e:
            if str(e) == "'NoneType' object has no attribute 'rowCount'":
                self.emit(SIGNAL('dialog(QString)'), "Uma ou mais tabelas não foram encontradas. Verifique a ortografia.")
                
            else:
                self.emit(SIGNAL('dialog(QString)'), str(e))
            feedbackMsg = feedbackMsg = ""
            self.emit(SIGNAL('feedback(QString)'), feedbackMsg)
        
        if functionValue:
            winsound.PlaySound('alert.wav',winsound.SND_FILENAME)
            
        return
    
    def emptyData(self,inputPdfPaths,outputPath,filesNumber = 1,pages=0,keywords=0,moveto=0):
        if outputPath == '':
            self.emit(SIGNAL('dialog(QString)'), "O diretório de saída não foi selecionado.")
            return 0

        if not len(inputPdfPaths):
            
            if self.sender == 'pushButton_run_zip':
                self.emit(SIGNAL('dialog(QString)'), "O diretório raiz não foi selecionado.")
            else:
                self.emit(SIGNAL('dialog(QString)'), "Selecione ao menos {} arquivo(s).".format(filesNumber))
            return 0
        
        if pages == '':
            self.emit(SIGNAL('dialog(QString)'), "Selecione ao menos 1 página.")
            return 0
        
        if keywords == '':
            self.emit(SIGNAL('dialog(QString)'), "Nenhum dado foi passado para pesquisar dentro do arquivo.")
            return 0

        if moveto == '':
            self.emit(SIGNAL('dialog(QString)'), "Nenhuma pasta foi indicada para exportar.")
            return 0

        return 1
        
    def buttonSelectCsvFiles(self):
        UIFunctions.csvPaths = QFileDialog.getOpenFileNames(self, 'Selecionar arquivo csv', QtCore.QDir.currentPath(), 'csv files (*.csv)',options=QFileDialog.DontUseNativeDialog)[0]
        PDFfunctions.importFromCSV(self)

    def moveFiles(self,fromPath,toPath): 
    # Mover arquivos. Informar caminho de origem e caminho de destino.
        if not os.path.exists(toPath):    
            shutil.move(fromPath,toPath)
        if os.path.exists(fromPath):
            os.remove(fromPath)

    def createDirectory(self,path): 
    # Criar diretório informado caso ele não exista.
        if not os.path.exists(path):
            os.makedirs(path)

    def getTableNames(self,pdfPaths,outputDir,filename):
        start_time = time.time()
        feedbackMsg = "Processando..."
        self.emit(SIGNAL('feedback(QString)'), feedbackMsg)
        
        # Para cada arquivo
        for path in pdfPaths:
            

            # Abrir arquivo
            with open (path, 'rb') as document:
                output = outputDir + "\\" + filename + ".csv"
                #Create resource manager
                rsrcmgr = PDFResourceManager()
                # Set parameters for analysis.
                laparams = LAParams(line_overlap=0.5, char_margin=2.0, line_margin=0.5,
                word_margin=0.1, boxes_flow=0.5, detect_vertical=False,
                all_texts=False)
                # Create a PDF page aggregator object.
                device = PDFPageAggregator(rsrcmgr, laparams=laparams)
                interpreter = PDFPageInterpreter(rsrcmgr, device)

                # Para cada página

                for page in PDFPage.get_pages(document):
                    
                    dic = {}

                    # Verificar nome a ser pesquisado
                    for i in range(self.ui.tableWidget_2.columnCount()):
                        counterFound = 0
                        key = self.ui.tableWidget_2.item(0,i).text()
                        index = 0
                        text = key
                        if re.findall(":",key):
                            textSplit = key.split(":")
                            text = textSplit[0]
                            index = int(textSplit[1])

                        interpreter.process_page(page)
                        # receive the LTPage object for the page.
                        layout = device.get_result()

                        # Para cada elemento do PDF
                        for obj in layout:
                            # Se contém texto
                            if isinstance(obj, LTTextBoxHorizontal):
                                getText = obj.get_text()
                                textRe, getTextRe =  PDFfunctions.regex(self,text,getText,True,False,False)

                                # Pesquisa palavra dentro do texto e verifica a ordem
                                if re.findall(textRe,getTextRe,flags=re.IGNORECASE):
                                    ignoreChars = [":","-","="]
                                    if index:
                                        counterFound+= 1
                                    if not index or (index and counterFound == index) :

                                        result = re.search(textRe + '(.+?)\n',str(getTextRe),flags=re.IGNORECASE)
                                        result = str(result.group(1))
                                        result = result.lstrip()
                                        for c in ignoreChars:
                                            if result.startswith(c):
                                                result = result.replace(c,"")
                                        result = result.lstrip()
                                        result = result.rstrip()
                                        dic[key] = result
                                        break

                    # Exporta para csv
                    
                    PDFfunctions.exportToCSV(self,output,dic)
                    print(dic)
        feedbackMsg = feedbackMsg = "Processo concluído em %.2f segundos." % (time.time() - start_time)
        self.emit(SIGNAL('feedback(QString)'), feedbackMsg)
        return 1
            
    def exportToCSV(self,csvPath,dic):
        header = True
        if not os.path.isfile(csvPath):
            header = False
        
        with open(csvPath, 'a+',newline='\n') as f:
            
            writer = csv.DictWriter(f, dic.keys())
            if not header:
                writer.writeheader()
            writer.writerow(dic)
            f.close()

    def regex(self,string,keyword,IsAscii,ignoreSpaces,ignorePunctuation):
        # Remover caracteres especiais e espaços do texto.
        # string recebe o texto.
        # ascii recebe boolean indicando se caracteres especiais devem ser ignorados na pesquisa.
        # ignoreSpaces recebe boolean indicando se espaços devem ser ignorados na pesquisa.
        # ignorePunctuation recebe boolean indicando se pontuação devem ser ignorados na pesquisa.

        if IsAscii:
            string = unicodedata.normalize('NFD', string)
            string = string.encode('ascii', 'ignore')
            string = string.decode("utf-8")
            keyword = unicodedata.normalize('NFD', keyword)
            keyword = keyword.encode('ascii', 'ignore')
            keyword = keyword.decode("utf-8")

        if ignoreSpaces:
            string = re.sub('[ ]+', '', string)
            string = string.replace('\n','')
            string = string.replace('\t','')
            keyword = re.sub('[ ]+', '', keyword)
            keyword = keyword.replace('\n','')
            keyword = keyword.replace('\t','')
            
        if ignorePunctuation:
            string = re.sub(r"[.,;/!?:-]+", '', string)
            keyword = re.sub(r"[.,;/!?:-]+", '', keyword)

        return string, keyword


        

