No outro arquivo:

import sys
from ui_main import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

class MainWindow(QMainWindow):

    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.ui.setupUi(self)
        self.ui = Ui_MainWindow()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())