# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI_BASE.ui'
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
        MainWindow.resize(1000, 720)
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
        brush11 = QBrush(QColor(210, 210, 210, 128))
        brush11.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
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
        brush12 = QBrush(QColor(210, 210, 210, 128))
        brush12.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
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
        brush13 = QBrush(QColor(51, 153, 255, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush13)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        brush14 = QBrush(QColor(210, 210, 210, 128))
        brush14.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
#endif
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
        self.frame_toggle.setMaximumSize(QSize(80, 16777215))
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
"background-image: url(:/20x20/icons/20x20/ahand.png);\n"
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
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(30)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_top_info.sizePolicy().hasHeightForWidth())
        self.frame_top_info.setSizePolicy(sizePolicy3)
        self.frame_top_info.setMinimumSize(QSize(0, 30))
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
        self.label_top_info_1.setMinimumSize(QSize(0, 20))
        self.label_top_info_1.setMaximumSize(QSize(16777215, 15))
        self.label_top_info_1.setFont(font)
        self.label_top_info_1.setStyleSheet(u"color: rgb(112, 117, 125);")

        self.horizontalLayout_8.addWidget(self.label_top_info_1)

        self.label_top_info_2 = QLabel(self.frame_top_info)
        self.label_top_info_2.setObjectName(u"label_top_info_2")
        self.label_top_info_2.setMinimumSize(QSize(0, 0))
        self.label_top_info_2.setMaximumSize(QSize(250, 20))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setBold(True)
        font2.setWeight(75)
        self.label_top_info_2.setFont(font2)
        self.label_top_info_2.setStyleSheet(u"color: rgb(112, 117, 125);")
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
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy4)
        self.frame_left_menu.setMinimumSize(QSize(80, 0))
        self.frame_left_menu.setMaximumSize(QSize(80, 16777215))
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
        self.frame_extra_menus.setMinimumSize(QSize(70, 0))
        self.frame_extra_menus.setMaximumSize(QSize(16777215, 16777215))
        self.frame_extra_menus.setFrameShape(QFrame.StyledPanel)
        self.frame_extra_menus.setFrameShadow(QFrame.Raised)
        self.layout_menu_bottom = QVBoxLayout(self.frame_extra_menus)
        self.layout_menu_bottom.setSpacing(5)
        self.layout_menu_bottom.setObjectName(u"layout_menu_bottom")
        self.layout_menu_bottom.setContentsMargins(0, 0, 0, 9)

        self.verticalLayout_5.addWidget(self.frame_extra_menus)


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
        self.verticalLayout_9 = QVBoxLayout(self.frame_content)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.page_merge = QWidget()
        self.page_merge.setObjectName(u"page_merge")
        sizePolicy.setHeightForWidth(self.page_merge.sizePolicy().hasHeightForWidth())
        self.page_merge.setSizePolicy(sizePolicy)
        self.verticalLayout_24 = QVBoxLayout(self.page_merge)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(9, 9, 9, 9)
        self.frame_main_merge = QFrame(self.page_merge)
        self.frame_main_merge.setObjectName(u"frame_main_merge")
        sizePolicy.setHeightForWidth(self.frame_main_merge.sizePolicy().hasHeightForWidth())
        self.frame_main_merge.setSizePolicy(sizePolicy)
        self.frame_main_merge.setFrameShape(QFrame.StyledPanel)
        self.frame_main_merge.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_main_merge)
        self.verticalLayout_17.setSpacing(30)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(5, 5, 5, 5)
        self.frame_home = QFrame(self.frame_main_merge)
        self.frame_home.setObjectName(u"frame_home")
        sizePolicy.setHeightForWidth(self.frame_home.sizePolicy().hasHeightForWidth())
        self.frame_home.setSizePolicy(sizePolicy)
        self.frame_home.setMinimumSize(QSize(0, 0))
        self.frame_home.setMaximumSize(QSize(16777215, 16777215))
        self.frame_home.setStyleSheet(u"")
        self.frame_home.setFrameShape(QFrame.StyledPanel)
        self.frame_home.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_home)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(5, 5, 5, 5)
        self.frame_merge = QFrame(self.frame_home)
        self.frame_merge.setObjectName(u"frame_merge")
        sizePolicy4.setHeightForWidth(self.frame_merge.sizePolicy().hasHeightForWidth())
        self.frame_merge.setSizePolicy(sizePolicy4)
        self.frame_merge.setMinimumSize(QSize(0, 0))
        self.frame_merge.setFrameShape(QFrame.StyledPanel)
        self.frame_merge.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_merge)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(9, 9, 9, 9)
        self.frame_description_merge = QFrame(self.frame_merge)
        self.frame_description_merge.setObjectName(u"frame_description_merge")
        self.frame_description_merge.setMinimumSize(QSize(0, 0))
        font3 = QFont()
        font3.setPointSize(13)
        self.frame_description_merge.setFont(font3)
        self.frame_description_merge.setFrameShape(QFrame.StyledPanel)
        self.frame_description_merge.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_description_merge)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(5, 5, 5, 5)
        self.label_description_merge = QLabel(self.frame_description_merge)
        self.label_description_merge.setObjectName(u"label_description_merge")
        self.label_description_merge.setMinimumSize(QSize(0, 0))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(13)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_description_merge.setFont(font4)
        self.label_description_merge.setStyleSheet(u"")

        self.horizontalLayout_14.addWidget(self.label_description_merge, 0, Qt.AlignHCenter)


        self.verticalLayout_10.addWidget(self.frame_description_merge, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.frame_top_page_merge = QFrame(self.frame_merge)
        self.frame_top_page_merge.setObjectName(u"frame_top_page_merge")
        self.frame_top_page_merge.setMinimumSize(QSize(750, 180))
        self.frame_top_page_merge.setMaximumSize(QSize(16777215, 16777215))
        self.frame_top_page_merge.setStyleSheet(u"background-color:#343A4B;\n"
"border-radius: 7px;\n"
"border-top: 3px solid rgb(85, 170, 255);")
        self.frame_top_page_merge.setFrameShape(QFrame.StyledPanel)
        self.frame_top_page_merge.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_top_page_merge)
        self.horizontalLayout_23.setSpacing(20)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(9, 9, 9, 5)
        self.frame_input_merge = QFrame(self.frame_top_page_merge)
        self.frame_input_merge.setObjectName(u"frame_input_merge")
        self.frame_input_merge.setMinimumSize(QSize(0, 0))
        self.frame_input_merge.setMaximumSize(QSize(16777215, 16777215))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        self.frame_input_merge.setFont(font5)
        self.frame_input_merge.setStyleSheet(u"border: 0px;")
        self.frame_input_merge.setFrameShape(QFrame.StyledPanel)
        self.frame_input_merge.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_input_merge)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.pushButton_run_merge = QPushButton(self.frame_input_merge)
        self.pushButton_run_merge.setObjectName(u"pushButton_run_merge")
        self.pushButton_run_merge.setMinimumSize(QSize(50, 35))
        self.pushButton_run_merge.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_run_merge.setAutoFillBackground(False)
        self.pushButton_run_merge.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"	border-radius: 5px;	\n"
"	background-color:#2E3342;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/20x20/icons/20x20/cil-media-play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_run_merge.setIcon(icon3)
        self.pushButton_run_merge.setIconSize(QSize(18, 18))

        self.gridLayout.addWidget(self.pushButton_run_merge, 0, 0, 1, 1)

        self.pushButton_selectFiles_merge = QPushButton(self.frame_input_merge)
        self.pushButton_selectFiles_merge.setObjectName(u"pushButton_selectFiles_merge")
        self.pushButton_selectFiles_merge.setMinimumSize(QSize(180, 35))
        self.pushButton_selectFiles_merge.setMaximumSize(QSize(16777215, 16777215))
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(12)
        self.pushButton_selectFiles_merge.setFont(font6)
        self.pushButton_selectFiles_merge.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"	border-radius: 5px;	\n"
"	background-color:#2E3342;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/20x20/icons/20x20/cil-file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_selectFiles_merge.setIcon(icon4)
        self.pushButton_selectFiles_merge.setIconSize(QSize(18, 18))

        self.gridLayout.addWidget(self.pushButton_selectFiles_merge, 0, 1, 1, 1)


        self.horizontalLayout_23.addWidget(self.frame_input_merge, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame_output_merge = QFrame(self.frame_top_page_merge)
        self.frame_output_merge.setObjectName(u"frame_output_merge")
        self.frame_output_merge.setMinimumSize(QSize(0, 0))
        self.frame_output_merge.setMaximumSize(QSize(16777215, 16777215))
        self.frame_output_merge.setStyleSheet(u"border: 0px;")
        self.frame_output_merge.setFrameShape(QFrame.StyledPanel)
        self.frame_output_merge.setFrameShadow(QFrame.Raised)
        self.formLayout_3 = QFormLayout(self.frame_output_merge)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setContentsMargins(9, 5, 9, 5)
        self.pushButton_outputPath_merge = QPushButton(self.frame_output_merge)
        self.pushButton_outputPath_merge.setObjectName(u"pushButton_outputPath_merge")
        self.pushButton_outputPath_merge.setMinimumSize(QSize(50, 35))
        self.pushButton_outputPath_merge.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"	border-radius: 5px;	\n"
"	background-color:#2E3342;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/20x20/icons/20x20/cil-folder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_outputPath_merge.setIcon(icon5)
        self.pushButton_outputPath_merge.setIconSize(QSize(18, 18))

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.pushButton_outputPath_merge)

        self.lineEdit_outputPath_merge = QLineEdit(self.frame_output_merge)
        self.lineEdit_outputPath_merge.setObjectName(u"lineEdit_outputPath_merge")
        self.lineEdit_outputPath_merge.setMinimumSize(QSize(370, 35))
        self.lineEdit_outputPath_merge.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_outputPath_merge.setFont(font6)
        self.lineEdit_outputPath_merge.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"}")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.lineEdit_outputPath_merge)

        self.lineEdit_filename_merge = QLineEdit(self.frame_output_merge)
        self.lineEdit_filename_merge.setObjectName(u"lineEdit_filename_merge")
        self.lineEdit_filename_merge.setMinimumSize(QSize(370, 35))
        self.lineEdit_filename_merge.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_filename_merge.setFont(font6)
        self.lineEdit_filename_merge.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"}")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.lineEdit_filename_merge)


        self.horizontalLayout_23.addWidget(self.frame_output_merge, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_10.addWidget(self.frame_top_page_merge, 0, Qt.AlignHCenter)


        self.verticalLayout_21.addWidget(self.frame_merge, 0, Qt.AlignHCenter)


        self.verticalLayout_17.addWidget(self.frame_home, 0, Qt.AlignHCenter)

        self.frame_drop_merge = QFrame(self.frame_main_merge)
        self.frame_drop_merge.setObjectName(u"frame_drop_merge")
        sizePolicy.setHeightForWidth(self.frame_drop_merge.sizePolicy().hasHeightForWidth())
        self.frame_drop_merge.setSizePolicy(sizePolicy)
        self.frame_drop_merge.setMinimumSize(QSize(600, 220))
        self.frame_drop_merge.setMaximumSize(QSize(16777215, 16777215))
        self.frame_drop_merge.setFrameShape(QFrame.StyledPanel)
        self.frame_drop_merge.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_drop_merge)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(5, 9, 5, -1)
        self.label_drop_merge = QLabel(self.frame_drop_merge)
        self.label_drop_merge.setObjectName(u"label_drop_merge")
        sizePolicy4.setHeightForWidth(self.label_drop_merge.sizePolicy().hasHeightForWidth())
        self.label_drop_merge.setSizePolicy(sizePolicy4)
        self.label_drop_merge.setMinimumSize(QSize(750, 0))
        self.label_drop_merge.setMaximumSize(QSize(16777215, 16777215))
        font7 = QFont()
        font7.setFamily(u"Segoe UI")
        font7.setPointSize(12)
        font7.setBold(True)
        font7.setWeight(75)
        self.label_drop_merge.setFont(font7)
        self.label_drop_merge.setStyleSheet(u"border-radius: 7px;\n"
"border: 4px dashed rgb(112, 117, 125);\n"
"color: rgb(112, 117, 125);")
        self.label_drop_merge.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_drop_merge, 0, Qt.AlignHCenter)


        self.verticalLayout_17.addWidget(self.frame_drop_merge, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_24.addWidget(self.frame_main_merge, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.stackedWidget.addWidget(self.page_merge)
        self.page_extract = QWidget()
        self.page_extract.setObjectName(u"page_extract")
        self.page_extract.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_22 = QVBoxLayout(self.page_extract)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.frame_main_extract = QFrame(self.page_extract)
        self.frame_main_extract.setObjectName(u"frame_main_extract")
        self.frame_main_extract.setMinimumSize(QSize(0, 0))
        self.frame_main_extract.setMaximumSize(QSize(16777215, 16777215))
        self.frame_main_extract.setFrameShape(QFrame.StyledPanel)
        self.frame_main_extract.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_main_extract)
        self.verticalLayout_13.setSpacing(9)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(-1, -1, -1, 9)
        self.frame_extract_main = QFrame(self.frame_main_extract)
        self.frame_extract_main.setObjectName(u"frame_extract_main")
        self.frame_extract_main.setMaximumSize(QSize(16777215, 16777215))
        self.frame_extract_main.setFrameShape(QFrame.StyledPanel)
        self.frame_extract_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_extract_main)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(9, 5, 9, 5)
        self.frame_description_extract = QFrame(self.frame_extract_main)
        self.frame_description_extract.setObjectName(u"frame_description_extract")
        self.frame_description_extract.setMinimumSize(QSize(0, 0))
        self.frame_description_extract.setFrameShape(QFrame.StyledPanel)
        self.frame_description_extract.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_description_extract)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(5, 5, 5, 5)
        self.label_description_extract = QLabel(self.frame_description_extract)
        self.label_description_extract.setObjectName(u"label_description_extract")
        self.label_description_extract.setMinimumSize(QSize(0, 0))
        self.label_description_extract.setFont(font4)
        self.label_description_extract.setStyleSheet(u"")

        self.horizontalLayout_16.addWidget(self.label_description_extract, 0, Qt.AlignLeft)


        self.verticalLayout_20.addWidget(self.frame_description_extract, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.frame_top_page_extract = QFrame(self.frame_extract_main)
        self.frame_top_page_extract.setObjectName(u"frame_top_page_extract")
        self.frame_top_page_extract.setMinimumSize(QSize(750, 160))
        self.frame_top_page_extract.setMaximumSize(QSize(750, 16777215))
        self.frame_top_page_extract.setStyleSheet(u"background-color:#343A4B;\n"
"border-radius: 7px;\n"
"border-top: 3px solid rgb(85, 170, 255);")
        self.frame_top_page_extract.setFrameShape(QFrame.StyledPanel)
        self.frame_top_page_extract.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_top_page_extract)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(9, 5, 9, 5)
        self.frame_input_left_extract = QFrame(self.frame_top_page_extract)
        self.frame_input_left_extract.setObjectName(u"frame_input_left_extract")
        self.frame_input_left_extract.setStyleSheet(u"border:0px;")
        self.frame_input_left_extract.setFrameShape(QFrame.StyledPanel)
        self.frame_input_left_extract.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_input_left_extract)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(-1, 9, -1, 9)
        self.frame_input_extract = QFrame(self.frame_input_left_extract)
        self.frame_input_extract.setObjectName(u"frame_input_extract")
        self.frame_input_extract.setMinimumSize(QSize(230, 0))
        self.frame_input_extract.setMaximumSize(QSize(16777215, 16777215))
        self.frame_input_extract.setFont(font5)
        self.frame_input_extract.setStyleSheet(u"border: 0px;")
        self.frame_input_extract.setFrameShape(QFrame.StyledPanel)
        self.frame_input_extract.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_input_extract)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(5, 0, 5, 5)
        self.pushButton_run_extract = QPushButton(self.frame_input_extract)
        self.pushButton_run_extract.setObjectName(u"pushButton_run_extract")
        self.pushButton_run_extract.setMinimumSize(QSize(50, 35))
        self.pushButton_run_extract.setMaximumSize(QSize(50, 16777215))
        self.pushButton_run_extract.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"	border-radius: 5px;	\n"
