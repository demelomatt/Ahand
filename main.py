# Importar arquivos
from ui_main import Ui_MainWindow
from ui_styles import Style
from ui_functions import UIFunctions
from app_functions import PDFfunctions

# Bibliotecas nativas
import sys, platform, os

# Bibliotecas externas
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent, SIGNAL)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

class MainWindow(QMainWindow):

    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.worker = PDFfunctions()

        self.setAcceptDrops(True)
    
        ########################################################################
        ## START - WINDOW ATTRIBUTES
        ########################################################################

        ## REMOVE ==> STANDARD TITLE BAR
        UIFunctions.removeTitleBar(True)
        ## ==> END ##

        ## SET ==> WINDOW TITLE
        self.setWindowTitle('Ahand')
        UIFunctions.labelTitle(self, 'Ahand')
        UIFunctions.labelDescription(self, 'Giving you a hand for automation.')
        ## ==> END ##

        ## REMOVE ==> STANDARD TITLE BAR
        startSize = QSize(1000, 720)
        self.resize(startSize)
        self.setMinimumSize(startSize)
        # UIFunctions.enableMaximumSize(self, 500, 720)
        ## ==> END ##

        ## ==> CREATE MENUS
        ########################################################################

        ## ==> TOGGLE MENU SIZE
        self.ui.pushButton_toggle_menu.clicked.connect(lambda: UIFunctions.toggleMenu(self, 200, True))
        ## ==> END ##

        ## ==> ADD CUSTOM MENUS
        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.addNewMenu(self, "Combinar", "pushButton_merge", "url(:/24x24/icons/24x24/merge.png)", True)
        UIFunctions.addNewMenu(self, "Extrair", "pushButton_extract", "url(:/24x24/icons/24x24/split.png)", True)
        UIFunctions.addNewMenu(self, "Escanear", "pushButton_scan", "url(:/24x24/icons/24x24/scanner.png)", True)
        UIFunctions.addNewMenu(self, "Classificar", "pushButton_search", "url(:/24x24/icons/24x24/search.png)", True)
        UIFunctions.addNewMenu(self, "Compactar", "pushButton_zip", "url(:/24x24/icons/24x24/zip.png)", True)
        UIFunctions.addNewMenu(self, "Créditos", "pushButton_credits", "url(:/24x24/icons/24x24/info.png)",isTopMenu = False)
        UIFunctions.addNewMenu(self, "Ajuda", "pushButton_help", "url(:/24x24/icons/24x24/question.png)",isTopMenu = False)
        ## ==> END ##

        # START MENU => SELECTION
        UIFunctions.selectStandardMenu(self, "pushButton_merge")
        ## ==> END ##

        ## ==> START PAGE
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_merge)
        ## ==> END ##

        ## ==> MOVE WINDOW / MAXIMIZE / RESTORE
        ########################################################################
        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if UIFunctions.returStatus() == 1:
                UIFunctions.maximize_restore(self)

            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # WIDGET TO MOVE
        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow
        ## ==> END ##

        ## ==> LOAD DEFINITIONS
        ########################################################################
        UIFunctions.uiDefinitions(self)
        ## ==> END ##

        ########################################################################
        ## END - WINDOW ATTRIBUTES
        ############################## ---/--/--- ##############################

        ## ==> LOAD DEFINITIONS
        ########################################################################
        ## ==> END ##

        # FIRST EXECUTION
        UIFunctions.deleteTab(self)
        UIFunctions.deleteTab(self)

        self.ui.checkBox_onlyPages_search.setChecked(True)
        self.ui.checkBox_ignoreSpecialChar_search.setChecked(True)
        self.ui.checkBox_ignorePontuation_search.setChecked(True)
        
        self.ui.checkBox_ignoreSpaces_search.setChecked(True)
        self.ui.checkBox_ignoreFirstPage_search.setChecked(True)

             # Exclusive checkbox
        checkboxGroup = QButtonGroup(self)
        checkboxGroup.addButton(self.ui.checkBox_extract)
        checkboxGroup.addButton(self.ui.checkBox_split)
        self.ui.checkBox_split.setChecked(True)

        
        ## ==> END ##

        ########################################################################
        #                                                                      #
        ## START -------------- WIDGETS FUNCTIONS/PARAMETERS ---------------- ##
        #                                                                      #
        
        # LABEL
        self.ui.label_feedback.clear()

        # SIGNALS
        self.ui.pushButton_deleteTable_search.clicked.connect(lambda: UIFunctions.deleteTab(self)) # Deletar tabela
        self.ui.pushButton_addTable_search.clicked.connect(lambda: PDFfunctions.buttonSelectCsvFiles(self)) # Adicionar tabela

            # merge function
        self.ui.pushButton_selectFiles_merge.clicked.connect(lambda: UIFunctions.buttonSelectPdfFiles(self))
        self.ui.pushButton_outputPath_merge.clicked.connect(lambda: UIFunctions.buttonSelectPath(self,self.ui.lineEdit_outputPath_merge,"Abrir diretório de saída"))
        self.ui.pushButton_run_merge.clicked.connect(self.processData)
        
            # ocr function
        self.ui.pushButton_selectFiles_ocr.clicked.connect(lambda: UIFunctions.buttonSelectPdfFiles(self))
        self.ui.pushButton_outputPath_ocr.clicked.connect(lambda: UIFunctions.buttonSelectPath(self,self.ui.lineEdit_outputPath_ocr,"Abrir diretório de saída"))
        self.ui.pushButton_run_ocr.clicked.connect(self.processData)
        
            # zip function
        self.ui.pushButton_selectRootDirectory_zip.clicked.connect(lambda: UIFunctions.buttonSelectPath(self,self.ui.lineEdit_rootDirectory_zip,"Abrir diretório raíz"))
        self.ui.pushButton_outputPath_zip.clicked.connect(lambda: UIFunctions.buttonSelectPath(self,self.ui.lineEdit_outputPath_zip,"Abrir diretório de saída"))
        self.ui.pushButton_run_zip.clicked.connect(self.processData)
        
            # search patterns function
        self.ui.pushButton_selectFiles_search.clicked.connect(lambda: UIFunctions.buttonSelectPdfFiles(self))
        self.ui.pushButton_outputPath_search.clicked.connect(lambda: UIFunctions.buttonSelectPath(self,self.ui.lineEdit_outputPath_search,"Abrir diretório de saída"))
        self.ui.pushButton_run_search.clicked.connect(self.processData)

            # extract function
        self.ui.pushButton_selectFiles_extract.clicked.connect(lambda: UIFunctions.buttonSelectPdfFiles(self))
        self.ui.pushButton_outputPath_extract.clicked.connect(lambda: UIFunctions.buttonSelectPath(self,self.ui.lineEdit_outputPath_extract,"Abrir diretório de saída"))
        self.ui.pushButton_run_extract.clicked.connect(self.processData)

        # Feedback
        self.connect(self.worker, SIGNAL("feedback(QString)"), self.setFeedbackText)
        self.connect(self.worker, SIGNAL("dialog(QString)"), self.showDialog)

        ## ==> END ##

        ########################################################################
        
        ## ==> QTableWidget PARAMETERS
        ########################################################################

        ########################################################################
        #                                                                      #
        ## END --------------- WIDGETS FUNCTIONS/PARAMETERS ----------------- ##
        #                                                                      #
        ############################## ---/--/--- ##############################

    
    def setFeedbackText(self,text):
        self.ui.label_feedback.setText(text)

    def processData(self):
        self.worker
        PDFfunctions.sender = self.sender().objectName()
        self.worker.start()

    def showDialog(self,text,title="Erro ao executar aplicação.",icon=QMessageBox.Critical,buttons=QMessageBox.Ok):
        # Qwidget para abrir diálogo de seleção de arquivos e armazenar o caminho
        msgBox = QMessageBox()
        msgBox.setIcon(icon)
        msgBox.setText(text)
        msgBox.setWindowTitle(title)
        msgBox.setStandardButtons(buttons)
        value = msgBox.exec()
        if value == buttons:
            return value

    ########################################################################
    ## MENUS ==> DYNAMIC MENUS FUNCTIONS
    ########################################################################

    def Button(self):
        # GET BT CLICKED
        pushButton_Widget = self.sender()

        # PAGE MERGE
        if pushButton_Widget.objectName() == "pushButton_merge":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_merge)
            UIFunctions.resetStyle(self, "pushButton_merge")
            UIFunctions.labelPage(self, "Combinar")
            pushButton_Widget.setStyleSheet(UIFunctions.selectMenu(pushButton_Widget.styleSheet()))
            UIFunctions.inputPaths = []

        # PAGE EXTRACT
        if pushButton_Widget.objectName() == "pushButton_extract":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_extract)
            UIFunctions.resetStyle(self, "pushButton_extract")
            UIFunctions.labelPage(self, "Extrair")
            pushButton_Widget.setStyleSheet(UIFunctions.selectMenu(pushButton_Widget.styleSheet()))
            UIFunctions.inputPaths = []

        # PAGE SCAN
        if pushButton_Widget.objectName() == "pushButton_scan":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_ocr)
            UIFunctions.resetStyle(self, "pushButton_scan")
            UIFunctions.labelPage(self, "Escanear")
            pushButton_Widget.setStyleSheet(UIFunctions.selectMenu(pushButton_Widget.styleSheet()))
            UIFunctions.inputPaths = []

        # PAGE ZIP
        if pushButton_Widget.objectName() == "pushButton_zip":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_zip)
            UIFunctions.resetStyle(self, "pushButton_zip")
            UIFunctions.labelPage(self, "Compactar")
            pushButton_Widget.setStyleSheet(UIFunctions.selectMenu(pushButton_Widget.styleSheet()))
            UIFunctions.inputPaths = []

        # PAGE  SEARCH PATTERNS
        if pushButton_Widget.objectName() == "pushButton_search":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_search)
            UIFunctions.resetStyle(self, "pushButton_search")
            UIFunctions.labelPage(self, "Classificar")
            pushButton_Widget.setStyleSheet(UIFunctions.selectMenu(pushButton_Widget.styleSheet()))
            UIFunctions.inputPaths = []

        # PAGE CREDITS
        if pushButton_Widget.objectName() == "pushButton_credits":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_credits)
            UIFunctions.resetStyle(self, "pushButton_credits")
            UIFunctions.labelPage(self, "Créditos")
            pushButton_Widget.setStyleSheet(UIFunctions.selectMenu(pushButton_Widget.styleSheet()))
            UIFunctions.inputPaths = []

        # PAGE  SEARCH HELP
        if pushButton_Widget.objectName() == "pushButton_help":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_help)
            UIFunctions.resetStyle(self, "pushButton_help")
            UIFunctions.labelPage(self, "Ajuda")
            pushButton_Widget.setStyleSheet(UIFunctions.selectMenu(pushButton_Widget.styleSheet()))
            UIFunctions.inputPaths = []
    ## ==> END ##

    ########################################################################
    ## START ==> APP EVENTS
    ########################################################################

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            pdfPaths = []
            pageID = self.ui.stackedWidget.currentIndex()
            for url in event.mimeData().urls():
                path = str(url.toLocalFile())
                if os.path.isfile(path) and (path.endswith(".pdf") or path.endswith(".PDF")):
                    event.acceptProposedAction()
                    pdfPaths.append(path)

                elif os.path.isfile(path) and ((path.endswith(".csv") or path.endswith(".CSV")) and pageID == 3):
                    event.acceptProposedAction()
                    UIFunctions.csvPaths = [path]
                    PDFfunctions.importFromCSV(self)

            if pdfPaths != []:
                UIFunctions.dropPdf(self,pdfPaths)
    
    ## EVENT ==> MOUSE CLICK
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
    ## ==> END ##
         
    ########################################################################
    ## END ==> APP EVENTS
    ############################## ---/--/--- ##############################

if __name__ == "__main__":
    app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())