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
        #self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.addNewMenu(self, "Exportar para tabela", "pushButton_export", "url(:/24x24/icons/24x24/tab.png)", True)

        ## ==> END ##

        # START MENU => SELECTION
        UIFunctions.selectStandardMenu(self, "pushButton_export")
        ## ==> END ##

        ## ==> START PAGE
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_exportToTable)

        
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
        self.ui.tableWidget_2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.ui.tableWidget_2.resizeColumnsToContents()
        UIFunctions.addRow(self,self.ui.tableWidget_2)

        ########################################################################
        #                                                                      #
        ## START -------------- WIDGETS FUNCTIONS/PARAMETERS ---------------- ##
        #                                                                      #
        
        # LABEL
        self.ui.label_feedback.clear()

            # merge function
        self.ui.pushButton_selectFiles_export.clicked.connect(lambda: UIFunctions.buttonSelectPdfFiles(self))
        self.ui.pushButton_outputPath_export.clicked.connect(lambda: UIFunctions.buttonSelectPath(self,self.ui.lineEdit_outputPath_export,"Abrir diretório de saída"))
        self.ui.pushButton_run_export.clicked.connect(self.processData)

        self.ui.pushButton_add_column_export.clicked.connect(lambda:UIFunctions.addColumn(self,self.ui.tableWidget_2))
        self.ui.pushButton_remove_column_export.clicked.connect(lambda:UIFunctions.removeColumn(self,self.ui.tableWidget_2))

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
        if pushButton_Widget.objectName() == "pushButton_test":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_merge)
            UIFunctions.resetStyle(self, "pushButton_test")
            UIFunctions.labelPage(self, "Test")
            pushButton_Widget.setStyleSheet(UIFunctions.selectMenu(pushButton_Widget.styleSheet()))


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