"	background-color:#2E3342;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_run_extract.setIcon(icon3)
        self.pushButton_run_extract.setIconSize(QSize(18, 18))

        self.horizontalLayout_22.addWidget(self.pushButton_run_extract)

        self.pushButton_selectFiles_extract = QPushButton(self.frame_input_extract)
        self.pushButton_selectFiles_extract.setObjectName(u"pushButton_selectFiles_extract")
        self.pushButton_selectFiles_extract.setMinimumSize(QSize(180, 35))
        self.pushButton_selectFiles_extract.setMaximumSize(QSize(180, 16777215))
        self.pushButton_selectFiles_extract.setFont(font6)
        self.pushButton_selectFiles_extract.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"	border-radius: 5px;	\n"
"	background-color:#2E3342;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_selectFiles_extract.setIcon(icon4)
        self.pushButton_selectFiles_extract.setIconSize(QSize(18, 18))

        self.horizontalLayout_22.addWidget(self.pushButton_selectFiles_extract)


        self.verticalLayout_30.addWidget(self.frame_input_extract, 0, Qt.AlignTop)


        self.horizontalLayout_25.addWidget(self.frame_input_left_extract, 0, Qt.AlignTop)

        self.frame_output_extract = QFrame(self.frame_top_page_extract)
        self.frame_output_extract.setObjectName(u"frame_output_extract")
        self.frame_output_extract.setMinimumSize(QSize(0, 0))
        self.frame_output_extract.setMaximumSize(QSize(16777215, 16777215))
        self.frame_output_extract.setStyleSheet(u"border: 0px;")
        self.frame_output_extract.setFrameShape(QFrame.StyledPanel)
        self.frame_output_extract.setFrameShadow(QFrame.Raised)
        self.formLayout_5 = QFormLayout(self.frame_output_extract)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.formLayout_5.setContentsMargins(9, 9, 9, 9)
        self.pushButton_outputPath_extract = QPushButton(self.frame_output_extract)
        self.pushButton_outputPath_extract.setObjectName(u"pushButton_outputPath_extract")
        self.pushButton_outputPath_extract.setMinimumSize(QSize(50, 35))
        self.pushButton_outputPath_extract.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_outputPath_extract.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"	border-radius: 5px;	\n"
"	background-color:#2E3342;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_outputPath_extract.setIcon(icon5)
        self.pushButton_outputPath_extract.setIconSize(QSize(18, 18))

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.pushButton_outputPath_extract)

        self.lineEdit_outputPath_extract = QLineEdit(self.frame_output_extract)
        self.lineEdit_outputPath_extract.setObjectName(u"lineEdit_outputPath_extract")
        self.lineEdit_outputPath_extract.setMinimumSize(QSize(370, 35))
        self.lineEdit_outputPath_extract.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_outputPath_extract.setFont(font6)
        self.lineEdit_outputPath_extract.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"}")

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.lineEdit_outputPath_extract)

        self.lineEdit_filename_extract = QLineEdit(self.frame_output_extract)
        self.lineEdit_filename_extract.setObjectName(u"lineEdit_filename_extract")
        self.lineEdit_filename_extract.setMinimumSize(QSize(370, 35))
        self.lineEdit_filename_extract.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_filename_extract.setFont(font6)
        self.lineEdit_filename_extract.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"}")

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.lineEdit_filename_extract)


        self.horizontalLayout_25.addWidget(self.frame_output_extract, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_20.addWidget(self.frame_top_page_extract, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_13.addWidget(self.frame_extract_main)

        self.frame_options_extract = QFrame(self.frame_main_extract)
        self.frame_options_extract.setObjectName(u"frame_options_extract")
        self.frame_options_extract.setMinimumSize(QSize(750, 130))
        self.frame_options_extract.setMaximumSize(QSize(750, 16777215))
        self.frame_options_extract.setStyleSheet(u"background-color:#343A4B;\n"
"border-radius: 7px;")
        self.frame_options_extract.setFrameShape(QFrame.StyledPanel)
        self.frame_options_extract.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_options_extract)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(-1, 9, -1, 9)
        self.frame_pages_extract = QFrame(self.frame_options_extract)
        self.frame_pages_extract.setObjectName(u"frame_pages_extract")
        self.frame_pages_extract.setFrameShape(QFrame.StyledPanel)
        self.frame_pages_extract.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_pages_extract)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(9, 9, 40, 9)
        self.comboBox_extractPages = QComboBox(self.frame_pages_extract)
        self.comboBox_extractPages.addItem("")
        self.comboBox_extractPages.addItem("")
        self.comboBox_extractPages.setObjectName(u"comboBox_extractPages")
        self.comboBox_extractPages.setMinimumSize(QSize(180, 35))
        self.comboBox_extractPages.setMaximumSize(QSize(180, 35))
        self.comboBox_extractPages.setFont(font6)
        self.comboBox_extractPages.setStyleSheet(u"border: 2px solid rgb(64, 71, 88);\n"
"border-radius: 5px;	\n"
"background-color:#2E3342;")

        self.verticalLayout_23.addWidget(self.comboBox_extractPages)

        self.lineEdit_intPages_extract = QLineEdit(self.frame_pages_extract)
        self.lineEdit_intPages_extract.setObjectName(u"lineEdit_intPages_extract")
        self.lineEdit_intPages_extract.setMinimumSize(QSize(0, 35))
        self.lineEdit_intPages_extract.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_intPages_extract.setFont(font6)
        self.lineEdit_intPages_extract.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
"border-radius: 5px;\n"
"border: 2px solid rgb(27, 29, 35);\n"
"padding-left: 10px;")

        self.verticalLayout_23.addWidget(self.lineEdit_intPages_extract)


        self.horizontalLayout_24.addWidget(self.frame_pages_extract, 0, Qt.AlignHCenter)

        self.frame__checkbox_extract = QFrame(self.frame_options_extract)
        self.frame__checkbox_extract.setObjectName(u"frame__checkbox_extract")
        self.frame__checkbox_extract.setFrameShape(QFrame.StyledPanel)
        self.frame__checkbox_extract.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame__checkbox_extract)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 9, 100, 9)
        self.checkBox_split = QCheckBox(self.frame__checkbox_extract)
        self.checkBox_split.setObjectName(u"checkBox_split")
        self.checkBox_split.setFont(font6)
        self.checkBox_split.setStyleSheet(u"QCheckBox::indicator {\n"
"   border: 2px solid rgb(64, 71, 88);\n"
"	border-radius: 9px;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_25.addWidget(self.checkBox_split)

        self.checkBox_extract = QCheckBox(self.frame__checkbox_extract)
        self.checkBox_extract.setObjectName(u"checkBox_extract")
        self.checkBox_extract.setFont(font6)
        self.checkBox_extract.setStyleSheet(u"QCheckBox::indicator {\n"
"   border: 2px solid rgb(64, 71, 88);\n"
"	border-radius: 9px;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_25.addWidget(self.checkBox_extract)


        self.horizontalLayout_24.addWidget(self.frame__checkbox_extract, 0, Qt.AlignHCenter)


        self.verticalLayout_13.addWidget(self.frame_options_extract, 0, Qt.AlignHCenter)

        self.frame_drop_extract = QFrame(self.frame_main_extract)
        self.frame_drop_extract.setObjectName(u"frame_drop_extract")
        self.frame_drop_extract.setMinimumSize(QSize(750, 0))
        self.frame_drop_extract.setMaximumSize(QSize(16777215, 16777215))
        self.frame_drop_extract.setFrameShape(QFrame.StyledPanel)
        self.frame_drop_extract.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_drop_extract)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(9, 9, 9, -1)
        self.label_drop_extract = QLabel(self.frame_drop_extract)
        self.label_drop_extract.setObjectName(u"label_drop_extract")
        self.label_drop_extract.setMinimumSize(QSize(750, 140))
        self.label_drop_extract.setMaximumSize(QSize(16777215, 16777215))
        self.label_drop_extract.setFont(font7)
        self.label_drop_extract.setStyleSheet(u"border: 4px dashed rgb(112, 117, 125);\n"
"color: rgb(112, 117, 125);")
        self.label_drop_extract.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.label_drop_extract, 0, Qt.AlignVCenter)


        self.verticalLayout_13.addWidget(self.frame_drop_extract, 0, Qt.AlignHCenter)


        self.verticalLayout_22.addWidget(self.frame_main_extract, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.stackedWidget.addWidget(self.page_extract)
        self.page_ocr = QWidget()
        self.page_ocr.setObjectName(u"page_ocr")
        self.verticalLayout_29 = QVBoxLayout(self.page_ocr)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.frame_main_ocr = QFrame(self.page_ocr)
        self.frame_main_ocr.setObjectName(u"frame_main_ocr")
        self.frame_main_ocr.setFrameShape(QFrame.StyledPanel)
        self.frame_main_ocr.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_main_ocr)
        self.verticalLayout_15.setSpacing(30)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(5, 5, 5, 5)
        self.frame_ocr = QFrame(self.frame_main_ocr)
        self.frame_ocr.setObjectName(u"frame_ocr")
        self.frame_ocr.setFrameShape(QFrame.StyledPanel)
        self.frame_ocr.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_ocr)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(9, 9, 9, 9)
        self.frame_description_ocr = QFrame(self.frame_ocr)
        self.frame_description_ocr.setObjectName(u"frame_description_ocr")
        self.frame_description_ocr.setMinimumSize(QSize(0, 0))
        self.frame_description_ocr.setFrameShape(QFrame.StyledPanel)
        self.frame_description_ocr.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_description_ocr)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(5, 5, 5, 5)
        self.label_description_ocr = QLabel(self.frame_description_ocr)
        self.label_description_ocr.setObjectName(u"label_description_ocr")
        self.label_description_ocr.setMinimumSize(QSize(0, 0))
        self.label_description_ocr.setFont(font4)
        self.label_description_ocr.setStyleSheet(u"")

        self.horizontalLayout_27.addWidget(self.label_description_ocr, 0, Qt.AlignLeft)


        self.verticalLayout_27.addWidget(self.frame_description_ocr)

        self.frame_top_page_ocr = QFrame(self.frame_ocr)
        self.frame_top_page_ocr.setObjectName(u"frame_top_page_ocr")
        self.frame_top_page_ocr.setMinimumSize(QSize(750, 180))
        self.frame_top_page_ocr.setMaximumSize(QSize(16777215, 16777215))
        self.frame_top_page_ocr.setStyleSheet(u"background-color:#343A4B;\n"
"border-radius: 7px;\n"
"border-top: 3px solid rgb(85, 170, 255);")
        self.frame_top_page_ocr.setFrameShape(QFrame.StyledPanel)
        self.frame_top_page_ocr.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_top_page_ocr)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(9, 5, 9, 5)
        self.frame_left_ocr = QFrame(self.frame_top_page_ocr)
        self.frame_left_ocr.setObjectName(u"frame_left_ocr")
        self.frame_left_ocr.setStyleSheet(u"border: 0px;")
        self.frame_left_ocr.setFrameShape(QFrame.StyledPanel)
        self.frame_left_ocr.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_left_ocr)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(5, 0, 5, 5)
        self.frame_input_ocr = QFrame(self.frame_left_ocr)
        self.frame_input_ocr.setObjectName(u"frame_input_ocr")
        self.frame_input_ocr.setMinimumSize(QSize(230, 0))
        self.frame_input_ocr.setMaximumSize(QSize(16777215, 16777215))
        self.frame_input_ocr.setFont(font5)
        self.frame_input_ocr.setStyleSheet(u"border: 0px;")
        self.frame_input_ocr.setFrameShape(QFrame.StyledPanel)
        self.frame_input_ocr.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_input_ocr)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(5, 5, 5, 5)
        self.pushButton_selectFiles_ocr = QPushButton(self.frame_input_ocr)
        self.pushButton_selectFiles_ocr.setObjectName(u"pushButton_selectFiles_ocr")
        self.pushButton_selectFiles_ocr.setMinimumSize(QSize(180, 30))
        self.pushButton_selectFiles_ocr.setMaximumSize(QSize(16777215, 35))
        self.pushButton_selectFiles_ocr.setFont(font6)
        self.pushButton_selectFiles_ocr.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"	border-radius: 5px;	\n"
