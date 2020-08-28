# Importar arquivos
from ui_main import Ui_MainWindow
from ui_styles import Style
from ui_functions import UIFunctions
from connect_functions import *

# Bibliotecas nativas
import sys, platform

# Bibliotecas externas
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    
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
        self.ui.pushButton_toggle_menu.clicked.connect(lambda: UIFunctions.toggleMenu(self, 220, True))
        ## ==> END ##

        ## ==> ADD CUSTOM MENUS
        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.addNewMenu(self, "Mesclar", "pushButton_merge", "url(:/20x20/icons/20x20/merge.png)", True)
        UIFunctions.addNewMenu(self, "Extrair", "pushButton_extract", "url(:/20x20/icons/20x20/split.png)", True)
        UIFunctions.addNewMenu(self, "Escanear", "pushButton_scan", "url(:/20x20/icons/20x20/scanner.png)", True)
        UIFunctions.addNewMenu(self, "Compactar", "pushButton_zip", "url(:/20x20/icons/20x20/zip.png)", True)
        UIFunctions.addNewMenu(self, "Procurar padrões", "pushButton_search", "url(:/20x20/icons/20x20/search.png)", True)
        UIFunctions.addNewMenu(self, "Créditos", "pushButton_credits", "url(:/20x20/icons/20x20/info.png)",isTopMenu = False)
        UIFunctions.addNewMenu(self, "Ajuda", "pushButton_help", "url(:/20x20/icons/20x20/question.png)",isTopMenu = False)
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

        # PRIMEIRA EXECUÇÃO
        UIFunctions.deleteTab(self)
        ## ==> END ##

        ########################################################################
        #                                                                      #
        ## START -------------- WIDGETS FUNCTIONS/PARAMETERS ---------------- ##
        #                                                                      #
        
        # LABEL
        self.ui.label_feedback.clear()

        #BUTTONS

        self.ui.pushButton_deleteTable_search.clicked.connect(lambda: UIFunctions.deleteTab(self)) # Deletar tabela
        self.ui.pushButton_addTable_search.clicked.connect(lambda: Connect.buttonRun(self,'PDFfunctions.importFromCSV(self)')) # Adicionar tabela

        # Função merge
        self.ui.pushButton_selectFiles_merge.clicked.connect(lambda: Connect.buttonSelectPdfFiles(self,self.ui.lineEdit_filename_merge,self.ui.label_files_selected_merge))
        self.ui.pushButton_outputPath_merge.clicked.connect(lambda: Connect.buttonSelectPath(self,self.ui.lineEdit_outputPath_merge,"Abrir diretório de saída"))
        self.ui.pushButton_run_merge.clicked.connect(lambda: Connect.buttonRun(self,'PDFfunctions.merge(self,PDFfunctions.inputPaths,self.ui.lineEdit_outputPath_merge.text(),self.ui.lineEdit_filename_merge.text())'))
        
        # Função ocr
        self.ui.pushButton_selectFiles_ocr.clicked.connect(lambda: Connect.buttonSelectPdfFiles(self,0,self.ui.label_files_selected_ocr))
        self.ui.pushButton_outputPath_ocr.clicked.connect(lambda: Connect.buttonSelectPath(self,self.ui.lineEdit_outputPath_ocr,"Abrir diretório de saída"))
        self.ui.pushButton_run_ocr.clicked.connect(lambda: Connect.buttonRun(self,'PDFfunctions.ocrPDF(self,PDFfunctions.inputPaths,self.ui.lineEdit_outputPath_ocr.text(),self.ui.lineEdit_filename_ocr.text(),self.ui.lineEdit_intDpi_ocr.text())'))
        
        # Função zip
        self.ui.pushButton_selectRootDirectory_zip.clicked.connect(lambda: Connect.buttonSelectPath(self,self.ui.lineEdit_rootDirectory_zip,"Abrir diretório raíz"))
        self.ui.pushButton_outputPath_zip.clicked.connect(lambda: Connect.buttonSelectPath(self,self.ui.lineEdit_outputPath_zip,"Abrir diretório de saída"))
        self.ui.pushButton_run_zip.clicked.connect(lambda: Connect.buttonRun(self,'PDFfunctions.zipCompress(self,self.ui.lineEdit_rootDirectory_zip.text(),self.ui.lineEdit_outputPath_zip.text(),self.ui.lineEdit_filename_zip.text())'))
        
        # Função search patterns
    
        self.ui.pushButton_selectFiles_search.clicked.connect(lambda: Connect.buttonSelectPdfFiles(self,0,self.ui.label_files_selected_search))
        self.ui.pushButton_outputPath_search.clicked.connect(lambda: Connect.buttonSelectPath(self,self.ui.lineEdit_outputPath_search,"Abrir diretório de saída"))
        self.ui.pushButton_run_search.clicked.connect(lambda: Connect.buttonRun(self,'PDFfunctions.searchPattern(self,PDFfunctions.inputPaths,self.ui.lineEdit_outputPath_search.text(),self.ui.lineEdit_filename_search.text())'))

        ########################################################################
        
        ## ==> QTableWidget PARAMETERS
        ########################################################################

        ########################################################################
        #                                                                      #
        ## END --------------- WIDGETS FUNCTIONS/PARAMETERS ----------------- ##
        #                                                                      #
        ############################## ---/--/--- ##############################

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
            UIFunctions.labelPage(self, "Mesclar")
            pushButton_Widget.setStyleSheet(UIFunctions.selectMenu(pushButton_Widget.styleSheet()))

        # PAGE EXTRACT
        if pushButton_Widget.objectName() == "pushButton_extract":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_extract)
            UIFunctions.resetStyle(self, "pushButton_extract")
            UIFunctions.labelPage(self, "Extrair")
            pushButton_Widget.setStyleSheet(UIFunctions.selectMenu(pushButton_Widget.styleSheet()))

        # PAGE SCAN
        if pushButton_Widget.objectName() == "pushButton_scan":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_ocr)
            UIFunctions.resetStyle(self, "pushButton_scan")
            UIFunctions.labelPage(self, "Escanear")
            pushButton_Widget.setStyleSheet(UIFunctions.selectMenu(pushButton_Widget.styleSheet()))

        # PAGE ZIP
        if pushButton_Widget.objectName() == "pushButton_zip":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_zip)
            UIFunctions.resetStyle(self, "pushButton_zip")
            UIFunctions.labelPage(self, "Compactar")
            pushButton_Widget.setStyleSheet(UIFunctions.selectMenu(pushButton_Widget.styleSheet()))

        # PAGE  SEARCH PATTERNS
        if pushButton_Widget.objectName() == "pushButton_search":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_search)
            UIFunctions.resetStyle(self, "pushButton_search")
            UIFunctions.labelPage(self, "Procurar padrões")
            pushButton_Widget.setStyleSheet(UIFunctions.selectMenu(pushButton_Widget.styleSheet()))

        # PAGE CREDITS
        if pushButton_Widget.objectName() == "pushButton_credits":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_credits)
            UIFunctions.resetStyle(self, "pushButton_credits")
            UIFunctions.labelPage(self, "Créditos")
            pushButton_Widget.setStyleSheet(UIFunctions.selectMenu(pushButton_Widget.styleSheet()))

        # PAGE  SEARCH HELP
        if pushButton_Widget.objectName() == "pushButton_help":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_help)
            UIFunctions.resetStyle(self, "pushButton_help")
            UIFunctions.labelPage(self, "Ajuda")
            pushButton_Widget.setStyleSheet(UIFunctions.selectMenu(pushButton_Widget.styleSheet()))
    ## ==> END ##

    ########################################################################
    ## START ==> APP EVENTS
    ########################################################################

    ## EVENT ==> MOUSE DOUBLE CLICK
    ########################################################################
    def eventFilter(self, watched, event):
        if watched == self.le and event.type() == QtCore.QEvent.MouseButtonDblClick:
            print("pos: ", event.pos())
    ## ==> END ##

    ## EVENT ==> MOUSE CLICK
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
        if event.buttons() == Qt.MidButton:
            print('Mouse click: MIDDLE BUTTON')
    ## ==> END ##

    ## EVENT ==> KEY PRESSED
    ########################################################################
    def keyPressEvent(self, event):
        print('Key: ' + str(event.key()) + ' | Text Press: ' + str(event.text()))
    ## ==> END ##

    ## EVENT ==> RESIZE EVENT
    ########################################################################
    def resizeEvent(self, event):
        self.resizeFunction()
        return super(MainWindow, self).resizeEvent(event)

    def resizeFunction(self):
        print('Height: ' + str(self.height()) + ' | Width: ' + str(self.width()))
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
