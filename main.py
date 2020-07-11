print("")
# Bibliotecas externas
import pytesseract,fitz, winshell
from PIL import Image
# Bibliotecas nativas do Python
import os, shutil, re, datetime, zipfile, csv, codecs

# Atribuição de variáveis globais
username = os.path.expanduser("~") 
dateTime = (datetime.datetime.now()) 
splitDateTime = [str(dateTime.year),str(dateTime.month)] 
fullDirNames, dirNamesWithoutExt, pdfFilenames, groups, keywordsByGroup, keywords, currentKeyword, searchForKeyword = [],[],[],[],[],[],"",""

# Atribuição de funções
def listFiles(path,ext): # Listar arquivos PDF de um diretório
    global fullDirNames, dirNamesWithoutExt, pdfFilenames
    fullDirNames = [] 
    dirNamesWithoutExt = []
    pdfFilenames = []
    files = os.listdir(path)
    for file in files:
        if file.endswith(ext):
            fullDirNames.append(path + file)
            dirNamesWithoutExt.append(file)
            pdfFilenames.append(os.path.splitext(file)[0])

def ocrPdf(path): # Transformar arquivos PDF em pesquisáveis
    createDirectory(inputDirectory)
    createDirectory(inputDirectory + "00 -- OCR\\") 
    listFiles(path,".pdf")
    filesNumber = len(fullDirNames)
    print("Arquivos encontrados para converter:",filesNumber)
    print("Carregando...")
    if filesNumber != 0:
        counterFiles, TotalPagesNumber, loadPdfPage, openPDF, zoom = 0, 0,"","", 4
        matrixZoom = fitz.Matrix(zoom,zoom)
        for file in fullDirNames: 
            openPDF = fitz.open(file)
            TotalPagesNumber = openPDF.pageCount
            counterPages = 0
            while counterPages < TotalPagesNumber: 
                loadPdfPage = openPDF.loadPage(counterPages)
                pix = loadPdfPage.getPixmap(matrixZoom)
                filename = inputDirectory + "00 -- OCR\\" + os.path.splitext(dirNamesWithoutExt[counterFiles])[0] + str(counterPages +1) 
                pix.writeImage(filename + ".jpeg","jpeg") 
                pdfOcr = pytesseract.image_to_pdf_or_hocr(filename + ".jpeg", lang = "por", extension = "pdf") 
                with open(filename + ".pdf","w+b") as f:
                    f.write(pdfOcr)
                os.remove(filename + ".jpeg")
                print("Página {} do arquivo {} convertida com sucesso.".format(counterPages +1,dirNamesWithoutExt[counterFiles]))
                counterPages += 1
            counterFiles += 1
        print("Sucesso ao converter arquivos.")

