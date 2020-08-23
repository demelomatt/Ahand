from app_functions import PDFfunctions
from ui_functions import UIFunctions
from ui_main import Ui_MainWindow

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import os
import time

class Connect(Ui_MainWindow):

## ==> BUTTONS FUNCTIONS

    def buttonSelectPdfFiles(self,lineEdit,label):
        PDFfunctions.inputPaths = QFileDialog.getOpenFileNames(self, 'Selecionar arquivos pdf', QtCore.QDir.currentPath(), 'pdf files (*.pdf)',options=QFileDialog.DontUseNativeDialog)[0]
        label.setText("{} arquivos selecionados.".format(len(PDFfunctions.inputPaths)))
        try:
            splitext = os.path.splitext(PDFfunctions.inputPaths[0])[0]
            basename = os.path.basename(splitext) # Nome do arquivo original sem a extensão e diretório.
            lineEdit.setText(basename)
        except:
            pass


    def buttonSelectOutputPath(self,lineEditOutput):
        lineEditOutput.setText(QFileDialog.getExistingDirectory(self,'Selecionar pasta de saída',QtCore.QDir.currentPath(),QFileDialog.DontUseNativeDialog))

    def buttonRun(self,appFunction):
        eval(appFunction)
        ui = Ui_MainWindow()
        ui.label_feedback.clear()
        return