"	background-color:#2E3342;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_selectFiles_ocr.setIcon(icon4)
        self.pushButton_selectFiles_ocr.setIconSize(QSize(18, 18))

        self.gridLayout_5.addWidget(self.pushButton_selectFiles_ocr, 0, 1, 1, 1)

        self.pushButton_run_ocr = QPushButton(self.frame_input_ocr)
        self.pushButton_run_ocr.setObjectName(u"pushButton_run_ocr")
        self.pushButton_run_ocr.setMinimumSize(QSize(50, 35))
        self.pushButton_run_ocr.setMaximumSize(QSize(40, 16777215))
        self.pushButton_run_ocr.setAutoFillBackground(False)
        self.pushButton_run_ocr.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"	border-radius: 5px;	\n"
"	background-color:#2E3342;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_run_ocr.setIcon(icon3)
        self.pushButton_run_ocr.setIconSize(QSize(18, 18))

        self.gridLayout_5.addWidget(self.pushButton_run_ocr, 0, 0, 1, 1)


        self.verticalLayout_28.addWidget(self.frame_input_ocr, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_dpi_ocr = QFrame(self.frame_left_ocr)
        self.frame_dpi_ocr.setObjectName(u"frame_dpi_ocr")
        self.frame_dpi_ocr.setMinimumSize(QSize(140, 0))
        self.frame_dpi_ocr.setFont(font5)
        self.frame_dpi_ocr.setFrameShape(QFrame.StyledPanel)
        self.frame_dpi_ocr.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_dpi_ocr)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(17)
        self.gridLayout_2.setContentsMargins(20, 0, 20, 9)
        self.label_intDpi_ocr = QLabel(self.frame_dpi_ocr)
        self.label_intDpi_ocr.setObjectName(u"label_intDpi_ocr")
        self.label_intDpi_ocr.setMinimumSize(QSize(0, 0))
        self.label_intDpi_ocr.setFont(font6)

        self.gridLayout_2.addWidget(self.label_intDpi_ocr, 0, 0, 1, 1, Qt.AlignHCenter)

        self.lineEdit_intDpi_ocr = QLineEdit(self.frame_dpi_ocr)
        self.lineEdit_intDpi_ocr.setObjectName(u"lineEdit_intDpi_ocr")
        self.lineEdit_intDpi_ocr.setMinimumSize(QSize(0, 30))
        self.lineEdit_intDpi_ocr.setMaximumSize(QSize(55, 16777215))
        self.lineEdit_intDpi_ocr.setFont(font6)
        self.lineEdit_intDpi_ocr.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"}")

        self.gridLayout_2.addWidget(self.lineEdit_intDpi_ocr, 0, 1, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_28.addWidget(self.frame_dpi_ocr, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout_28.addWidget(self.frame_left_ocr, 0, Qt.AlignTop)

        self.frame_output_ocr = QFrame(self.frame_top_page_ocr)
        self.frame_output_ocr.setObjectName(u"frame_output_ocr")
        self.frame_output_ocr.setMinimumSize(QSize(428, 0))
        self.frame_output_ocr.setMaximumSize(QSize(16777215, 16777215))
        self.frame_output_ocr.setStyleSheet(u"border: 0px;")
        self.frame_output_ocr.setFrameShape(QFrame.StyledPanel)
        self.frame_output_ocr.setFrameShadow(QFrame.Raised)
        self.formLayout_6 = QFormLayout(self.frame_output_ocr)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.formLayout_6.setContentsMargins(9, 5, 9, 5)
        self.pushButton_outputPath_ocr = QPushButton(self.frame_output_ocr)
        self.pushButton_outputPath_ocr.setObjectName(u"pushButton_outputPath_ocr")
        self.pushButton_outputPath_ocr.setMinimumSize(QSize(50, 35))
        self.pushButton_outputPath_ocr.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"	border-radius: 5px;	\n"
"	background-color:#2E3342;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_outputPath_ocr.setIcon(icon5)
        self.pushButton_outputPath_ocr.setIconSize(QSize(18, 18))

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.pushButton_outputPath_ocr)

        self.lineEdit_outputPath_ocr = QLineEdit(self.frame_output_ocr)
        self.lineEdit_outputPath_ocr.setObjectName(u"lineEdit_outputPath_ocr")
        self.lineEdit_outputPath_ocr.setMinimumSize(QSize(370, 35))
        self.lineEdit_outputPath_ocr.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_outputPath_ocr.setFont(font6)
        self.lineEdit_outputPath_ocr.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"}")

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.lineEdit_outputPath_ocr)

        self.lineEdit_filename_ocr = QLineEdit(self.frame_output_ocr)
        self.lineEdit_filename_ocr.setObjectName(u"lineEdit_filename_ocr")
        self.lineEdit_filename_ocr.setMinimumSize(QSize(370, 35))
        self.lineEdit_filename_ocr.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_filename_ocr.setFont(font6)
        self.lineEdit_filename_ocr.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"}")

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.lineEdit_filename_ocr)


        self.horizontalLayout_28.addWidget(self.frame_output_ocr, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_27.addWidget(self.frame_top_page_ocr, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_15.addWidget(self.frame_ocr, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_drop_ocr = QFrame(self.frame_main_ocr)
        self.frame_drop_ocr.setObjectName(u"frame_drop_ocr")
        self.frame_drop_ocr.setMinimumSize(QSize(0, 200))
        self.frame_drop_ocr.setMaximumSize(QSize(16777215, 16777215))
        self.frame_drop_ocr.setFrameShape(QFrame.StyledPanel)
        self.frame_drop_ocr.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_drop_ocr)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(5, 0, 5, -1)
        self.label_drop_ocr = QLabel(self.frame_drop_ocr)
        self.label_drop_ocr.setObjectName(u"label_drop_ocr")
        self.label_drop_ocr.setMinimumSize(QSize(750, 0))
        self.label_drop_ocr.setMaximumSize(QSize(16777215, 16777215))
        self.label_drop_ocr.setFont(font7)
        self.label_drop_ocr.setStyleSheet(u"border: 4px dashed rgb(112, 117, 125);\n"
"color: rgb(112, 117, 125);")
        self.label_drop_ocr.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.label_drop_ocr)


        self.verticalLayout_15.addWidget(self.frame_drop_ocr, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_29.addWidget(self.frame_main_ocr, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.stackedWidget.addWidget(self.page_ocr)
        self.page_search = QWidget()
        self.page_search.setObjectName(u"page_search")
        self.verticalLayout_12 = QVBoxLayout(self.page_search)
        self.verticalLayout_12.setSpacing(16)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(14, 5, 20, 5)
        self.frame_top_page_search = QFrame(self.page_search)
        self.frame_top_page_search.setObjectName(u"frame_top_page_search")
        self.frame_top_page_search.setMinimumSize(QSize(860, 0))
        self.frame_top_page_search.setMaximumSize(QSize(840, 16777215))
        self.frame_top_page_search.setFrameShape(QFrame.StyledPanel)
        self.frame_top_page_search.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_top_page_search)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, -1, 5, 0)
        self.frame_description_search = QFrame(self.frame_top_page_search)
        self.frame_description_search.setObjectName(u"frame_description_search")
        self.frame_description_search.setFrameShape(QFrame.StyledPanel)
        self.frame_description_search.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_description_search)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(5, 5, 5, 5)
        self.label_description_search = QLabel(self.frame_description_search)
        self.label_description_search.setObjectName(u"label_description_search")
        self.label_description_search.setFont(font4)

        self.horizontalLayout_30.addWidget(self.label_description_search, 0, Qt.AlignLeft)


        self.verticalLayout_11.addWidget(self.frame_description_search)

        self.frame_middle = QFrame(self.frame_top_page_search)
        self.frame_middle.setObjectName(u"frame_middle")
        self.frame_middle.setMinimumSize(QSize(860, 0))
        self.frame_middle.setMaximumSize(QSize(840, 16777215))
        self.frame_middle.setStyleSheet(u"background-color:#343A4B;\n"
"border-radius: 7px;\n"
"border-top: 3px solid rgb(85, 170, 255);")
        self.frame_middle.setFrameShape(QFrame.StyledPanel)
        self.frame_middle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_middle)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(9, 5, 5, 5)
        self.frame_keywords = QFrame(self.frame_middle)
        self.frame_keywords.setObjectName(u"frame_keywords")
        self.frame_keywords.setMinimumSize(QSize(0, 0))
        self.frame_keywords.setMaximumSize(QSize(16777215, 16777215))
        self.frame_keywords.setStyleSheet(u"border:0px;")
        self.frame_keywords.setFrameShape(QFrame.StyledPanel)
        self.frame_keywords.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_keywords)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(5, 5, 9, 5)
        self.lineEdit_moveto_search = QLineEdit(self.frame_keywords)
        self.lineEdit_moveto_search.setObjectName(u"lineEdit_moveto_search")
        self.lineEdit_moveto_search.setMinimumSize(QSize(0, 35))
        self.lineEdit_moveto_search.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_moveto_search.setFont(font6)
        self.lineEdit_moveto_search.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"}")
        self.lineEdit_moveto_search.setReadOnly(False)

        self.gridLayout_3.addWidget(self.lineEdit_moveto_search, 0, 2, 1, 1)

        self.label_else_search = QLabel(self.frame_keywords)
        self.label_else_search.setObjectName(u"label_else_search")
        self.label_else_search.setMinimumSize(QSize(200, 0))
        self.label_else_search.setMaximumSize(QSize(16777215, 16777215))
        self.label_else_search.setFont(font6)
        self.label_else_search.setStyleSheet(u"color: rgb(112, 117, 125);")
        self.label_else_search.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_else_search, 1, 3, 1, 1, Qt.AlignHCenter)

        self.label_moveto_search = QLabel(self.frame_keywords)
        self.label_moveto_search.setObjectName(u"label_moveto_search")
        self.label_moveto_search.setMaximumSize(QSize(16777215, 16777215))
        self.label_moveto_search.setFont(font6)
        self.label_moveto_search.setStyleSheet(u"color: rgb(112, 117, 125);")
        self.label_moveto_search.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_moveto_search, 1, 2, 1, 1, Qt.AlignHCenter)

        self.pushButton_run_search = QPushButton(self.frame_keywords)
        self.pushButton_run_search.setObjectName(u"pushButton_run_search")
        self.pushButton_run_search.setMinimumSize(QSize(120, 35))
        self.pushButton_run_search.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_run_search.setFont(font6)
        self.pushButton_run_search.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"	border-radius: 5px;	\n"
"	background-color:#2E3342;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/16x16/icons/16x16/cil-media-play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_run_search.setIcon(icon6)
        self.pushButton_run_search.setIconSize(QSize(18, 18))

        self.gridLayout_3.addWidget(self.pushButton_run_search, 0, 0, 1, 1)

        self.lineEdit_else_search = QLineEdit(self.frame_keywords)
        self.lineEdit_else_search.setObjectName(u"lineEdit_else_search")
        self.lineEdit_else_search.setMinimumSize(QSize(0, 35))
        self.lineEdit_else_search.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_else_search.setFont(font6)
        self.lineEdit_else_search.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"}")

        self.gridLayout_3.addWidget(self.lineEdit_else_search, 0, 3, 1, 1)

        self.label_keywords_search = QLabel(self.frame_keywords)
        self.label_keywords_search.setObjectName(u"label_keywords_search")
        self.label_keywords_search.setMinimumSize(QSize(0, 0))
        self.label_keywords_search.setMaximumSize(QSize(16777215, 16777215))
        self.label_keywords_search.setFont(font6)
        self.label_keywords_search.setStyleSheet(u"color: rgb(112, 117, 125);")
        self.label_keywords_search.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_keywords_search, 1, 1, 1, 1, Qt.AlignHCenter)

        self.lineEdit_keywords_search = QLineEdit(self.frame_keywords)
        self.lineEdit_keywords_search.setObjectName(u"lineEdit_keywords_search")
        self.lineEdit_keywords_search.setMinimumSize(QSize(230, 35))
        self.lineEdit_keywords_search.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_keywords_search.setFont(font6)
        self.lineEdit_keywords_search.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"}")

        self.gridLayout_3.addWidget(self.lineEdit_keywords_search, 0, 1, 1, 1)


        self.verticalLayout_19.addWidget(self.frame_keywords)


        self.verticalLayout_11.addWidget(self.frame_middle)


        self.verticalLayout_12.addWidget(self.frame_top_page_search, 0, Qt.AlignHCenter)

        self.frame_top_page = QFrame(self.page_search)
        self.frame_top_page.setObjectName(u"frame_top_page")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_top_page.sizePolicy().hasHeightForWidth())
        self.frame_top_page.setSizePolicy(sizePolicy5)
        self.frame_top_page.setMinimumSize(QSize(860, 110))
        self.frame_top_page.setMaximumSize(QSize(860, 16777215))
        self.frame_top_page.setStyleSheet(u"background-color:#343A4B;\n"
"border-radius: 7px;")
        self.frame_top_page.setFrameShape(QFrame.StyledPanel)
        self.frame_top_page.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_top_page)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(9, 5, 9, 5)
        self.frame_input = QFrame(self.frame_top_page)
        self.frame_input.setObjectName(u"frame_input")
        self.frame_input.setMinimumSize(QSize(180, 0))
        self.frame_input.setMaximumSize(QSize(170, 16777215))
        self.frame_input.setFont(font5)
        self.frame_input.setStyleSheet(u"border: 0px;")
        self.frame_input.setFrameShape(QFrame.StyledPanel)
        self.frame_input.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_input)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(9, 5, 5, 5)
        self.pushButton_selectFiles_search = QPushButton(self.frame_input)
        self.pushButton_selectFiles_search.setObjectName(u"pushButton_selectFiles_search")
        self.pushButton_selectFiles_search.setMinimumSize(QSize(170, 35))
        self.pushButton_selectFiles_search.setMaximumSize(QSize(120, 16777215))
        font8 = QFont()
        font8.setFamily(u"Segoe UI")
        font8.setPointSize(11)
        self.pushButton_selectFiles_search.setFont(font8)
        self.pushButton_selectFiles_search.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"	border-radius: 5px;	\n"
