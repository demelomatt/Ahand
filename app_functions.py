# Importar arquivos
from ui_main import Ui_MainWindow
from ui_functions import *

# Bibliotecas nativas
import sqlite3, os, shutil, datetime, time, re, unicodedata, csv, codecs, zipfile
from io import StringIO

# Bibliotecas externas
from PyPDF2 import PdfFileWriter, PdfFileReader # PDF
from PIL import Image # IMAGE
from pdf2image import convert_from_path # PDF2IMAGE
import pytesseract # TESSERACT

    #pdfminer
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from pdfminer.high_level import extract_pages

class DataBase():
# Classe para manipular banco de dados.

    def __init__(self,path,tableName):
        # Iniciar banco de dados.

        self.dbConnection = sqlite3.connect(path)
        self.cursor = self.dbConnection.cursor()
        self.tableName = tableName

    def commitDB(self):
        # Comitar mudanças.
        self.dbConnection.commit()

    def closeDB(self):
        # Fechar banco de dados.
        self.dbConnection.close()
        
    def executeQuery(self,query,data=""):
        # Executar uma query.
        result = self.cursor.execute(query,data)
        return result

    def createDBTable(self):
        # Criar tabela..
        query = ''' CREATE TABLE IF NOT EXISTS "{}" (
                    "Column0" integer, "Column1" text, "Column2" text
                    );  '''.format(self.tableName)
        self.executeQuery(query)
        self.dbConnection.commit()

    def deleteDBtable(self):
        # Deletar tabela.
        query = ''' DROP TABLE IF EXISTS "{}" '''.format(self.tableName)
        self.executeQuery(query)
        self.dbConnection.commit()

    def insertRowInDB(self,rowData):
        # Inserir registro no banco de dados.
        query = ''' INSERT INTO "{}" VALUES {} '''.format(self.tableName,rowData)
        self.executeQuery(query)
        self.dbConnection.commit()

    def insertColumnInDB(self):
        # Inserir coluna no banco de dados.
        columnName = "Column" + str(self.loadData()[1] + 1)
        query = '''ALTER TABLE "{}" ADD "{}" text'''.format(self.tableName,columnName)
        self.executeQuery(query)
        self.dbConnection.commit()

    def loadData(self):
        query = "SELECT * FROM {}".format(self.tableName)
        result = self.executeQuery(query)
        columnCount = 0
        rowCount = 0
        for row_number, row_data in enumerate(result):
            rowCount = row_number
            for column_number, column_data in enumerate(row_data):
                columnCount = column_number
        return rowCount, columnCount