def searchAndExport(): # Pesquisar por palavras dentro de PDF e mover arquivo caso encontrar
    global searchForKeyword,currentKeyword
    def export(): # Mover arquivo
        outputName = groups[counterGroups] + "\\" + splitDateTime[0] + "-" + splitDateTime[1] + " " + pdfFilenames[counterFiles] + " - " + keywords[counterKeywords] + ".pdf" 
        createDirectory(outputDirectory)
        createDirectory(outputDirectory + groups[counterGroups])
        try:
            moveFiles(file, outputDirectory + outputName) 
        except: 
            openPDF.close() 
            moveFiles(file, outputDirectory + outputName) 
        print("A palavra {} foi encontrada no arquivo {} e movida para a pasta {}.".format(keywords[counterKeywords],file,groups[counterGroups]))
    
    def inputData(): # Importar dados através de arquivo CSV
        global groups, keywordsByGroup, keywords
        csvFile = codecs.open("keywords.csv", encoding = "utf-8") 
        reader = csv.reader(csvFile) 
        list_of_rows = list(reader)
        groups = list_of_rows[0]
        keywordsByGroup = list_of_rows[1] 
        keywords = (list_of_rows[2]) 

    def regex(): # Pesquisar por palavras com e sem acento
        global currentKeyword,searchForKeyword
        symbols = ["Ã","Â","Á","À","Ê","É","È","Í","Õ","Ô","Ó","Ò","Ú","Ù","Ç"] 
        symbolsByLetters = [4,3,1,4,2,1] 
        letters = ["A","E","I","O","U","C"] 
        counterLetters = 0 
        counterSymbols = 0 
        newKeyword = currentKeyword 
        while counterLetters < len(letters): 
            counterSymbolsByLetters = 0
            while counterSymbolsByLetters < symbolsByLetters[counterLetters]: 
                newKeyword = re.sub(symbols[counterSymbols],letters[counterLetters],newKeyword)
                counterSymbolsByLetters += 1
                counterSymbols +=1
            counterLetters += 1
        if (newKeyword != currentKeyword): 
            print("Palavra pesquisada: ",newKeyword)            
            searchForKeyword = page.searchFor(newKeyword, hit_max = 16) 

    def remainingFiles(path): # Arquivos não encontrados
        files = os.listdir(inputDirectory + "00 -- OCR\\")
        if files != []:
            createDirectory(outputDirectory + "00 -- NOT FOUNDED\\")
            for file in files:
                try:
                    moveFiles(inputDirectory + "00 -- OCR\\"+ file,outputDirectory + "00 -- NOT FOUNDED\\" + file) 
                except Exception as e:
                    print(e)
                    pass
    inputData()
    listFiles(inputDirectory + "00 -- OCR\\",".pdf")
    files = fullDirNames
    print("Arquivos encontrados para pesquisar:",len(files))
    counterFiles = 0
    if (files == []): 
        print("Não existem arquivos PDF na pasta {}\nInsira os arquivos e tecle algo para continuar...".format(inputDirectory))
        input()
        ocrPdf(inputDirectory)
        listFiles(inputDirectory + "00 -- OCR\\",".pdf")
        files = fullDirNames  
    else:
        print("Pesquisando por palavras...")
    for file in files: 
        print("Pesquisando em arquivo: {}".format(file))
        openPDF = fitz.open(file) 
        page = openPDF.loadPage(0) 
        counterKeywords = 0 
        counterGroups = 0 
        foundBoolean = 0 
        while counterGroups < len(groups) and (foundBoolean==0): 
            print("Total de palavras para pesquisar: {} de {}.".format(counterKeywords+1,len(keywords)))
            print("Pesquisando grupo {} de {}.".format(counterGroups+1,len(groups)))
            while counterKeywords < len(keywords) and (foundBoolean ==0): 
                print("Grupo: ",groups[counterGroups])
                print("Palavras-chave nesse grupo: {}".format(keywordsByGroup[counterGroups]))
                counterKeywordsByGroup = 0 
                while counterKeywordsByGroup < int(keywordsByGroup[counterGroups]): 
                    print("Pesquisando palavra {} de {}.".format(counterKeywordsByGroup+1,int(keywordsByGroup[counterGroups])))
                    currentKeyword = keywords[counterKeywords] 
                    print("Palavra pesquisada: ",currentKeyword)
                    searchForKeyword = page.searchFor(currentKeyword, hit_max = 16) 
                    if (searchForKeyword!= []): 
                        export()
                        foundBoolean = 1
                        break
                    else:
                        regex()
                        if (searchForKeyword!= []):
                            export()
                            foundBoolean = 1
                            break
                        else:
                            print("A palavra {} não foi encontrada neste arquivo.".format(keywords[counterKeywords]))
                    counterKeywords += 1
                    counterKeywordsByGroup +=1
                counterGroups += 1
        counterFiles += 1
    remainingFiles(inputDirectory + "00 -- OCR\\")
    if (files != []): 
        print("Sucesso ao encontrar palavras e exportar arquivos.")

def zipCompress(path): # Compactar arquivos em ZIP
    for root, subdirs, files in os.walk(path):
        for subdir in subdirs:
            if ((subdir != "00 -- NOT FOUNDED") and (subdir != "00 -- ZIP FILES")):
                outputPath = outputDirectory + "00 -- ZIP FILES\\"
                createDirectory(outputPath) 
                zipFilename =  subdir + ".zip" 
                createZipFile = zipfile.ZipFile(zipFilename, "w")
                listFiles(path + subdir + "\\",".pdf")
                for file in fullDirNames:
                    createZipFile.write(file,os.path.basename(file))
                createZipFile.close()
                moveFiles(zipFilename,outputPath + zipFilename) 
                print("Arquivo {} movido de {} para {}".format(zipFilename,os.path.join(path, subdir),outputPath))

def moveFiles(fromPath,toPath): # Mover arquivos
    if not os.path.exists(toPath):    
        shutil.move(fromPath,toPath)
    if os.path.exists(fromPath):
        os.remove(fromPath)

def createDirectory(path): # Criar diretórios se não existirem
    if not os.path.exists(path):
        os.makedirs(path)

def runMain(): # Função que engloba as principais funções
    ocrPdf(inputDirectory)
    searchAndExport()
    zipCompress(outputDirectory)
    print("Processos concluídos com sucesso.")

# Verificar se diretórios existem
desktop = winshell.desktop()
rootDirectory = desktop + "\\Ahand\\"
createDirectory(rootDirectory)

inputDirectory = rootDirectory + "input\\"
outputDirectory = rootDirectory + "output\\"

runMain()