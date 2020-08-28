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

        self.horizontalLayout_8.addWidget(self.label_top_info_2, 0, Qt.AlignRight)


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
        self.frame_left_menu.setMinimumSize(QSize(0, 0))
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
        self.frame_extra_menus.setMinimumSize(QSize(70, 0))
        self.frame_extra_menus.setMaximumSize(QSize(16777215, 16777215))
        self.frame_extra_menus.setFrameShape(QFrame.StyledPanel)
        self.frame_extra_menus.setFrameShadow(QFrame.Raised)
        self.layout_menu_bottom = QVBoxLayout(self.frame_extra_menus)
        self.layout_menu_bottom.setSpacing(10)
        self.layout_menu_bottom.setObjectName(u"layout_menu_bottom")
        self.layout_menu_bottom.setContentsMargins(0, 0, 0, 25)

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
        self.verticalLayout_24 = QVBoxLayout(self.page_merge)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(9, 9, 9, 9)
        self.frame_home = QFrame(self.page_merge)
        self.frame_home.setObjectName(u"frame_home")
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
        self.frame_merge.setFrameShape(QFrame.StyledPanel)
        self.frame_merge.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_merge)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(5, 5, 5, 5)
        self.frame_description_merge = QFrame(self.frame_merge)
        self.frame_description_merge.setObjectName(u"frame_description_merge")
        self.frame_description_merge.setMinimumSize(QSize(0, 0))
        self.frame_description_merge.setFrameShape(QFrame.StyledPanel)
        self.frame_description_merge.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_description_merge)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(5, 5, 5, 5)
        self.label_description_merge = QLabel(self.frame_description_merge)
        self.label_description_merge.setObjectName(u"label_description_merge")
        self.label_description_merge.setMinimumSize(QSize(0, 0))
        self.label_description_merge.setFont(font1)
        self.label_description_merge.setStyleSheet(u"")

        self.horizontalLayout_14.addWidget(self.label_description_merge, 0, Qt.AlignLeft)


        self.verticalLayout_10.addWidget(self.frame_description_merge, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.frame_top_page_merge = QFrame(self.frame_merge)
        self.frame_top_page_merge.setObjectName(u"frame_top_page_merge")
        self.frame_top_page_merge.setMinimumSize(QSize(630, 0))
        self.frame_top_page_merge.setMaximumSize(QSize(16777215, 16777215))
        self.frame_top_page_merge.setStyleSheet(u"background-color:#343A4B;\n"
"border-radius: 7px;\n"
"border-top: 3px solid rgb(85, 170, 255);")
        self.frame_top_page_merge.setFrameShape(QFrame.StyledPanel)
        self.frame_top_page_merge.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_top_page_merge)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(5, 5, 5, 5)
        self.frame_input_merge = QFrame(self.frame_top_page_merge)
        self.frame_input_merge.setObjectName(u"frame_input_merge")
        self.frame_input_merge.setMinimumSize(QSize(230, 0))
        self.frame_input_merge.setMaximumSize(QSize(16777215, 16777215))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        self.frame_input_merge.setFont(font3)
        self.frame_input_merge.setStyleSheet(u"border: 0px;")
        self.frame_input_merge.setFrameShape(QFrame.StyledPanel)
        self.frame_input_merge.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_input_merge)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 0, 5)
        self.pushButton_selectFiles_merge = QPushButton(self.frame_input_merge)
        self.pushButton_selectFiles_merge.setObjectName(u"pushButton_selectFiles_merge")
        self.pushButton_selectFiles_merge.setMinimumSize(QSize(0, 30))
        self.pushButton_selectFiles_merge.setMaximumSize(QSize(160, 16777215))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(9)
        self.pushButton_selectFiles_merge.setFont(font4)
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
        icon3 = QIcon()
        icon3.addFile(u":/20x20/icons/20x20/cil-file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_selectFiles_merge.setIcon(icon3)
        self.pushButton_selectFiles_merge.setIconSize(QSize(18, 18))

        self.gridLayout.addWidget(self.pushButton_selectFiles_merge, 0, 1, 1, 1)

        self.pushButton_run_merge = QPushButton(self.frame_input_merge)
        self.pushButton_run_merge.setObjectName(u"pushButton_run_merge")
        self.pushButton_run_merge.setMaximumSize(QSize(40, 30))
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
        icon4 = QIcon()
        icon4.addFile(u":/20x20/icons/20x20/cil-media-play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_run_merge.setIcon(icon4)
        self.pushButton_run_merge.setIconSize(QSize(18, 18))

        self.gridLayout.addWidget(self.pushButton_run_merge, 0, 0, 1, 1)

        self.label_files_selected_merge = QLabel(self.frame_input_merge)
        self.label_files_selected_merge.setObjectName(u"label_files_selected_merge")
        self.label_files_selected_merge.setFont(font)
        self.label_files_selected_merge.setStyleSheet(u"color: rgb(122, 127, 135);")

        self.gridLayout.addWidget(self.label_files_selected_merge, 1, 1, 1, 1, Qt.AlignHCenter)


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
        self.formLayout_3.setContentsMargins(0, 5, 5, 5)
        self.lineEdit_outputPath_merge = QLineEdit(self.frame_output_merge)
        self.lineEdit_outputPath_merge.setObjectName(u"lineEdit_outputPath_merge")
        self.lineEdit_outputPath_merge.setMinimumSize(QSize(0, 30))
        self.lineEdit_outputPath_merge.setMaximumSize(QSize(320, 16777215))
        self.lineEdit_outputPath_merge.setFont(font)
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
        self.lineEdit_filename_merge.setMinimumSize(QSize(0, 30))
        self.lineEdit_filename_merge.setMaximumSize(QSize(320, 16777215))
        self.lineEdit_filename_merge.setFont(font)
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

        self.label_tags_merge = QLabel(self.frame_output_merge)
        self.label_tags_merge.setObjectName(u"label_tags_merge")
        self.label_tags_merge.setMinimumSize(QSize(0, 0))
        self.label_tags_merge.setMaximumSize(QSize(16777215, 16777215))
        self.label_tags_merge.setFont(font)
        self.label_tags_merge.setStyleSheet(u"color: rgb(112, 117, 125);")

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.label_tags_merge)

        self.pushButton_outputPath_merge = QPushButton(self.frame_output_merge)
        self.pushButton_outputPath_merge.setObjectName(u"pushButton_outputPath_merge")
        self.pushButton_outputPath_merge.setMinimumSize(QSize(40, 30))
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


        self.horizontalLayout_23.addWidget(self.frame_output_merge, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_10.addWidget(self.frame_top_page_merge)


        self.verticalLayout_21.addWidget(self.frame_merge, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame_mergebatch = QFrame(self.frame_home)
        self.frame_mergebatch.setObjectName(u"frame_mergebatch")
        self.frame_mergebatch.setFrameShape(QFrame.StyledPanel)
        self.frame_mergebatch.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_mergebatch)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(5, 5, 5, 5)
        self.frame_description_mergebatch = QFrame(self.frame_mergebatch)
        self.frame_description_mergebatch.setObjectName(u"frame_description_mergebatch")
        self.frame_description_mergebatch.setMinimumSize(QSize(0, 0))
        self.frame_description_mergebatch.setFrameShape(QFrame.StyledPanel)
        self.frame_description_mergebatch.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_description_mergebatch)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(5, 5, 5, 5)
        self.label_description_mergebatch = QLabel(self.frame_description_mergebatch)
        self.label_description_mergebatch.setObjectName(u"label_description_mergebatch")
        self.label_description_mergebatch.setMinimumSize(QSize(0, 0))
        self.label_description_mergebatch.setFont(font1)
        self.label_description_mergebatch.setStyleSheet(u"")

        self.horizontalLayout_20.addWidget(self.label_description_mergebatch, 0, Qt.AlignLeft)


        self.verticalLayout_17.addWidget(self.frame_description_mergebatch, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.frame_top_page_mergebatch = QFrame(self.frame_mergebatch)
        self.frame_top_page_mergebatch.setObjectName(u"frame_top_page_mergebatch")
        self.frame_top_page_mergebatch.setMinimumSize(QSize(630, 0))
        self.frame_top_page_mergebatch.setMaximumSize(QSize(16777215, 16777215))
        self.frame_top_page_mergebatch.setStyleSheet(u"background-color:#343A4B;\n"
"border-radius: 7px;\n"
"border-top: 3px solid rgb(85, 170, 255);")
        self.frame_top_page_mergebatch.setFrameShape(QFrame.StyledPanel)
        self.frame_top_page_mergebatch.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_top_page_mergebatch)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(5, 5, 5, 5)
        self.frame_input_mergebatch = QFrame(self.frame_top_page_mergebatch)
        self.frame_input_mergebatch.setObjectName(u"frame_input_mergebatch")
        self.frame_input_mergebatch.setMinimumSize(QSize(230, 0))
        self.frame_input_mergebatch.setMaximumSize(QSize(16777215, 16777215))
        self.frame_input_mergebatch.setFont(font3)
        self.frame_input_mergebatch.setStyleSheet(u"border: 0px;")
        self.frame_input_mergebatch.setFrameShape(QFrame.StyledPanel)
        self.frame_input_mergebatch.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_input_mergebatch)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(5, 5, 0, 5)
        self.lineEdit_rootDirectory_mergebatch = QLineEdit(self.frame_input_mergebatch)
        self.lineEdit_rootDirectory_mergebatch.setObjectName(u"lineEdit_rootDirectory_mergebatch")
        self.lineEdit_rootDirectory_mergebatch.setMinimumSize(QSize(0, 30))
        self.lineEdit_rootDirectory_mergebatch.setMaximumSize(QSize(180, 16777215))
        self.lineEdit_rootDirectory_mergebatch.setFont(font)
        self.lineEdit_rootDirectory_mergebatch.setStyleSheet(u"QLineEdit {\n"
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

        self.gridLayout_6.addWidget(self.lineEdit_rootDirectory_mergebatch, 1, 1, 1, 1)

        self.pushButton_selectRootDirectory_mergebatch = QPushButton(self.frame_input_mergebatch)
        self.pushButton_selectRootDirectory_mergebatch.setObjectName(u"pushButton_selectRootDirectory_mergebatch")
        self.pushButton_selectRootDirectory_mergebatch.setMinimumSize(QSize(180, 30))
        self.pushButton_selectRootDirectory_mergebatch.setMaximumSize(QSize(150, 16777215))
        self.pushButton_selectRootDirectory_mergebatch.setFont(font4)
        self.pushButton_selectRootDirectory_mergebatch.setStyleSheet(u"QPushButton {\n"
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
        self.pushButton_selectRootDirectory_mergebatch.setIcon(icon5)
        self.pushButton_selectRootDirectory_mergebatch.setIconSize(QSize(18, 18))

        self.gridLayout_6.addWidget(self.pushButton_selectRootDirectory_mergebatch, 0, 1, 1, 1)

        self.pushButton_run_mergebatch = QPushButton(self.frame_input_mergebatch)
        self.pushButton_run_mergebatch.setObjectName(u"pushButton_run_mergebatch")
        self.pushButton_run_mergebatch.setMinimumSize(QSize(40, 30))
        self.pushButton_run_mergebatch.setMaximumSize(QSize(40, 30))
        self.pushButton_run_mergebatch.setStyleSheet(u"QPushButton {\n"
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
        self.pushButton_run_mergebatch.setIcon(icon4)
        self.pushButton_run_mergebatch.setIconSize(QSize(18, 18))

        self.gridLayout_6.addWidget(self.pushButton_run_mergebatch, 0, 0, 1, 1)


        self.horizontalLayout_24.addWidget(self.frame_input_mergebatch, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame_output_mergebatch = QFrame(self.frame_top_page_mergebatch)
        self.frame_output_mergebatch.setObjectName(u"frame_output_mergebatch")
        self.frame_output_mergebatch.setMinimumSize(QSize(371, 115))
        self.frame_output_mergebatch.setMaximumSize(QSize(16777215, 16777215))
        self.frame_output_mergebatch.setStyleSheet(u"border: 0px;")
        self.frame_output_mergebatch.setFrameShape(QFrame.StyledPanel)
        self.frame_output_mergebatch.setFrameShadow(QFrame.Raised)
        self.formLayout_4 = QFormLayout(self.frame_output_mergebatch)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setContentsMargins(0, 5, 5, 5)
        self.lineEdit_filename_mergebatch = QLineEdit(self.frame_output_mergebatch)
        self.lineEdit_filename_mergebatch.setObjectName(u"lineEdit_filename_mergebatch")
        self.lineEdit_filename_mergebatch.setMinimumSize(QSize(250, 30))
        self.lineEdit_filename_mergebatch.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_filename_mergebatch.setFont(font)
        self.lineEdit_filename_mergebatch.setStyleSheet(u"QLineEdit {\n"
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

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.lineEdit_filename_mergebatch)

        self.label_tags_mergebatch = QLabel(self.frame_output_mergebatch)
        self.label_tags_mergebatch.setObjectName(u"label_tags_mergebatch")
        self.label_tags_mergebatch.setMinimumSize(QSize(0, 30))
        self.label_tags_mergebatch.setMaximumSize(QSize(16777215, 16777215))
        self.label_tags_mergebatch.setFont(font)
        self.label_tags_mergebatch.setStyleSheet(u"color: rgb(112, 117, 125);")

        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.label_tags_mergebatch)

        self.pushButton_outputPath_mergebatch = QPushButton(self.frame_output_mergebatch)
        self.pushButton_outputPath_mergebatch.setObjectName(u"pushButton_outputPath_mergebatch")
        self.pushButton_outputPath_mergebatch.setMinimumSize(QSize(40, 30))
        self.pushButton_outputPath_mergebatch.setStyleSheet(u"QPushButton {\n"
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
        self.pushButton_outputPath_mergebatch.setIcon(icon5)
        self.pushButton_outputPath_mergebatch.setIconSize(QSize(18, 18))

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.pushButton_outputPath_mergebatch)

        self.lineEdit_outputPath_mergebatch = QLineEdit(self.frame_output_mergebatch)
        self.lineEdit_outputPath_mergebatch.setObjectName(u"lineEdit_outputPath_mergebatch")
        self.lineEdit_outputPath_mergebatch.setMinimumSize(QSize(250, 30))
        self.lineEdit_outputPath_mergebatch.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_outputPath_mergebatch.setFont(font)
        self.lineEdit_outputPath_mergebatch.setStyleSheet(u"QLineEdit {\n"
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

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.lineEdit_outputPath_mergebatch)


        self.horizontalLayout_24.addWidget(self.frame_output_mergebatch, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_17.addWidget(self.frame_top_page_mergebatch)


        self.verticalLayout_21.addWidget(self.frame_mergebatch, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_24.addWidget(self.frame_home, 0, Qt.AlignTop)

        self.stackedWidget.addWidget(self.page_merge)
        self.page_extract = QWidget()
        self.page_extract.setObjectName(u"page_extract")
        self.page_extract.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_22 = QVBoxLayout(self.page_extract)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.frame_extract = QFrame(self.page_extract)
        self.frame_extract.setObjectName(u"frame_extract")
        self.frame_extract.setMinimumSize(QSize(0, 330))
        self.frame_extract.setMaximumSize(QSize(16777215, 16777215))
        self.frame_extract.setFrameShape(QFrame.StyledPanel)
        self.frame_extract.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_extract)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(5, 5, 5, 5)
        self.frame_extract_main = QFrame(self.frame_extract)
        self.frame_extract_main.setObjectName(u"frame_extract_main")
        self.frame_extract_main.setMaximumSize(QSize(16777215, 16777215))
        self.frame_extract_main.setFrameShape(QFrame.StyledPanel)
        self.frame_extract_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_extract_main)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(5, 5, 5, 5)
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
        self.label_description_extract.setFont(font1)
        self.label_description_extract.setStyleSheet(u"")

        self.horizontalLayout_16.addWidget(self.label_description_extract, 0, Qt.AlignLeft)


        self.verticalLayout_20.addWidget(self.frame_description_extract, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.frame_top_page_extract = QFrame(self.frame_extract_main)
        self.frame_top_page_extract.setObjectName(u"frame_top_page_extract")
        self.frame_top_page_extract.setMinimumSize(QSize(630, 0))
        self.frame_top_page_extract.setMaximumSize(QSize(16777215, 16777215))
        self.frame_top_page_extract.setStyleSheet(u"background-color:#343A4B;\n"
"border-radius: 7px;\n"
"border-top: 3px solid rgb(85, 170, 255);")
        self.frame_top_page_extract.setFrameShape(QFrame.StyledPanel)
        self.frame_top_page_extract.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_top_page_extract)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(5, 5, 5, 5)
        self.frame_input_extract = QFrame(self.frame_top_page_extract)
        self.frame_input_extract.setObjectName(u"frame_input_extract")
        self.frame_input_extract.setMinimumSize(QSize(230, 0))
        self.frame_input_extract.setMaximumSize(QSize(16777215, 16777215))
        self.frame_input_extract.setFont(font3)
        self.frame_input_extract.setStyleSheet(u"border: 0px;")
        self.frame_input_extract.setFrameShape(QFrame.StyledPanel)
        self.frame_input_extract.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_input_extract)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(5, 5, 0, 5)
        self.pushButton_selectFiles_extract = QPushButton(self.frame_input_extract)
        self.pushButton_selectFiles_extract.setObjectName(u"pushButton_selectFiles_extract")
        self.pushButton_selectFiles_extract.setMinimumSize(QSize(0, 30))
        self.pushButton_selectFiles_extract.setMaximumSize(QSize(160, 16777215))
        self.pushButton_selectFiles_extract.setFont(font4)
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
        self.pushButton_selectFiles_extract.setIcon(icon3)
        self.pushButton_selectFiles_extract.setIconSize(QSize(18, 18))

        self.gridLayout_2.addWidget(self.pushButton_selectFiles_extract, 0, 1, 1, 1)

        self.pushButton_run_extract = QPushButton(self.frame_input_extract)
        self.pushButton_run_extract.setObjectName(u"pushButton_run_extract")
        self.pushButton_run_extract.setMaximumSize(QSize(40, 30))
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
        self.pushButton_run_extract.setIcon(icon4)
        self.pushButton_run_extract.setIconSize(QSize(18, 18))

        self.gridLayout_2.addWidget(self.pushButton_run_extract, 0, 0, 1, 1)

        self.label_files_selected_extract = QLabel(self.frame_input_extract)
        self.label_files_selected_extract.setObjectName(u"label_files_selected_extract")
        self.label_files_selected_extract.setFont(font)
        self.label_files_selected_extract.setStyleSheet(u"color: rgb(122, 127, 135);")

        self.gridLayout_2.addWidget(self.label_files_selected_extract, 1, 1, 1, 1, Qt.AlignHCenter)


        self.horizontalLayout_25.addWidget(self.frame_input_extract, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame_output_extract = QFrame(self.frame_top_page_extract)
        self.frame_output_extract.setObjectName(u"frame_output_extract")
        self.frame_output_extract.setMinimumSize(QSize(0, 0))
        self.frame_output_extract.setMaximumSize(QSize(16777215, 16777215))
        self.frame_output_extract.setStyleSheet(u"border: 0px;")
        self.frame_output_extract.setFrameShape(QFrame.StyledPanel)
        self.frame_output_extract.setFrameShadow(QFrame.Raised)
        self.formLayout_5 = QFormLayout(self.frame_output_extract)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.formLayout_5.setContentsMargins(0, 5, 5, 5)
        self.pushButton_outputPath_extract = QPushButton(self.frame_output_extract)
        self.pushButton_outputPath_extract.setObjectName(u"pushButton_outputPath_extract")
        self.pushButton_outputPath_extract.setMinimumSize(QSize(40, 30))
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
        self.lineEdit_outputPath_extract.setMinimumSize(QSize(320, 30))
        self.lineEdit_outputPath_extract.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_outputPath_extract.setFont(font)
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
        self.lineEdit_filename_extract.setMinimumSize(QSize(320, 30))
        self.lineEdit_filename_extract.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_filename_extract.setFont(font)
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

        self.label_tags_extract = QLabel(self.frame_output_extract)
        self.label_tags_extract.setObjectName(u"label_tags_extract")
        self.label_tags_extract.setMinimumSize(QSize(0, 0))
        self.label_tags_extract.setMaximumSize(QSize(16777215, 16777215))
        self.label_tags_extract.setFont(font)
        self.label_tags_extract.setStyleSheet(u"color: rgb(112, 117, 125);")

        self.formLayout_5.setWidget(3, QFormLayout.FieldRole, self.label_tags_extract)


        self.horizontalLayout_25.addWidget(self.frame_output_extract, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_20.addWidget(self.frame_top_page_extract)


        self.verticalLayout_23.addWidget(self.frame_extract_main, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame_extract_pages = QFrame(self.frame_extract)
        self.frame_extract_pages.setObjectName(u"frame_extract_pages")
        self.frame_extract_pages.setMinimumSize(QSize(630, 100))
        self.frame_extract_pages.setMaximumSize(QSize(16777215, 16777215))
        self.frame_extract_pages.setStyleSheet(u"background-color:#343A4B;\n"
"border-radius: 7px;\n"
"\n"
"")
        self.frame_extract_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_extract_pages.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_extract_pages)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(30, 5, 5, 5)
        self.frame_lineEdit_extract = QFrame(self.frame_extract_pages)
        self.frame_lineEdit_extract.setObjectName(u"frame_lineEdit_extract")
        self.frame_lineEdit_extract.setMaximumSize(QSize(180, 16777215))
        self.frame_lineEdit_extract.setStyleSheet(u"border: 0px;")
        self.frame_lineEdit_extract.setFrameShape(QFrame.StyledPanel)
        self.frame_lineEdit_extract.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_lineEdit_extract)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(5, 9, 5, 5)
        self.label_pages_extract = QLabel(self.frame_lineEdit_extract)
        self.label_pages_extract.setObjectName(u"label_pages_extract")
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(11)
        self.label_pages_extract.setFont(font5)

        self.verticalLayout_26.addWidget(self.label_pages_extract)

        self.lineEdit_intPages_extract = QLineEdit(self.frame_lineEdit_extract)
        self.lineEdit_intPages_extract.setObjectName(u"lineEdit_intPages_extract")
        self.lineEdit_intPages_extract.setMinimumSize(QSize(0, 30))
        self.lineEdit_intPages_extract.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_intPages_extract.setFont(font)
        self.lineEdit_intPages_extract.setStyleSheet(u"QLineEdit {\n"
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

        self.verticalLayout_26.addWidget(self.lineEdit_intPages_extract, 0, Qt.AlignTop)


        self.horizontalLayout_26.addWidget(self.frame_lineEdit_extract, 0, Qt.AlignTop)

        self.frame_checkBox_extract = QFrame(self.frame_extract_pages)
        self.frame_checkBox_extract.setObjectName(u"frame_checkBox_extract")
        self.frame_checkBox_extract.setStyleSheet(u"border:0px")
        self.frame_checkBox_extract.setFrameShape(QFrame.StyledPanel)
        self.frame_checkBox_extract.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_checkBox_extract)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(5, 5, 5, 5)
        self.checkBox_extractPages = QCheckBox(self.frame_checkBox_extract)
        self.checkBox_extractPages.setObjectName(u"checkBox_extractPages")
        self.checkBox_extractPages.setFont(font)
        self.checkBox_extractPages.setStyleSheet(u"QCheckBox::indicator {\n"
"   border: 2px solid rgb(64, 71, 88);\n"
"	border-radius: 9px;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_25.addWidget(self.checkBox_extractPages)

        self.checkBox_extractAfter = QCheckBox(self.frame_checkBox_extract)
        self.checkBox_extractAfter.setObjectName(u"checkBox_extractAfter")
        self.checkBox_extractAfter.setFont(font)
        self.checkBox_extractAfter.setStyleSheet(u"QCheckBox::indicator {\n"
"   border: 2px solid rgb(64, 71, 88);\n"
"	border-radius: 9px;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_25.addWidget(self.checkBox_extractAfter)

        self.checkBox_extractEach = QCheckBox(self.frame_checkBox_extract)
        self.checkBox_extractEach.setObjectName(u"checkBox_extractEach")
        self.checkBox_extractEach.setFont(font)
        self.checkBox_extractEach.setStyleSheet(u"QCheckBox::indicator {\n"
"   border: 2px solid rgb(64, 71, 88);\n"
"	border-radius: 9px;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_25.addWidget(self.checkBox_extractEach)


        self.horizontalLayout_26.addWidget(self.frame_checkBox_extract, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_23.addWidget(self.frame_extract_pages, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_22.addWidget(self.frame_extract, 0, Qt.AlignTop)

        self.stackedWidget.addWidget(self.page_extract)
        self.page_ocr = QWidget()
        self.page_ocr.setObjectName(u"page_ocr")
        self.verticalLayout_29 = QVBoxLayout(self.page_ocr)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.frame_ocr = QFrame(self.page_ocr)
        self.frame_ocr.setObjectName(u"frame_ocr")
        self.frame_ocr.setFrameShape(QFrame.StyledPanel)
        self.frame_ocr.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_ocr)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(5, 5, 5, 5)
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
        self.label_description_ocr.setFont(font1)
        self.label_description_ocr.setStyleSheet(u"")

        self.horizontalLayout_27.addWidget(self.label_description_ocr, 0, Qt.AlignLeft)


        self.verticalLayout_27.addWidget(self.frame_description_ocr)

        self.frame_top_page_ocr = QFrame(self.frame_ocr)
        self.frame_top_page_ocr.setObjectName(u"frame_top_page_ocr")
        self.frame_top_page_ocr.setMinimumSize(QSize(0, 0))
        self.frame_top_page_ocr.setMaximumSize(QSize(16777215, 16777215))
        self.frame_top_page_ocr.setStyleSheet(u"background-color:#343A4B;\n"
"border-radius: 7px;\n"
"border-top: 3px solid rgb(85, 170, 255);")
        self.frame_top_page_ocr.setFrameShape(QFrame.StyledPanel)
        self.frame_top_page_ocr.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_top_page_ocr)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(5, 5, 5, 5)
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
        self.frame_input_ocr.setFont(font3)
        self.frame_input_ocr.setStyleSheet(u"border: 0px;")
        self.frame_input_ocr.setFrameShape(QFrame.StyledPanel)
        self.frame_input_ocr.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_input_ocr)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 5, 0, 0)
        self.pushButton_run_ocr = QPushButton(self.frame_input_ocr)
        self.pushButton_run_ocr.setObjectName(u"pushButton_run_ocr")
        self.pushButton_run_ocr.setMaximumSize(QSize(40, 30))
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
        self.pushButton_run_ocr.setIcon(icon4)
        self.pushButton_run_ocr.setIconSize(QSize(18, 18))

        self.gridLayout_5.addWidget(self.pushButton_run_ocr, 0, 0, 1, 1)

        self.pushButton_selectFiles_ocr = QPushButton(self.frame_input_ocr)
        self.pushButton_selectFiles_ocr.setObjectName(u"pushButton_selectFiles_ocr")
        self.pushButton_selectFiles_ocr.setMinimumSize(QSize(160, 30))
        self.pushButton_selectFiles_ocr.setMaximumSize(QSize(150, 16777215))
        self.pushButton_selectFiles_ocr.setFont(font4)
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
        self.pushButton_selectFiles_ocr.setIcon(icon3)
        self.pushButton_selectFiles_ocr.setIconSize(QSize(18, 18))

        self.gridLayout_5.addWidget(self.pushButton_selectFiles_ocr, 0, 1, 1, 1)

        self.label_files_selected_ocr = QLabel(self.frame_input_ocr)
        self.label_files_selected_ocr.setObjectName(u"label_files_selected_ocr")
        self.label_files_selected_ocr.setFont(font)
        self.label_files_selected_ocr.setStyleSheet(u"color: rgb(122, 127, 135);")

        self.gridLayout_5.addWidget(self.label_files_selected_ocr, 1, 1, 1, 1, Qt.AlignHCenter)


        self.verticalLayout_28.addWidget(self.frame_input_ocr, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_dpi_ocr = QFrame(self.frame_left_ocr)
        self.frame_dpi_ocr.setObjectName(u"frame_dpi_ocr")
        self.frame_dpi_ocr.setMinimumSize(QSize(0, 50))
        self.frame_dpi_ocr.setFont(font3)
        self.frame_dpi_ocr.setFrameShape(QFrame.StyledPanel)
        self.frame_dpi_ocr.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_dpi_ocr)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(9, 0, 9, 5)
        self.label_intDpi_ocr = QLabel(self.frame_dpi_ocr)
        self.label_intDpi_ocr.setObjectName(u"label_intDpi_ocr")
        self.label_intDpi_ocr.setFont(font)

        self.horizontalLayout_9.addWidget(self.label_intDpi_ocr, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.lineEdit_intDpi_ocr = QLineEdit(self.frame_dpi_ocr)
        self.lineEdit_intDpi_ocr.setObjectName(u"lineEdit_intDpi_ocr")
        self.lineEdit_intDpi_ocr.setMinimumSize(QSize(0, 23))
        self.lineEdit_intDpi_ocr.setMaximumSize(QSize(50, 16777215))
        self.lineEdit_intDpi_ocr.setFont(font4)
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

        self.horizontalLayout_9.addWidget(self.lineEdit_intDpi_ocr, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_28.addWidget(self.frame_dpi_ocr, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.horizontalLayout_28.addWidget(self.frame_left_ocr, 0, Qt.AlignTop)

        self.frame_output_ocr = QFrame(self.frame_top_page_ocr)
        self.frame_output_ocr.setObjectName(u"frame_output_ocr")
        self.frame_output_ocr.setMinimumSize(QSize(0, 0))
        self.frame_output_ocr.setMaximumSize(QSize(16777215, 16777215))
        self.frame_output_ocr.setStyleSheet(u"border: 0px;")
        self.frame_output_ocr.setFrameShape(QFrame.StyledPanel)
        self.frame_output_ocr.setFrameShadow(QFrame.Raised)
        self.formLayout_6 = QFormLayout(self.frame_output_ocr)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.formLayout_6.setContentsMargins(0, 5, 5, 5)
        self.pushButton_outputPath_ocr = QPushButton(self.frame_output_ocr)
        self.pushButton_outputPath_ocr.setObjectName(u"pushButton_outputPath_ocr")
        self.pushButton_outputPath_ocr.setMinimumSize(QSize(40, 30))
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
        self.lineEdit_outputPath_ocr.setMinimumSize(QSize(0, 30))
        self.lineEdit_outputPath_ocr.setMaximumSize(QSize(320, 16777215))
        self.lineEdit_outputPath_ocr.setFont(font)
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
        self.lineEdit_filename_ocr.setMinimumSize(QSize(0, 30))
        self.lineEdit_filename_ocr.setMaximumSize(QSize(320, 16777215))
        self.lineEdit_filename_ocr.setFont(font)
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

        self.label_tags_ocr = QLabel(self.frame_output_ocr)
        self.label_tags_ocr.setObjectName(u"label_tags_ocr")
        self.label_tags_ocr.setMinimumSize(QSize(0, 0))
        self.label_tags_ocr.setMaximumSize(QSize(16777215, 16777215))
        self.label_tags_ocr.setFont(font)
        self.label_tags_ocr.setStyleSheet(u"color: rgb(112, 117, 125);")

        self.formLayout_6.setWidget(3, QFormLayout.FieldRole, self.label_tags_ocr)


        self.horizontalLayout_28.addWidget(self.frame_output_ocr, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_27.addWidget(self.frame_top_page_ocr)


        self.verticalLayout_29.addWidget(self.frame_ocr, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.stackedWidget.addWidget(self.page_ocr)
        self.page_zip = QWidget()
        self.page_zip.setObjectName(u"page_zip")
        self.verticalLayout_8 = QVBoxLayout(self.page_zip)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_zip = QFrame(self.page_zip)
        self.frame_zip.setObjectName(u"frame_zip")
        self.frame_zip.setFrameShape(QFrame.StyledPanel)
        self.frame_zip.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_zip)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
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
        self.label_description_zip.setFont(font1)
        self.label_description_zip.setStyleSheet(u"")

        self.horizontalLayout_21.addWidget(self.label_description_zip, 0, Qt.AlignLeft)


        self.verticalLayout_6.addWidget(self.frame_description_zip)

        self.frame_top_page_zip = QFrame(self.frame_zip)
        self.frame_top_page_zip.setObjectName(u"frame_top_page_zip")
        self.frame_top_page_zip.setMinimumSize(QSize(646, 0))
        self.frame_top_page_zip.setMaximumSize(QSize(16777215, 16777215))
        self.frame_top_page_zip.setStyleSheet(u"background-color:#343A4B;\n"
"border-radius: 7px;\n"
"border-top: 3px solid rgb(85, 170, 255);")
        self.frame_top_page_zip.setFrameShape(QFrame.StyledPanel)
        self.frame_top_page_zip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_top_page_zip)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(5, 5, 5, 5)
        self.frame_input_zip = QFrame(self.frame_top_page_zip)
        self.frame_input_zip.setObjectName(u"frame_input_zip")
        self.frame_input_zip.setMinimumSize(QSize(230, 0))
        self.frame_input_zip.setMaximumSize(QSize(16777215, 16777215))
        self.frame_input_zip.setFont(font3)
        self.frame_input_zip.setStyleSheet(u"border: 0px;")
        self.frame_input_zip.setFrameShape(QFrame.StyledPanel)
        self.frame_input_zip.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_input_zip)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(5, 5, 0, 5)
        self.lineEdit_rootDirectory_zip = QLineEdit(self.frame_input_zip)
        self.lineEdit_rootDirectory_zip.setObjectName(u"lineEdit_rootDirectory_zip")
        self.lineEdit_rootDirectory_zip.setMinimumSize(QSize(0, 30))
        self.lineEdit_rootDirectory_zip.setMaximumSize(QSize(180, 16777215))
        self.lineEdit_rootDirectory_zip.setFont(font)
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

        self.gridLayout_7.addWidget(self.lineEdit_rootDirectory_zip, 1, 1, 1, 1)

        self.pushButton_selectRootDirectory_zip = QPushButton(self.frame_input_zip)
        self.pushButton_selectRootDirectory_zip.setObjectName(u"pushButton_selectRootDirectory_zip")
        self.pushButton_selectRootDirectory_zip.setMinimumSize(QSize(160, 30))
        self.pushButton_selectRootDirectory_zip.setMaximumSize(QSize(180, 16777215))
        self.pushButton_selectRootDirectory_zip.setFont(font4)
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

        self.gridLayout_7.addWidget(self.pushButton_selectRootDirectory_zip, 0, 1, 1, 1)

        self.pushButton_run_zip = QPushButton(self.frame_input_zip)
        self.pushButton_run_zip.setObjectName(u"pushButton_run_zip")
        self.pushButton_run_zip.setMinimumSize(QSize(40, 30))
        self.pushButton_run_zip.setMaximumSize(QSize(40, 30))
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
        self.pushButton_run_zip.setIcon(icon4)
        self.pushButton_run_zip.setIconSize(QSize(18, 18))

        self.gridLayout_7.addWidget(self.pushButton_run_zip, 0, 0, 1, 1)


        self.horizontalLayout_29.addWidget(self.frame_input_zip, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame_output_zip = QFrame(self.frame_top_page_zip)
        self.frame_output_zip.setObjectName(u"frame_output_zip")
        self.frame_output_zip.setMinimumSize(QSize(371, 115))
        self.frame_output_zip.setMaximumSize(QSize(16777215, 16777215))
        self.frame_output_zip.setStyleSheet(u"border: 0px;")
        self.frame_output_zip.setFrameShape(QFrame.StyledPanel)
        self.frame_output_zip.setFrameShadow(QFrame.Raised)
        self.formLayout_7 = QFormLayout(self.frame_output_zip)
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.formLayout_7.setContentsMargins(0, 5, 5, 5)
        self.lineEdit_filename_zip = QLineEdit(self.frame_output_zip)
        self.lineEdit_filename_zip.setObjectName(u"lineEdit_filename_zip")
        self.lineEdit_filename_zip.setMinimumSize(QSize(250, 30))
        self.lineEdit_filename_zip.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_filename_zip.setFont(font)
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

        self.label_tags_zip = QLabel(self.frame_output_zip)
        self.label_tags_zip.setObjectName(u"label_tags_zip")
        self.label_tags_zip.setMinimumSize(QSize(0, 30))
        self.label_tags_zip.setMaximumSize(QSize(16777215, 16777215))
        self.label_tags_zip.setFont(font)
        self.label_tags_zip.setStyleSheet(u"color: rgb(112, 117, 125);")

        self.formLayout_7.setWidget(3, QFormLayout.FieldRole, self.label_tags_zip)

        self.pushButton_outputPath_zip = QPushButton(self.frame_output_zip)
        self.pushButton_outputPath_zip.setObjectName(u"pushButton_outputPath_zip")
        self.pushButton_outputPath_zip.setMinimumSize(QSize(40, 30))
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
        self.lineEdit_outputPath_zip.setMinimumSize(QSize(250, 30))
        self.lineEdit_outputPath_zip.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_outputPath_zip.setFont(font)
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


        self.horizontalLayout_29.addWidget(self.frame_output_zip, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_6.addWidget(self.frame_top_page_zip)


        self.verticalLayout_8.addWidget(self.frame_zip, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.stackedWidget.addWidget(self.page_zip)
        self.page_search = QWidget()
        self.page_search.setObjectName(u"page_search")
        self.verticalLayout_12 = QVBoxLayout(self.page_search)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(30, 9, 30, 5)
        self.frame_search = QFrame(self.page_search)
        self.frame_search.setObjectName(u"frame_search")
        self.frame_search.setMinimumSize(QSize(830, 0))
        self.frame_search.setFrameShape(QFrame.StyledPanel)
        self.frame_search.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_search)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(5, 5, 5, 5)
        self.frame_description_search = QFrame(self.frame_search)
        self.frame_description_search.setObjectName(u"frame_description_search")
        self.frame_description_search.setFrameShape(QFrame.StyledPanel)
        self.frame_description_search.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_description_search)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(5, 5, 5, 5)
        self.label_description_search = QLabel(self.frame_description_search)
        self.label_description_search.setObjectName(u"label_description_search")
        self.label_description_search.setFont(font1)

        self.horizontalLayout_30.addWidget(self.label_description_search, 0, Qt.AlignLeft)


        self.verticalLayout_18.addWidget(self.frame_description_search, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.frame_top_page = QFrame(self.frame_search)
        self.frame_top_page.setObjectName(u"frame_top_page")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_top_page.sizePolicy().hasHeightForWidth())
        self.frame_top_page.setSizePolicy(sizePolicy5)
        self.frame_top_page.setMinimumSize(QSize(0, 0))
        self.frame_top_page.setMaximumSize(QSize(830, 16777215))
        self.frame_top_page.setStyleSheet(u"background-color:#343A4B;\n"
"border-radius: 7px;\n"
"border-top: 3px solid rgb(85, 170, 255);")
        self.frame_top_page.setFrameShape(QFrame.StyledPanel)
        self.frame_top_page.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_top_page)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(5, 5, 5, 5)
        self.frame_input = QFrame(self.frame_top_page)
        self.frame_input.setObjectName(u"frame_input")
        self.frame_input.setMinimumSize(QSize(160, 0))
        self.frame_input.setMaximumSize(QSize(16777215, 16777215))
        self.frame_input.setFont(font3)
        self.frame_input.setStyleSheet(u"border: 0px;")
        self.frame_input.setFrameShape(QFrame.StyledPanel)
        self.frame_input.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_input)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(9, 5, 9, 5)
        self.pushButton_selectFiles_search = QPushButton(self.frame_input)
        self.pushButton_selectFiles_search.setObjectName(u"pushButton_selectFiles_search")
        self.pushButton_selectFiles_search.setMinimumSize(QSize(160, 30))
        self.pushButton_selectFiles_search.setMaximumSize(QSize(160, 16777215))
        self.pushButton_selectFiles_search.setFont(font4)
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
        self.pushButton_selectFiles_search.setIcon(icon3)
        self.pushButton_selectFiles_search.setIconSize(QSize(18, 18))

        self.verticalLayout_14.addWidget(self.pushButton_selectFiles_search)

        self.label_files_selected_search = QLabel(self.frame_input)
        self.label_files_selected_search.setObjectName(u"label_files_selected_search")
        self.label_files_selected_search.setFont(font)
        self.label_files_selected_search.setStyleSheet(u"color: rgb(122, 127, 135);")

        self.verticalLayout_14.addWidget(self.label_files_selected_search, 0, Qt.AlignHCenter)


        self.horizontalLayout_13.addWidget(self.frame_input, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame_output = QFrame(self.frame_top_page)
        self.frame_output.setObjectName(u"frame_output")
        self.frame_output.setMinimumSize(QSize(0, 0))
        self.frame_output.setMaximumSize(QSize(370, 16777215))
        self.frame_output.setStyleSheet(u"border: 0px;")
        self.frame_output.setFrameShape(QFrame.StyledPanel)
        self.frame_output.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_output)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(9, 5, 9, 5)
        self.pushButton_outputPath_search = QPushButton(self.frame_output)
        self.pushButton_outputPath_search.setObjectName(u"pushButton_outputPath_search")
        self.pushButton_outputPath_search.setMinimumSize(QSize(40, 30))
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

        self.label_tags_search = QLabel(self.frame_output)
        self.label_tags_search.setObjectName(u"label_tags_search")
        self.label_tags_search.setMinimumSize(QSize(0, 0))
        self.label_tags_search.setMaximumSize(QSize(16777215, 16777215))
        self.label_tags_search.setFont(font)
        self.label_tags_search.setStyleSheet(u"color: rgb(112, 117, 125);")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.label_tags_search)

        self.lineEdit_outputPath_search = QLineEdit(self.frame_output)
        self.lineEdit_outputPath_search.setObjectName(u"lineEdit_outputPath_search")
        self.lineEdit_outputPath_search.setMinimumSize(QSize(0, 30))
        self.lineEdit_outputPath_search.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_outputPath_search.setFont(font)
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
        self.lineEdit_filename_search.setMinimumSize(QSize(0, 30))
        self.lineEdit_filename_search.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_filename_search.setFont(font)
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


        self.horizontalLayout_13.addWidget(self.frame_output)

        self.frame_checkBox_ = QFrame(self.frame_top_page)
        self.frame_checkBox_.setObjectName(u"frame_checkBox_")
        self.frame_checkBox_.setMinimumSize(QSize(0, 0))
        self.frame_checkBox_.setMaximumSize(QSize(16777215, 16777215))
        self.frame_checkBox_.setFont(font4)
        self.frame_checkBox_.setStyleSheet(u"border: 0px;")
        self.frame_checkBox_.setFrameShape(QFrame.StyledPanel)
        self.frame_checkBox_.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_checkBox_)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(20)
        self.gridLayout_4.setContentsMargins(9, 5, 9, 5)
        Ui_MainWindow.checkBox_ignoreSpecialChar_search = QCheckBox(self.frame_checkBox_)
        self.checkBox_ignoreSpecialChar_search.setObjectName(u"checkBox_ignoreSpecialChar_search")
        self.checkBox_ignoreSpecialChar_search.setMinimumSize(QSize(0, 20))
        self.checkBox_ignoreSpecialChar_search.setFont(font4)
        self.checkBox_ignoreSpecialChar_search.setStyleSheet(u"QCheckBox::indicator {\n"
"   border: 2px solid rgb(64, 71, 88);\n"
"	border-radius: 9px;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"}")
        self.checkBox_ignoreSpecialChar_search.setTristate(False)

        self.gridLayout_4.addWidget(self.checkBox_ignoreSpecialChar_search, 1, 0, 1, 1)

        Ui_MainWindow.checkBox_onlyPages_search = QCheckBox(self.frame_checkBox_)
        self.checkBox_onlyPages_search.setObjectName(u"checkBox_onlyPages_search")
        self.checkBox_onlyPages_search.setMinimumSize(QSize(0, 20))
        self.checkBox_onlyPages_search.setFont(font4)
        self.checkBox_onlyPages_search.setStyleSheet(u"QCheckBox::indicator {\n"
"   border: 2px solid rgb(64, 71, 88);\n"
"	border-radius: 9px;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"}")

        self.gridLayout_4.addWidget(self.checkBox_onlyPages_search, 0, 0, 1, 1)

        Ui_MainWindow.checkBox_ignorePontuation_search = QCheckBox(self.frame_checkBox_)
        self.checkBox_ignorePontuation_search.setObjectName(u"checkBox_ignorePontuation_search")
        self.checkBox_ignorePontuation_search.setMinimumSize(QSize(0, 20))
        self.checkBox_ignorePontuation_search.setFont(font4)
        self.checkBox_ignorePontuation_search.setStyleSheet(u"QCheckBox::indicator {\n"
"   border: 2px solid rgb(64, 71, 88);\n"
"	border-radius: 9px;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"}")

        self.gridLayout_4.addWidget(self.checkBox_ignorePontuation_search, 2, 0, 1, 1)

        Ui_MainWindow.checkBox_ignoreSpaces_search = QCheckBox(self.frame_checkBox_)
        self.checkBox_ignoreSpaces_search.setObjectName(u"checkBox_ignoreSpaces_search")
        self.checkBox_ignoreSpaces_search.setMinimumSize(QSize(0, 20))
        self.checkBox_ignoreSpaces_search.setFont(font4)
        self.checkBox_ignoreSpaces_search.setStyleSheet(u"QCheckBox::indicator {\n"
"   border: 2px solid rgb(64, 71, 88);\n"
"	border-radius: 9px;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"}")

        self.gridLayout_4.addWidget(self.checkBox_ignoreSpaces_search, 0, 1, 1, 1)

        Ui_MainWindow.checkBox_ignoreFirstPage_search = QCheckBox(self.frame_checkBox_)
        self.checkBox_ignoreFirstPage_search.setObjectName(u"checkBox_ignoreFirstPage_search")
        self.checkBox_ignoreFirstPage_search.setMinimumSize(QSize(0, 20))
        self.checkBox_ignoreFirstPage_search.setFont(font4)
        self.checkBox_ignoreFirstPage_search.setStyleSheet(u"QCheckBox::indicator {\n"
"   border: 2px solid rgb(64, 71, 88);\n"
"	border-radius: 9px;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"}")

        self.gridLayout_4.addWidget(self.checkBox_ignoreFirstPage_search, 1, 1, 1, 1)


        self.horizontalLayout_13.addWidget(self.frame_checkBox_, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_18.addWidget(self.frame_top_page, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_12.addWidget(self.frame_search, 0, Qt.AlignHCenter)

        self.frame_content_page = QFrame(self.page_search)
        self.frame_content_page.setObjectName(u"frame_content_page")
        self.frame_content_page.setStyleSheet(u"border:0px;")
        self.frame_content_page.setFrameShape(QFrame.StyledPanel)
        self.frame_content_page.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_content_page)
        self.verticalLayout_13.setSpacing(16)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(5, 5, 5, 0)
        self.frame_middle = QFrame(self.frame_content_page)
        self.frame_middle.setObjectName(u"frame_middle")
        self.frame_middle.setMinimumSize(QSize(830, 0))
        self.frame_middle.setStyleSheet(u"background-color:#343A4B;\n"
"border-radius: 7px;\n"
"\n"
"")
        self.frame_middle.setFrameShape(QFrame.StyledPanel)
        self.frame_middle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_middle)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(5, 5, 5, 5)
        self.frame_config = QFrame(self.frame_middle)
        self.frame_config.setObjectName(u"frame_config")
        self.frame_config.setMaximumSize(QSize(16777215, 16777215))
        self.frame_config.setStyleSheet(u"border:0px;")
        self.frame_config.setFrameShape(QFrame.StyledPanel)
        self.frame_config.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_config)
        self.horizontalLayout_18.setSpacing(10)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(-1, -1, -1, 5)
        self.pushButton_run_search = QPushButton(self.frame_config)
        self.pushButton_run_search.setObjectName(u"pushButton_run_search")
        self.pushButton_run_search.setMinimumSize(QSize(40, 30))
        self.pushButton_run_search.setMaximumSize(QSize(40, 16777215))
        self.pushButton_run_search.setFont(font3)
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

        self.horizontalLayout_18.addWidget(self.pushButton_run_search)

        self.pushButton_save_search = QPushButton(self.frame_config)
        self.pushButton_save_search.setObjectName(u"pushButton_save_search")
        self.pushButton_save_search.setMinimumSize(QSize(40, 30))
        self.pushButton_save_search.setMaximumSize(QSize(40, 16777215))
        self.pushButton_save_search.setStyleSheet(u"QPushButton {\n"
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
        icon7.addFile(u":/20x20/icons/20x20/cil-save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_save_search.setIcon(icon7)
        self.pushButton_save_search.setIconSize(QSize(18, 18))

        self.horizontalLayout_18.addWidget(self.pushButton_save_search)

        self.pushButton_delete_search = QPushButton(self.frame_config)
        self.pushButton_delete_search.setObjectName(u"pushButton_delete_search")
        self.pushButton_delete_search.setMinimumSize(QSize(40, 30))
        self.pushButton_delete_search.setMaximumSize(QSize(40, 16777215))
        self.pushButton_delete_search.setFont(font3)
        self.pushButton_delete_search.setStyleSheet(u"QPushButton {\n"
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
        self.pushButton_delete_search.setIcon(icon8)
        self.pushButton_delete_search.setIconSize(QSize(18, 18))

        self.horizontalLayout_18.addWidget(self.pushButton_delete_search)

        self.comboBox_configs_search = QComboBox(self.frame_config)
        self.comboBox_configs_search.addItem("")
        self.comboBox_configs_search.setObjectName(u"comboBox_configs_search")
        self.comboBox_configs_search.setMinimumSize(QSize(0, 30))
        self.comboBox_configs_search.setMaximumSize(QSize(150, 16777215))
        self.comboBox_configs_search.setFont(font4)
        self.comboBox_configs_search.setStyleSheet(u"QComboBox {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"	border-radius: 5px;	\n"
"	background-color:#2E3342;\n"
"}\n"
"QComboBox:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.comboBox_configs_search.setEditable(True)
        self.comboBox_configs_search.setDuplicatesEnabled(False)
        self.comboBox_configs_search.setFrame(True)

        self.horizontalLayout_18.addWidget(self.comboBox_configs_search)

        self.label_subtitles_search = QLabel(self.frame_config)
        self.label_subtitles_search.setObjectName(u"label_subtitles_search")
        self.label_subtitles_search.setFont(font)
        self.label_subtitles_search.setStyleSheet(u"color: rgb(112, 117, 125);")

        self.horizontalLayout_18.addWidget(self.label_subtitles_search)


        self.verticalLayout_19.addWidget(self.frame_config)

        self.frame_keywords = QFrame(self.frame_middle)
        self.frame_keywords.setObjectName(u"frame_keywords")
        self.frame_keywords.setMaximumSize(QSize(16777215, 16777215))
        self.frame_keywords.setStyleSheet(u"border:0px;")
        self.frame_keywords.setFrameShape(QFrame.StyledPanel)
        self.frame_keywords.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_keywords)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(-1, 5, -1, 9)
        self.label_moveto_search = QLabel(self.frame_keywords)
        self.label_moveto_search.setObjectName(u"label_moveto_search")
        self.label_moveto_search.setMaximumSize(QSize(16777215, 16777215))
        self.label_moveto_search.setFont(font)
        self.label_moveto_search.setStyleSheet(u"color: rgb(112, 117, 125);")
        self.label_moveto_search.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_moveto_search, 1, 2, 1, 1)

        self.label_keywords_search = QLabel(self.frame_keywords)
        self.label_keywords_search.setObjectName(u"label_keywords_search")
        self.label_keywords_search.setMinimumSize(QSize(0, 0))
        self.label_keywords_search.setMaximumSize(QSize(16777215, 16777215))
        self.label_keywords_search.setFont(font)
        self.label_keywords_search.setStyleSheet(u"color: rgb(112, 117, 125);")
        self.label_keywords_search.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_keywords_search, 1, 1, 1, 1)

        Ui_MainWindow.comboBox_operator_search = QComboBox(self.frame_keywords)
        self.comboBox_operator_search.addItem("")
        self.comboBox_operator_search.addItem("")
        self.comboBox_operator_search.setObjectName(u"comboBox_operator_search")
        self.comboBox_operator_search.setMinimumSize(QSize(0, 30))
        self.comboBox_operator_search.setMaximumSize(QSize(16777215, 16777215))
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(8)
        self.comboBox_operator_search.setFont(font6)
        self.comboBox_operator_search.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}F")

        self.gridLayout_3.addWidget(self.comboBox_operator_search, 0, 0, 1, 1)

        Ui_MainWindow.lineEdit_keywords_search = QLineEdit(self.frame_keywords)
        self.lineEdit_keywords_search.setObjectName(u"lineEdit_keywords_search")
        self.lineEdit_keywords_search.setMinimumSize(QSize(0, 30))
        self.lineEdit_keywords_search.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_keywords_search.setFont(font)
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

        self.label_else_search = QLabel(self.frame_keywords)
        self.label_else_search.setObjectName(u"label_else_search")
        self.label_else_search.setMaximumSize(QSize(16777215, 16777215))
        font7 = QFont()
        font7.setFamily(u"Segoe UI")
        font7.setPointSize(10)
        font7.setBold(False)
        font7.setWeight(50)
        self.label_else_search.setFont(font7)
        self.label_else_search.setStyleSheet(u"color: rgb(112, 117, 125);")
        self.label_else_search.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_else_search, 1, 3, 1, 1)

        Ui_MainWindow.lineEdit_moveto_search = QLineEdit(self.frame_keywords)
        self.lineEdit_moveto_search.setObjectName(u"lineEdit_moveto_search")
        self.lineEdit_moveto_search.setMinimumSize(QSize(200, 30))
        self.lineEdit_moveto_search.setMaximumSize(QSize(220, 16777215))
        self.lineEdit_moveto_search.setFont(font)
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

        Ui_MainWindow.lineEdit_else_search = QLineEdit(self.frame_keywords)
        self.lineEdit_else_search.setObjectName(u"lineEdit_else_search")
        self.lineEdit_else_search.setMinimumSize(QSize(200, 30))
        self.lineEdit_else_search.setMaximumSize(QSize(220, 16777215))
        self.lineEdit_else_search.setFont(font)
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


        self.verticalLayout_19.addWidget(self.frame_keywords)


        self.verticalLayout_13.addWidget(self.frame_middle, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_tab = QFrame(self.frame_content_page)
        self.frame_tab.setObjectName(u"frame_tab")
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
        icon9 = QIcon()
        icon9.addFile(u":/20x20/icons/20x20/cil-library-add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_addTable_search.setIcon(icon9)
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
        self.pushButton_deleteTable_search.setIcon(icon8)
        self.pushButton_deleteTable_search.setIconSize(QSize(18, 18))

        self.horizontalLayout_11.addWidget(self.pushButton_deleteTable_search)


        self.verticalLayout_7.addWidget(self.frame_vbuttons, 0, Qt.AlignLeft)

        Ui_MainWindow.tabWidget = QTabWidget(self.frame_tab)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setFont(font4)
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

        self.verticalLayout_7.addWidget(self.tabWidget)


        self.verticalLayout_13.addWidget(self.frame_tab)


        self.verticalLayout_12.addWidget(self.frame_content_page)

        self.stackedWidget.addWidget(self.page_search)
        self.page_credits = QWidget()
        self.page_credits.setObjectName(u"page_credits")
        self.stackedWidget.addWidget(self.page_credits)
        self.page_help = QWidget()
        self.page_help.setObjectName(u"page_help")
        self.stackedWidget.addWidget(self.page_help)

        self.verticalLayout_9.addWidget(self.stackedWidget)

        self.frame_bottom = QFrame(self.frame_content)
        self.frame_bottom.setObjectName(u"frame_bottom")
        self.frame_bottom.setMinimumSize(QSize(0, 30))
        self.frame_bottom.setMaximumSize(QSize(16777215, 16777215))
        self.frame_bottom.setFrameShape(QFrame.StyledPanel)
        self.frame_bottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_bottom)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(30, 0, 0, 0)
        self.label_feedback = QLabel(self.frame_bottom)
        self.label_feedback.setObjectName(u"label_feedback")
        self.label_feedback.setMinimumSize(QSize(0, 30))
        self.label_feedback.setMaximumSize(QSize(16777215, 16777215))
        self.label_feedback.setFont(font5)

        self.verticalLayout_16.addWidget(self.label_feedback, 0, Qt.AlignTop)


        self.verticalLayout_9.addWidget(self.frame_bottom, 0, Qt.AlignTop)

        self.frame_bottom.raise_()
        self.stackedWidget.raise_()

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
        self.label_credits.setFont(font)
        self.label_credits.setStyleSheet(u"color: rgb(112, 117, 125);")

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

        self.stackedWidget.setCurrentIndex(0)
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
        self.label_description_merge.setText(QCoreApplication.translate("MainWindow", u"MESCLAR ARQUIVOS PDF", None))
        self.pushButton_selectFiles_merge.setText(QCoreApplication.translate("MainWindow", u"Selecionar arquivos", None))
        self.pushButton_run_merge.setText("")
        self.label_files_selected_merge.setText(QCoreApplication.translate("MainWindow", u"0 arquivos selecionados.", None))
        self.lineEdit_outputPath_merge.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecionar diret\u00f3rio de sa\u00edda", None))
        self.lineEdit_filename_merge.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome do arquivo: #basename", None))
        self.label_tags_merge.setText(QCoreApplication.translate("MainWindow", u"Tags dispon\u00edveis: #year #month #day #time #basename", None))
        self.pushButton_outputPath_merge.setText("")
        self.label_description_mergebatch.setText(QCoreApplication.translate("MainWindow", u"MESCLAR ARQUIVOS PDF DE UM DIRET\u00d3RIO", None))
        self.lineEdit_rootDirectory_mergebatch.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Diret\u00f3rio raiz", None))
        self.pushButton_selectRootDirectory_mergebatch.setText(QCoreApplication.translate("MainWindow", u"Abrir diret\u00f3rio raiz", None))
        self.pushButton_run_mergebatch.setText("")
        self.lineEdit_filename_mergebatch.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome do arquivo: #basename", None))
        self.label_tags_mergebatch.setText(QCoreApplication.translate("MainWindow", u"Tags dispon\u00edveis: #year #month #day #time #basename", None))
        self.pushButton_outputPath_mergebatch.setText("")
        self.lineEdit_outputPath_mergebatch.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecionar diret\u00f3rio de sa\u00edda", None))
        self.label_description_extract.setText(QCoreApplication.translate("MainWindow", u"EXTRAIR P\u00c1GINAS", None))
        self.pushButton_selectFiles_extract.setText(QCoreApplication.translate("MainWindow", u"Selecionar arquivos", None))
        self.pushButton_run_extract.setText("")
        self.label_files_selected_extract.setText(QCoreApplication.translate("MainWindow", u"0 arquivos selecionados.", None))
        self.pushButton_outputPath_extract.setText("")
        self.lineEdit_outputPath_extract.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecionar diret\u00f3rio de sa\u00edda", None))
        self.lineEdit_filename_extract.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome do arquivo: #basename", None))
        self.label_tags_extract.setText(QCoreApplication.translate("MainWindow", u"Tags dispon\u00edveis: #year #month #day\n"
"#time #page #basename", None))
        self.label_pages_extract.setText(QCoreApplication.translate("MainWindow", u"P\u00e1ginas", None))
        self.lineEdit_intPages_extract.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ex: 3,8,12", None))
        self.checkBox_extractPages.setText(QCoreApplication.translate("MainWindow", u"Todas as p\u00e1ginas indicadas", None))
        self.checkBox_extractAfter.setText(QCoreApplication.translate("MainWindow", u"Dividir nas p\u00e1ginas indicadas", None))
        self.checkBox_extractEach.setText(QCoreApplication.translate("MainWindow", u"A cada n p\u00e1ginas", None))
        self.label_description_ocr.setText(QCoreApplication.translate("MainWindow", u"ESCANEAR ARQUIVOS PDF", None))
        self.pushButton_run_ocr.setText("")
        self.pushButton_selectFiles_ocr.setText(QCoreApplication.translate("MainWindow", u"Selecionar arquivos", None))
        self.label_files_selected_ocr.setText(QCoreApplication.translate("MainWindow", u"0 arquivos selecionados.", None))
        self.label_intDpi_ocr.setText(QCoreApplication.translate("MainWindow", u"DPI:", None))
        self.lineEdit_intDpi_ocr.setPlaceholderText(QCoreApplication.translate("MainWindow", u"200", None))
        self.pushButton_outputPath_ocr.setText("")
        self.lineEdit_outputPath_ocr.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecionar diret\u00f3rio de sa\u00edda", None))
        self.lineEdit_filename_ocr.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome do arquivo: #basename", None))
        self.label_tags_ocr.setText(QCoreApplication.translate("MainWindow", u"Tags dispon\u00edveis: #year #month #day #time #basename", None))
        self.label_description_zip.setText(QCoreApplication.translate("MainWindow", u"CRIAR FICHEIRO ZIP DE ARQUIVOS PDF DE UM DIRET\u00d3RIO", None))
        self.lineEdit_rootDirectory_zip.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Diret\u00f3rio raiz", None))
        self.pushButton_selectRootDirectory_zip.setText(QCoreApplication.translate("MainWindow", u"Abrir diret\u00f3rio", None))
        self.pushButton_run_zip.setText("")
        self.lineEdit_filename_zip.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome do arquivo: #basename", None))
        self.label_tags_zip.setText(QCoreApplication.translate("MainWindow", u"Tags dispon\u00edveis: #year #month #day #time #basename", None))
        self.pushButton_outputPath_zip.setText("")
        self.lineEdit_outputPath_zip.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecionar diret\u00f3rio de sa\u00edda", None))
        self.label_description_search.setText(QCoreApplication.translate("MainWindow", u"ORGANIZAR ARQUIVOS PDF PROCURANDO POR EXPRESS\u00d5ES REGULARES", None))
        self.pushButton_selectFiles_search.setText(QCoreApplication.translate("MainWindow", u"Selecionar arquivos", None))
        self.label_files_selected_search.setText(QCoreApplication.translate("MainWindow", u"0 arquivos selecionados.", None))
        self.pushButton_outputPath_search.setText("")
        self.label_tags_search.setText(QCoreApplication.translate("MainWindow", u"Tags dispon\u00edveis: #year #month #day #time\n"
"#page #basename #group #keywords", None))
        self.lineEdit_outputPath_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecionar diret\u00f3rio de sa\u00edda", None))
        self.lineEdit_filename_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome do arquivo: #basename", None))
        self.checkBox_ignoreSpecialChar_search.setText(QCoreApplication.translate("MainWindow", u"Ignorar acentos", None))
        self.checkBox_onlyPages_search.setText(QCoreApplication.translate("MainWindow", u"Mover apenas p\u00e1ginas", None))
        self.checkBox_ignorePontuation_search.setText(QCoreApplication.translate("MainWindow", u"Ignorar pontua\u00e7\u00e3o", None))
        self.checkBox_ignoreSpaces_search.setText(QCoreApplication.translate("MainWindow", u"Ignorar espa\u00e7os", None))
        self.checkBox_ignoreFirstPage_search.setText(QCoreApplication.translate("MainWindow", u"Ignorar primeira linha", None))
        self.pushButton_run_search.setText("")
        self.pushButton_save_search.setText("")
        self.pushButton_delete_search.setText("")
        self.comboBox_configs_search.setItemText(0, QCoreApplication.translate("MainWindow", u"Nova configura\u00e7\u00e3o", None))

        self.comboBox_configs_search.setCurrentText(QCoreApplication.translate("MainWindow", u"Nova configura\u00e7\u00e3o", None))
        self.label_subtitles_search.setText(QCoreApplication.translate("MainWindow", u"Nome_da_tabela:N\u00famero_da_coluna", None))
        self.label_moveto_search.setText(QCoreApplication.translate("MainWindow", u"Mover para pasta", None))
        self.label_keywords_search.setText(QCoreApplication.translate("MainWindow", u"Procurar por express\u00f5es", None))
        self.comboBox_operator_search.setItemText(0, QCoreApplication.translate("MainWindow", u"OU", None))
        self.comboBox_operator_search.setItemText(1, QCoreApplication.translate("MainWindow", u"E", None))

        self.lineEdit_keywords_search.setText("")
        self.lineEdit_keywords_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ex: Banco de dados:1,Banco de dados:2", None))
        self.label_else_search.setText(QCoreApplication.translate("MainWindow", u"Se n\u00e3o encontrar mover para pasta", None))
        self.lineEdit_moveto_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ex: Banco de dados:2", None))
        self.lineEdit_else_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ex: N\u00e3o encontrado", None))
        self.pushButton_addTable_search.setText("")
        self.pushButton_deleteTable_search.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.label_feedback.setText(QCoreApplication.translate("MainWindow", u"Pesquisando por palavra...", None))
        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"https://github.com/demelomatt", None))
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"v1.1.0", None))
    # retranslateUi

