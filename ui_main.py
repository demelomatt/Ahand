# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI_BASE_reborn.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 721)
        MainWindow.setMinimumSize(QSize(1000, 720))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(66, 73, 90, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(55, 61, 75, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(22, 24, 30, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(29, 32, 40, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        brush6 = QBrush(QColor(210, 210, 210, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        brush8 = QBrush(QColor(85, 170, 255, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Active, QPalette.Link, brush8)
        brush9 = QBrush(QColor(255, 0, 127, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush10 = QBrush(QColor(44, 49, 60, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        brush11 = QBrush(QColor(51, 153, 255, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush11)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QMainWindow {background: transparent; }\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(27, 29, 35, 160);\n"
"	border: 1px solid rgb(40, 40, 40);\n"
"	border-radius: 2px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background: transparent;\n"
"color: rgb(210, 210, 210);")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"/* LINE EDIT */\n"
"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* SCROLL BARS */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(85, 170, 255);\n"
"    min-width: 25px;\n"
"	border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
""
                        "	border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(85, 170, 255);\n"
"    min-height: 25px;\n"
"	border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63"
                        ", 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* CHECKBOX */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/16x16/icons/16x16/cil-check-alt.png);\n"
"}\n"
"\n"
"/* RADIO BUTTON */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius"
                        ": 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* COMBOBOX */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb("
                        "85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* SLIDERS */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 9px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:verti"
                        "cal {\n"
"    background-color: rgb(85, 170, 255);\n"
"	border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 65))
        self.frame_top.setMaximumSize(QSize(16777215, 65))
        self.frame_top.setStyleSheet(u"background-color: transparent;")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.frame_top)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 16777215))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton_toggle_menu = QPushButton(self.frame_toggle)
        self.pushButton_toggle_menu.setObjectName(u"pushButton_toggle_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_toggle_menu.sizePolicy().hasHeightForWidth())
        self.pushButton_toggle_menu.setSizePolicy(sizePolicy)
        self.pushButton_toggle_menu.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(27, 29, 35);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.pushButton_toggle_menu)


        self.horizontalLayout_3.addWidget(self.frame_toggle)

        self.frame_top_right = QFrame(self.frame_top)
        self.frame_top_right.setObjectName(u"frame_top_right")
        self.frame_top_right.setStyleSheet(u"background: transparent;")
        self.frame_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_top_right)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top_btns = QFrame(self.frame_top_right)
        self.frame_top_btns.setObjectName(u"frame_top_btns")
        self.frame_top_btns.setMaximumSize(QSize(16777215, 42))
        self.frame_top_btns.setStyleSheet(u"background-color: rgba(27, 29, 35, 200)")
        self.frame_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_label_top_btns = QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setObjectName(u"frame_label_top_btns")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_label_top_btns.sizePolicy().hasHeightForWidth())
        self.frame_label_top_btns.setSizePolicy(sizePolicy1)
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)
        self.frame_icon_top_bar = QFrame(self.frame_label_top_btns)
        self.frame_icon_top_bar.setObjectName(u"frame_icon_top_bar")
        self.frame_icon_top_bar.setMaximumSize(QSize(30, 30))
        self.frame_icon_top_bar.setStyleSheet(u"background: transparent;\n"
"background-image: url(:/16x16/icons/16x16/cil-terminal.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"")
        self.frame_icon_top_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_icon_top_bar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_icon_top_bar)

        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_title_bar_top.setFont(font1)
        self.label_title_bar_top.setStyleSheet(u"background: transparent;\n"
"")

        self.horizontalLayout_10.addWidget(self.label_title_bar_top)

        self.label_title_bar_top.raise_()
        self.frame_icon_top_bar.raise_()

        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)

        self.frame_btns_right = QFrame(self.frame_top_btns)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        sizePolicy1.setHeightForWidth(self.frame_btns_right.sizePolicy().hasHeightForWidth())
        self.frame_btns_right.setSizePolicy(sizePolicy1)
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pushButton_minimize = QPushButton(self.frame_btns_right)
        self.pushButton_minimize.setObjectName(u"pushButton_minimize")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_minimize.sizePolicy().hasHeightForWidth())
        self.pushButton_minimize.setSizePolicy(sizePolicy2)
        self.pushButton_minimize.setMinimumSize(QSize(40, 0))
        self.pushButton_minimize.setMaximumSize(QSize(40, 16777215))
        self.pushButton_minimize.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/16x16/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_minimize.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.pushButton_minimize)

        self.pushButton_maximize_restore = QPushButton(self.frame_btns_right)
        self.pushButton_maximize_restore.setObjectName(u"pushButton_maximize_restore")
        sizePolicy2.setHeightForWidth(self.pushButton_maximize_restore.sizePolicy().hasHeightForWidth())
        self.pushButton_maximize_restore.setSizePolicy(sizePolicy2)
        self.pushButton_maximize_restore.setMinimumSize(QSize(40, 0))
        self.pushButton_maximize_restore.setMaximumSize(QSize(40, 16777215))
        self.pushButton_maximize_restore.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/16x16/icons/16x16/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_maximize_restore.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.pushButton_maximize_restore)

        self.pushButton_close = QPushButton(self.frame_btns_right)
        self.pushButton_close.setObjectName(u"pushButton_close")
        sizePolicy2.setHeightForWidth(self.pushButton_close.sizePolicy().hasHeightForWidth())
        self.pushButton_close.setSizePolicy(sizePolicy2)
        self.pushButton_close.setMinimumSize(QSize(40, 0))
        self.pushButton_close.setMaximumSize(QSize(40, 16777215))
        self.pushButton_close.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_close.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.pushButton_close)


        self.horizontalLayout_4.addWidget(self.frame_btns_right, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_top_btns)

        self.frame_top_info = QFrame(self.frame_top_right)
        self.frame_top_info.setObjectName(u"frame_top_info")
        self.frame_top_info.setMaximumSize(QSize(16777215, 65))
        self.frame_top_info.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_top_info.setFrameShape(QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_top_info)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.label_top_info_1 = QLabel(self.frame_top_info)
        self.label_top_info_1.setObjectName(u"label_top_info_1")
        self.label_top_info_1.setMaximumSize(QSize(16777215, 15))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        self.label_top_info_1.setFont(font2)
        self.label_top_info_1.setStyleSheet(u"color: rgb(98, 103, 111); ")

        self.horizontalLayout_8.addWidget(self.label_top_info_1)

        self.label_top_info_2 = QLabel(self.frame_top_info)
        self.label_top_info_2.setObjectName(u"label_top_info_2")
        self.label_top_info_2.setMinimumSize(QSize(0, 0))
        self.label_top_info_2.setMaximumSize(QSize(250, 20))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setBold(True)
        font3.setWeight(75)
        self.label_top_info_2.setFont(font3)
        self.label_top_info_2.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_top_info_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_top_info_2)


        self.verticalLayout_2.addWidget(self.frame_top_info)


        self.horizontalLayout_3.addWidget(self.frame_top_right)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        sizePolicy.setHeightForWidth(self.frame_center.sizePolicy().hasHeightForWidth())
        self.frame_center.setSizePolicy(sizePolicy)
        self.frame_center.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.frame_center)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy3)
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_menus = QFrame(self.frame_left_menu)
        self.frame_menus.setObjectName(u"frame_menus")
        self.frame_menus.setFrameShape(QFrame.NoFrame)
        self.frame_menus.setFrameShadow(QFrame.Raised)
        self.layout_menus = QVBoxLayout(self.frame_menus)
        self.layout_menus.setSpacing(0)
        self.layout_menus.setObjectName(u"layout_menus")
        self.layout_menus.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.frame_menus, 0, Qt.AlignTop)

        self.frame_extra_menus = QFrame(self.frame_left_menu)
        self.frame_extra_menus.setObjectName(u"frame_extra_menus")
        sizePolicy3.setHeightForWidth(self.frame_extra_menus.sizePolicy().hasHeightForWidth())
        self.frame_extra_menus.setSizePolicy(sizePolicy3)
        self.frame_extra_menus.setFrameShape(QFrame.NoFrame)
        self.frame_extra_menus.setFrameShadow(QFrame.Raised)
        self.layout_menu_bottom = QVBoxLayout(self.frame_extra_menus)
        self.layout_menu_bottom.setSpacing(10)
        self.layout_menu_bottom.setObjectName(u"layout_menu_bottom")
        self.layout_menu_bottom.setContentsMargins(0, 0, 0, 25)
        self.label_user_icon = QLabel(self.frame_extra_menus)
        self.label_user_icon.setObjectName(u"label_user_icon")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_user_icon.sizePolicy().hasHeightForWidth())
        self.label_user_icon.setSizePolicy(sizePolicy4)
        self.label_user_icon.setMinimumSize(QSize(60, 60))
        self.label_user_icon.setMaximumSize(QSize(60, 60))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(12)
        self.label_user_icon.setFont(font4)
        self.label_user_icon.setStyleSheet(u"QLabel {\n"
"	border-radius: 30px;\n"
"	background-color: rgb(44, 49, 60);\n"
"	border: 5px solid rgb(39, 44, 54);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}")
        self.label_user_icon.setAlignment(Qt.AlignCenter)

        self.layout_menu_bottom.addWidget(self.label_user_icon, 0, Qt.AlignHCenter)


        self.verticalLayout_5.addWidget(self.frame_extra_menus, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_content_right = QFrame(self.frame_center)
        self.frame_content_right.setObjectName(u"frame_content_right")
        self.frame_content_right.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.frame_content_right.setFrameShape(QFrame.NoFrame)
        self.frame_content_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_content_right)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_content = QFrame(self.frame_content_right)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_content)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(5, 5, 5, 5)
        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMaximumSize(QSize(850, 16777215))
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_10 = QVBoxLayout(self.page_home)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_home_holding_5 = QFrame(self.page_home)
        self.frame_home_holding_5.setObjectName(u"frame_home_holding_5")
        self.frame_home_holding_5.setStyleSheet(u"")
        self.frame_home_holding_5.setFrameShape(QFrame.StyledPanel)
        self.frame_home_holding_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_home_holding_5)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_home_children_5 = QFrame(self.frame_home_holding_5)
        self.frame_home_children_5.setObjectName(u"frame_home_children_5")
        self.frame_home_children_5.setStyleSheet(u"")
        self.frame_home_children_5.setFrameShape(QFrame.StyledPanel)
        self.frame_home_children_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_home_children_5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_merge_pdf = QLabel(self.frame_home_children_5)
        self.label_merge_pdf.setObjectName(u"label_merge_pdf")
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(36)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_merge_pdf.setFont(font5)

        self.verticalLayout_12.addWidget(self.label_merge_pdf, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_merge_pdf_desc = QLabel(self.frame_home_children_5)
        self.label_merge_pdf_desc.setObjectName(u"label_merge_pdf_desc")
        self.label_merge_pdf_desc.setMinimumSize(QSize(0, 50))
        font6 = QFont()
        font6.setPointSize(12)
        self.label_merge_pdf_desc.setFont(font6)

        self.verticalLayout_12.addWidget(self.label_merge_pdf_desc, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_13.addWidget(self.frame_home_children_5)


        self.verticalLayout_10.addWidget(self.frame_home_holding_5)

        self.frame_home_holding_4 = QFrame(self.page_home)
        self.frame_home_holding_4.setObjectName(u"frame_home_holding_4")
        self.frame_home_holding_4.setStyleSheet(u"")
        self.frame_home_holding_4.setFrameShape(QFrame.StyledPanel)
        self.frame_home_holding_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_home_holding_4)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_home_children_4 = QFrame(self.frame_home_holding_4)
        self.frame_home_children_4.setObjectName(u"frame_home_children_4")
        self.frame_home_children_4.setMinimumSize(QSize(200, 0))
        self.frame_home_children_4.setMaximumSize(QSize(226, 100))
        self.frame_home_children_4.setStyleSheet(u"background-color: rgb(36, 40, 51);\n"
"border-radius: 5px;\n"
"")
        self.frame_home_children_4.setFrameShape(QFrame.StyledPanel)
        self.frame_home_children_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_home_children_4)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_select_pdf = QLabel(self.frame_home_children_4)
        self.label_select_pdf.setObjectName(u"label_select_pdf")
        self.label_select_pdf.setMinimumSize(QSize(150, 20))
        self.label_select_pdf.setMaximumSize(QSize(150, 20))
        font7 = QFont()
        font7.setFamily(u"Segoe UI")
        font7.setPointSize(10)
        font7.setBold(False)
        font7.setWeight(50)
        self.label_select_pdf.setFont(font7)
        self.label_select_pdf.setContextMenuPolicy(Qt.NoContextMenu)

        self.gridLayout_10.addWidget(self.label_select_pdf, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.pushButton_open_pdf = QPushButton(self.frame_home_children_4)
        self.pushButton_open_pdf.setObjectName(u"pushButton_open_pdf")
        self.pushButton_open_pdf.setMinimumSize(QSize(180, 0))
        self.pushButton_open_pdf.setMaximumSize(QSize(180, 30))
        self.pushButton_open_pdf.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/16x16/icons/16x16/cil-folder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_open_pdf.setIcon(icon3)

        self.gridLayout_10.addWidget(self.pushButton_open_pdf, 1, 0, 1, 1)

        self.label_files_selection = QLabel(self.frame_home_children_4)
        self.label_files_selection.setObjectName(u"label_files_selection")
        self.label_files_selection.setMinimumSize(QSize(150, 16))
        self.label_files_selection.setMaximumSize(QSize(140, 16))
        font8 = QFont()
        font8.setPointSize(10)
        self.label_files_selection.setFont(font8)
        self.label_files_selection.setStyleSheet(u"color: rgb(98, 103, 111);")

        self.gridLayout_10.addWidget(self.label_files_selection, 2, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_14.addWidget(self.frame_home_children_4)

        self.frame_9 = QFrame(self.frame_home_holding_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_9)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_home_children_11 = QFrame(self.frame_9)
        self.frame_home_children_11.setObjectName(u"frame_home_children_11")
        self.frame_home_children_11.setMinimumSize(QSize(250, 100))
        self.frame_home_children_11.setMaximumSize(QSize(200, 100))
        self.frame_home_children_11.setStyleSheet(u"background-color: rgb(36, 40, 51);\n"
"border-radius: 5px;\n"
"")
        self.frame_home_children_11.setFrameShape(QFrame.StyledPanel)
        self.frame_home_children_11.setFrameShadow(QFrame.Raised)
        self.label_rootdir_3 = QLabel(self.frame_home_children_11)
        self.label_rootdir_3.setObjectName(u"label_rootdir_3")
        self.label_rootdir_3.setGeometry(QRect(78, 4, 94, 17))
        self.label_rootdir_3.setMaximumSize(QSize(16777215, 22))
        self.label_rootdir_3.setFont(font7)
        self.label_rootdir_3.setStyleSheet(u"")
        self.pushButton_open_rootdir_3 = QPushButton(self.frame_home_children_11)
        self.pushButton_open_rootdir_3.setObjectName(u"pushButton_open_rootdir_3")
        self.pushButton_open_rootdir_3.setGeometry(QRect(35, 35, 180, 30))
        self.pushButton_open_rootdir_3.setMinimumSize(QSize(180, 30))
        self.pushButton_open_rootdir_3.setMaximumSize(QSize(180, 30))
        self.pushButton_open_rootdir_3.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_open_rootdir_3.setIcon(icon3)
        self.lineEdit_rootdir_3 = QLineEdit(self.frame_home_children_11)
        self.lineEdit_rootdir_3.setObjectName(u"lineEdit_rootdir_3")
        self.lineEdit_rootdir_3.setGeometry(QRect(10, 73, 230, 22))
        self.lineEdit_rootdir_3.setMinimumSize(QSize(230, 0))
        self.lineEdit_rootdir_3.setMaximumSize(QSize(180, 16777215))
        self.lineEdit_rootdir_3.setFont(font8)
        self.lineEdit_rootdir_3.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.verticalLayout_17.addWidget(self.frame_home_children_11)


        self.horizontalLayout_14.addWidget(self.frame_9)


        self.verticalLayout_10.addWidget(self.frame_home_holding_4, 0, Qt.AlignHCenter)

        self.frame_home_holding_3 = QFrame(self.page_home)
        self.frame_home_holding_3.setObjectName(u"frame_home_holding_3")
        self.frame_home_holding_3.setStyleSheet(u"")
        self.frame_home_holding_3.setFrameShape(QFrame.StyledPanel)
        self.frame_home_holding_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_home_holding_3)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_home_children_3 = QFrame(self.frame_home_holding_3)
        self.frame_home_children_3.setObjectName(u"frame_home_children_3")
        self.frame_home_children_3.setMinimumSize(QSize(0, 80))
        self.frame_home_children_3.setMaximumSize(QSize(850, 80))
        self.frame_home_children_3.setStyleSheet(u"background-color: rgb(36, 40, 51);\n"
"border-radius: 5px;\n"
"")
        self.frame_home_children_3.setFrameShape(QFrame.StyledPanel)
        self.frame_home_children_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_home_children_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_prefix = QLabel(self.frame_home_children_3)
        self.label_prefix.setObjectName(u"label_prefix")
        self.label_prefix.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.label_prefix.sizePolicy().hasHeightForWidth())
        self.label_prefix.setSizePolicy(sizePolicy3)
        self.label_prefix.setMinimumSize(QSize(135, 22))
        self.label_prefix.setMaximumSize(QSize(135, 22))
        self.label_prefix.setFont(font1)
        self.label_prefix.setCursor(QCursor(Qt.ArrowCursor))
        self.label_prefix.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_3.addWidget(self.label_prefix, 0, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.label_exemple_prefix = QLabel(self.frame_home_children_3)
        self.label_exemple_prefix.setObjectName(u"label_exemple_prefix")
        self.label_exemple_prefix.setMinimumSize(QSize(180, 15))
        self.label_exemple_prefix.setMaximumSize(QSize(180, 15))
        self.label_exemple_prefix.setFont(font8)
        self.label_exemple_prefix.setStyleSheet(u"color: rgb(98, 103, 111);")

        self.gridLayout_3.addWidget(self.label_exemple_prefix, 1, 0, 1, 6, Qt.AlignVCenter)

        self.lineEdit_prefix = QLineEdit(self.frame_home_children_3)
        self.lineEdit_prefix.setObjectName(u"lineEdit_prefix")
        self.lineEdit_prefix.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_prefix.setFont(font8)
        self.lineEdit_prefix.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit_prefix.setClearButtonEnabled(False)

        self.gridLayout_3.addWidget(self.lineEdit_prefix, 0, 1, 1, 1, Qt.AlignVCenter)


        self.horizontalLayout_15.addWidget(self.frame_home_children_3)


        self.verticalLayout_10.addWidget(self.frame_home_holding_3)

        self.frame_home_holding_2 = QFrame(self.page_home)
        self.frame_home_holding_2.setObjectName(u"frame_home_holding_2")
        self.frame_home_holding_2.setStyleSheet(u"")
        self.frame_home_holding_2.setFrameShape(QFrame.StyledPanel)
        self.frame_home_holding_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_home_holding_2)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_home_children_2 = QFrame(self.frame_home_holding_2)
        self.frame_home_children_2.setObjectName(u"frame_home_children_2")
        self.frame_home_children_2.setMinimumSize(QSize(0, 80))
        self.frame_home_children_2.setMaximumSize(QSize(850, 80))
        self.frame_home_children_2.setStyleSheet(u"background-color: rgb(36, 40, 51);\n"
"border-radius: 5px;\n"
"")
        self.frame_home_children_2.setFrameShape(QFrame.StyledPanel)
        self.frame_home_children_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_home_children_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_outputdir = QLabel(self.frame_home_children_2)
        self.label_outputdir.setObjectName(u"label_outputdir")
        self.label_outputdir.setMaximumSize(QSize(16777215, 22))
        self.label_outputdir.setFont(font1)
        self.label_outputdir.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.label_outputdir, 0, 0, 1, 1)

        self.lineEdit_outputdir = QLineEdit(self.frame_home_children_2)
        self.lineEdit_outputdir.setObjectName(u"lineEdit_outputdir")
        self.lineEdit_outputdir.setMaximumSize(QSize(686, 16777215))
        self.lineEdit_outputdir.setFont(font8)
        self.lineEdit_outputdir.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.gridLayout_4.addWidget(self.lineEdit_outputdir, 1, 0, 1, 1, Qt.AlignVCenter)

        self.pushButton_open_dir = QPushButton(self.frame_home_children_2)
        self.pushButton_open_dir.setObjectName(u"pushButton_open_dir")
        self.pushButton_open_dir.setMinimumSize(QSize(180, 30))
        self.pushButton_open_dir.setMaximumSize(QSize(180, 30))
        self.pushButton_open_dir.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_open_dir.setIcon(icon3)

        self.gridLayout_4.addWidget(self.pushButton_open_dir, 1, 1, 1, 1)


        self.horizontalLayout_16.addWidget(self.frame_home_children_2)


        self.verticalLayout_10.addWidget(self.frame_home_holding_2)

        self.frame_home_holding_1 = QFrame(self.page_home)
        self.frame_home_holding_1.setObjectName(u"frame_home_holding_1")
        self.frame_home_holding_1.setStyleSheet(u"")
        self.frame_home_holding_1.setFrameShape(QFrame.StyledPanel)
        self.frame_home_holding_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_home_holding_1)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_home_children_1 = QFrame(self.frame_home_holding_1)
        self.frame_home_children_1.setObjectName(u"frame_home_children_1")
        self.frame_home_children_1.setStyleSheet(u"")
        self.frame_home_children_1.setFrameShape(QFrame.StyledPanel)
        self.frame_home_children_1.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_home_children_1)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.pushButton_execute = QPushButton(self.frame_home_children_1)
        self.pushButton_execute.setObjectName(u"pushButton_execute")
        self.pushButton_execute.setMinimumSize(QSize(180, 30))
        self.pushButton_execute.setMaximumSize(QSize(180, 30))
        self.pushButton_execute.setFont(font6)
        self.pushButton_execute.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/16x16/icons/16x16/cil-media-play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_execute.setIcon(icon4)

        self.gridLayout_7.addWidget(self.pushButton_execute, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_log = QLabel(self.frame_home_children_1)
        self.label_log.setObjectName(u"label_log")
        self.label_log.setFont(font4)
        self.label_log.setStyleSheet(u"color: rgb(169, 169, 169);")

        self.gridLayout_7.addWidget(self.label_log, 1, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_17.addWidget(self.frame_home_children_1)


        self.verticalLayout_10.addWidget(self.frame_home_holding_1)

        self.stackedWidget.addWidget(self.page_home)
        self.page_scanner = QWidget()
        self.page_scanner.setObjectName(u"page_scanner")
        self.verticalLayout_9 = QVBoxLayout(self.page_scanner)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.page_scanner)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.frame_home_children_6 = QFrame(self.frame_8)
        self.frame_home_children_6.setObjectName(u"frame_home_children_6")
        self.frame_home_children_6.setStyleSheet(u"")
        self.frame_home_children_6.setFrameShape(QFrame.StyledPanel)
        self.frame_home_children_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_home_children_6)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_scan_pdf_2 = QLabel(self.frame_home_children_6)
        self.label_scan_pdf_2.setObjectName(u"label_scan_pdf_2")
        self.label_scan_pdf_2.setFont(font5)

        self.verticalLayout_14.addWidget(self.label_scan_pdf_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_scan_pdf_desc_2 = QLabel(self.frame_home_children_6)
        self.label_scan_pdf_desc_2.setObjectName(u"label_scan_pdf_desc_2")
        self.label_scan_pdf_desc_2.setMinimumSize(QSize(0, 50))
        self.label_scan_pdf_desc_2.setFont(font6)

        self.verticalLayout_14.addWidget(self.label_scan_pdf_desc_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_25.addWidget(self.frame_home_children_6)


        self.verticalLayout_9.addWidget(self.frame_8)

        self.frame_7 = QFrame(self.page_scanner)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.frame_home_children_7 = QFrame(self.frame_7)
        self.frame_home_children_7.setObjectName(u"frame_home_children_7")
        self.frame_home_children_7.setMaximumSize(QSize(226, 112))
        self.frame_home_children_7.setStyleSheet(u"background-color: rgb(36, 40, 51);\n"
"border-radius: 5px;\n"
"")
        self.frame_home_children_7.setFrameShape(QFrame.StyledPanel)
        self.frame_home_children_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_home_children_7)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_select_pdf_2 = QLabel(self.frame_home_children_7)
        self.label_select_pdf_2.setObjectName(u"label_select_pdf_2")
        self.label_select_pdf_2.setMinimumSize(QSize(150, 20))
        self.label_select_pdf_2.setMaximumSize(QSize(150, 20))
        self.label_select_pdf_2.setFont(font7)
        self.label_select_pdf_2.setContextMenuPolicy(Qt.NoContextMenu)

        self.verticalLayout_16.addWidget(self.label_select_pdf_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.pushButton_open_pdf_2 = QPushButton(self.frame_home_children_7)
        self.pushButton_open_pdf_2.setObjectName(u"pushButton_open_pdf_2")
        self.pushButton_open_pdf_2.setMinimumSize(QSize(180, 0))
        self.pushButton_open_pdf_2.setMaximumSize(QSize(180, 30))
        self.pushButton_open_pdf_2.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/16x16/icons/16x16/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_open_pdf_2.setIcon(icon5)

        self.verticalLayout_16.addWidget(self.pushButton_open_pdf_2, 0, Qt.AlignHCenter)

        self.label_files_selection_2 = QLabel(self.frame_home_children_7)
        self.label_files_selection_2.setObjectName(u"label_files_selection_2")
        self.label_files_selection_2.setMinimumSize(QSize(150, 16))
        self.label_files_selection_2.setMaximumSize(QSize(140, 16))
        self.label_files_selection_2.setFont(font8)
        self.label_files_selection_2.setStyleSheet(u"color: rgb(98, 103, 111);")

        self.verticalLayout_16.addWidget(self.label_files_selection_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_24.addWidget(self.frame_home_children_7)


        self.verticalLayout_9.addWidget(self.frame_7)

        self.frame_6 = QFrame(self.page_scanner)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.frame_home_children_8 = QFrame(self.frame_6)
        self.frame_home_children_8.setObjectName(u"frame_home_children_8")
        self.frame_home_children_8.setMinimumSize(QSize(0, 80))
        self.frame_home_children_8.setMaximumSize(QSize(850, 80))
        self.frame_home_children_8.setStyleSheet(u"background-color: rgb(36, 40, 51);\n"
"border-radius: 5px;\n"
"")
        self.frame_home_children_8.setFrameShape(QFrame.StyledPanel)
        self.frame_home_children_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_home_children_8)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_prefix_2 = QLabel(self.frame_home_children_8)
        self.label_prefix_2.setObjectName(u"label_prefix_2")
        self.label_prefix_2.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.label_prefix_2.sizePolicy().hasHeightForWidth())
        self.label_prefix_2.setSizePolicy(sizePolicy3)
        self.label_prefix_2.setMinimumSize(QSize(135, 22))
        self.label_prefix_2.setMaximumSize(QSize(135, 22))
        self.label_prefix_2.setFont(font1)
        self.label_prefix_2.setCursor(QCursor(Qt.ArrowCursor))
        self.label_prefix_2.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_5.addWidget(self.label_prefix_2, 0, 0, 1, 1, Qt.AlignLeft|Qt.AlignVCenter)

        self.label_exemple_prefix_2 = QLabel(self.frame_home_children_8)
        self.label_exemple_prefix_2.setObjectName(u"label_exemple_prefix_2")
        self.label_exemple_prefix_2.setMinimumSize(QSize(180, 15))
        self.label_exemple_prefix_2.setMaximumSize(QSize(180, 15))
        self.label_exemple_prefix_2.setFont(font8)
        self.label_exemple_prefix_2.setStyleSheet(u"color: rgb(98, 103, 111);")

        self.gridLayout_5.addWidget(self.label_exemple_prefix_2, 1, 0, 1, 6, Qt.AlignVCenter)

        self.lineEdit_prefix_2 = QLineEdit(self.frame_home_children_8)
        self.lineEdit_prefix_2.setObjectName(u"lineEdit_prefix_2")
        self.lineEdit_prefix_2.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_prefix_2.setFont(font8)
        self.lineEdit_prefix_2.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit_prefix_2.setClearButtonEnabled(False)

        self.gridLayout_5.addWidget(self.lineEdit_prefix_2, 0, 1, 1, 1, Qt.AlignVCenter)


        self.horizontalLayout_23.addWidget(self.frame_home_children_8)


        self.verticalLayout_9.addWidget(self.frame_6)

        self.frame_5 = QFrame(self.page_scanner)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.frame_home_holding_6 = QFrame(self.frame_5)
        self.frame_home_holding_6.setObjectName(u"frame_home_holding_6")
        self.frame_home_holding_6.setStyleSheet(u"")
        self.frame_home_holding_6.setFrameShape(QFrame.StyledPanel)
        self.frame_home_holding_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_home_holding_6)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_home_children_9 = QFrame(self.frame_home_holding_6)
        self.frame_home_children_9.setObjectName(u"frame_home_children_9")
        self.frame_home_children_9.setMinimumSize(QSize(0, 80))
        self.frame_home_children_9.setMaximumSize(QSize(850, 80))
        self.frame_home_children_9.setStyleSheet(u"background-color: rgb(36, 40, 51);\n"
"border-radius: 5px;\n"
"")
        self.frame_home_children_9.setFrameShape(QFrame.StyledPanel)
        self.frame_home_children_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_home_children_9)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_outputdir_2 = QLabel(self.frame_home_children_9)
        self.label_outputdir_2.setObjectName(u"label_outputdir_2")
        self.label_outputdir_2.setMaximumSize(QSize(16777215, 22))
        self.label_outputdir_2.setFont(font1)
        self.label_outputdir_2.setStyleSheet(u"")

        self.gridLayout_6.addWidget(self.label_outputdir_2, 0, 0, 1, 1)

        self.lineEdit_outputdir_2 = QLineEdit(self.frame_home_children_9)
        self.lineEdit_outputdir_2.setObjectName(u"lineEdit_outputdir_2")
        self.lineEdit_outputdir_2.setMaximumSize(QSize(686, 16777215))
        self.lineEdit_outputdir_2.setFont(font8)
        self.lineEdit_outputdir_2.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.gridLayout_6.addWidget(self.lineEdit_outputdir_2, 1, 0, 1, 1, Qt.AlignVCenter)

        self.pushButton_open_dir_2 = QPushButton(self.frame_home_children_9)
        self.pushButton_open_dir_2.setObjectName(u"pushButton_open_dir_2")
        self.pushButton_open_dir_2.setMinimumSize(QSize(180, 30))
        self.pushButton_open_dir_2.setMaximumSize(QSize(180, 30))
        self.pushButton_open_dir_2.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_open_dir_2.setIcon(icon3)

        self.gridLayout_6.addWidget(self.pushButton_open_dir_2, 1, 1, 1, 1)


        self.horizontalLayout_19.addWidget(self.frame_home_children_9)


        self.horizontalLayout_22.addWidget(self.frame_home_holding_6)


        self.verticalLayout_9.addWidget(self.frame_5)

        self.frame_4 = QFrame(self.page_scanner)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_home_holding_7 = QFrame(self.frame_4)
        self.frame_home_holding_7.setObjectName(u"frame_home_holding_7")
        self.frame_home_holding_7.setStyleSheet(u"")
        self.frame_home_holding_7.setFrameShape(QFrame.StyledPanel)
        self.frame_home_holding_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_home_holding_7)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_home_children_10 = QFrame(self.frame_home_holding_7)
        self.frame_home_children_10.setObjectName(u"frame_home_children_10")
        self.frame_home_children_10.setStyleSheet(u"")
        self.frame_home_children_10.setFrameShape(QFrame.StyledPanel)
        self.frame_home_children_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_home_children_10)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.pushButton_execute_2 = QPushButton(self.frame_home_children_10)
        self.pushButton_execute_2.setObjectName(u"pushButton_execute_2")
        self.pushButton_execute_2.setMinimumSize(QSize(180, 30))
        self.pushButton_execute_2.setMaximumSize(QSize(180, 30))
        self.pushButton_execute_2.setFont(font6)
        self.pushButton_execute_2.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_execute_2.setIcon(icon4)

        self.gridLayout_8.addWidget(self.pushButton_execute_2, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_log_2 = QLabel(self.frame_home_children_10)
        self.label_log_2.setObjectName(u"label_log_2")
        self.label_log_2.setFont(font4)
        self.label_log_2.setStyleSheet(u"color: rgb(169, 169, 169);")

        self.gridLayout_8.addWidget(self.label_log_2, 1, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_20.addWidget(self.frame_home_children_10)


        self.horizontalLayout_21.addWidget(self.frame_home_holding_7)


        self.verticalLayout_9.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.page_scanner)
        self.page_searchpatterns = QWidget()
        self.page_searchpatterns.setObjectName(u"page_searchpatterns")
        self.verticalLayout_13 = QVBoxLayout(self.page_searchpatterns)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_searchpatterns_holding = QFrame(self.page_searchpatterns)
        self.frame_searchpatterns_holding.setObjectName(u"frame_searchpatterns_holding")
        self.frame_searchpatterns_holding.setStyleSheet(u"")
        self.frame_searchpatterns_holding.setFrameShape(QFrame.StyledPanel)
        self.frame_searchpatterns_holding.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_searchpatterns_holding)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_searchpatterns_holding)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.pushButton_save = QPushButton(self.frame)
        self.pushButton_save.setObjectName(u"pushButton_save")
        self.pushButton_save.setMinimumSize(QSize(0, 30))
        self.pushButton_save.setMaximumSize(QSize(180, 16777215))
        self.pushButton_save.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/16x16/icons/16x16/cil-save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_save.setIcon(icon6)

        self.horizontalLayout_9.addWidget(self.pushButton_save)

        self.pushButton_add = QPushButton(self.frame)
        self.pushButton_add.setObjectName(u"pushButton_add")
        self.pushButton_add.setMinimumSize(QSize(0, 30))
        self.pushButton_add.setMaximumSize(QSize(180, 16777215))
        icon7 = QIcon()
        icon7.addFile(u":/16x16/icons/16x16/cil-plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_add.setIcon(icon7)

        self.horizontalLayout_9.addWidget(self.pushButton_add)

        self.pushButton_delete = QPushButton(self.frame)
        self.pushButton_delete.setObjectName(u"pushButton_delete")
        self.pushButton_delete.setMinimumSize(QSize(0, 30))
        self.pushButton_delete.setMaximumSize(QSize(180, 16777215))
        self.pushButton_delete.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/16x16/icons/16x16/cil-remove.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_delete.setIcon(icon8)

        self.horizontalLayout_9.addWidget(self.pushButton_delete)


        self.verticalLayout_18.addWidget(self.frame)

        self.tableWidget = QTableWidget(self.frame_searchpatterns_holding)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(0, 0, 0);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	color: rgb(39, 96, 128);\n"
"	background-color: rgb(39, 96, 128);\n"
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
"    border-right: 1px soli"
                        "d rgb(44, 49, 60);\n"
"}\n"
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
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setFrameShadow(QFrame.Plain)
        self.tableWidget.setLineWidth(0)
        self.tableWidget.setMidLineWidth(0)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setEditTriggers(QAbstractItemView.AllEditTriggers)
        self.tableWidget.setTabKeyNavigation(True)
        self.tableWidget.setProperty("showDropIndicator", True)
        self.tableWidget.setDragEnabled(False)
        self.tableWidget.setDragDropOverwriteMode(True)
        self.tableWidget.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.tableWidget.setDefaultDropAction(Qt.IgnoreAction)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.tableWidget.setTextElideMode(Qt.ElideRight)
        self.tableWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(370)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_18.addWidget(self.tableWidget)


        self.verticalLayout_13.addWidget(self.frame_searchpatterns_holding)

        self.stackedWidget.addWidget(self.page_searchpatterns)
        self.page_widgets = QWidget()
        self.page_widgets.setObjectName(u"page_widgets")
        self.verticalLayout_6 = QVBoxLayout(self.page_widgets)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.stackedWidget.addWidget(self.page_widgets)

        self.horizontalLayout_18.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.frame_content)

        self.frame_grip = QFrame(self.frame_content_right)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(0, 25))
        self.frame_grip.setMaximumSize(QSize(16777215, 25))
        self.frame_grip.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_grip.setFrameShape(QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_grip)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 2, 0)
        self.frame_label_bottom = QFrame(self.frame_grip)
        self.frame_label_bottom.setObjectName(u"frame_label_bottom")
        self.frame_label_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.label_credits = QLabel(self.frame_label_bottom)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setFont(font2)
        self.label_credits.setStyleSheet(u"color: rgb(98, 103, 111);")

        self.horizontalLayout_7.addWidget(self.label_credits)

        self.label_version = QLabel(self.frame_label_bottom)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setMaximumSize(QSize(100, 16777215))
        self.label_version.setFont(font2)
        self.label_version.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_version)


        self.horizontalLayout_6.addWidget(self.frame_label_bottom)

        self.frame_size_grip = QFrame(self.frame_grip)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMaximumSize(QSize(20, 20))
        self.frame_size_grip.setStyleSheet(u"QSizeGrip {\n"
"	background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_size_grip)


        self.verticalLayout_4.addWidget(self.frame_grip)


        self.horizontalLayout_2.addWidget(self.frame_content_right)


        self.verticalLayout.addWidget(self.frame_center)


        self.horizontalLayout.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.pushButton_minimize, self.pushButton_maximize_restore)
        QWidget.setTabOrder(self.pushButton_maximize_restore, self.pushButton_close)
        QWidget.setTabOrder(self.pushButton_close, self.pushButton_toggle_menu)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_toggle_menu.setText("")
        self.label_title_bar_top.setText(QCoreApplication.translate("MainWindow", u"Ahand", None))
