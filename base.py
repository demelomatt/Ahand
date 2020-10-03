
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import *
from io import StringIO

pdfPath = "test.pdf"
pdfObjFather = 'LTTextBoxHorizontal'
pdfObjChild = 'LTTextLineHorizontal'
pdfObjGrandchild = 'LTText'

def writeTxt(element,strElement):
    try:
        getText = element.get_text()
        txtFile = strElement + ".txt"
        f= open(txtFile,"a+",encoding='UTF-8')
        f.write(getText)
        print(getText)
    except Exception as e:
        print(e)
        pass
    return 0

document = open(pdfPath, 'rb')
#Create resource manager
rsrcmgr = PDFResourceManager()
# Set parameters for analysis.
laparams = LAParams(line_overlap=0.5, char_margin=2.0, line_margin=0.5,
word_margin=0.1, boxes_flow=0.5, detect_vertical=False,
all_texts=False)
# Create a PDF page aggregator object.
device = PDFPageAggregator(rsrcmgr, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)
for page in PDFPage.get_pages(document):
    interpreter.process_page(page)
    # receive the LTPage object for the page.
    layout = device.get_result()
    for father in layout:
        if isinstance(father, eval(pdfObjFather)):
            #writeTxt(father,pdfObjFather)
            for child in father:
                if isinstance(child, eval(pdfObjChild)):
                    #writeTxt(child,pdfObjChild)
                    for grandchild in child:
                        if isinstance(grandchild, eval(pdfObjGrandchild)):
                            writeTxt(grandchild,pdfObjGrandchild)