class PDFfunctions():
# Classe para agrupar as funções dos arquivos PDF.
    
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

    def rename(self,arguments,outputDirectory,basename='',page=0,ext='.pdf',keywords='',group='',rowIDs=[]):
    # Renomear arquivos PDF. arguments deve receber algum dos parâmetros em dic ou então uma string.
    # outputDirectory recebe o diretório de saída do arquivo.
    # basename recebe o nome do arquivo sem a extensão e diretório.
    # page recebe o(s) número da(s) página(s) que devem conter no nome do arquivo.
    # ext recebe a extensão do arquivo. O padrão é ".pdf".
    # keywords e group são parâmetros definidos somente para a função searchPattern.

        name = []
        delimiter = "_"
        # Verificar se foi informada somente uma página ou uma lista de páginas. 
        # Caso seja lista, é retornado o primeiro e o último índice.
        if type(page) == int:
            page = str(page + 1)
        else:
            page = str(page[0] + 1) + "-" + str(page[-1] + 1)

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
        dic = {"#year":year,"#month":month,"#day":day,"#time":time,"#page":page,"#basename":basename,"#group":group,"#keywords":keywords}

        arguments = arguments.split(",") # Transformar argumentos em lista

        for argument in arguments:
            # Transforma lista do parâmetro keywords em string.
            if argument == "#keywords":
                for keyword in keywords:
                    keyword = PDFfunctions.regex(self,keyword,keyword,False,False,True)[0]
                    name.append(keyword)
            # Adiciona argumentos ao nome.
            else:
                try:
                    name.append(dic[re.sub('[ ]+', '', argument)]) # Remover espaços e procurar palavra no dicionário
                except:
                    try:
                        # objeto tablewidget
                        # linha
                        # coluna

                        queryList = argument.split(":")
                        tableName = queryList[0]
                        columnID = int(queryList[1]) - 1
                        tableWidgetObject = "tableWidget " + tableName
                        tableWidgt = self.findChild(QTableWidget, tableWidgetObject)

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
                        name.append(argument)
                
        # Se o nome for vazio, recebe a tag basename
        if name == [] or name[0] == '':
            name[0] = basename

        name = delimiter.join(name) # Junta o delimitador "_" ao nome.
        finalName = outputDirectory + "/" + name + ext 
        # Retorna o nome final do arquivo.
        return finalName

    def extract(self,paths,pages,outputDirectory,name):

        if outputDirectory == '':
            UIFunctions.showDialog(UIFunctions,"O diretório de saída não foi selecionado.")
            return 0

        if not len(paths):
            UIFunctions.showDialog(UIFunctions,"Selecione ao menos 1 arquivo para extrair páginas.")
            return 0

        if pages == '':
            UIFunctions.showDialog(UIFunctions,"Selecione ao menos 1 página para extrair.")
            return 0

        pages = pages.split(",")

        if name == "":
            name = "#basename,#page"

        if self.ui.checkBox_extractPages.checkState():
            PDFfunctions.extractPages(self,paths,pages,outputDirectory,name)
            return 1

        if self.ui.checkBox_extractAfter.checkState():
            PDFfunctions.extractAfter(self,paths,pages,outputDirectory,name)
            return 1

        if self.ui.checkBox_extractEach.checkState():
            PDFfunctions.extractEach(self,paths,pages[0],outputDirectory,name)
            return 1

    def extractPages(self,paths,pages,outputDirectory,name):
    # Extrair páginas indicadas de PDF.
    # paths recebe os caminhos dos arquivos a trabalhar.
    # pages recebe as páginas a serem exportadas ou "allpages" para extrair todas as páginas.
    # outputDirectory recebe o diretório de saída do arquivo.
    # name são os parâmetros da função rename ou então uma string. 

        # Para cada arquivo.
        for path in paths:
            splitext = os.path.splitext(path)[0]
            basename = os.path.basename(splitext)

            # Abrir arquivo.
            with open(path, 'rb') as infile:
                pdf_reader = PdfFileReader(infile)
                pdf_writer = PdfFileWriter()
                totalPages = pdf_reader.getNumPages()
                allpages = False
                pages = pages
                if pages[0] == "allpages":
                    pages = range(totalPages)
                    allpages = True
                
                #Para cada página do arquivo.
                for page in pages:
                    if not allpages:
                        page = int(page)
                        page -= 1
                    else:
                        pages = list(["allpages"]) #string para lista

                    # Exportar página.
                    pdf_writer = PdfFileWriter()
                    pdf_writer.addPage(pdf_reader.getPage(page))
                    
                    if name:
                        outputFile = PDFfunctions.rename(self,name,outputDirectory,basename,page)
                    else:
                        outputFile = outputDirectory

                    with open(outputFile, 'wb') as outfile:
                        pdf_writer.write(outfile)
                        outfile.close()

    def extractAfter(self,paths,pages,outputDirectory,name):
    # Extrair páginas de arquivo PDF até a sequência indicada. 
    # paths recebe os caminhos dos arquivos a trabalhar.
    # pages recebe as páginas a serem exportadas. Ex: [3,7]. Irá gerar três arquivos. Da página 1 até a 3, da 4 até a 7, e de 7 ao número total de páginas do arquivo.
    # outputDirectory recebe o diretório de saída do arquivo.
    # name são os parâmetros da função rename ou então uma string. 

        # Tamanho da lista.
        pagesLength = len(pages) 
        pages.append(pagesLength)

        # Para cada arquivo.
        for path in paths:
            ignorePages = [] # Ignorar páginas que já foram importadas.
            pageNumber = [] # Lista com os números da página.
            splitext = os.path.splitext(path)[0]
            basename = os.path.basename(splitext)

            #Abrir arquivo.
            with open(path, 'rb') as infile:
                pdf_reader = PdfFileReader(infile)
                pdf_writer = PdfFileWriter()
                totalPages = pdf_reader.getNumPages()
                pages[pagesLength] = totalPages

                # Para cada página do arquivo.
                for page in pages:
                    page = int(page)
                    pdf_writer = PdfFileWriter()
                    pageNumber.clear()

                    # Para cada número dentro do intervalo da página.
                    for number in range(page):
                        if number not in ignorePages:
                            pdf_writer.addPage(pdf_reader.getPage(number))
                            ignorePages.append(number)
                            pageNumber.append(number)

                    # Exportar páginas.
                    outputFile = PDFfunctions.rename(self,name,outputDirectory,basename,pageNumber)
                    with open(outputFile, 'wb') as outfile:
                        pdf_writer.write(outfile)
                        outfile.close()

    def extractEach(self,paths,n,outputDirectory,name):
    # Extrair páginas a cada n páginas. 
    # paths recebe os caminhos dos arquivos a trabalhar.
    # n recebe o padrão em que as páginas serão exportadas. Ex: 2. A cada 2 páginas, o documento será divido. (2,4,6,8)...
    # name são os parâmetros da função rename ou então uma string. 

        m = int(n) # Salva o número de m

        # Para cada arquivo.
        for path in paths:
            splitext = os.path.splitext(path)[0]
            basename = os.path.basename(splitext)
            ignorePages = []
            pageNumber = []
            n = m # Reseta o valor de n

            # Abrir arquivo.
            with open(path, 'rb') as infile:
                pdf_reader = PdfFileReader(infile)
                pdf_writer = PdfFileWriter()
                totalPages = pdf_reader.getNumPages()

                # Enquanto n for menor ou igual o total de páginas do arquivo.
                while n <= totalPages:
                    pdf_writer = PdfFileWriter()
                    pageNumber.clear()

                    # Para cada página no intervalo de n.
                    for page in range(n):
                        if page not in ignorePages:
                            pdf_writer.addPage(pdf_reader.getPage(page))
                            ignorePages.append(page)
                            pageNumber.append(page)

                    # Salvar arquivo.
                    outputFile = PDFfunctions.rename(self,name,outputDirectory,basename,pageNumber)
                    with open(outputFile, 'wb') as outfile:
                        pdf_writer.write(outfile)
                        outfile.close()

                    # Verifica se o loop deve reiniciar ou continuar.
                    if n == totalPages:
                        break
                    elif n+m <= totalPages:
                            n += m
                    else:
                        n = totalPages

    def merge(self,paths, outputDirectory, name):
    # Juntar vários arquivos PDF em um único arquivo.
    # paths recebe os caminhos dos arquivos a trabalhar.
    # outputDirectory recebe o diretório de saída do arquivo.
    # name são os parâmetros da função rename ou então uma string.

        if outputDirectory == '':
            UIFunctions.showDialog(UIFunctions,"O diretório de saída não foi selecionado.")
            return 0

        if len(paths) <= 1:
            UIFunctions.showDialog(UIFunctions,"Selecione ao menos 2 arquivos para mesclar.")
            return 0

        pdf_writer = PdfFileWriter() # Escrever em PDF.

        # Para cada arquivo.
        for path in paths:
            pdf_reader = PdfFileReader(path) # Ler PDF.
            splitext = os.path.splitext(paths[0])[0]
            basename = os.path.basename(splitext) # Nome do arquivo original sem a extensão e diretório.
            outputFile = PDFfunctions.rename(self,name,outputDirectory,basename) # Retorna o nome final do arquivo.

            # Para cada página do arquivo.
            for page in range(pdf_reader.getNumPages()):
                # Adiciona cada página para o writer object
                pdf_writer.addPage(pdf_reader.getPage(page))

        # Salva o PDF mesclado.
        PDFfunctions.createDirectory(self,os.path.split(outputFile)[0])
        with open(outputFile, 'wb') as out:
            pdf_writer.write(out)
            out.close()
        return 1
        
    def ocrPDF(self,paths,outputDirectory,name,dpi):
    # Escanear arquivos PDF (extrair texto).
    # paths recebe os caminhos dos arquivos a trabalhar.
    # outputDirectory recebe o diretório de saída do arquivo.
    # name são os parâmetros da função rename ou então uma string.
    # dpi recebe um int com a qualidade em dpi da página extraída.

        if outputDirectory == '':
            UIFunctions.showDialog(UIFunctions,"O diretório de saída não foi selecionado.")
            return 0

        if not len(paths):
            UIFunctions.showDialog(UIFunctions,"Selecione ao menos 1 arquivo para escanear.")
            return 0

        counterFiles = 0
        pytesseract.pytesseract.tesseract_cmd = "tesseract\\tesseract" # Caminho do tesseract.

        # Para cada arquivo.
        for path in paths:
            counterPages = 0
            splitext = os.path.splitext(path)[0]
            basename = os.path.basename(splitext) # Nome do arquivo sem extensão e diretório.
            pages = convert_from_path(path,dpi,poppler_path="poppler\\bin") # biblioteca pdf2img
            counterFiles+=1

            # Para cada página do arquivo.
            for page in pages:

                print("Convertendo página {}/{} do arquivo {}/{}.".format(counterPages + 1,len(pages),counterFiles,len(paths)))
                # Verifica se é a primeira página do arquivo. Se for, esse será o nome do arquivo final.
                if not counterPages:
                    finalName = PDFfunctions.rename(self,name,outputDirectory,basename)
                    pdfName = finalName
                # Esse será o nome das outras páginas.
                else:
                    pdfName = PDFfunctions.rename(self,"#basename,#page",outputDirectory,basename,counterPages)
                # Salva a página do arquivo PDF em uma imagem JPEG.
                imgName = PDFfunctions.rename(self, "#basename,#page",outputDirectory,basename,counterPages,".jpg")
                page.save(imgName,'JPEG')

                # Tesseract extrai o texto da imagem e converte para um arquivo PDF.
                pdfOcr = pytesseract.image_to_pdf_or_hocr(imgName, lang = "por+eng")
                with open(pdfName,"w+b") as f:
                    f.write(pdfOcr)
                    f.close()
                os.remove(imgName) # Imagem removida.

                # Verifica se é a primeira página do arquivo.
                # Se não for, o pdf será juntado com o primeiro pdf.
                if counterPages:
                    PDFfunctions.merge(self,[finalName,pdfName],outputDirectory,'#basename')
                    os.remove(pdfName) # Arquivo auxiliar removido.
                counterPages += 1
        return 1


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
            keyword = re.sub('[ ]+', '', keyword)

        if ignorePunctuation:
            string = re.sub(r"[.,;/!?:-]+", '', string)
            keyword = re.sub(r"[.,;/!?:-]+", '', keyword)

        return string, keyword

    def searchPattern(self,paths,outputDirectory,name):
    # Procurar por padrões dentro de um arquivo PDF.
    # paths recebe os caminhos dos arquivos a trabalhar.
    # outputDirectory recebe o diretório de saída do arquivo.

        # Verificar se há dados vazios

        if outputDirectory == '':
            UIFunctions.showDialog(UIFunctions,"O diretório de saída não foi selecionado.")
            return 0

        if not len(paths):
            UIFunctions.showDialog(UIFunctions,"Selecione ao menos 1 arquivo para procurar por expressões.")
            return 0

        if self.ui.lineEdit_keywords_search.text() == '':
            UIFunctions.showDialog(UIFunctions,"Nenhum dado foi passado para pesquisar dentro do arquivo.")
            return 0

        if self.ui.lineEdit_moveto_search.text() == '':
            UIFunctions.showDialog(UIFunctions,"Nenhuma pasta foi indicada para exportar.")
            return 0

        ignoreFirstPage = Ui_MainWindow.checkBox_ignoreFirstPage_search.checkState()  

        tableCurrentIndex = Ui_MainWindow.tabWidget.currentIndex()
        tableCurrentName = Ui_MainWindow.tabWidget.tabText(tableCurrentIndex)

        # Recebe o nome da lineEdit e extrai o nome da tabela e coluna para onde o arquivo será exportado
        # Localiza a tabela com o nome dado
        queryMoveToColumn = Ui_MainWindow.lineEdit_moveto_search.text()
        queryMoveToColumnList = queryMoveToColumn.split(",")
        tableMoveToColumnList = queryMoveToColumnList[0].split(":")
        tableNameMoveToColumn = tableMoveToColumnList[0]
        columnIDMoveToColumn = int(tableMoveToColumnList[1]) - 1
        rowIDMoveToColumn = 0
        tableWidgetObjectMoveTo = "tableWidget " + tableNameMoveToColumn
        tableWidgtMoveTo = self.findChild(QTableWidget, tableWidgetObjectMoveTo)
        
        # Recebe o nome da lineEdit com a query a ser executada e atribui a uma lista
        queryKeyword = Ui_MainWindow.lineEdit_keywords_search.text()
        queryKeywordList = queryKeyword.split(",")

        output_string = None
        counterFiles = 0

        # Para cada arquivo.
        for path in paths:
            counterFiles += 1  # Contador para quantidade de arquivos.
            fileFoundedList = [] # Reseta a lista com as palavras encontradas dentro do arquivo.
            counterPages = 0 # Reseta o contador para quantidade de páginas do arquivo.
            fileExport = False # Reseta a variável que verifica se o arquivo deve ser movido.
            splitext = os.path.splitext(path)[0]
            basename = os.path.basename(splitext)
            queryFound = [] # Reseta a lista com as querys já encontradas

            # Verificar quantidade de páginas do arquivo
            pdf_reader = PdfFileReader(path)
            totalPages = pdf_reader.getNumPages()

            # Abrir arquivo
            with open(path, 'rb') as in_file:
                parser = PDFParser(in_file)
                doc = PDFDocument(parser)
                rsrcmgr = PDFResourceManager()
                device = None
                interpreter = None

                # Para cada página do arquivo.
                try:
                    for page in PDFPage.create_pages(doc):
                        
                        rowIDs = [] # Reseta a lista que a armazena o nome da tabela e a linha onde a palavra foi encontrada
                        
                        pageExport = False # Reseta a variável que verifica se a página foi exportada
                        if fileExport:
                            break
                        pageFoundedList = [] # Reseta a lista com as palavras encontradas dentro de uma página.
                        pageTableKeyword = []
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
                                keywordBreak = False # Reseta a variável que para o loop caso uma palavra for encontrada
                                
                                keywords = [] # Reseta a lista das palavras a pesquisar
                                if pageExport:
                                    break
                                # Recebe o nome da lineEdit e extrai o nome da tabela e coluna com as palavras a serem pesquisadas
                                # Localiza a tabela com o nome dado
                                tableKeywordList = query.split(":")
                                tableName = tableKeywordList[0]
                                columnID = int(tableKeywordList[1]) - 1
                                tableWidgetObject = "tableWidget " + tableName
                                tableWidgt = self.findChild(QTableWidget, tableWidgetObject)

                                totalRows = tableWidgt.rowCount() # Total de linhas

                                # Verificar se alguma linha deve ser ignorada
                                for i in range(totalRows):
                                    if not (ignoreFirstPage and not i):
                                        keywords.append(tableWidgt.item(i,columnID).text())
                            
                            # Para cada palavra.
                                for rowNumber, keyword in enumerate(keywords):
                                    if keywordBreak:
                                        break

                                    # Verifica se a primeira linha deve ser ignorada. Se sim, é adicionado + 1
                                    if ignoreFirstPage:
                                        rowId = rowNumber + 1
                                    else:
                                        rowId = rowNumber
                                        
                                    #counterKeywords += 1
                                    oldKeyword = keyword # Salva a palavra antiga antes da modificação.
                                    IsAscii = Ui_MainWindow.checkBox_ignoreSpecialChar_search.checkState()
                                    ignoreSpaces = Ui_MainWindow.checkBox_ignoreSpaces_search.checkState()
                                    ignorePontuation = Ui_MainWindow.checkBox_ignorePontuation_search.checkState()
                                    text,keyword = PDFfunctions.regex(self,text,keyword,IsAscii,ignoreSpaces,ignorePontuation)
                                    
                                    moveFullFile = Ui_MainWindow.checkBox_onlyPages_search.checkState() # moveFullFile é um boolean que indica se será movido somente as páginas que contem as palavras informadas ou o arquivo todo.
                                    operator = Ui_MainWindow.comboBox_operator_search.currentText() # operator é uma lista que indica se todas (E) as palavras da lista devem estar no arquivo/página (OU) somente alguma delas.
                                    # Se todas as palavras da lista devem estar no arquivo/página.
                                    if operator == "E":
                                        if re.search(keyword,text,re.IGNORECASE):
                                            if (keyword not in fileFoundedList) and (moveFullFile): # Se palavra foi encontrada adicionar em uma lista para os arquivos caso moveFullFile seja verdadeiro.
                                                fileFoundedList.append(oldKeyword)
                                                if (len(fileFoundedList) == len(keywords)):
                                                    fileTableKeyword.append(oldKeyword)

                                            elif (keyword not in pageFoundedList) and (not moveFullFile): # Se palavra foi encontrada adicionar em uma lista para as páginas caso moveFullFile seja falso.
                                                pageFoundedList.append(keyword)
                                                if (len(pageFoundedList) == len(keywords) and oldKeyword not in pageTableKeyword):
                                                    pageTableKeyword.append(oldKeyword)

                                            print("Expressão '{}' encontrada na página {} do arquivo {}.".format(oldKeyword,counterPages,counterFiles))
                                    
                                    # Se somente uma das palavras deve estar no arquivo/página.
                                    else:
                                        if re.search(keyword,text,re.IGNORECASE):
                                            print("Expressão '{}' encontrada na página {} do arquivo {}.".format(oldKeyword,counterPages,counterFiles))
                                            # Se a palavra já não foi encontrada
                                            if oldKeyword not in pageTableKeyword:
                                                pageTableKeyword.append(oldKeyword) # Adiciona a palavra encontrada a uma lista 
                                                queryFound.append(query) # Adiciona a query executada a uma lista para que não seja repetida
                                                rowIDs.append(tableName + ":" + str(rowId)) # Adiciona o nome da tabela e linha onde foi encontrada a palavra em uma lista
                                                keywordBreak = True
                                            
                                            # Verifica qual é a linha da tabela que contém o nome da pasta para qual será exportada
                                            if tableName == tableNameMoveToColumn:
                                                rowIDMoveToColumn = rowId

                                    # Se todas as querys foram executadas e foi encontrado palavras
                                    if len(pageTableKeyword) == len(queryKeywordList):
                                        # Verifica se somente as páginas ou todo o arquivo será movido.
                                        if not moveFullFile:
                                            print("Exportar arquivo e prosseguir para próximo arquivo.")
                                            folder = tableWidgtMoveTo.item(rowIDMoveToColumn + 1,columnIDMoveToColumn).text() # Nome da pasta
                                            finalOutputDirectory = outputDirectory + "/" + folder # Caminho do diretório
                                            PDFfunctions.createDirectory(self,finalOutputDirectory)
                                            finalName = PDFfunctions.rename(self,name,finalOutputDirectory,basename,counterPages,'.pdf',fileFoundedList,folder,rowIDs)
                                            in_file.close()
                                            PDFfunctions.moveFiles(self,path,finalName)
                                            fileExport = True
                                            break # prosseguir para o próximo arquivo
                                        else:
                                            print("Exportar página e prosseguir para próxima página.")
                                            folder = tableWidgtMoveTo.item(rowIDMoveToColumn,columnIDMoveToColumn).text() # Nome da pasta
                                            finalOutputDirectory = outputDirectory + "/" + folder # Caminho do diretório
                                            PDFfunctions.createDirectory(self,finalOutputDirectory)
                                            finalName = PDFfunctions.rename(self,name,finalOutputDirectory,basename,counterPages,".pdf",pageTableKeyword,folder,rowIDs)
                                            #in_file.close()
                                            PDFfunctions.extractPages(self,[path],[counterPages],finalName,0)
                                            pageExport = True
                                            break # prosseguir para próxima página

                                    # Se nenhuma das palavras foi encontrada na página/arquivo
                                    else:
                                        folderNotFound = Ui_MainWindow.lineEdit_else_search.text()
                                        if folderNotFound != '' and rowId == len(keywords) and counterPages == totalPages:
                                            if not moveFullFile:
                                                print("Nenhuma expressão encontrada neste arquivo. Exportar para folderNotFound.")
                                                finalOutputDirectory = outputDirectory + "/" + folderNotFound + "/"
                                                PDFfunctions.createDirectory(self,finalOutputDirectory)
                                                finalName = finalOutputDirectory + basename + ".pdf"
                                                in_file.close()
                                                PDFfunctions.moveFiles(self,path,finalName)
                                                fileExport = True
                                                break # prosseguir para o próximo arquivo
                                            else:
                                                print("Nenhuma expressão encontrada nesta página. Exportar para folderNotFound.")
                                                finalOutputDirectory = outputDirectory + "/" + folderNotFound + "/"
                                                PDFfunctions.createDirectory(self,finalOutputDirectory)
                                                #in_file.close()
                                                finalName = finalOutputDirectory + basename + "_page_" + str(counterPages) + ".pdf"
                                                PDFfunctions.extractPages(self,[path],[counterPages],finalName,0)
                                                pageExport = True
                                                break # prosseguir para próxima página
                except Exception as e:
                    print(e)
                    pass

                # Fecha os objetos abertos.
                    output_string.close()
                    device.close()
                in_file.close()
        return 1


    def importFromCSV(self):
        # Importar dados de arquivo csv
        fileDialog = QFileDialog.getOpenFileNames(self, 'Selecionar arquivo csv', QtCore.QDir.currentPath(), 'csv files (*.csv)',options=QFileDialog.DontUseNativeDialog)[0]

        # Para cada arquivo
        for path in fileDialog:
            csvPath = "".join(path)
            # Verificar codificação
            try:
                csvFile = codecs.open(csvPath, encoding = "utf-8")
                dialect = csv.Sniffer().sniff(csvFile.read(), delimiters=";,") # Verificar delimitadores
            except:
                csvFile = codecs.open(csvPath)
                dialect = csv.Sniffer().sniff(csvFile.read(), delimiters=";,")
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

            currentTabIndex = self.ui.tabWidget.currentIndex() + 1 # Tabela atual
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

        if outputDirectory == '':
            UIFunctions.showDialog(UIFunctions,"O diretório de saída não foi selecionado.")
            return 0

        if rootDirectory == '':
            UIFunctions.showDialog(UIFunctions,"O diretório raiz não foi selecionado.")
            return 0

        # Pasta raiz, subpastas e arquivos
        for root, subdirs, files in os.walk(rootDirectory):
            # Para cada pasta
            for subdir in subdirs:
                counterPDF = []
                zipFilename = PDFfunctions.rename(self,name,outputDirectory,subdir,ext='.zip') # Nome do arquivo ZIP
                fullPath = root + "/" + subdir + "/" # Pasta raiz + subpasta
                for file in os.listdir(fullPath): # Para cada arquivo da subpasta
                    if file.endswith(".pdf"): # Se é pdf
                        counterPDF.append(os.path.basename(file)) # Adicionar paga exportar
                if len(counterPDF):
                    createZipFile = zipfile.ZipFile(zipFilename, "w") # Criar ZIP
                    for pdf in counterPDF:
                        createZipFile.write(fullPath + file, pdf) # Escrever
                    createZipFile.close() # Fechar

        return 1
