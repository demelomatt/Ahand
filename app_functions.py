## ==> GUI FILE
#from main import *

# Bibliotecas nativas
import sqlite3, os, shutil, datetime, time, re, unicodedata
from io import StringIO

# Bibliotecas externas
from PyPDF2 import PdfFileWriter, PdfFileReader
from PIL import Image
from pdf2image import convert_from_path 
import pytesseract

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

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
        query = ''' CREATE TABLE IF NOT EXISTS {} (
                    ID integer, IF text, DO text
                    );  '''.format(self.tableName)
        self.executeQuery(query)
        self.dbConnection.commit()

    def deleteDBtable(self):
        # Deletar tabela.
        query = ''' DROP TABLE IF EXISTS {} '''.format(self.tableName)
        self.executeQuery(query)
        self.dbConnection.commit()

    def insertRowInDB(self,rowData):
        # Inserir registro no banco de dados.
        query = ''' INSERT INTO {} ('ID','IF','DO') VALUES (?,?,?) '''.format(self.tableName)
        self.executeQuery(query,rowData)
        self.dbConnection.commit()


class PDFfunctions():
# Classe para agrupar as funções dos arquivos PDF.

    def moveFiles(fromPath,toPath): 
    # Mover arquivos. Informar caminho de origem e caminho de destino.

        if not os.path.exists(toPath):    
            shutil.move(fromPath,toPath)
        if os.path.exists(fromPath):
            os.remove(fromPath)

    def createDirectory(path): 
    # Criar diretório informado caso ele não exista.

        if not os.path.exists(path):
            os.makedirs(path)

    def rename(arguments,outputDirectory,basename='',page=0,ext='.pdf',keywords='',group=''):
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
            page = "page " + str(page + 1)
        else:
            page = "page " + str(page[0] + 1) + "-" + str(page[-1] + 1)

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
        dic = {"year":year,"month":month,"day":day,"time":time,"page":page,"basename":basename,"group":group,"keywords":keywords}

        for argument in arguments:
            # Transforma lista do parâmetro keywords em string.
            if argument == "keywords":
                for keyword in keywords:
                    name.append(keyword)
            # Adiciona argumentos ao nome.
            else:
                try:
                    name.append(dic[argument])
                except:
                    name.append(argument)

        name = delimiter.join(name) # Junta o delimitador "_" ao nome.
        finalName = outputDirectory + name + ext 
        # Retorna o nome final do arquivo.
        return finalName

    

    def extractPages(paths,pages,outputDirectory,name):
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
                        page -= 1
                    else:
                        pages = list(["allpages"]) #string para lista

                    # Exportar página.
                    pdf_writer = PdfFileWriter()
                    pdf_writer.addPage(pdf_reader.getPage(page))
                    outputFile = PDFfunctions.rename(name,outputDirectory,basename,page)

                    with open(outputFile, 'wb') as outfile:
                        pdf_writer.write(outfile)
                        outfile.close()

    def extractAfter(paths,pages,outputDirectory,name):
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
                    pdf_writer = PdfFileWriter()
                    pageNumber.clear()

                    # Para cada número dentro do intervalo da página.
                    for number in range(page):
                        if number not in ignorePages:
                            pdf_writer.addPage(pdf_reader.getPage(number))
                            ignorePages.append(number)
                            pageNumber.append(number)

                    # Exportar páginas.
                    outputFile = PDFfunctions.rename(name,outputDirectory,basename,pageNumber)
                    with open(outputFile, 'wb') as outfile:
                        pdf_writer.write(outfile)
                        outfile.close()

    def extractEach(paths,n,outputDirectory,name):
    # Extrair páginas a cada n páginas. 
    # paths recebe os caminhos dos arquivos a trabalhar.
    # n recebe o padrão em que as páginas serão exportadas. Ex: 2. A cada 2 páginas, o documento será divido. (2,4,6,8)...
    # name são os parâmetros da função rename ou então uma string. 

        m = n # Salva o número de m

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
                    outputFile = PDFfunctions.rename(name,outputDirectory,basename,pageNumber)
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

    def merge(paths, outputDirectory, name):
    # Juntar vários arquivos PDF em um único arquivo.
    # paths recebe os caminhos dos arquivos a trabalhar.
    # outputDirectory recebe o diretório de saída do arquivo.
    # name são os parâmetros da função rename ou então uma string.

        pdf_writer = PdfFileWriter() # Escrever em PDF.

        # Para cada arquivo.
        for path in paths:
            pdf_reader = PdfFileReader(path) # Ler PDF.
            splitext = os.path.splitext(paths[0])[0]
            basename = os.path.basename(splitext) # Nome do arquivo original sem a extensão e diretório.
            outputFile = PDFfunctions.rename(name,outputDirectory,basename) # Retorna o nome final do arquivo.

            # Para cada página do arquivo.
            for page in range(pdf_reader.getNumPages()):
                # Adiciona cada página para o writer object
                pdf_writer.addPage(pdf_reader.getPage(page))

        # Salva o PDF mesclado.
        PDFfunctions.createDirectory(os.path.split(outputFile)[0])
        with open(outputFile, 'wb') as out:
            pdf_writer.write(out)
            out.close()

    def mergeBatch(rootDirectory,outputRootDirectory,name):
    # Juntar vários arquivos PDF contidos dentro de subpastas.
    # rootDirectory recebe o diretório raiz onde estão as subpastas.
    # outputDirectory recebe o diretório de saída do arquivo.
    # name são os parâmetros da função rename ou então uma string.

        counterFiles = 0 # contador para o número de arquivos encontrados.
        listPdfFiles = []

        # Retorna para listPdfFiles as subpastas dentro de rootDirectory.
        for amount in os.listdir(rootDirectory):
            if os.path.isdir(os.path.join(rootDirectory,amount)):
                listPdfFiles.append(amount)

        # Retorna para files todos os arquivos pdf contidos dentro da subpasta.
        for subdir in listPdfFiles:
            counterFiles = 0
            files = [] 
            path = os.path.join(rootDirectory,subdir)
            for file in os.listdir(path):
                if file.endswith(".pdf"):
                    counterFiles+=1
                    files.append(os.path.join(path,file))

        # Se existirem arquivos PDF, eles serão juntados em um único arquivo.
            if counterFiles != 0:
                outpuDirectory = os.path.join(outputRootDirectory,subdir) + "_"
                PDFfunctions.merge(files,outpuDirectory,name)

    def ocrPDF(paths,outputDirectory,suffix,dpi=200):
    # Escanear arquivos PDF (extrair texto).
    # paths recebe os caminhos dos arquivos a trabalhar.
    # outputDirectory recebe o diretório de saída do arquivo.
    # suffix recebe a string que procede o nome dos arquivos.
    # dpi recebe um int com a qualidade em dpi da página extraída.

        print("Carregando...")
        counterFiles = 0
        pytesseract.pytesseract.tesseract_cmd = "tesseract\\tesseract" # Caminho do tesseract.

        # Para cada arquivo.
        for path in paths:
            counterPages = 1
            splitext = os.path.splitext(path)[0]
            basename = os.path.basename(splitext) # Nome do arquivo sem extensão e diretório.
            pages = convert_from_path(path,dpi,poppler_path="poppler\\bin") # biblioteca pdf2img
            counterFiles+=1

            # Para cada página do arquivo.
            for page in pages:
                print("Convertendo página {}/{} do arquivo {}/{}.".format(counterPages,len(pages),counterFiles,len(paths)))
                # Verifica se é a primeira página do arquivo. Se for, esse será o nome do arquivo final.
                if counterPages == 1:
                    finalName = PDFfunctions.rename(["basename",suffix],outputDirectory,basename)
                    pdfName = finalName
                # Esse será o nome das outras páginas.
                else:
                    pdfName = PDFfunctions.rename(["basename","page"],outputDirectory,basename,counterPages)
                
                # Salva a página do arquivo PDF em uma imagem JPEG.
                imgName = PDFfunctions.rename(["basename","page"],outputDirectory,basename,counterPages,".jpg")
                page.save(imgName,'JPEG')

                # Tesseract extrai o texto da imagem e converte para um arquivo PDF.
                pdfOcr = pytesseract.image_to_pdf_or_hocr(imgName, lang = "por+eng")
                with open(pdfName,"w+b") as f:
                    f.write(pdfOcr)
                    f.close()
                os.remove(imgName) # Imagem removida.

                # Verifica se é a primeira página do arquivo.
                # Se não for, o pdf será juntado com o primeiro pdf.
                if counterPages !=1:
                    PDFfunctions.merge([finalName,pdfName],outputDirectory,["basename"])
                    os.remove(pdfName) # Arquivo auxiliar removido.
                counterPages += 1

    def regex(string,keyword,ascii=False,ignoreSpaces=False,ignorePunctuation=False):
        # Remover caracteres especiais e espaços do texto.
        # string recebe o texto.
        # ascii recebe boolean indicando se caracteres especiais devem ser ignorados na pesquisa.
        # ignoreSpaces recebe boolean indicando se espaços devem ser ignorados na pesquisa.
        # ignorePunctuation recebe boolean indicando se pontuação devem ser ignorados na pesquisa.

        if ascii:
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

    def searchPattern(paths,outputDirectory,moveFullFile=False,allWords=False,folderNotFound=True):
    # Procurar por padrões dentro de um arquivo PDF.
    # paths recebe os caminhos dos arquivos a trabalhar.
    # outputDirectory recebe o diretório de saída do arquivo.
    # moveFullFile é um boolean que indica se será movido somente as páginas que contem as palavras informadas ou o arquivo todo.
    # allWords é um boolean que indica se todas as palavras da lista devem estar no arquivo/página.
    # folderNotFound é um boolean que indica se será criada uma pasta para mover os arquivos não encontrados.

        keywords = [] # Lista com as palavras para pesquisar dentro do arquivo.
        output_string = None
        counterFiles = 0
        # Para cada arquivo.
        for path in paths:
            counterFiles += 1  # Contador para quantidade de arquivos.
            fileFoundedList = [] # Reseta a lista com as palavras encontradas dentro do arquivo.
            counterPages = 0 # Reseta o contador para quantidade de páginas do arquivo.
            export = False # Reseta a variável que verifica se o arquivo deve ser movido.

            # Abrir arquivo
            with open(path, 'rb') as in_file:
                parser = PDFParser(in_file)
                doc = PDFDocument(parser)
                rsrcmgr = PDFResourceManager()
                device = None
                interpreter = None

                # Para cada página do arquivo.
                for page in PDFPage.create_pages(doc):
                    if export:
                        break
                    pageFoundedList = [] # Reseta a lista com as palavras encontradas dentro de uma página.
                    #counterKeywords = 0 # Reseta o contador para quantidade de palavras a ser pesquisada.
                    counterPages += 1
                    output_string = StringIO()
                    device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
                    interpreter = PDFPageInterpreter(rsrcmgr, device)
                    interpreter.process_page(page)
                    text = output_string.getvalue()
                    
                    # Para cada palavra.
                    for keyword in keywords:
                        founded = False # Resetar variável
                        #counterKeywords += 1
                        oldKeyword = keyword # Salva a palavra antiga antes da modificação.
                        text,keyword = PDFfunctions.regex(text,keyword,True,True,True)
                        #print(text)
                        
                        # Se todas as palavras da lista devem estar no arquivo/página.
                        if allWords:
                            if re.search(keyword,text,re.IGNORECASE):
                                if (keyword not in fileFoundedList) and (moveFullFile): # Se palavra foi encontrada adicionar em uma lista para os arquivos caso moveFullFile seja verdadeiro.
                                    fileFoundedList.append(keyword)
                                elif (keyword not in pageFoundedList) and (not moveFullFile): # Se palavra foi encontrada adicionar em uma lista para as páginas caso moveFullFile seja falso.
                                    pageFoundedList.append(keyword)
                                print("Expressão '{}' encontrada na página {} do arquivo {}.".format(oldKeyword,counterPages,counterFiles))
                        
                        # Se somente uma das palavras deve estar no arquivo/página.
                        else:
                            if re.search(keyword,text,re.IGNORECASE):
                                print("Expressão '{}' encontrada na página {} do arquivo {}.".format(oldKeyword,counterPages,counterFiles))
                                founded = True # Se uma das palavras foi encontrada dentro da página.

                        # Se uma das palavras for encontrada / ou se todas as palavras foram encontradas dentro de um arquivo / ou se todas as palavras foram encontradas dentro de uma página.
                        if founded or (len(fileFoundedList) == len(keywords)) or (len(pageFoundedList) == len(keywords)):
                            
                            # Verifica se somente as páginas ou todo o arquivo será movido.
                            if moveFullFile:
                                print("Exportar arquivo e prosseguir para próximo arquivo.")
                                export = True
                                break # prosseguir para o próximo arquivo
                            else:
                                print("Exportar página e prosseguir para próxima página.")
                                break # prosseguir para próxima página

                # Fecha os objetos abertos.
                    output_string.close()
                    device.close()
                in_file.close()