"	background-color:#2E3342;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_selectFiles_search.setIcon(icon4)
        self.pushButton_selectFiles_search.setIconSize(QSize(18, 18))

        self.verticalLayout_14.addWidget(self.pushButton_selectFiles_search)


        self.horizontalLayout_13.addWidget(self.frame_input, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_output = QFrame(self.frame_top_page)
        self.frame_output.setObjectName(u"frame_output")
        self.frame_output.setMinimumSize(QSize(310, 0))
        self.frame_output.setMaximumSize(QSize(16777215, 16777215))
        self.frame_output.setStyleSheet(u"border: 0px;")
        self.frame_output.setFrameShape(QFrame.StyledPanel)
        self.frame_output.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_output)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(4, 5, 14, 5)
        self.pushButton_outputPath_search = QPushButton(self.frame_output)
        self.pushButton_outputPath_search.setObjectName(u"pushButton_outputPath_search")
        self.pushButton_outputPath_search.setMinimumSize(QSize(50, 35))
        self.pushButton_outputPath_search.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"	border-radius: 5px;	\n"
"	background-color:#2E3342;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_outputPath_search.setIcon(icon5)
        self.pushButton_outputPath_search.setIconSize(QSize(18, 18))

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.pushButton_outputPath_search)

        self.lineEdit_outputPath_search = QLineEdit(self.frame_output)
        self.lineEdit_outputPath_search.setObjectName(u"lineEdit_outputPath_search")
        self.lineEdit_outputPath_search.setMinimumSize(QSize(0, 35))
        self.lineEdit_outputPath_search.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_outputPath_search.setFont(font6)
        self.lineEdit_outputPath_search.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"}")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_outputPath_search)

        self.lineEdit_filename_search = QLineEdit(self.frame_output)
        self.lineEdit_filename_search.setObjectName(u"lineEdit_filename_search")
        self.lineEdit_filename_search.setMinimumSize(QSize(0, 35))
        self.lineEdit_filename_search.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_filename_search.setFont(font6)
        self.lineEdit_filename_search.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"}")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_filename_search)


        self.horizontalLayout_13.addWidget(self.frame_output, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame_checkBox_ = QFrame(self.frame_top_page)
        self.frame_checkBox_.setObjectName(u"frame_checkBox_")
        self.frame_checkBox_.setMinimumSize(QSize(0, 0))
        self.frame_checkBox_.setMaximumSize(QSize(16777215, 16777215))
        font9 = QFont()
        font9.setFamily(u"Segoe UI")
        font9.setPointSize(9)
        self.frame_checkBox_.setFont(font9)
        self.frame_checkBox_.setStyleSheet(u"border: 0px;")
        self.frame_checkBox_.setFrameShape(QFrame.StyledPanel)
        self.frame_checkBox_.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_checkBox_)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(20)
        self.gridLayout_4.setContentsMargins(0, 5, 9, 5)
        self.checkBox_ignorePontuation_search = QCheckBox(self.frame_checkBox_)
        self.checkBox_ignorePontuation_search.setObjectName(u"checkBox_ignorePontuation_search")
        self.checkBox_ignorePontuation_search.setMinimumSize(QSize(0, 20))
        self.checkBox_ignorePontuation_search.setFont(font)
        self.checkBox_ignorePontuation_search.setStyleSheet(u"QCheckBox::indicator {\n"
"   border: 2px solid rgb(64, 71, 88);\n"
"	border-radius: 9px;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"}")

        self.gridLayout_4.addWidget(self.checkBox_ignorePontuation_search, 2, 0, 1, 1)

        self.checkBox_ignoreSpecialChar_search = QCheckBox(self.frame_checkBox_)
        self.checkBox_ignoreSpecialChar_search.setObjectName(u"checkBox_ignoreSpecialChar_search")
        self.checkBox_ignoreSpecialChar_search.setMinimumSize(QSize(0, 20))
        self.checkBox_ignoreSpecialChar_search.setFont(font)
        self.checkBox_ignoreSpecialChar_search.setStyleSheet(u"QCheckBox::indicator {\n"
"   border: 2px solid rgb(64, 71, 88);\n"
"	border-radius: 9px;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"}")
        self.checkBox_ignoreSpecialChar_search.setTristate(False)

        self.gridLayout_4.addWidget(self.checkBox_ignoreSpecialChar_search, 1, 0, 1, 1)

        self.checkBox_onlyPages_search = QCheckBox(self.frame_checkBox_)
        self.checkBox_onlyPages_search.setObjectName(u"checkBox_onlyPages_search")
        self.checkBox_onlyPages_search.setMinimumSize(QSize(0, 20))
        self.checkBox_onlyPages_search.setFont(font)
        self.checkBox_onlyPages_search.setStyleSheet(u"QCheckBox::indicator {\n"
"   border: 2px solid rgb(64, 71, 88);\n"
"	border-radius: 9px;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"}")

        self.gridLayout_4.addWidget(self.checkBox_onlyPages_search, 0, 0, 1, 1)

        self.checkBox_ignoreSpaces_search = QCheckBox(self.frame_checkBox_)
        self.checkBox_ignoreSpaces_search.setObjectName(u"checkBox_ignoreSpaces_search")
        self.checkBox_ignoreSpaces_search.setMinimumSize(QSize(0, 20))
        self.checkBox_ignoreSpaces_search.setFont(font)
        self.checkBox_ignoreSpaces_search.setStyleSheet(u"QCheckBox::indicator {\n"
"   border: 2px solid rgb(64, 71, 88);\n"
"	border-radius: 9px;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"}")

        self.gridLayout_4.addWidget(self.checkBox_ignoreSpaces_search, 0, 1, 1, 1)

        self.checkBox_ignoreFirstPage_search = QCheckBox(self.frame_checkBox_)
        self.checkBox_ignoreFirstPage_search.setObjectName(u"checkBox_ignoreFirstPage_search")
        self.checkBox_ignoreFirstPage_search.setMinimumSize(QSize(0, 20))
        self.checkBox_ignoreFirstPage_search.setFont(font)
        self.checkBox_ignoreFirstPage_search.setStyleSheet(u"QCheckBox::indicator {\n"
"   border: 2px solid rgb(64, 71, 88);\n"
"	border-radius: 9px;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"}")

        self.gridLayout_4.addWidget(self.checkBox_ignoreFirstPage_search, 1, 1, 1, 1)


        self.horizontalLayout_13.addWidget(self.frame_checkBox_, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_12.addWidget(self.frame_top_page, 0, Qt.AlignHCenter)

        self.frame_drop_search = QFrame(self.page_search)
        self.frame_drop_search.setObjectName(u"frame_drop_search")
        self.frame_drop_search.setMinimumSize(QSize(0, 0))
        self.frame_drop_search.setMaximumSize(QSize(860, 16777215))
        self.frame_drop_search.setFrameShape(QFrame.StyledPanel)
        self.frame_drop_search.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_drop_search)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(9, 0, 9, 0)
        self.label_drop_search = QLabel(self.frame_drop_search)
        self.label_drop_search.setObjectName(u"label_drop_search")
        self.label_drop_search.setMinimumSize(QSize(840, 90))
        self.label_drop_search.setMaximumSize(QSize(16777215, 100))
        self.label_drop_search.setFont(font7)
        self.label_drop_search.setStyleSheet(u"border: 4px dashed rgb(112, 117, 125);\n"
"color: rgb(112, 117, 125);")
        self.label_drop_search.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_drop_search)


        self.verticalLayout_12.addWidget(self.frame_drop_search, 0, Qt.AlignHCenter)

        self.frame_tab = QFrame(self.page_search)
        self.frame_tab.setObjectName(u"frame_tab")
        self.frame_tab.setMinimumSize(QSize(860, 0))
        self.frame_tab.setStyleSheet(u"background-color:#343A4B;\n"
"border-radius: 7px;")
        self.frame_tab.setFrameShape(QFrame.StyledPanel)
        self.frame_tab.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_tab)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(9, 3, 9, 9)
        self.frame_vbuttons = QFrame(self.frame_tab)
        self.frame_vbuttons.setObjectName(u"frame_vbuttons")
        self.frame_vbuttons.setFrameShape(QFrame.StyledPanel)
        self.frame_vbuttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_vbuttons)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 5, 0, 5)
        self.pushButton_addTable_search = QPushButton(self.frame_vbuttons)
        self.pushButton_addTable_search.setObjectName(u"pushButton_addTable_search")
        self.pushButton_addTable_search.setMinimumSize(QSize(40, 30))
        self.pushButton_addTable_search.setMaximumSize(QSize(40, 16777215))
        self.pushButton_addTable_search.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"	border-radius: 5px;	\n"
"	background-color:#2E3342;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/20x20/icons/20x20/cil-library-add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_addTable_search.setIcon(icon7)
        self.pushButton_addTable_search.setIconSize(QSize(18, 18))

        self.horizontalLayout_11.addWidget(self.pushButton_addTable_search)

        self.pushButton_deleteTable_search = QPushButton(self.frame_vbuttons)
        self.pushButton_deleteTable_search.setObjectName(u"pushButton_deleteTable_search")
        self.pushButton_deleteTable_search.setMinimumSize(QSize(40, 30))
        self.pushButton_deleteTable_search.setMaximumSize(QSize(40, 16777215))
        self.pushButton_deleteTable_search.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"	border-radius: 5px;	\n"
"	background-color:#2E3342;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/20x20/icons/20x20/cil-trash.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_deleteTable_search.setIcon(icon8)
        self.pushButton_deleteTable_search.setIconSize(QSize(18, 18))

        self.horizontalLayout_11.addWidget(self.pushButton_deleteTable_search)


        self.verticalLayout_7.addWidget(self.frame_vbuttons, 0, Qt.AlignLeft)

        self.tabWidget = QTabWidget(self.frame_tab)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setFont(font9)
        self.tabWidget.setStyleSheet(u"QTabBar::tab {\n"
"    background: rgb(39, 44, 54);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"	background-color: rgb(85, 170, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	\n"
"}\n"
"")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Triangular)
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setStyleSheet(u"")
        self.horizontalLayout_Table = QHBoxLayout(self.tab)
        self.horizontalLayout_Table.setObjectName(u"horizontalLayout_Table")
        self.horizontalLayout_Table.setContentsMargins(5, 0, 0, 0)
        self.tableWidget = QTableWidget(self.tab)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
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
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderVi"
                        "ew::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"")
        self.tableWidget.setFrameShape(QFrame.StyledPanel)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setTabKeyNavigation(True)
        self.tableWidget.setProperty("showDropIndicator", True)
        self.tableWidget.setDragDropOverwriteMode(True)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.tableWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)

        self.horizontalLayout_Table.addWidget(self.tableWidget)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setStyleSheet(u"")
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_7.addWidget(self.tabWidget)


        self.verticalLayout_12.addWidget(self.frame_tab)

        self.stackedWidget.addWidget(self.page_search)
        self.page_exportToTable = QWidget()
        self.page_exportToTable.setObjectName(u"page_exportToTable")
        self.verticalLayout_32 = QVBoxLayout(self.page_exportToTable)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.frame_exportToTable = QFrame(self.page_exportToTable)
        self.frame_exportToTable.setObjectName(u"frame_exportToTable")
        self.frame_exportToTable.setFrameShape(QFrame.StyledPanel)
        self.frame_exportToTable.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_exportToTable)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.frame_export = QFrame(self.frame_exportToTable)
        self.frame_export.setObjectName(u"frame_export")
        sizePolicy4.setHeightForWidth(self.frame_export.sizePolicy().hasHeightForWidth())
        self.frame_export.setSizePolicy(sizePolicy4)
        self.frame_export.setMinimumSize(QSize(0, 0))
        self.frame_export.setFrameShape(QFrame.StyledPanel)
        self.frame_export.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_export)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(9, 9, 9, 9)
        self.frame_description_export = QFrame(self.frame_export)
        self.frame_description_export.setObjectName(u"frame_description_export")
        self.frame_description_export.setMinimumSize(QSize(0, 0))
        self.frame_description_export.setFont(font3)
        self.frame_description_export.setFrameShape(QFrame.StyledPanel)
        self.frame_description_export.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_description_export)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(5, 5, 5, 5)
        self.label_description_export = QLabel(self.frame_description_export)
        self.label_description_export.setObjectName(u"label_description_export")
        self.label_description_export.setMinimumSize(QSize(0, 0))
        self.label_description_export.setFont(font4)
        self.label_description_export.setStyleSheet(u"")

        self.horizontalLayout_31.addWidget(self.label_description_export, 0, Qt.AlignHCenter)


        self.verticalLayout_26.addWidget(self.frame_description_export, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.frame_top_page_export = QFrame(self.frame_export)
        self.frame_top_page_export.setObjectName(u"frame_top_page_export")
        self.frame_top_page_export.setMinimumSize(QSize(750, 180))
        self.frame_top_page_export.setMaximumSize(QSize(16777215, 16777215))
        self.frame_top_page_export.setStyleSheet(u"background-color:#343A4B;\n"
"border-radius: 7px;\n"
"border-top: 3px solid rgb(85, 170, 255);")
        self.frame_top_page_export.setFrameShape(QFrame.StyledPanel)
        self.frame_top_page_export.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_top_page_export)
        self.horizontalLayout_32.setSpacing(20)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(9, 9, 9, 5)
        self.frame_input_export = QFrame(self.frame_top_page_export)
        self.frame_input_export.setObjectName(u"frame_input_export")
        self.frame_input_export.setMinimumSize(QSize(0, 0))
        self.frame_input_export.setMaximumSize(QSize(16777215, 16777215))
        self.frame_input_export.setFont(font5)
        self.frame_input_export.setStyleSheet(u"border: 0px;")
        self.frame_input_export.setFrameShape(QFrame.StyledPanel)
        self.frame_input_export.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_input_export)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(6)
        self.gridLayout_6.setContentsMargins(5, 5, 5, 5)
        self.pushButton_run_export = QPushButton(self.frame_input_export)
        self.pushButton_run_export.setObjectName(u"pushButton_run_export")
        self.pushButton_run_export.setMinimumSize(QSize(50, 35))
        self.pushButton_run_export.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_run_export.setAutoFillBackground(False)
        self.pushButton_run_export.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"	border-radius: 5px;	\n"
