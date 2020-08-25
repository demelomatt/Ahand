from app_functions import PDFfunctions
from ui_functions import UIFunctions
from ui_main import Ui_MainWindow

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import os, time, winsound

class Connect(Ui_MainWindow):

## ==> BUTTONS FUNCTIONS

    def buttonSelectPdfFiles(self,lineEdit,label):
        # Selecionar arquivos PDF e salvar caminho
        # lineEdit recebe o QWidget lineEdit para armazenar o nome do arquivo sem a extensão
        # label recebe o QWidget para armazenar a quantidade de arquivos selecionados

        # Abre arquivos e salva caminho 
        PDFfunctions.inputPaths = QFileDialog.getOpenFileNames(self, 'Selecionar arquivos pdf', QtCore.QDir.currentPath(), 'pdf files (*.pdf)',options=QFileDialog.DontUseNativeDialog)[0]
        # Setar texto
        label.setText("{} arquivos selecionados.".format(len(PDFfunctions.inputPaths)))
        try:
            splitext = os.path.splitext(PDFfunctions.inputPaths[0])[0]
            basename = os.path.basename(splitext) # Nome do arquivo original sem a extensão e diretório.
            lineEdit.setText(basename)
        except:
            pass

    def buttonSelectOutputPath(self,lineEditOutput):
        # Selecionar pasta de saída e salvar caminho
        # lineEditOutput recebe o QWidget lineEdit para armazenar o caminho do diretório

        lineEditOutput.setText(QFileDialog.getExistingDirectory(self,'Selecionar pasta de saída',QtCore.QDir.currentPath(),QFileDialog.DontUseNativeDialog))

    def buttonRun(self,appFunction):
        # Executar uma função da classe PDFFunctions
        # Função necessária pois não é possível importar essa classe no arquivo principal

        eval(appFunction)
        return