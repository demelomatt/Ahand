# Importar arquivos
from ui_main import Ui_MainWindow
from ui_styles import Style

# Bibliotecas nativas
import os

# Bibliotecas externas
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

## ==> GLOBALS
GLOBAL_STATE = 0
GLOBAL_TITLE_BAR = True

## ==> COUT INITIAL MENU
count = 1

# Classes
class UIFunctions(Ui_MainWindow):

    ## ==> GLOBALS
    GLOBAL_STATE = 0
    GLOBAL_TITLE_BAR = True

    csvPaths = []
    inputPdfPaths_ocr = []
    inputPdfPaths_merge = []
    inputPdfPaths_extract = []
    inputPdfPaths_zip = []
    inputPdfPaths_search = []

    ########################################################################
    ## START - GUI FUNCTIONS
    ########################################################################

    ## ==> MAXIMIZE/RESTORE
    ########################################################################
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == 0:
            self.showMaximized()
            GLOBAL_STATE = 1
            self.ui.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            self.ui.pushButton_maximize_restore.setToolTip("Restore")
            self.ui.pushButton_maximize_restore.setIcon(QtGui.QIcon(u":/16x16/icons/16x16/cil-window-restore.png"))
            self.ui.frame_top_btns.setStyleSheet("background-color: rgb(27, 29, 35)")
            self.ui.frame_size_grip.hide()
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.horizontalLayout.setContentsMargins(10, 10, 10, 10)
            self.ui.pushButton_maximize_restore.setToolTip("Maximize")
            self.ui.pushButton_maximize_restore.setIcon(QtGui.QIcon(u":/16x16/icons/16x16/cil-window-maximize.png"))
            self.ui.frame_top_btns.setStyleSheet("background-color: rgba(27, 29, 35, 200)")
            self.ui.frame_size_grip.show()

    ## ==> RETURN STATUS
    def returStatus():
        return GLOBAL_STATE

    ## ==> SET STATUS
    def setStatus(status):
        global GLOBAL_STATE
        GLOBAL_STATE = status

    ## ==> ENABLE MAXIMUM SIZE
    ########################################################################
    def enableMaximumSize(self, width, height):
        if width != '' and height != '':
            self.setMaximumSize(QSize(width, height))
            self.ui.frame_size_grip.hide()
            self.ui.pushButton_maximize_restore.hide()

    ## ==> TOGGLE MENU
    ########################################################################
    def toggleMenu(self, maxWidth, enable):
        if enable:
            # GET WIDTH
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 80

            # SET MAX WIDTH
            if width == 80:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(300)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    ## ==> SET TITLE BAR
    ########################################################################
    def removeTitleBar(status):
        global GLOBAL_TITLE_BAR
        GLOBAL_TITLE_BAR = status

    ## ==> HEADER TEXTS
    ########################################################################
    # LABEL TITLE
    def labelTitle(self, text):
        self.ui.label_title_bar_top.setText(text)

    # LABEL DESCRIPTION
    def labelDescription(self, text):
        self.ui.label_top_info_1.setText(text)

    ## ==> DYNAMIC MENUS
    ########################################################################
    def addNewMenu(self, name, objName, icon, isTopMenu):
        font = QFont()
        font.setFamily(u"Segoe UI")
        button = QPushButton(str(count),self)
        button.setObjectName(objName)
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(button.sizePolicy().hasHeightForWidth())
        button.setSizePolicy(sizePolicy3)
        button.setMinimumSize(QSize(0, 80))
        button.setLayoutDirection(Qt.LeftToRight)
        button.setFont(font)
        button.setStyleSheet(Style.style_bt_standard.replace('ICON_REPLACE', icon))
        button.setText(name)
        button.setToolTip(name)
        button.clicked.connect(self.Button)

        if isTopMenu:
            self.ui.layout_menus.addWidget(button)

        else:
            self.ui.layout_menu_bottom.addWidget(button)
            self.ui.layout_menu_bottom.setAlignment(Qt.AlignBottom|Qt.AlignVCenter)
        


    ## ==> SELECT/DESELECT MENU
    ########################################################################
    ## ==> SELECT
    def selectMenu(getStyle):
        select = getStyle + ("QPushButton { border-right: 7px solid rgb(44, 49, 60); }")
        return select

    ## ==> DESELECT
    def deselectMenu(getStyle):
        deselect = getStyle.replace("QPushButton { border-right: 7px solid rgb(44, 49, 60); }", "")
        return deselect

    ## ==> START SELECTION
    def selectStandardMenu(self, widget):
        for w in self.ui.frame_left_menu.findChildren(QPushButton):
            if w.objectName() == widget:
                w.setStyleSheet(UIFunctions.selectMenu(w.styleSheet()))

    ## ==> RESET SELECTION
    def resetStyle(self, widget):
        for w in self.ui.frame_left_menu.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(UIFunctions.deselectMenu(w.styleSheet()))

    ## ==> CHANGE PAGE LABEL TEXT
    def labelPage(self, text):
        newText = '| ' + text.upper()
        self.ui.label_top_info_2.setText(newText)

    ########################################################################
    ## END - GUI FUNCTIONS
    ########################################################################

    ########################################################################
    ## START - GUI DEFINITIONS
    ########################################################################

    ## ==> UI DEFINITIONS
    ########################################################################
    def uiDefinitions(self):
        def dobleClickMaximizeRestore(event):
            # IF DOUBLE CLICK CHANGE STATUS
            if event.type() == QtCore.QEvent.MouseButtonDblClick:
                QtCore.QTimer.singleShot(250, lambda: UIFunctions.maximize_restore(self))

        ## REMOVE ==> STANDARD TITLE BAR
        if GLOBAL_TITLE_BAR:
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
            self.ui.frame_label_top_btns.mouseDoubleClickEvent = dobleClickMaximizeRestore
        else:
            self.ui.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            self.ui.frame_label_top_btns.setContentsMargins(8, 0, 0, 5)
            self.ui.frame_label_top_btns.setMinimumHeight(42)
            self.ui.frame_icon_top_bar.hide()
            self.ui.frame_btns_right.hide()
            self.ui.frame_size_grip.hide()

        ## SHOW ==> DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.frame_main.setGraphicsEffect(self.shadow)

        ## ==> RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.frame_size_grip)
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

        ### ==> MINIMIZE
        self.ui.pushButton_minimize.clicked.connect(lambda: self.showMinimized())

        ## ==> MAXIMIZE/RESTORE
        self.ui.pushButton_maximize_restore.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        ## SHOW ==> CLOSE APPLICATION
        self.ui.pushButton_close.clicked.connect(lambda: self.close())
    
    def deleteTab(self):
        # Deletar tabela
        currentTabIndex = self.ui.tabWidget.currentIndex()
        self.ui.tabWidget.removeTab(currentTabIndex)
        if currentTabIndex >= 0:
            UIFunctions.label_drop_csv(self)

    def buttonSelectPath(self,lineEditOutput,msg):
        # Selecionar pasta de saída e salvar caminho
        # lineEditOutput recebe o QWidget lineEdit para armazenar o caminho do diretório
        # msg recebe a mensagem a ser exibida ao abrir diálogo

        lineEditOutput.setText(QFileDialog.getExistingDirectory(self,msg,QtCore.QDir.currentPath(),QFileDialog.DontUseNativeDialog))

    def buttonSelectPdfFiles(self):
        # Selecionar arquivos PDF e salvar caminho
        # lineEdit recebe o QWidget lineEdit para armazenar o nome do arquivo sem a extensão
        # label recebe o QWidget para armazenar a quantidade de arquivos selecionados

        # Abre arquivos e salva caminho
        paths = QFileDialog.getOpenFileNames(self, 'Selecionar arquivos pdf', QtCore.QDir.currentPath(), 'pdf files (*.pdf)',options=QFileDialog.DontUseNativeDialog)[0]
        if paths != []:
            UIFunctions.dropPdf(self,paths)

    def dropPdf(self,paths):
        pageID = self.ui.stackedWidget.currentIndex()
        
        if pageID == 0:
            label = self.ui.label_drop_merge
            UIFunctions.inputPdfPaths_merge = paths
            lineEdit_output = self.ui.lineEdit_outputPath_merge
            lineEdit_filename = self.ui.lineEdit_filename_merge

        elif pageID == 1:
            label = self.ui.label_drop_extract
            UIFunctions.inputPdfPaths_extract = paths
            lineEdit_output = self.ui.lineEdit_outputPath_extract
            lineEdit_filename = self.ui.lineEdit_filename_extract

        elif pageID == 2:
            label = self.ui.label_drop_ocr
            UIFunctions.inputPdfPaths_ocr = paths
            lineEdit_output = self.ui.lineEdit_outputPath_ocr
            lineEdit_filename = self.ui.lineEdit_filename_ocr
        
        elif pageID == 3:
            label = self.ui.label_drop_search
            UIFunctions.inputPdfPaths_search = paths
            lineEdit_output = self.ui.lineEdit_outputPath_search
            lineEdit_filename = self.ui.lineEdit_filename_search
        else:
            return

        splitext = os.path.splitext(paths[0])[0]
        basename = os.path.basename(splitext) # Nome do arquivo original sem a extensão e diretório.

        if not pageID:
            lineEdit_filename.setText(basename)


        lineEdit_output.setText(os.path.dirname(paths[0]))

        listPdfFiles = []
        for path in paths:
            listPdfFiles.append(os.path.basename(path))
        stringPdfFiles = ",".join(listPdfFiles)
        stringPdfFiles = stringPdfFiles.replace(",","\n")

        label.setStyleSheet(u"border-radius: 7px;border: 2px dashed rgb(112, 117, 125)")
        font7 = QFont()
        font7.setFamily(u"Segoe UI")
        font7.setPointSize(10)
        font7.setBold(True)
        font7.setWeight(75)

        font8 = QFont()
        font8.setFamily(u"Segoe UI")
        font8.setPointSize(12)
        font8.setBold(True)
        font8.setWeight(75)

        # Setar texto
        lenFilesName  = "{} arquivo(s) selecionado(s).".format(len(paths))

        if pageID == 3:
            label.setFont(font8)
            label.setText(lenFilesName)

        else:
            label.setFont(font7)
            label.setText(lenFilesName + "\n\n" + stringPdfFiles)

    def label_drop_csv(self):
        if not self.ui.tabWidget.count():
            
            self.ui.label_drop_csv = QLabel(self.ui.frame_tab)
            self.ui.label_drop_csv.setObjectName(u"label_drop_CSV")
            font8 = QFont()
            font8.setFamily(u"Segoe UI")
            font8.setPointSize(12)
            font8.setBold(True)
            font8.setWeight(75)
            self.ui.label_drop_csv.setFont(font8)
            self.ui.label_drop_csv.setStyleSheet(u"border: 4px dashed rgb(112, 117, 125);\n""color: rgb(112, 117, 125);")
            
            self.ui.label_drop_csv.setMinimumSize(QSize(0, 80))
            self.ui.label_drop_csv.setMaximumSize(QSize(9999, 400))

            self.ui.label_drop_csv.setText("ARRASTE E SOLTE ARQUIVOS CSV AQUI")
            self.ui.verticalLayout_7.addWidget(self.ui.label_drop_csv,Qt.AlignCenter)
            self.ui.label_drop_csv.setAlignment(Qt.AlignCenter)