# Importar arquivos
from ui_main import Ui_MainWindow
from ui_functions import UIFunctions

# Bibliotecas nativas
import os, shutil, datetime, time, re, unicodedata, csv, codecs, zipfile
from io import StringIO

# Bibliotecas externas
from PyPDF2 import PdfFileWriter, PdfFileReader # PDF
from PIL import Image # IMAGE
from pdf2image import convert_from_path # PDF2IMAGE
import pytesseract, winsound

    #pdfminer
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from pdfminer.high_level import extract_pages

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
                
            else:
                inputPdfPaths = UIFunctions.inputPdfPaths_search
                lineEdit_outputPath = self.ui.lineEdit_outputPath_search.text()

                lineEdit_keywords_search = self.ui.lineEdit_keywords_search.text().lstrip().rstrip()
                lineEdit_moveto_search = self.ui.lineEdit_moveto_search.text().lstrip().rstrip()

                goForward = self.emptyData(inputPdfPaths,lineEdit_outputPath,keywords=lineEdit_keywords_search,moveto=lineEdit_moveto_search)
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

    def rename(self,arguments,outputDirectory,basename='',pages=0,ext='.pdf',keywords='',group='',rowIDs=[]):
    # Renomear arquivos PDF. arguments deve receber algum dos parâmetros em dic ou então uma string.
    # outputDirectory recebe o diretório de saída do arquivo.
    # basename recebe o nome do arquivo sem a extensão e diretório.
    # page recebe o(s) número da(s) página(s) que devem conter no nome do arquivo.
    # ext recebe a extensão do arquivo. O padrão é ".pdf".
    # keywords e group são parâmetros definidos somente para a função searchPattern.

        name = []
        delimiter = "_"
        if type(pages) == int:
            pages = (str(pages + 1))
        
        elif len(pages) > 1:
            pages = ",".join(pages)

        else:
            pages = str(pages[0])
        

        # Verificar se foi informada somente uma página ou uma lista de páginas. 
        # Caso seja lista, é retornado o primeiro e o último índice.

        # Parâmetros de data.
        dt = datetime.datetime.today()
        year = str(dt.year)
        month = str("{:02d}".format(dt.month))
        day = str("{:02d}".format(dt.day))
        hour = str("{:02d}".format(dt.hour))
        minutes = str("{:02d}".format(dt.minute))
        seconds = str("{:02d}".format(dt.second))
        time = delimiter.join([hour,minutes,seconds])

        # Atribuição de chaves-valor.
        dic = {"#year":year,"#month":month,"#day":day,"#time":time,"#pages":pages,"#origin":basename}

        arguments = arguments.split(",") # Transformar argumentos em lista

        for argument in arguments:
            # Adiciona argumentos ao nome.
            noSpaceArgument = re.sub('[ ]+', '', argument)
            try:
                name.append(dic[re.sub('[ ]+', '', noSpaceArgument)]) # Remover espaços e procurar palavra no dicionário
            except:
                try:
                    # Verificar se é uma tabela
                    queryList = noSpaceArgument.split(":")
                    tableName = queryList[0]
                    columnID = int(queryList[1]) - 1
                    tableWidgetObject = "tableWidget " + tableName
                    tableWidgt = self.ui.tabWidget.findChild(QTableWidget, tableWidgetObject)

                    for ID in rowIDs:
                        queryrowIDList = ID.split(":")
                        tablerowIDName = queryrowIDList[0]
                        if tablerowIDName == tableName:
                            rowID = int(queryrowIDList[1])
                            break

                    item = tableWidgt.item(rowID,columnID).text()
                    item = PDFfunctions.regex(self,item,item,False,False,True)[0]
                    name.append(item)
                except:
                    # Adicionar string ao nome
                    if not re.findall(r":", argument):
                        name.append(argument)
                
        # Se o nome for vazio, recebe a tag basename
        if name == [] or name[0] == '':
            name[0] = basename

        name = delimiter.join(name) # Junta o delimitador "_" ao nome.
        finalName = outputDirectory + "/" + name + ext 
        # Retorna o nome final do arquivo.
        return finalName

    def extractOrSplit(self,paths,pages,outputDirectory,name):
        if self.ui.checkBox_split.isChecked():
            self.split(paths,pages,outputDirectory,name)
            return 1

        else:
            self.extract(paths,pages,outputDirectory,name)
            return 1
            
    def extract(self,paths,pages,outputDirectory,name):
    # Extrair páginas indicadas de PDF.
    # paths recebe os caminhos dos arquivos a trabalhar.
    # pages recebe as páginas a serem exportadas ou "allpages" para extrair todas as páginas.
    # outputDirectory recebe o diretório de saída do arquivo.
    # name são os parâmetros da função rename ou então uma string. 
        start_time = time.time()
        feedbackMsg = feedbackMsg = "Extraindo páginas..."
        self.emit(SIGNAL('feedback(QString)'), feedbackMsg)

        try:
            pages = pages.split(",")
        except:
            pass

        if name == "":
            name = "#origin,#pages"

        # Para cada arquivo.
        for path in paths:

            splitext = os.path.splitext(path)[0]
            basename = os.path.basename(splitext)

            # Abrir arquivo.
            with open(r"{}".format(path), 'rb') as infile:
                pdf_reader = PdfFileReader(infile,strict = False)
                pdf_writer = PdfFileWriter()
                totalPages = pdf_reader.getNumPages()

                if not self.ui.comboBox_extractPages.currentIndex():
                
                #Para cada página do arquivo.
                    for page in pages:
                        try:
                            page = int(page)
                            page -= 1
                            # Exportar página.
                            pdf_writer.addPage(pdf_reader.getPage(page))

                        except:
                            pageList = page.split("-")
                            firstPage = int(pageList[0]) - 1
                            lastPage = int(pageList[1])
                            for number in range(firstPage,lastPage):
                                pdf_writer.addPage(pdf_reader.getPage(number))

                    if name:
                        outputFile = PDFfunctions.rename(self,name,outputDirectory,basename,pages)
                    else:
                        outputFile = outputDirectory
                else:
                    page = int(pages[0])
                    pdf_writer = PdfFileWriter()
                    pageNumbers = []
                    for number in range(0,totalPages,page):
                        pdf_writer.addPage(pdf_reader.getPage(number))
                        pageNumbers.append(str(number + 1))
                    if name:
                        outputFile = PDFfunctions.rename(self,name,outputDirectory,basename,pageNumbers)
                    else:
                        outputFile = outputDirectory
                
                #PDFfunctions.createDirectory(self,outputDirectory)
            
                with open(r"{}".format(outputFile), 'wb') as outfile:
                    pdf_writer.write(outfile)
                    outfile.close()

        feedbackMsg = feedbackMsg = "Páginas extraídas em %.2f segundos." % (time.time() - start_time)
        self.emit(SIGNAL('feedback(QString)'), feedbackMsg)
        return 1

    def split(self,paths,pages,outputDirectory,name):
        start_time = time.time()
        feedbackMsg = feedbackMsg = "Divindo arquivo..."
        self.emit(SIGNAL('feedback(QString)'), feedbackMsg)

        pages = pages.split(",")

        if name == "":
            name = "#origin,#pages"

        # Para cada arquivo.
        for path in paths:
            splitext = os.path.splitext(path)[0]
            basename = os.path.basename(splitext)

            # Abrir arquivo.
            with open(r"{}".format(path), 'rb') as infile:
                pdf_reader = PdfFileReader(infile,strict = False)
                pdf_writer = PdfFileWriter()
                totalPages = pdf_reader.getNumPages()

                if not self.ui.comboBox_extractPages.currentIndex():
                    for page in pages:
                        try:
                            page = int(page)
                            page -= 1
                            # Exportar página.
                            pdf_reader = PdfFileReader(infile,strict = False)
                            pdf_writer = PdfFileWriter()
                            pdf_writer.addPage(pdf_reader.getPage(page))
                            if name:
                                outputFile = PDFfunctions.rename(self,name,outputDirectory,basename,page)
                            else:
                                outputFile = outputDirectory
                            with open(r"{}".format(outputFile), 'wb') as outfile:
                                pdf_writer.write(outfile)
                                outfile.close()

                        except Exception as e:
                            with open(r"{}".format(path), 'rb') as infile:
                                pdf_reader = PdfFileReader(infile,strict = False)
                                pdf_writer = PdfFileWriter()
                                totalPages = pdf_reader.getNumPages()
                            
                                print(e)
                                pageList = page.split("-")
                                firstPage = int(pageList[0]) - 1
                                lastPage = int(pageList[1])
                                
                                pdf_writer = PdfFileWriter()
                                for number in range(firstPage,lastPage):
                                    pdf_writer.addPage(pdf_reader.getPage(number))

                                if name:
                                    outputFile = PDFfunctions.rename(self,name,outputDirectory,basename,[page])
                                else:
                                    outputFile = outputDirectory
                                with open(r"{}".format(outputFile), 'wb') as outfile:
                                    pdf_writer.write(outfile)
                                    outfile.close()
                
                else:
                    with open(r"{}".format(path), 'rb') as infile:
                        pdf_reader = PdfFileReader(infile,strict = False)
                        pdf_writer = PdfFileWriter()
                        totalPages = pdf_reader.getNumPages()
                        page = int(pages[0])
                        
                        for n in range(0,totalPages,page):
                            nextn = n + page
                            pdf_reader = PdfFileReader(infile,strict = False)
                            pdf_writer = PdfFileWriter()
                            pageNumbers = [str(n+1) + str("-") + str(nextn)]
                            for i in range(n,nextn):
                                pdf_writer.addPage(pdf_reader.getPage(i))
                                
                            if name:
                                outputFile = PDFfunctions.rename(self,name,outputDirectory,basename,pageNumbers)
                            else:
                                outputFile = outputDirectory
                                
                            PDFfunctions.createDirectory(self,outputDirectory)
                            with open(r"{}".format(outputFile), 'wb') as outfile:
                                pdf_writer.write(outfile)
                                outfile.close()

        feedbackMsg = feedbackMsg = "Arquivos divididos em %.2f segundos." % (time.time() - start_time)
        self.emit(SIGNAL('feedback(QString)'), feedbackMsg)
        return 1


    def merge(self,paths, outputDirectory, name):
    # Juntar vários arquivos PDF em um único arquivo.
    # paths recebe os caminhos dos arquivos a trabalhar.
    # outputDirectory recebe o diretório de saída do arquivo.
    # name são os parâmetros da função rename ou então uma string

        start_time = time.time()
        feedbackMsg = feedbackMsg = "Mesclando arquivos..."
        self.emit(SIGNAL('feedback(QString)'), feedbackMsg)

        pdf_writer = PdfFileWriter() # Escrever em PDF.

        # Para cada arquivo.
        for path in paths:
            pdf_reader = PdfFileReader(path,strict = False) # Ler PDF.
            splitext = os.path.splitext(paths[0])[0]
            basename = os.path.basename(splitext) # Nome do arquivo original sem a extensão e diretório.
            outputFile = PDFfunctions.rename(self,name,outputDirectory,basename) # Retorna o nome final do arquivo.

            # Para cada página do arquivo.
            for page in range(pdf_reader.getNumPages()):
                # Adiciona cada página para o writer object
                pdf_writer.addPage(pdf_reader.getPage(page))

        # Salva o PDF mesclado.
        PDFfunctions.createDirectory(self,os.path.split(outputFile)[0])
        with open(r"{}".format(outputFile), 'wb') as out:
            pdf_writer.write(out)
            out.close()
        feedbackMsg = feedbackMsg = "Arquivos mesclados em %.2f segundos." % (time.time() - start_time)
        self.emit(SIGNAL('feedback(QString)'), feedbackMsg)
        return 1
        
    def ocrPDF(self,paths,outputDirectory,name,dpi):
    # Escanear arquivos PDF (extrair texto).
    # paths recebe os caminhos dos arquivos a trabalhar.
    # outputDirectory recebe o diretório de saída do arquivo.
    # name são os parâmetros da função rename ou então uma string.
    # dpi recebe um int com a qualidade em dpi da página extraída.
        start_time=  time.time()
        feedbackMsg = "Processando..."
        self.emit(SIGNAL('feedback(QString)'), feedbackMsg)
        
        counterFiles = 0
        pytesseract.pytesseract.tesseract_cmd = "tesseract\\tesseract" # Caminho do tesseract.

        # Para cada arquivo.
        for path in paths:
            pdf_reader = PdfFileReader(path,strict = False)
            totalPages = pdf_reader.getNumPages()
            counterPages = 0
            splitext = os.path.splitext(path)[0]
            basename = os.path.basename(splitext) # Nome do arquivo sem extensão e diretório.
            try:
                pagedpi = int(self.ui.lineEdit_intDpi_ocr.text())
            except:
                pagedpi = 200
             
            counterFiles+=1

            # Para cada página do arquivo.
            for page in range(totalPages):
                pages = convert_from_path(path,dpi=pagedpi, first_page=page + 1,last_page=page + 1,poppler_path="poppler\\bin",fmt="jpeg",use_pdftocairo=False) # biblioteca pdf2img
                feedbackMsg = "Convertendo página {}/{} do arquivo {}/{}...".format(counterPages + 1,totalPages,counterFiles,len(paths))
                self.emit(SIGNAL('feedback(QString)'), feedbackMsg)
                
                if not counterPages:
                    finalName = PDFfunctions.rename(self,name,outputDirectory,basename)
                    pdfName = finalName
                # Esse será o nome das outras páginas.
                else:
                    pdfName = PDFfunctions.rename(self,"#origin,#pages",outputDirectory,basename,counterPages)
                
                PDFfunctions.createDirectory(self,outputDirectory)
                    
                # Verifica se é a primeira página do arquivo. Se for, esse será o nome do arquivo final.
            
                # Salva a página do arquivo PDF em uma imagem JPEG.

                # Tesseract extrai o texto da imagem e converte para um arquivo PDF.
                pdfOcr = pytesseract.image_to_pdf_or_hocr(pages[0], lang = "por+eng")
                with open(r"{}".format(pdfName),"w+b") as f:
                    f.write(pdfOcr)
                    f.close()

                if counterPages:
                    PDFfunctions.merge(self,[finalName,pdfName],outputDirectory,'#origin')
                    os.remove(pdfName) # Arquivo auxiliar removido.
                pages[0].close()
                counterPages += 1

        feedbackMsg = "Arquivos convertidos com sucesso em %.2f segundos." % (time.time() - start_time)
        self.emit(SIGNAL('feedback(QString)'), feedbackMsg)
        return 1

    def searchPattern(self,paths,outputDirectory,name):
    # Procurar por padrões dentro de um arquivo PDF.
    # paths recebe os caminhos dos arquivos a trabalhar.
    # outputDirectory recebe o diretório de saída do arquivo.

        # Verificar se há dados vazios

        start_time = time.time()
        feedbackMsg = "Processando..."
        self.emit(SIGNAL('feedback(QString)'), feedbackMsg)

        ignoreFirstPage = self.ui.checkBox_ignoreFirstPage_search.checkState()  

        # Recebe o nome da lineEdit e extrai o nome da tabela e coluna para onde o arquivo será exportado
        # Localiza a tabela com o nome dado
        queryMoveToColumn = self.ui.lineEdit_moveto_search.text().lstrip().rstrip()
        queryMoveToColumnList = queryMoveToColumn.split(",")
        tableMoveToColumnList = queryMoveToColumnList[0].split(":")
        tableNameMoveToColumn = tableMoveToColumnList[0]
        columnIDMoveToColumn = int(tableMoveToColumnList[1]) - 1
        rowIDMoveToColumn = 0
        tableWidgetObjectMoveTo = "tableWidget " + tableNameMoveToColumn
        tableWidgtMoveTo = self.ui.tabWidget.findChild(QTableWidget, tableWidgetObjectMoveTo)
        
        # Recebe o nome da lineEdit com a query a ser executada e atribui a uma lista
        queryKeyword = self.ui.lineEdit_keywords_search.text().lstrip().rstrip()
        queryKeywordList = queryKeyword.split(",")

        output_string = None
        counterFiles = 0

        # Para cada arquivo.
        for path in paths:
            counterFiles += 1  # Contador para quantidade de arquivos.
            queryFound = [] # Reseta a lista com as querys já encontradas
            keywordsFound = [] # Reseta a lista com as palavras encontradas dentro do arquivo.
            counterPages = 0 # Reseta o contador para quantidade de páginas do arquivo.
            export = False # Reseta a variável que verifica se o arquivo deve ser movido.
            splitext = os.path.splitext(path)[0]
            basename = os.path.basename(splitext)
            
            # Verificar quantidade de páginas do arquivo
            pdf_reader = PdfFileReader(path,strict = False)
            totalPages = pdf_reader.getNumPages()
            moveOnlyPages = self.ui.checkBox_onlyPages_search.checkState() # moveOnlyPages é um boolean que indica se será movido somente as páginas que contem as palavras informadas ou o arquivo todo.

            # Abrir arquivo
            with open(r"{}".format(path), 'rb') as in_file:
                parser = PDFParser(in_file)
                doc = PDFDocument(parser)
                rsrcmgr = PDFResourceManager()
                device = None
                interpreter = None

                # Para cada página do arquivo.
                try:
                    for page in PDFPage.create_pages(doc):
                    
                        if moveOnlyPages:
                            queryFound = []
                            keywordsFound = []
                            export = False # Reseta a variável que verifica se a página foi exportada
                        
                        rowIDs = [] # Reseta a lista que a armazena o nome da tabela e a linha onde a palavra foi encontrada
                        
                        if export:
                            break
                        
                        #counterKeywords = 0 # Reseta o contador para quantidade de palavras a ser pesquisada.
                        counterPages += 1
                        output_string = StringIO()
                        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
                        interpreter = PDFPageInterpreter(rsrcmgr, device)
                        interpreter.process_page(page)
                        text = output_string.getvalue()

                        # Para cada query a ser executada
                        for query in queryKeywordList:
                            # Se as palavras da query ainda não foram encontradas
                            if query not in queryFound:
                                
                                keywords = [] # Reseta a lista das palavras a pesquisar
                                if export:
                                    break
                                # Recebe o nome da lineEdit e extrai o nome da tabela e coluna com as palavras a serem pesquisadas
                                # Localiza a tabela com o nome dado
                                tableKeywordList = query.split(":")
                                tableName = tableKeywordList[0]
                                columnID = int(tableKeywordList[1]) - 1
                                tableWidgetObject = "tableWidget " + tableName
                                tableWidgt = self.ui.tabWidget.findChild(QTableWidget, tableWidgetObject)
                                totalRows = tableWidgt.rowCount() # Total de linhas

                                # Verificar se alguma linha deve ser ignorada
                                for i in range(totalRows):
                                    if not (ignoreFirstPage and not i):
                                        keywords.append(tableWidgt.item(i,columnID).text())
                            
                            # Para cada palavra.
                                for rowNumber, keyword in enumerate(keywords):

                                    # Verifica se a primeira linha deve ser ignorada. Se sim, é adicionado + 1
                                    if ignoreFirstPage:
                                        rowId = rowNumber + 1
                                    else:
                                        rowId = rowNumber
                                        
                                    #counterKeywords += 1
                                    oldKeyword = keyword # Salva a palavra antiga antes da modificação.
                                    IsAscii = self.ui.checkBox_ignoreSpecialChar_search.checkState()
                                    ignoreSpaces = self.ui.checkBox_ignoreSpaces_search.checkState()
                                    ignorePontuation = self.ui.checkBox_ignorePontuation_search.checkState()
                                    text,keyword = PDFfunctions.regex(self,text,keyword,IsAscii,ignoreSpaces,ignorePontuation)
                                    
                                    # Pesquisar por palavra
                                    if re.search(keyword,text,re.IGNORECASE):
                                        feedbackMsg = "Expressão '{}' encontrada na página {} do arquivo {}.".format(oldKeyword,counterPages,counterFiles)
                                        self.emit(SIGNAL('feedback(QString)'), feedbackMsg)

                                        # Se a palavra já não foi encontrada
                                        if oldKeyword not in keywordsFound:
                                            keywordsFound.append(oldKeyword) # Adiciona a palavra encontrada a uma lista 
                                            queryFound.append(query) # Adiciona a query executada a uma lista para que não seja repetida
                                            rowIDs.append(tableName + ":" + str(rowId)) # Adiciona o nome da tabela e linha onde foi encontrada a palavra em uma lista
                                        
                                        # Verifica qual é a linha da tabela que contém o nome da pasta para qual será exportada
                                        if tableName == tableNameMoveToColumn:
                                            rowIDMoveToColumn = rowId

                                    # Se todas as querys foram executadas e foi encontrado palavras
                                    if len(keywordsFound) == len(queryKeywordList):
                                        # Verifica se somente as páginas ou todo o arquivo será movido.
                                        test = PDFfunctions.rename(self,self.ui.lineEdit_moveto_search.text(),'',ext='',rowIDS = rowIDs)
                                        folder = tableWidgtMoveTo.item(rowIDMoveToColumn,columnIDMoveToColumn).text() # Nome da pasta
                                        #folder = PDFfunctions.regex(self,folder,folder,False,False,True)[0] # Remover pontuação
                                        finalOutputDirectory = outputDirectory + "/" + folder # Caminho do diretório
                                        PDFfunctions.createDirectory(self,finalOutputDirectory)
                                        finalName = PDFfunctions.rename(self,name,finalOutputDirectory,basename,counterPages,'.pdf',keywordsFound,folder,rowIDs)
                                        if moveOnlyPages:
                                            self.ui.comboBox_extractPages.setCurrentIndex(0)
                                            PDFfunctions.extract(self,[path],[counterPages],finalName,0)
                                        else:
                                            in_file.close()
                                            PDFfunctions.moveFiles(self,path,finalName)
                                        export = True
                                        break
                                            
                                    # Se nenhuma das palavras foi encontrada na página/arquivo
                                    else:
                                        folderNotFound = self.ui.lineEdit_else_search.text().lstrip().rstrip()
                                        if (folderNotFound != '' and (rowId == len(keywords) and query == queryKeywordList[-1])):
                                            finalOutputDirectory = outputDirectory + "/" + folderNotFound + "/"
                                            PDFfunctions.createDirectory(self,finalOutputDirectory)
                                            if moveOnlyPages:
                                                feedbackMsg = "Expressões não encontradas nesta página"
                                                self.emit(SIGNAL('feedback(QString)'), feedbackMsg)
                                                finalName = finalOutputDirectory + basename + "_page_" + str(counterPages) + ".pdf"
                                                self.ui.comboBox_extractPages.setCurrentIndex(0)
                                                PDFfunctions.extract(self,[path],[counterPages],finalName,0)
                                                export = True
                                                break # prosseguir para o próximo arquivo
                                            else:
                                                if counterPages == totalPages:
                                                    feedbackMsg = "Expressões não encontradas neste arquivo."
                                                    self.emit(SIGNAL('feedback(QString)'), feedbackMsg)
                                                    finalName = finalOutputDirectory + basename + ".pdf"
                                                    in_file.close()
                                                    PDFfunctions.moveFiles(self,path,finalName)
                                                    export = True
                                                    break # prosseguir para o próximo arquivo   
                except:
                    pass
                # Fecha os objetos abertos.
                    output_string.close()
                    device.close()
                in_file.close()

        feedbackMsg = feedbackMsg = "Pesquisa concluída em %.2f segundos." % (time.time() - start_time)
        self.emit(SIGNAL('feedback(QString)'), feedbackMsg)
        return 1

    def importFromCSV(self):
        # Importar dados de arquivo csv
        self.ui.label_drop_csv.setParent(None)
        csvPaths = UIFunctions.csvPaths

        # Para cada arquivo
        for path in csvPaths:
            csvPath = "".join(path)
            # Verificar codificação
            try:
                csvFile = codecs.open(csvPath, encoding = "utf-8")
                dialect = csv.Sniffer().sniff(csvFile.read(), delimiters=";,") # Verificar delimitadores
            except:
                try:
                    csvFile = codecs.open(csvPath)
                    dialect = csv.Sniffer().sniff(csvFile.read(), delimiters=";,")
                except:
                    self.emit(SIGNAL('dialog(QString)'), "Não foi possível determinar os delimitadores do arquivo {}.".format(os.path.basename(os.path.splitext(csvPath)[0])))
                    feedbackMsg = ""
                    self.emit(SIGNAL('feedback(QString)'), feedbackMsg)
                    return 0

            csvFile.seek(0)
            reader = csv.reader(csvFile, dialect) # Ler dados
            list_of_rows = list(reader) # Salvar dados

            # Total de linhas
            # Ignorar linhas com espaço
            rowNumber = 0
            for row in list_of_rows: 
                if row[0] != "":
                    rowNumber += 1
            columnNumber = len(list_of_rows[0]) # Número de colunas
            
            # Nome da tabela
            splitext = os.path.splitext(csvPath)[0]
            basename = os.path.basename(splitext)
            tableName = basename

            totalTables = self.ui.tabWidget.count() # Total de tabelas

            # Criar tabela
            # TabWidget
            self.ui.tab = QWidget()
            self.ui.horizontalLayout_Table = QHBoxLayout(self.ui.tab)
            self.ui.horizontalLayout_Table.setContentsMargins(5, 0, 0, 0)

            # TableWidget
            tableWidgt = QTableWidget(self.ui.tab)
            tableWidgt.setObjectName("tableWidget " + tableName)
            tableWidgt.setStyleSheet(u"QTableWidget {	\n"
    "	background-color: rgb(39, 44, 54);\n"
    "	padding: 10px;\n"
    "	border-radius: 5px;\n"
    "	gridline-color: rgb(44, 49, 60);\n"
    "	border-bottom: 1px solid rgb(44, 49, 60);\n"
    "}\n"
    "QScrollBar:horizontal {\n"
    "    border: none;\n"
    "    background: rgb(52, 59, 72);\n"
    "    height: 14px;\n"
    "    margin: 0px 21px 0 21px;\n"
    "	border-radius: 0px;\n"
    "}\n"
    " QScrollBar:vertical {\n"
    "	border: none;\n"
    "    background: rgb(52, 59, 72);\n"
    "    width: 14px;\n"
    "    margin: 21px 0 21px 0;\n"
    "	border-radius: 0px;\n"
    " }\n"
    "QHeaderView::section{\n"
    "	Background-color: rgb(39, 44, 54);\n"
    "	max-width: 30px;\n"
    "	border: 1px solid rgb(44, 49, 60);\n"
    "	border-style: none;\n"
    "    border-bottom: 1px solid rgb(44, 49, 60);\n"
    "    border-right: 1px solid rgb(44, 49, 60);\n"
    "}\n"
    "QHeaderView::section:horizontal\n"
    "{\n"
    "    border: 1px solid rgb(32, 34, 42);\n"
    "	background-color: rgb(27, 29, 35);\n"
    "	padding: 3px;\n"
    "	border-top-left-radius: 7px;\n"
    "    border-top-right-radius: 7px;\n"
    "}\n"
    "QHeaderVi"
                            "ew::section:vertical\n"
    "{\n"
    "    border: 1px solid rgb(44, 49, 60);\n"
    "}\n"
    "\n"
    "")
            tableWidgt.setFrameShape(QFrame.StyledPanel)
            tableWidgt.setAutoScroll(True)
            tableWidgt.setEditTriggers(QAbstractItemView.NoEditTriggers)
            tableWidgt.setTabKeyNavigation(True)
            tableWidgt.setProperty("showDropIndicator", True)
            tableWidgt.setDragDropOverwriteMode(True)
            tableWidgt.setAlternatingRowColors(False)
            tableWidgt.setSelectionMode(QAbstractItemView.ExtendedSelection)
            tableWidgt.setSelectionBehavior(QAbstractItemView.SelectItems)
            tableWidgt.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
            tableWidgt.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
            tableWidgt.setShowGrid(True)
            tableWidgt.setRowCount(rowNumber)
            tableWidgt.setColumnCount(columnNumber)

            self.ui.horizontalLayout_Table.addWidget(tableWidgt)

            self.ui.tabWidget.addTab(self.ui.tab, tableName)
            self.ui.tabWidget.setCurrentIndex(totalTables) # Ir para a tabela criada

            # Para cada linha do arquivo
            for row_key, row_data in (enumerate(list_of_rows)):
                # Para cada coluna da linha
                for column_key, column_data in (enumerate(row_data)):
                    # Escrever item
                    tableWidgt.setItem(row_key,column_key,QtWidgets.QTableWidgetItem(str(column_data)))
        return 

    def zipCompress(self,rootDirectory,outputDirectory,name): 
        # Compactar arquivos em ZIP
        # rootDirectory recebe o diretório raiz onde estão as subpastas.
        # outputDirectory recebe o diretório de saída do arquivo.
        # name são os parâmetros da função rename ou então uma string.
        start_time = time.time()
        feedbackMsg = "Processando..."
        self.emit(SIGNAL('feedback(QString)'), feedbackMsg)

        # Pasta raiz, subpastas e arquivos
        for root, subdirs, files in os.walk(rootDirectory):
            # Para cada pasta
            for subdir in subdirs:
                counterPDF = []
                zipFilename = PDFfunctions.rename(self,name,outputDirectory,subdir,ext='.zip') # Nome do arquivo ZIP
                fullPath = root + "/" + subdir + "/" # Pasta raiz + subpasta
                for file in os.listdir(fullPath): # Para cada arquivo da subpasta
                    if file.endswith(".pdf") or file.endswith(".PDF"): # Se é pdf
                        counterPDF.append(os.path.basename(file)) # Adicionar paga exportar
                if len(counterPDF):
                    createZipFile = zipfile.ZipFile(zipFilename, "w") # Criar ZIP
                    for pdf in counterPDF:
                        createZipFile.write(fullPath + pdf,pdf) # Escrever
                    createZipFile.close() # Fechar
        feedbackMsg = feedbackMsg = "Arquivos compactados em %.2f segundos." % (time.time() - start_time)
        self.emit(SIGNAL('feedback(QString)'), feedbackMsg)
        return 1