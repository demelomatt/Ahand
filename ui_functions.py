import re
## ==> GUI FILE
from main import *

## ==> APP FUNCTIONS
from app_functions import *

## ==> GLOBALS
GLOBAL_STATE = 0
GLOBAL_TITLE_BAR = True

## ==> COUT INITIAL MENU
count = 1

class UIFunctions(MainWindow):
    
    ## ==> GLOBALS
    GLOBAL_STATE = 0
    GLOBAL_TITLE_BAR = True
    tableWidgetIndex = []
    deletedTables = []

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
            standard = 70

            # SET MAX WIDTH
            if width == 70:
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
        button.setMinimumSize(QSize(0, 70))
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

    ## ==> TABLE FUNCTIONS
        ########################################################################

    def addTab(self):
        # Adicionar nova tabela ao tabWidget

        currentTabIndex = self.ui.tabWidget.currentIndex() + 1
        if UIFunctions.deletedTables != []:
            # Se existem tabelas deletadas
            totalTables = min(UIFunctions.deletedTables) # Pegar o índice mínimo
            UIFunctions.deletedTables.remove(totalTables) # Remover índice
        else:
            totalTables = self.ui.tabWidget.count() # Total de tabelas
        tabWidgetName = "Tab" + str(totalTables + 1) 
        tableWidgetName = "self.ui.TabWidget" + str(totalTables + 1)
        UIFunctions.tableWidgetIndex.insert(currentTabIndex, tableWidgetName)
        
        # TabWidget
        self.ui.tab = QWidget()
        self.ui.horizontalLayout_Table = QHBoxLayout(self.ui.tab)
        self.ui.horizontalLayout_Table.setContentsMargins(5, 0, 0, 0)

        # TableWidget
        UIFunctions.tableWidgetIndex[currentTabIndex] = QTableWidget(self.ui.tab)
        UIFunctions.tableWidgetIndex[currentTabIndex].setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        UIFunctions.tableWidgetIndex[currentTabIndex].setFrameShape(QFrame.StyledPanel)
        UIFunctions.tableWidgetIndex[currentTabIndex].setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        UIFunctions.tableWidgetIndex[currentTabIndex].setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        UIFunctions.tableWidgetIndex[currentTabIndex].setRowCount(15)
        UIFunctions.tableWidgetIndex[currentTabIndex].setColumnCount(15)

        self.ui.horizontalLayout_Table.addWidget(UIFunctions.tableWidgetIndex[currentTabIndex])

        self.ui.tabWidget.addTab(self.ui.tab, tabWidgetName)
        self.ui.tabWidget.setCurrentIndex(totalTables) # Ir para a tabela criada

    def extractIntFromString(self,string):
        result = int(re.search(r'\d+', string)[0]) - 1
        return result

    def deleteTab(self):
        # Deletar tabela
        currentTabIndex = self.ui.tabWidget.currentIndex()
        tabWidgetName = self.ui.tabWidget.tabText(currentTabIndex)
        self.ui.tabWidget.removeTab(currentTabIndex)
        tabIndex = UIFunctions.extractIntFromString(self,tabWidgetName)
        UIFunctions.deletedTables.append(tabIndex)

    def addRow(self):
        currentTabIndex = self.ui.tabWidget.currentIndex()
        tabWidgetName = self.ui.tabWidget.tabText(currentTabIndex)
        tabIndex = UIFunctions.extractIntFromString(self,tabWidgetName)

        rowCount =  UIFunctions.tableWidgetIndex[tabIndex].rowCount()
        UIFunctions.tableWidgetIndex[tabIndex].insertRow(rowCount)

    def deleteRow(self):
        currentTabIndex = self.ui.tabWidget.currentIndex()
        tabWidgetName = self.ui.tabWidget.tabText(currentTabIndex)
        tabIndex = UIFunctions.extractIntFromString(self,tabWidgetName)

        rowCount =  UIFunctions.tableWidgetIndex[tabIndex].rowCount()
        UIFunctions.tableWidgetIndex[tabIndex].removeRow(rowCount - 1)

    def addColumn(self):
        currentTabIndex = self.ui.tabWidget.currentIndex()
        tabWidgetName = self.ui.tabWidget.tabText(currentTabIndex)
        tabIndex = UIFunctions.extractIntFromString(self,tabWidgetName)

        columnCount =  UIFunctions.tableWidgetIndex[tabIndex].columnCount()
        UIFunctions.tableWidgetIndex[tabIndex].insertColumn(columnCount)

    def deleteColumn(self):
        currentTabIndex = self.ui.tabWidget.currentIndex()
        tabWidgetName = self.ui.tabWidget.tabText(currentTabIndex)
        tabIndex = UIFunctions.extractIntFromString(self,tabWidgetName)
        columnCount =  UIFunctions.tableWidgetIndex[tabIndex].columnCount()
        UIFunctions.tableWidgetIndex[tabIndex].removeColumn(columnCount - 1)

    # Ignorar

    def importFromCSV(self):
        # Importar dados de arquivo csv
        csvPath = PDFfunctions.fileDialog(self,"csv")
        csvFile = codecs.open(csvPath)
        reader = csv.reader(csvFile)
        list_of_rows = list(reader)
        print(list_of_rows[0])
        print(list_of_rows[1])

    def setItem(self,row,column,item):
        self.ui.tableWidget.setItem(row,column,item)

    def launchRow(self,row,column,text,addRow=True):
        rowcount = self.ui.tableWidget.rowCount()
        if addRow:
            UIFunctions.addRow(self,rowcount)
        item = QtWidgets.QTableWidgetItem()
        UIFunctions.setItem(self,row,column,item)
        item.setText(QCoreApplication.translate("MainWindow", text, None));
        item.setTextAlignment(Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsEditable)

    def saveData(self,dbPath,tableName):
        DB = DataBase(dbPath,tableName)
        rowCount = self.ui.tableWidget.rowCount()
        columnCount = self.ui.tableWidget.columnCount()
        DB.deleteDBtable()
        DB.createDBTable()
        for row in range(rowCount):
            rowData = []
            for column in range(columnCount):
                widgetItem =  self.ui.tableWidget.item(row,column)
                if widgetItem and widgetItem.text():
                    rowData.append(widgetItem.text())
            if row:
                try:
                    DB.insertRowInDB(rowData)
                except:
                    pass
        DB.closeDB()
        
    def loadData(self,dbPath,tableName):
        DB = DataBase(dbPath,tableName)
        query = "SELECT * FROM {}".format(tableName)
        result = DB.executeQuery(query)
        for row_number, row_data in enumerate(result):
            UIFunctions.addRow(self, row_number + 1)
            for column_number, column_data in enumerate(row_data):
                if not isinstance(column_data, int):
                    UIFunctions.setItem(self,row_number + 1,column_number,QtWidgets.QTableWidgetItem(str(column_data)))
                else:
                    UIFunctions.launchRow(self,row_number + 1,column_number, str(column_data) ,False)

        while self.ui.tableWidget.rowCount() <= 16:
            UIFunctions.launchRow(self,self.ui.tableWidget.rowCount(),0,str(self.ui.tableWidget.rowCount()))      