"	background-color:#2E3342;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_run_export.setIcon(icon3)
        self.pushButton_run_export.setIconSize(QSize(18, 18))

        self.gridLayout_6.addWidget(self.pushButton_run_export, 0, 0, 1, 1)

        self.pushButton_selectFiles_export = QPushButton(self.frame_input_export)
        self.pushButton_selectFiles_export.setObjectName(u"pushButton_selectFiles_export")
        self.pushButton_selectFiles_export.setMinimumSize(QSize(180, 35))
        self.pushButton_selectFiles_export.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_selectFiles_export.setFont(font6)
        self.pushButton_selectFiles_export.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"	border-radius: 5px;	\n"
"	background-color:#2E3342;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_selectFiles_export.setIcon(icon4)
        self.pushButton_selectFiles_export.setIconSize(QSize(18, 18))

        self.gridLayout_6.addWidget(self.pushButton_selectFiles_export, 0, 1, 1, 1)


        self.horizontalLayout_32.addWidget(self.frame_input_export, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame_output_export = QFrame(self.frame_top_page_export)
        self.frame_output_export.setObjectName(u"frame_output_export")
        self.frame_output_export.setMinimumSize(QSize(0, 0))
        self.frame_output_export.setMaximumSize(QSize(16777215, 16777215))
        self.frame_output_export.setStyleSheet(u"border: 0px;")
        self.frame_output_export.setFrameShape(QFrame.StyledPanel)
        self.frame_output_export.setFrameShadow(QFrame.Raised)
        self.formLayout_4 = QFormLayout(self.frame_output_export)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setContentsMargins(9, 5, 9, 5)
        self.pushButton_outputPath_export = QPushButton(self.frame_output_export)
        self.pushButton_outputPath_export.setObjectName(u"pushButton_outputPath_export")
        self.pushButton_outputPath_export.setMinimumSize(QSize(50, 35))
        self.pushButton_outputPath_export.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"	border-radius: 5px;	\n"
"	background-color:#2E3342;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_outputPath_export.setIcon(icon5)
        self.pushButton_outputPath_export.setIconSize(QSize(18, 18))

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.pushButton_outputPath_export)

        Ui_MainWindow.lineEdit_outputPath_export = QLineEdit(self.frame_output_export)
        self.lineEdit_outputPath_export.setObjectName(u"lineEdit_outputPath_export")
        self.lineEdit_outputPath_export.setMinimumSize(QSize(370, 35))
        self.lineEdit_outputPath_export.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_outputPath_export.setFont(font6)
        self.lineEdit_outputPath_export.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"}")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.lineEdit_outputPath_export)

        Ui_MainWindow.lineEdit_filename_export = QLineEdit(self.frame_output_export)
        self.lineEdit_filename_export.setObjectName(u"lineEdit_filename_export")
        self.lineEdit_filename_export.setMinimumSize(QSize(370, 35))
        self.lineEdit_filename_export.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_filename_export.setFont(font6)
        self.lineEdit_filename_export.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"}")

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.lineEdit_filename_export)


        self.horizontalLayout_32.addWidget(self.frame_output_export, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_26.addWidget(self.frame_top_page_export, 0, Qt.AlignHCenter)


        self.horizontalLayout_20.addWidget(self.frame_export, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_32.addWidget(self.frame_exportToTable)

        self.frame_drop_export = QFrame(self.page_exportToTable)
        self.frame_drop_export.setObjectName(u"frame_drop_export")
        self.frame_drop_export.setMinimumSize(QSize(0, 40))
        self.frame_drop_export.setFrameShape(QFrame.StyledPanel)
        self.frame_drop_export.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_drop_export)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.label_drop_export = QLabel(self.frame_drop_export)
        self.label_drop_export.setObjectName(u"label_drop_export")
        sizePolicy4.setHeightForWidth(self.label_drop_export.sizePolicy().hasHeightForWidth())
        self.label_drop_export.setSizePolicy(sizePolicy4)
        self.label_drop_export.setMinimumSize(QSize(750, 100))
        self.label_drop_export.setMaximumSize(QSize(16777215, 16777215))
        self.label_drop_export.setFont(font7)
        self.label_drop_export.setStyleSheet(u"border-radius: 7px;\n"
"border: 4px dashed rgb(112, 117, 125);\n"
"color: rgb(112, 117, 125);")
        self.label_drop_export.setAlignment(Qt.AlignCenter)

        self.verticalLayout_33.addWidget(self.label_drop_export)


        self.verticalLayout_32.addWidget(self.frame_drop_export, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame_export_table = QFrame(self.page_exportToTable)
        self.frame_export_table.setObjectName(u"frame_export_table")
        self.frame_export_table.setMinimumSize(QSize(780, 0))
        self.frame_export_table.setMaximumSize(QSize(16777215, 16777215))
        self.frame_export_table.setFrameShape(QFrame.StyledPanel)
        self.frame_export_table.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_export_table)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(5, 5, 5, 5)
        self.frame_vbuttons_export = QFrame(self.frame_export_table)
        self.frame_vbuttons_export.setObjectName(u"frame_vbuttons_export")
        self.frame_vbuttons_export.setMinimumSize(QSize(0, 40))
        self.frame_vbuttons_export.setFrameShape(QFrame.StyledPanel)
        self.frame_vbuttons_export.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_vbuttons_export)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.pushButton_add_column_export = QPushButton(self.frame_vbuttons_export)
        self.pushButton_add_column_export.setObjectName(u"pushButton_add_column_export")
        self.pushButton_add_column_export.setMinimumSize(QSize(40, 30))
        self.pushButton_add_column_export.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_add_column_export.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"	border-radius: 5px;	\n"
"	background-color:#2E3342;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/16x16/icons/16x16/cil-plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_add_column_export.setIcon(icon9)
        self.pushButton_add_column_export.setIconSize(QSize(18, 18))

        self.horizontalLayout_26.addWidget(self.pushButton_add_column_export)

        self.pushButton_remove_column_export = QPushButton(self.frame_vbuttons_export)
        self.pushButton_remove_column_export.setObjectName(u"pushButton_remove_column_export")
        self.pushButton_remove_column_export.setMinimumSize(QSize(40, 30))
        self.pushButton_remove_column_export.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_remove_column_export.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"	border-radius: 5px;	\n"
"	background-color:#2E3342;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_remove_column_export.setIcon(icon8)
        self.pushButton_remove_column_export.setIconSize(QSize(18, 18))

        self.horizontalLayout_26.addWidget(self.pushButton_remove_column_export)


        self.verticalLayout_31.addWidget(self.frame_vbuttons_export, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_tab_export = QFrame(self.frame_export_table)
        self.frame_tab_export.setObjectName(u"frame_tab_export")
        self.frame_tab_export.setMinimumSize(QSize(0, 0))
        self.frame_tab_export.setMaximumSize(QSize(768, 100))
        self.frame_tab_export.setFrameShape(QFrame.StyledPanel)
        self.frame_tab_export.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_tab_export)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(5, 0, 5, 0)
        Ui_MainWindow.tableWidget_2 = QTableWidget(self.frame_tab_export)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setMinimumSize(QSize(0, 100))
        font10 = QFont()
        font10.setPointSize(8)
        self.tableWidget_2.setFont(font10)
        self.tableWidget_2.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
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
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderVi"
                        "ew::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"")
        self.tableWidget_2.setShowGrid(True)
        self.tableWidget_2.setSortingEnabled(False)
        self.tableWidget_2.setWordWrap(True)
        self.tableWidget_2.setCornerButtonEnabled(True)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.horizontalHeader().setVisible(False)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.horizontalHeader().setHighlightSections(True)
        self.tableWidget_2.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.verticalHeader().setHighlightSections(True)

        self.horizontalLayout_33.addWidget(self.tableWidget_2)


        self.verticalLayout_31.addWidget(self.frame_tab_export)


        self.verticalLayout_32.addWidget(self.frame_export_table, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.stackedWidget.addWidget(self.page_exportToTable)
        self.page_zip = QWidget()
        self.page_zip.setObjectName(u"page_zip")
        self.verticalLayout_8 = QVBoxLayout(self.page_zip)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_main_zip = QFrame(self.page_zip)
        self.frame_main_zip.setObjectName(u"frame_main_zip")
        self.frame_main_zip.setFrameShape(QFrame.StyledPanel)
        self.frame_main_zip.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_main_zip)
        self.verticalLayout_18.setSpacing(30)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 5, 0, 5)
        self.frame_zip = QFrame(self.frame_main_zip)
        self.frame_zip.setObjectName(u"frame_zip")
        self.frame_zip.setFrameShape(QFrame.StyledPanel)
        self.frame_zip.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_zip)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_description_zip = QFrame(self.frame_zip)
        self.frame_description_zip.setObjectName(u"frame_description_zip")
        self.frame_description_zip.setMinimumSize(QSize(0, 0))
        self.frame_description_zip.setFrameShape(QFrame.StyledPanel)
        self.frame_description_zip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_description_zip)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(5, 5, 5, 5)
        self.label_description_zip = QLabel(self.frame_description_zip)
        self.label_description_zip.setObjectName(u"label_description_zip")
        self.label_description_zip.setMinimumSize(QSize(0, 0))
        self.label_description_zip.setFont(font4)
        self.label_description_zip.setStyleSheet(u"")

        self.horizontalLayout_21.addWidget(self.label_description_zip, 0, Qt.AlignLeft)


        self.verticalLayout_6.addWidget(self.frame_description_zip)

        self.frame_top_page_zip = QFrame(self.frame_zip)
        self.frame_top_page_zip.setObjectName(u"frame_top_page_zip")
        self.frame_top_page_zip.setMinimumSize(QSize(750, 180))
        self.frame_top_page_zip.setMaximumSize(QSize(16777215, 16777215))
        self.frame_top_page_zip.setStyleSheet(u"background-color:#343A4B;\n"
"border-radius: 7px;\n"
"border-top: 3px solid rgb(85, 170, 255);")
        self.frame_top_page_zip.setFrameShape(QFrame.StyledPanel)
        self.frame_top_page_zip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_top_page_zip)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 5, 0, 5)
        self.frame_input_zip = QFrame(self.frame_top_page_zip)
        self.frame_input_zip.setObjectName(u"frame_input_zip")
        self.frame_input_zip.setMinimumSize(QSize(0, 0))
        self.frame_input_zip.setMaximumSize(QSize(16777215, 16777215))
        self.frame_input_zip.setFont(font5)
        self.frame_input_zip.setStyleSheet(u"border: 0px;")
        self.frame_input_zip.setFrameShape(QFrame.StyledPanel)
        self.frame_input_zip.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_input_zip)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(9, 5, 9, 5)
        self.lineEdit_rootDirectory_zip = QLineEdit(self.frame_input_zip)
        self.lineEdit_rootDirectory_zip.setObjectName(u"lineEdit_rootDirectory_zip")
        self.lineEdit_rootDirectory_zip.setMinimumSize(QSize(260, 35))
        self.lineEdit_rootDirectory_zip.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_rootDirectory_zip.setFont(font6)
        self.lineEdit_rootDirectory_zip.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"}")

        self.gridLayout_7.addWidget(self.lineEdit_rootDirectory_zip, 1, 2, 1, 1)

        self.pushButton_selectRootDirectory_zip = QPushButton(self.frame_input_zip)
        self.pushButton_selectRootDirectory_zip.setObjectName(u"pushButton_selectRootDirectory_zip")
        self.pushButton_selectRootDirectory_zip.setMinimumSize(QSize(50, 35))
        self.pushButton_selectRootDirectory_zip.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"	border-radius: 5px;	\n"
"	background-color:#2E3342;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_selectRootDirectory_zip.setIcon(icon5)
        self.pushButton_selectRootDirectory_zip.setIconSize(QSize(18, 18))

        self.gridLayout_7.addWidget(self.pushButton_selectRootDirectory_zip, 1, 1, 1, 1)

        self.pushButton_run_zip = QPushButton(self.frame_input_zip)
        self.pushButton_run_zip.setObjectName(u"pushButton_run_zip")
        self.pushButton_run_zip.setMinimumSize(QSize(50, 35))
        self.pushButton_run_zip.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_run_zip.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"	border-radius: 5px;	\n"