#if QT_CONFIG(tooltip)
        self.pushButton_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_maximize_restore.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_maximize_restore.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_close.setText("")
        self.label_top_info_1.setText(QCoreApplication.translate("MainWindow", u"Giving you a hand for automation.", None))
        self.label_top_info_2.setText(QCoreApplication.translate("MainWindow", u"| HOME", None))
        self.label_user_icon.setText(QCoreApplication.translate("MainWindow", u"Ahand", None))
        self.label_merge_pdf.setText(QCoreApplication.translate("MainWindow", u"PDF MERGE", None))
        self.label_merge_pdf_desc.setText(QCoreApplication.translate("MainWindow", u"Mesclar diversos PDF'S em arquivo \u00fanico.", None))
        self.label_select_pdf.setText(QCoreApplication.translate("MainWindow", u"Selecionar arquivos PDF", None))
        self.pushButton_open_pdf.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.label_files_selection.setText(QCoreApplication.translate("MainWindow", u"10 arquivos selecionados.", None))
        self.label_rootdir_3.setText(QCoreApplication.translate("MainWindow", u"Mesclar em lote", None))
        self.pushButton_open_rootdir_3.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.lineEdit_rootdir_3.setText("")
        self.lineEdit_rootdir_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecionar diret\u00f3rio ra\u00edz", None))
        self.label_prefix.setText(QCoreApplication.translate("MainWindow", u"Sufixo dos arquivos:", None))
        self.label_exemple_prefix.setText(QCoreApplication.translate("MainWindow", u"Exemplo: yourpdf_MERGE.pdf", None))
        self.lineEdit_prefix.setText("")
        self.lineEdit_prefix.setPlaceholderText(QCoreApplication.translate("MainWindow", u"_MERGE", None))
        self.label_outputdir.setText(QCoreApplication.translate("MainWindow", u"Selecionar diret\u00f3rio de sa\u00edda", None))
        self.lineEdit_outputdir.setPlaceholderText(QCoreApplication.translate("MainWindow", u"C:\\Users\\root\\Downloads\\", None))
        self.pushButton_open_dir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.pushButton_execute.setText(QCoreApplication.translate("MainWindow", u"Executar", None))
        self.label_log.setText(QCoreApplication.translate("MainWindow", u"Arquivos mesclados com sucesso.", None))
        self.label_scan_pdf_2.setText(QCoreApplication.translate("MainWindow", u"PDF SCANNER", None))
        self.label_scan_pdf_desc_2.setText(QCoreApplication.translate("MainWindow", u"Usar a tecnologia OCR para extrair texto e converter PDF em pesquis\u00e1vel.", None))
        self.label_select_pdf_2.setText(QCoreApplication.translate("MainWindow", u"Selecionar arquivos PDF", None))
        self.pushButton_open_pdf_2.setText(QCoreApplication.translate("MainWindow", u"Selecionar", None))
        self.label_files_selection_2.setText(QCoreApplication.translate("MainWindow", u"10 arquivos selecionados.", None))
        self.label_prefix_2.setText(QCoreApplication.translate("MainWindow", u"Sufixo dos arquivos:", None))
        self.label_exemple_prefix_2.setText(QCoreApplication.translate("MainWindow", u"Exemplo: yourpdf_OCR.pdf", None))
        self.lineEdit_prefix_2.setText("")
        self.lineEdit_prefix_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"_OCR", None))
        self.label_outputdir_2.setText(QCoreApplication.translate("MainWindow", u"Selecionar diret\u00f3rio de sa\u00edda", None))
        self.lineEdit_outputdir_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"C:\\Users\\root\\Downloads\\", None))
        self.pushButton_open_dir_2.setText(QCoreApplication.translate("MainWindow", u"Selecionar", None))
        self.pushButton_execute_2.setText(QCoreApplication.translate("MainWindow", u"Executar", None))
        self.label_log_2.setText(QCoreApplication.translate("MainWindow", u"Convertendo p\u00e1gina 1/27 do arquivo 1/8.", None))
        self.pushButton_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.pushButton_add.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.pushButton_delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"Copyright (C) 2020 Matheus Melo", None))
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"v2.0.0", None))
    # retranslateUi