"	background-color:#2E3342;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_run_zip.setIcon(icon3)
        self.pushButton_run_zip.setIconSize(QSize(18, 18))

        self.gridLayout_7.addWidget(self.pushButton_run_zip, 1, 0, 1, 1)


        self.horizontalLayout_29.addWidget(self.frame_input_zip, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame_output_zip = QFrame(self.frame_top_page_zip)
        self.frame_output_zip.setObjectName(u"frame_output_zip")
        self.frame_output_zip.setMinimumSize(QSize(432, 115))
        self.frame_output_zip.setMaximumSize(QSize(428, 16777215))
        self.frame_output_zip.setStyleSheet(u"border: 0px;")
        self.frame_output_zip.setFrameShape(QFrame.StyledPanel)
        self.frame_output_zip.setFrameShadow(QFrame.Raised)
        self.formLayout_7 = QFormLayout(self.frame_output_zip)
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.formLayout_7.setContentsMargins(9, 5, 12, 5)
        self.pushButton_outputPath_zip = QPushButton(self.frame_output_zip)
        self.pushButton_outputPath_zip.setObjectName(u"pushButton_outputPath_zip")
        self.pushButton_outputPath_zip.setMinimumSize(QSize(50, 35))
        self.pushButton_outputPath_zip.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"	border-radius: 5px;	\n"
"	background-color:#2E3342;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_outputPath_zip.setIcon(icon5)
        self.pushButton_outputPath_zip.setIconSize(QSize(18, 18))

        self.formLayout_7.setWidget(0, QFormLayout.LabelRole, self.pushButton_outputPath_zip)

        self.lineEdit_outputPath_zip = QLineEdit(self.frame_output_zip)
        self.lineEdit_outputPath_zip.setObjectName(u"lineEdit_outputPath_zip")
        self.lineEdit_outputPath_zip.setMinimumSize(QSize(0, 35))
        self.lineEdit_outputPath_zip.setMaximumSize(QSize(355, 16777215))
        self.lineEdit_outputPath_zip.setFont(font6)
        self.lineEdit_outputPath_zip.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"}")

        self.formLayout_7.setWidget(0, QFormLayout.FieldRole, self.lineEdit_outputPath_zip)

        self.lineEdit_filename_zip = QLineEdit(self.frame_output_zip)
        self.lineEdit_filename_zip.setObjectName(u"lineEdit_filename_zip")
        self.lineEdit_filename_zip.setMinimumSize(QSize(0, 35))
        self.lineEdit_filename_zip.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_filename_zip.setFont(font6)
        self.lineEdit_filename_zip.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"}")

        self.formLayout_7.setWidget(1, QFormLayout.FieldRole, self.lineEdit_filename_zip)


        self.horizontalLayout_29.addWidget(self.frame_output_zip, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_6.addWidget(self.frame_top_page_zip, 0, Qt.AlignHCenter)


        self.verticalLayout_18.addWidget(self.frame_zip, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_8.addWidget(self.frame_main_zip, 0, Qt.AlignTop)

        self.stackedWidget.addWidget(self.page_zip)
        self.page_credits = QWidget()
        self.page_credits.setObjectName(u"page_credits")
        self.horizontalLayout_12 = QHBoxLayout(self.page_credits)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(30, 20, 30, -1)
        self.textBrowser_credits = QTextBrowser(self.page_credits)
        self.textBrowser_credits.setObjectName(u"textBrowser_credits")
        self.textBrowser_credits.setStyleSheet(u"background-color:#343A4B;\n"
"border-radius: 7px;")
        self.textBrowser_credits.setOpenExternalLinks(True)

        self.horizontalLayout_12.addWidget(self.textBrowser_credits)

        self.stackedWidget.addWidget(self.page_credits)
        self.page_help = QWidget()
        self.page_help.setObjectName(u"page_help")
        self.horizontalLayout_15 = QHBoxLayout(self.page_help)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(30, 20, 30, -1)
        self.textBrowser = QTextBrowser(self.page_help)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setStyleSheet(u"QTextBrowser {\n"
"background-color:#343A4B;\n"
"border-radius: 7px;\n"
"padding-left: 20px;\n"
"padding-top: 20px;\n"
"padding-bottom: 20px;\n"
"}\n"
"")

        self.horizontalLayout_15.addWidget(self.textBrowser)

        self.stackedWidget.addWidget(self.page_help)

        self.verticalLayout_9.addWidget(self.stackedWidget)

        self.frame_bottom = QFrame(self.frame_content)
        self.frame_bottom.setObjectName(u"frame_bottom")
        self.frame_bottom.setMinimumSize(QSize(0, 0))
        self.frame_bottom.setMaximumSize(QSize(16777215, 16777215))
        self.frame_bottom.setFrameShape(QFrame.StyledPanel)
        self.frame_bottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_bottom)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(50, 9, 0, 9)
        self.label_feedback = QLabel(self.frame_bottom)
        self.label_feedback.setObjectName(u"label_feedback")
        self.label_feedback.setMinimumSize(QSize(0, 0))
        self.label_feedback.setMaximumSize(QSize(16777215, 16777215))
        self.label_feedback.setFont(font6)

        self.verticalLayout_16.addWidget(self.label_feedback, 0, Qt.AlignVCenter)


        self.verticalLayout_9.addWidget(self.frame_bottom, 0, Qt.AlignVCenter)


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
        self.frame_label_bottom.setMinimumSize(QSize(0, 30))
        self.frame_label_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.label_credits = QLabel(self.frame_label_bottom)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setMinimumSize(QSize(0, 20))
        self.label_credits.setFont(font8)
        self.label_credits.setStyleSheet(u"")
        self.label_credits.setOpenExternalLinks(True)

        self.horizontalLayout_7.addWidget(self.label_credits, 0, Qt.AlignTop)

        self.label_version = QLabel(self.frame_label_bottom)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setMinimumSize(QSize(0, 20))
        self.label_version.setMaximumSize(QSize(100, 16777215))
        self.label_version.setFont(font)
        self.label_version.setStyleSheet(u"color: rgb(112, 117, 125);")
        self.label_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_version, 0, Qt.AlignTop)


        self.horizontalLayout_6.addWidget(self.frame_label_bottom, 0, Qt.AlignTop)

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

        self.stackedWidget.setCurrentIndex(4)
        self.tabWidget.setCurrentIndex(0)


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
        self.label_description_merge.setText(QCoreApplication.translate("MainWindow", u"UNIR ARQUIVOS PDF", None))
        self.pushButton_run_merge.setText("")
        self.pushButton_selectFiles_merge.setText(QCoreApplication.translate("MainWindow", u"Selecionar arquivos", None))
        self.pushButton_outputPath_merge.setText("")
        self.lineEdit_outputPath_merge.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecionar diret\u00f3rio de sa\u00edda", None))
        self.lineEdit_filename_merge.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome do arquivo: #origin", None))
        self.label_drop_merge.setText(QCoreApplication.translate("MainWindow", u"ARRASTE E SOLTE ARQUIVOS PDF AQUI", None))
        self.label_description_extract.setText(QCoreApplication.translate("MainWindow", u"EXTRAIR P\u00c1GINAS OU DIVIDIR ARQUIVOS PDF", None))
        self.pushButton_run_extract.setText("")
        self.pushButton_selectFiles_extract.setText(QCoreApplication.translate("MainWindow", u"Selecionar arquivos", None))
        self.pushButton_outputPath_extract.setText("")
        self.lineEdit_outputPath_extract.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecionar diret\u00f3rio de sa\u00edda", None))
        self.lineEdit_filename_extract.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome do arquivo: #origin,#pages", None))
        self.comboBox_extractPages.setItemText(0, QCoreApplication.translate("MainWindow", u"P\u00e1ginas indicadas", None))
        self.comboBox_extractPages.setItemText(1, QCoreApplication.translate("MainWindow", u"A cada n p\u00e1ginas", None))

        self.lineEdit_intPages_extract.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ex: 3, 7-8, 11-14", None))
        self.checkBox_split.setText(QCoreApplication.translate("MainWindow", u"Dividir arquivo", None))
        self.checkBox_extract.setText(QCoreApplication.translate("MainWindow", u"Extrair no mesmo arquivo", None))
        self.label_drop_extract.setText(QCoreApplication.translate("MainWindow", u"ARRASTE E SOLTE ARQUIVOS PDF AQUI", None))
        self.label_description_ocr.setText(QCoreApplication.translate("MainWindow", u"ESCANEAR ARQUIVOS PDF (OCR)", None))
        self.pushButton_selectFiles_ocr.setText(QCoreApplication.translate("MainWindow", u"Selecionar arquivos", None))
        self.pushButton_run_ocr.setText("")
        self.label_intDpi_ocr.setText(QCoreApplication.translate("MainWindow", u"DPI:", None))
        self.lineEdit_intDpi_ocr.setPlaceholderText(QCoreApplication.translate("MainWindow", u"200", None))
        self.pushButton_outputPath_ocr.setText("")
        self.lineEdit_outputPath_ocr.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecionar diret\u00f3rio de sa\u00edda", None))
        self.lineEdit_filename_ocr.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome do arquivo: #origin", None))
        self.label_drop_ocr.setText(QCoreApplication.translate("MainWindow", u"ARRASTE E SOLTE ARQUIVOS PDF AQUI", None))
        self.label_description_search.setText(QCoreApplication.translate("MainWindow", u"ORGANIZAR ARQUIVOS PDF", None))
        self.lineEdit_moveto_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ex: Tabela1:2", None))
        self.label_else_search.setText(QCoreApplication.translate("MainWindow", u"Se n\u00e3o encontrar mover para pasta", None))
        self.label_moveto_search.setText(QCoreApplication.translate("MainWindow", u"Criar subpastas", None))
        self.pushButton_run_search.setText(QCoreApplication.translate("MainWindow", u"Executar", None))
        self.lineEdit_else_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ex: N\u00e3o encontrado", None))
        self.label_keywords_search.setText(QCoreApplication.translate("MainWindow", u"Procurar por express\u00f5es", None))
        self.lineEdit_keywords_search.setText("")
        self.lineEdit_keywords_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ex: Tabela1:1, Tabela2:1", None))
        self.pushButton_selectFiles_search.setText(QCoreApplication.translate("MainWindow", u"Selecionar arquivos", None))
        self.pushButton_outputPath_search.setText("")
        self.lineEdit_outputPath_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecionar diret\u00f3rio de sa\u00edda", None))
        self.lineEdit_filename_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome do arquivo: #origin", None))
        self.checkBox_ignorePontuation_search.setText(QCoreApplication.translate("MainWindow", u"Ignorar pontua\u00e7\u00e3o", None))
        self.checkBox_ignoreSpecialChar_search.setText(QCoreApplication.translate("MainWindow", u"Ignorar acentos", None))
        self.checkBox_onlyPages_search.setText(QCoreApplication.translate("MainWindow", u"Mover apenas p\u00e1ginas", None))
        self.checkBox_ignoreSpaces_search.setText(QCoreApplication.translate("MainWindow", u"Ignorar espa\u00e7os", None))
        self.checkBox_ignoreFirstPage_search.setText(QCoreApplication.translate("MainWindow", u"Ignorar primeira linha", None))
        self.label_drop_search.setText(QCoreApplication.translate("MainWindow", u"ARRASTE E SOLTE ARQUIVOS PDF AQUI", None))
        self.pushButton_addTable_search.setText("")
        self.pushButton_deleteTable_search.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.label_description_export.setText(QCoreApplication.translate("MainWindow", u"EXPORTAR PARA TABELA", None))
        self.pushButton_run_export.setText("")
        self.pushButton_selectFiles_export.setText(QCoreApplication.translate("MainWindow", u"Selecionar arquivos", None))
        self.pushButton_outputPath_export.setText("")
        self.lineEdit_outputPath_export.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecionar diret\u00f3rio de sa\u00edda", None))
        self.lineEdit_filename_export.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome do arquivo: #origin", None))
        self.label_drop_export.setText(QCoreApplication.translate("MainWindow", u"ARRASTE E SOLTE ARQUIVOS PDF AQUI", None))
        self.pushButton_add_column_export.setText("")
        self.pushButton_remove_column_export.setText("")
        self.label_description_zip.setText(QCoreApplication.translate("MainWindow", u"CRIAR FICHEIRO ZIP DE ARQUIVOS PDF", None))
        self.lineEdit_rootDirectory_zip.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecionar diret\u00f3rio raiz", None))
        self.pushButton_selectRootDirectory_zip.setText("")
        self.pushButton_run_zip.setText("")
        self.pushButton_outputPath_zip.setText("")
        self.lineEdit_outputPath_zip.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecionar diret\u00f3rio de sa\u00edda", None))
        self.lineEdit_filename_zip.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome do arquivo ZIP: #origin", None))
        self.textBrowser_credits.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Ahand: Giving you a hand for automation.</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Copyright (C) 2020  Matheus Melo</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-botto"
                        "m:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/demelomatt/\"><span style=\" font-size:10pt; text-decoration: underline; color:#70757d;\">https://github.com/demelomatt/</span></a></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent"
                        ":0px; font-size:10pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://www.gnu.org/licenses/\"><span style=\" font-size:10pt; text-decoration: underline; color:#70757d;\">https://www.gnu.org/licenses/</span></a></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px"
                        "; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">User interface created with QT Creator.</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://www.qt.io/\"><span style=\" font-size:10pt; text-decoration: underline; color:#70757d;\">https://www.qt.io/</span></a></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Licensed under LGPLv3 conditions.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size"
                        ":10pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">QT Python binaries by Pyside.</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://www.qt.io/qt-for-python/\"><span style=\" font-size:10pt; text-decoration: underline; color:#70757d;\">https://www.qt.io/qt-for-python/</span></a></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Licensed under LGPLv3 conditions.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0"
                        "px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">PySide Base by Wanderson Magalhaes.</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/Wanderson-Magalhaes/\"><span style=\" font-size:10pt; text-decoration: underline; color:#70757d;\">https://github.com/Wanderson-Magalhaes/</span></a></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Licensed under MIT License conditions.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                        "text-indent:0px;\"><span style=\" font-size:10pt;\">OCR engine by Tesseract.</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/tesseract-ocr/tesseract/\"><span style=\" font-size:10pt; text-decoration: underline; color:#70757d;\">https://github.com/tesseract-ocr/tesseract/</span></a></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Licensed under Apache License 2.0 conditions.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Tes"
                        "seract installer for Windows by UB-Mannheim.</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/UB-Mannheim/tesseract/\"><span style=\" font-size:10pt; text-decoration: underline; color:#70757d;\">https://github.com/UB-Mannheim/tesseract/</span></a></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Python-tesseract wrapper by pytesseract.</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/madmaze/pytesseract/\"><span style=\" font-size:"
                        "10pt; text-decoration: underline; color:#70757d;\">https://github.com/madmaze/pytesseract/</span></a></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Licensed under Apache License 2.0 conditions.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Python Imaging Library by Pillow</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/python-pillow/Pillow/\"><span style=\" font-size:10pt; text-decoration: underline; color:#70757d;\">htt"
                        "ps://github.com/python-pillow/Pillow/</span></a></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Licensed under the open source PIL Software License conditions.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Convert PDF to a PIL Image object by pdf2image.</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/Belval/pdf2image/\"><span style=\" font-size:10pt; text-decoration: underline; color:#70757d;\">https://github.com/Belval/p"
                        "df2image/</span></a></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Licensed under MIT License conditions.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">PDF rendering library by Poppler.</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://poppler.freedesktop.org/\"><span style=\" font-size:10pt; text-decoration: underline; color:#70757d;\">https://poppler.freedesktop.org/</span></a></p>\n"
"<p align=\"center\" style=\" margin-top:0px; m"
                        "argin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Licensed under GPLv3 conditions.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Poppler Windows binaries by oschwartz10612.</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/oschwartz10612/poppler-windows/releases/\"><span style=\" font-size:10pt; text-decoration: underline; color:#70757d;\">https://github.com/oschwartz10612/poppler-windows/releases/</span></a></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-to"
                        "p:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Python PDF toolkit by PYPDF2.</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/mstamy2/PyPDF2/\"><span style=\" font-size:10pt; text-decoration: underline; color:#70757d;\">https://github.com/mstamy2/PyPDF2/</span></a></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Licensed under BSD License conditions.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-inde"
                        "nt:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Extracts the text from a PDF page by pdfminer.six.</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/pdfminer/pdfminer.six/\"><span style=\" font-size:10pt; text-decoration: underline; color:#70757d;\">https://github.com/pdfminer/pdfminer.six/</span></a></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Licensed under MIT License conditions.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\""
                        "><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Sound-playing interface for Windows by winsound.</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://docs.python.org/3/library/winsound.html\"><span style=\" font-size:10pt; text-decoration: underline; color:#70757d;\">https://docs.python.org/3/library/winsound.html</span></a></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Icons by Flaticon.</span></p>\n"
"<p align=\"center\" style=\" margi"
                        "n-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://www.flaticon.com/\"><span style=\" font-size:10pt; text-decoration: underline; color:#70757d;\">https://www.flaticon.com/</span></a></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Sound Effects by Freesound.</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://freesound.org/\"><span style=\" font-size:10pt; text-decoration: underline; color:#70757d;\">https://freesound.org/</span></a></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-to"
                        "p:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Developed with Python.</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://www.python.org/\"><span style=\" font-size:10pt; text-decoration: underline; color:#70757d;\">https://www.python.org/</span></a></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Licensed under PSF LICENSE conditions.</span></p></body></html>", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:14pt; font-weight:600;\">Descri\u00e7\u00e3o:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:11pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Ahand (Give me a hand) \u00e9 um programa para otimiza"
                        "\u00e7\u00e3o de processos que envolvam arquivos PDF.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Com Ahand \u00e9 poss\u00edvel:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">- Unir arquivos PDF.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0"
                        "px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">- Extrair p\u00e1ginas de arquivos PDF.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">- Dividir arquivos PDF.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">- Escanear arquivos PDF atrav\u00e9s do reconhecimento \u00f3ptico de caracteres (OCR), transformando em um PDF pesquis\u00e1vel.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">- Organizar arquivos PDF de acordo com as frases ou palavras encontradas dentro do arquivo.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; "
                        "-qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">- Compactar arquivos PDF contidos em subpastas de uma pasta raiz.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">    </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:14pt; font-weight:600;\">Nomenclatura dos arquivos:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Dentro do programa, existem tags, "
                        "elas s\u00e3o vari\u00e1veis que abrangem alguns padr\u00f5es bastante usados na hora de renomear um arquivo. As tags s\u00e3o indicadas por #.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:600;\">#origin</span><span style=\" font-family:'Segoe UI'; font-size:11pt;\"> = Nome original do arquivo.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:600;\">#year</span><span style=\" font-family:'Segoe UI'; font-size:11pt;\"> = Ano atual.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                        "text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:600;\">#month</span><span style=\" font-family:'Segoe UI'; font-size:11pt;\"> = M\u00eas atual.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:600;\">#day</span><span style=\" font-family:'Segoe UI'; font-size:11pt;\"> = Dia atual.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:600;\">#hour</span><span style=\" font-family:'Segoe UI'; font-size:11pt;\"> = Hora atual.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:600;\">#minutes</span><span style=\" font-family:'Sego"
                        "e UI'; font-size:11pt;\"> = Minutos atuais.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:600;\">#seconds</span><span style=\" font-family:'Segoe UI'; font-size:11pt;\"> = Segundos atuais</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:600;\">#time</span><span style=\" font-family:'Segoe UI'; font-size:11pt;\"> = Hora, minutos e segundos atuais.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:600;\">#pages</span><span style=\" font-family:'Segoe UI'; font-size:11pt;\"> = P\u00e1gina(s) exportadas do arquivo. Dispon\u00edvel apenas para as fun\u00e7\u00f5"
                        "es Separar/Dividir e Organizar(caso a caixa de sele\u00e7\u00e3o &quot;Mover apenas p\u00e1ginas esteja marcada&quot;).</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Por padr\u00e3o, caso o campo de nome esteja vazio, os arquivos s\u00e3o salvos com a tag #origin, com exce\u00e7\u00e3o da fun\u00e7\u00e3o Separar/Dividir, que utiliza as tags #origin,#pages.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Para utilizar um conjunto de tags, \u00e9 necess\u00e1rio delimitar por v\u00edrgulas.</span></p>\n"
"<p style=\"-qt-paragra"
                        "ph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Veja um exemplo de nomenclatura de um arquivo:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Arquivos de entrada: </span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;\">C:\\Downloads\\file1.pdf, C:\\Downloads\\file2.pdf</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Extrair p\u00e1gina indicada: </span><span style=\" font-family:'"
                        "Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;\">3</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Diret\u00f3rio de sa\u00edda: </span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;\">C:\\Downloads</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Nome do arquivo: </span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;\">#origin,#pages,Contas a pagar,#year,#month,#day</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Resultado: </span><span style=\" font-family:'Segoe UI'; font-size:11pt; fon"
                        "t-style:italic; color:#a0a0a0;\">C:\\Downloads\\file1_3_Contas a pagar_2020_10_14, C:\\Downloads\\file2_3_Contas a pagar_2020_10_14</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Note que voc\u00ea pode utilizar tags e texto em conjunto, mas eles devem ser delimitados por v\u00edrgula.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:14pt;"
                        " font-weight:600;\">Unir arquivos PDF:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Exemplo:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Arquivos de entrada: </span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;\">C:\\Downloads\\file1.pdf, C:\\Downloads\\file2.pdf</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Diret\u00f3rio de sa\u00edda: </span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;\">C:\\Downloads\\</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margi"
                        "n-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Nome do arquivo: </span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;\">merged</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Resultado: </span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;\">C:\\Downloads\\merged.pdf</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:14pt; font-weight:600;\">Extrair p\u00e1ginas ou dividir arquivos PDF:</span></p"
                        ">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Lista - P\u00e1ginas indicadas: Extrair ou dividir nas p\u00e1ginas indicadas.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Lista - A cada n p\u00e1ginas: Extrair ou dividir a cada &quot;n&quot; p\u00e1ginas.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Caixa de sele\u00e7\u00e3o - Dividir arquivo: Atrav\u00e9s de um arquivo, outros s\u00e3o gerados, os dividindo nas p\u00e1ginas indicadas.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" "
                        "font-family:'Segoe UI'; font-size:11pt;\">Caixa de sele\u00e7\u00e3o - Extrair no mesmo arquivo: As p\u00e1ginas indicadas s\u00e3o extra\u00eddas em um mesmo arquivo.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Exemplos:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Arquivo de entrada:</span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;\"> C:\\Downloads\\file.pdf</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; t"
                        "ext-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Diret\u00f3rio de sa\u00edda: </span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;\">C:\\Downloads\\</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Nome do arquivo: </span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;\">#origin,#pages</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Exemplo 1:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px;"
                        " margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Lista = </span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;\">P\u00e1ginas indicadas</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Caixa de sele\u00e7\u00e3o = </span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;\">Dividir arquivo</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">P\u00e1ginas = </span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;\">3,7-8,11-16</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-inden"
                        "t:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Resultado: </span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;\">C:\\Downloads\\file_3.pdf, C:\\Downloads\\file_7-8.pdf, C:\\Downloads\\file_11-16.pdf</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Exemplo 2:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Lista = </span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;\">P\u00e1ginas indicadas</span></p>\n"
"<p style=\" margin-top"
                        ":0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Caixa de sele\u00e7\u00e3o = </span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;\">Extrair no mesmo arquivo</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">P\u00e1ginas = </span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;\">3,7-8,11-16</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Resultado: </span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;\">C:\\Downloads\\file_3,7-8,11-16.pdf</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-to"
                        "p:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Exemplo 3:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Lista = </span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;\">A cada n p\u00e1ginas</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Caixa de sele\u00e7\u00e3o = </span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;\">Dividir arquivo</span></p>\n"
"<p style="
                        "\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">P\u00e1ginas = </span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;\">4</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Resultado: </span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;\">C:\\Downloads\\file_1-4.pdf, C:\\Downloads\\file_5-8.pdf, C:\\Downloads\\file_9-12.pdf, C:\\Downloads\\file_13-16.pdf</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; tex"
                        "t-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Exemplo 4:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Lista = </span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;\">A cada n p\u00e1ginas</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Caixa de sele\u00e7\u00e3o = </span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;\">Extrair no mesmo arquivo</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">P\u00e1ginas = </span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-"
                        "style:italic; color:#a0a0a0;\">4</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Resultado: </span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;\">C:\\Downloads\\file_4,8,12,16.pdf</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:14pt; font-weight:600;\">Escanear arquivos PDF (OCR):</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Exemplo:</span></p>\n"
""
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Arquivos de entrada: </span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;\">C:\\Downloads\\file1.pdf, C:\\Downloads\\file2.pdf</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Diret\u00f3rio de sa\u00edda: </span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;\">C:\\Downloads\\</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Nome do arquivo: </span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;\">#origin,OCR</span></p>\n"
"<p st"
                        "yle=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">DPI: </span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;\">200</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Resultado: </span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;\">C:\\Downloads\\file1_OCR.pdf, C:\\Downloads\\file2_OCR.pdf</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-siz"
                        "e:11pt;\">Note que quanto maior o DPI, maior o tamanho da imagem.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Caso o reconhecimento \u00f3ptico de caracteres (OCR) n\u00e3o atinja um resultado satisfat\u00f3rio, experimente alterar o DPI.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:14pt; font-weight:600;\">Organizar arquivos PDF:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Voc\u00ea"
                        " pode organizar arquivos PDF de acordo com as frases ou palavras encontradas dentro do arquivo.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Suponhamos que voc\u00ea seja um professor e queira organizar os trabalhos enviados por seus alunos por escola, turma, ano atual, mat\u00e9ria, tema do trabalho e nome do aluno:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">- Primeiro, certifique-se de que o documento PDF seja pesquis\u00e1vel, isto \u00e9, contenha texto. Caso seja uma imagem escaneada, utilize a fun\u00e7\u00e3o &quo"
                        "t;Escanear arquivos PDF&quot; antes de proceder.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">- Importe os arquivos PDF que voc\u00ea deseja organizar.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">- Selecione o diret\u00f3rio de sa\u00edda. Como exemplo ser\u00e1 &quot;</span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;\">C:Desktop\\</span><span style=\" font-family:'Segoe UI'; font-size:11pt;\">&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">- Importe um ou mais arquivos CSV com a tabela que cont\u00e9m as palavras a pesquisar"
                        " (voc\u00ea pode gerar o arquivo com um editor de planilhas, como o Excel).</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Alunos.csv</span>  </p>\n"
"<table border=\"0\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; border-collapse:collapse;\" cellspacing=\"2\" cellpadding=\"0\"><thead>\n"
"<tr>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-botto"
                        "m-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">Nome do aluno</span>    </p></td>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">N\u00famero de chamada</span>    </p></td>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-t"
                        "op-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">Turma</span>    </p></td>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">Escola</span>    </p></td>\n"
"<td style=\" vertical-align:top; paddin"
                        "g-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">Mun\u00edcipio</span>    </p></td>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -"
                        "qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">Cidade</span>    </p></td></tr></thead>\n"
"<tr>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">Bianca Helena Cavalcanti</span>    </p></td>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-"
                        "style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">1</span>    </p></td>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">2C</span>    </p></td>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border"
                        "-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">Durvalino Grion Prof</span>    </p></td>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">Adamantina</span>    </p></td>\n"
"<"
                        "td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">S\u00e3o Paulo</span>    </p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; mar"
                        "gin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">Catarina Jaqueline Nunes</span>    </p></td>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">3</span>    </p></td>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-c"
                        "olor:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">1A</span>    </p></td>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">Alice Maciel Sanches Professora</span>    </p></td>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; bord"
                        "er-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">Santo Anast\u00e1cio</span>    </p></td>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-fa"
                        "mily:'Segoe UI';\">S\u00e3o Paulo</span>    </p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">Clara Emanuelly Luiza Carvalho</span>    </p></td>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-s"
                        "tyle:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">6</span>    </p></td>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">2B</span>    </p></td>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-colo"
                        "r:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">Ferdinando Ienny</span>    </p></td>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">Ouro Verde</span>    </p></td>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-ri"
                        "ght:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">S\u00e3o Paulo</span>    </p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-blo"
                        "ck-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">Francisco Edson Gon\u00e7alves</span>    </p></td>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">11</span>    </p></td>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-"
                        "style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">3D</span>    </p></td>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">Jadyr Salles Professor Etec</span>    </p></td>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border"
                        "-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">Porto Ferreira</span>    </p></td>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">S\u00e3o Paulo</span>    </p></td></tr>\n"
""
                        "<tr>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">Gabriela Emanuelly Baptista</span>    </p></td>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top"
                        ":0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">15</span>    </p></td>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">3E</span>    </p></td>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000"
                        "; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">Durvalino Grion Prof</span>    </p></td>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">Adamantina</span>    </p></td>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; bor"
                        "der-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">S\u00e3o Paulo</span>    </p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'S"
                        "egoe UI';\">Julio Jorge Arag\u00e3o</span>    </p></td>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">21</span>    </p></td>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
""
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">2F</span>    </p></td>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">Ferdinando Ienny</span>    </p></td>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-colo"
                        "r:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">Ouro Verde</span>    </p></td>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">S\u00e3o Paulo</span>    </p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-to"
                        "p:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">Pietra Giovanna Joana Almada</span>    </p></td>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text"
                        "-indent:0px;\"><span style=\" font-family:'Segoe UI';\">32</span>    </p></td>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">1C</span>    </p></td>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; borde"
                        "r-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">Djalma Forjaz Doutor</span>    </p></td>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">Porto Ferreira</span>    </p></td>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; bor"
                        "der-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">S\u00e3o Paulo</span>    </p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">Silvana Stefany Mirella Nascimento</span>    </p></td>\n"
"<td style"
                        "=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">37</span>    </p></td>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; m"
                        "argin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">1C</span>    </p></td>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">Alice Maciel Sanches Professora</span>    </p></td>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-s"
                        "tyle:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">Santo Anast\u00e1cio</span>    </p></td>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">S\u00e3o Paulo</span>    </p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px;"
                        " border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">T\u00e2nia Allana Monteiro</span>    </p></td>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:"
                        "'Segoe UI';\">40</span>    </p></td>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">3C</span>    </p></td>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" mar"
                        "gin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">Santo Antonio</span>    </p></td>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">Santo Ant\u00f4nio De Posse</span>    </p></td>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bott"
                        "om-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">S\u00e3o Paulo</span>  </p></td></tr></table>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">(Todos os dados referentes a alunos foram gerados aleatoriamente).</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bo"
                        "ttom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Mat\u00e9rias.csv</span>  </p>\n"
"<table border=\"0\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; border-collapse:collapse;\" cellspacing=\"2\" cellpadding=\"0\"><thead>\n"
"<tr>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">Tema</span>    </p></td>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; pa"
                        "dding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">Mat\u00e9ria</span>    </p></td></tr></thead>\n"
"<tr>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-i"
                        "ndent:0px;\"><span style=\" font-family:'Segoe UI';\">Deslocamento escalar</span>    </p></td>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">Cinem\u00e1tica</span>    </p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-st"
                        "yle:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">Energia potencial el\u00e9trica</span>    </p></td>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">El\u00e9trica</span>    </p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px"
                        "; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">Leis de Newton</span>    </p></td>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">Din\u00e2mica</"
                        "span>    </p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">Trajet\u00f3ria</span>    </p></td>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p sty"
                        "le=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">Cinem\u00e1tica</span>    </p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">Lentes convergentes</span>    </p></td>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#00"
                        "0000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">\u00d3ptica</span>    </p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">Movimento e repouso</span>    </p></td>\n"
"<td style=\" vertical-align:top; padding-left:"
                        "5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">Cinem\u00e1tica</span>    </p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-righ"
                        "t:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">Campo el\u00e9trico</span>    </p></td>\n"
"<td style=\" vertical-align:top; padding-left:5; padding-right:5; padding-top:10; padding-bottom:10; border-top:1px; border-right:1px; border-bottom:1px; border-left:1px; border-top-color:#000000; border-right-color:#000000; border-bottom-color:#000000; border-left-color:#000000; border-top-style:solid; border-right-style:solid; border-bottom-style:solid; border-left-style:solid;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">El\u00e9trica</span>  </p></td></tr></table>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-"
                        "indent:0px; font-family:'Segoe UI'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Iremos procurar pelo nome de todos os alunos, que se encontra na tabela </span><span style=\" font-family:'Segoe UI'; font-size:11pt; color:#a0a0a0;\">Alunos</span><span style=\" font-family:'Segoe UI'; font-size:11pt;\"> coluna </span><span style=\" font-family:'Segoe UI'; font-size:11pt; color:#a0a0a0;\">1</span><span style=\" font-family:'Segoe UI'; font-size:11pt;\">, junto a todos os temas de trabalho, que se encontra na tabela </span><span style=\" font-family:'Segoe UI'; font-size:11pt; color:#a0a0a0;\">Mat\u00e9rias</span><span style=\" font-family:'Segoe UI'; font-size:11pt;\"> coluna </span><span style=\" font-family:'Segoe UI'; font-size:11pt; color:#a0a0a0;\">1</span><span style=\" font-family:'Segoe UI'; font-size:11pt;\">.</span></p>\n"
"<p style=\" marg"
                        "in-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Ent\u00e3o temos a defini\u00e7\u00e3o </span><span style=\" font-family:'Segoe UI'; font-size:11pt; color:#a0a0a0;\">tabela:coluna</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Sendo assim, o campo &quot;</span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;\">Procurar por express\u00f5es</span><span style=\" font-family:'Segoe UI'; font-size:11pt;\">&quot; recebe o seguinte valor: </span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#"
                        "a0a0a0;\">Alunos:1,Mat\u00e9rias:1</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Se houver mais de um conjunto tabela:coluna, eles devem ser delimitados por v\u00edrgulas, como no exemplo acima.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Note que se o valor de uma linha for localizado, temos acesso a todos os valores das outras colunas adjacentes nessa tabela.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'"
                        "Segoe UI'; font-size:11pt;\">Como por exemplo, se dentro do arquivo conter o nome &quot;Bianca Helena Cavalcanti&quot;, podemos pedir para o programa retornar o valor da coluna 3, que para essa linha \u00e9 &quot;2C&quot;.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Dessa forma, temos acesso a valores que n\u00e3o necessariamente precisam estar dentro do arquivo.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Com isso em mente:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; "
                        "-qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Iremos informar o destino que queremos exportar o arquivo caso as condi\u00e7\u00f5es forem satisfeitas:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Queremos criar uma \u00e1rvore de diret\u00f3rio nesse modelo: </span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;\">diret\u00f3rio_de_sa\u00edda\\ano_atual\\escola\\turma\\mat\u00e9ria\\tema_do_trabalho\\</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-"
                        "size:11pt;\">Ent\u00e3o iremos informar em qual tabela e coluna esses valores se encontram.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Sendo assim, o campo &quot;</span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;\">Criar subpastas</span><span style=\" font-family:'Segoe UI'; font-size:11pt;\">&quot; recebe o seguinte valor: </span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;\">#year,Alunos:4,Alunos:3,Mat\u00e9rias:2,Mat\u00e9rias:1</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\""
                        " font-family:'Segoe UI'; font-size:11pt;\">Caso as condi\u00e7\u00f5es n\u00e3o sejam satisfeitas dentro de um arquivo, podemos indicar um diret\u00f3rio para mov\u00ea-lo.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Sendo assim, o campo &quot;</span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;\">Se n\u00e3o encontrar mover para pasta</span><span style=\" font-family:'Segoe UI'; font-size:11pt;\">&quot; recebe o seguinte valor: </span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;\">N\u00e3o encontrado</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Caso vazio, os arquivos em que n\u00e3o foram encontradas todas as palavras n\u00e3o ser\u00e3"
                        "o movidos.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Agora, iremos informar o nome do arquivo, neste caso queremos o nome do aluno.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Sendo assim, o campo &quot;</span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;\">Nome do arquivo</span><span style=\" font-family:'Segoe UI'; font-size:11pt;\">&quot; recebe o seguinte valor: </span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;\">Alunos:1</span"
                        "></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">H\u00e1 ainda algumas caixas de sele\u00e7\u00e3o:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;\">Mover apenas p\u00e1ginas:</span><span style=\" font-family:'Segoe UI'; font-size:11pt;\"> Se marcado, ir\u00e1 procurar pelas palavras dentro de cada p\u00e1"
                        "gina e exporta-la caso os requisitos sejam satisfeitos. \u00datil quando cada p\u00e1gina representa um arquivo, como uma nota fiscal. Caso contr\u00e1rio, as palavras ser\u00e3o pesquisadas dentro de todo o arquivo.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;\">Ignorar primeira linha:</span><span style=\" font-family:'Segoe UI'; font-size:11pt;\"> Marcar caso a primeira linha seja cabe\u00e7alho e voc\u00ea n\u00e3o queira pesquisa-la dentro do arquivo.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;\">Ignorar acentos:</span><span style=\" font-family:'Segoe UI'; font-size:11pt;\"> Realizar pesquisa desconsiderando acentos. Marcar para maior precis\u00e3o.</"
                        "span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;\">Ignorar pontua\u00e7\u00e3o:</span><span style=\" font-family:'Segoe UI'; font-size:11pt;\"> Realizar pesquisa desconsiderando pontua\u00e7\u00e3o tais como &quot;.,;/?!&quot;. Marcar para maior precis\u00e3o.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;\">Ignorar espa\u00e7os:</span><span style=\" font-family:'Segoe UI'; font-size:11pt;\"> Realizar pesquisa desconsiderando espa\u00e7os. Marcar para maior precis\u00e3o.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:11"
                        "pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Para este exemplo, iremos desmarcar apenas a op\u00e7\u00e3o &quot;Mover apenas p\u00e1ginas&quot;.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Ent\u00e3o, como exemplo de resultado, caso ambas as palavras &quot;Bianca Helena Cavalcanti&quot; e &quot;Deslocamento escalar&quot; sejam encontradas no arquivo, temos:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-famil"
                        "y:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;\">C:Desktop\\2020\\Durvalino Grion Prof\\2C\\Cinem\u00e1tica\\Deslocamento escalar\\Bianca Helena Cavalcanti.pdf</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Se em vez de criar uma \u00e1rvore de diret\u00f3rio </span><span style=\" font-family:'Segoe UI','sans-serif'; font-size:11pt;\">quis\u00e9ssemos </span><span style=\" font-family:'Segoe UI'; font-size:11pt;\">apenas renomear o arquivo, bastava informar os valores no campo &quot;</span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;\">Nome do arquivo</span><span style=\" font-family:'Segoe UI'; font-size:11pt"
                        ";\">&quot; e deixar o campo &quot;</span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;\">Criar subpastas</span><span style=\" font-family:'Segoe UI'; font-size:11pt;\">&quot; vazio.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Ent\u00e3o, como exemplo de resultado, temos:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;\">C:Desktop\\2020_Durvalino Grion Prof_2C_Cinem\u00e1tica_Deslocamento escalar_Bianca Helena Cavalcanti.pdf</span></p>\n"
"<p style=\"-"
                        "qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:14pt; font-weight:600;\">Criar ficheiro ZIP de arquivos PDF:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Exemplo:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Diret\u00f3rio raiz: </span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;\">C:\\Downloads\\root\\</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-"
                        "left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Subpastas contidas no diret\u00f3rio raiz: Janeiro,Fevereiro,Mar\u00e7o</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Diret\u00f3rio de sa\u00edda: </span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;\">C:\\Downloads\\output\\</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Nome do arquivo ZIP: </span><span style=\" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;\">#origin,#year</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-fa"
                        "mily:'Segoe UI'; font-size:11pt;\">Resultado: </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt; font-style:italic; color:#a0a0a0;\">C:\\Downloads\\output\\Janeiro_2020.zip, C:\\Downloads\\output\\Fevereiro_2020.zip, C:\\Downloads\\output\\Mar\u00e7o_2020.zip</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:11pt;\">Portanto, todos os arquivos PDF contidos nas subpastas Janeiro,Fevereiro,Mar\u00e7o ser\u00e3o compactados.</span></p></body></html>", None))
        self.label_feedback.setText(QCoreApplication.translate("MainWindow", u"Pesquisando por palavra...", None))
        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://github.com/demelomatt/\"><span style=\" color:#70757d;\">https://github.com/demelomatt/</span></a></p></body></html>", None))
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"v1.1.0", None))
    # retranslateUi

