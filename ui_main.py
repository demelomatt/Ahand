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
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(9, 9, 9, 9)
        self.frame_main_merge = QFrame(self.page_merge)
        self.frame_main_merge.setObjectName(u"frame_main_merge")
        self.frame_main_merge.setFrameShape(QFrame.StyledPanel)
        self.frame_main_merge.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_main_merge)
        self.verticalLayout_17.setSpacing(30)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(5, 5, 5, 5)
        self.frame_home = QFrame(self.frame_main_merge)
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
        self.frame_merge.setMinimumSize(QSize(0, 0))
        self.frame_merge.setFrameShape(QFrame.StyledPanel)
        self.frame_merge.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_merge)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(9, 9, 9, 9)
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
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(11)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_description_merge.setFont(font3)
        self.label_description_merge.setStyleSheet(u"")

        self.horizontalLayout_14.addWidget(self.label_description_merge, 0, Qt.AlignHCenter)


        self.verticalLayout_10.addWidget(self.frame_description_merge, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.frame_top_page_merge = QFrame(self.frame_merge)
        self.frame_top_page_merge.setObjectName(u"frame_top_page_merge")
        self.frame_top_page_merge.setMinimumSize(QSize(0, 150))
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
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        self.frame_input_merge.setFont(font4)
        self.frame_input_merge.setStyleSheet(u"border: 0px;")
        self.frame_input_merge.setFrameShape(QFrame.StyledPanel)
        self.frame_input_merge.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_input_merge)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setContentsMargins(9, 5, 0, 5)
        self.pushButton_run_merge = QPushButton(self.frame_input_merge)
        self.pushButton_run_merge.setObjectName(u"pushButton_run_merge")
        self.pushButton_run_merge.setMinimumSize(QSize(40, 0))
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
        icon3 = QIcon()
        icon3.addFile(u":/20x20/icons/20x20/cil-media-play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_run_merge.setIcon(icon3)
        self.pushButton_run_merge.setIconSize(QSize(18, 18))

        self.gridLayout.addWidget(self.pushButton_run_merge, 0, 0, 1, 1)

        self.pushButton_selectFiles_merge = QPushButton(self.frame_input_merge)
        self.pushButton_selectFiles_merge.setObjectName(u"pushButton_selectFiles_merge")
        self.pushButton_selectFiles_merge.setMinimumSize(QSize(160, 30))
        self.pushButton_selectFiles_merge.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_selectFiles_merge.setFont(font)
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
        Ui_MainWindow.lineEdit_outputPath_merge = QLineEdit(self.frame_output_merge)
        self.lineEdit_outputPath_merge.setObjectName(u"lineEdit_outputPath_merge")
        self.lineEdit_outputPath_merge.setMinimumSize(QSize(0, 30))
        self.lineEdit_outputPath_merge.setMaximumSize(QSize(360, 16777215))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(12)
        self.lineEdit_outputPath_merge.setFont(font5)
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

        Ui_MainWindow.lineEdit_filename_merge = QLineEdit(self.frame_output_merge)
        self.lineEdit_filename_merge.setObjectName(u"lineEdit_filename_merge")
        self.lineEdit_filename_merge.setMinimumSize(QSize(330, 30))
        self.lineEdit_filename_merge.setMaximumSize(QSize(360, 16777215))
        self.lineEdit_filename_merge.setFont(font5)
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
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(11)
        self.label_tags_merge.setFont(font6)
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


        self.verticalLayout_10.addWidget(self.frame_top_page_merge, 0, Qt.AlignHCenter)


        self.verticalLayout_21.addWidget(self.frame_merge, 0, Qt.AlignHCenter)


        self.verticalLayout_17.addWidget(self.frame_home)

        self.frame_drop_merge = QFrame(self.frame_main_merge)
        self.frame_drop_merge.setObjectName(u"frame_drop_merge")
        self.frame_drop_merge.setMinimumSize(QSize(600, 200))
        self.frame_drop_merge.setMaximumSize(QSize(16777215, 16777215))
        self.frame_drop_merge.setFrameShape(QFrame.StyledPanel)
        self.frame_drop_merge.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_drop_merge)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(5, 9, 5, -1)
        self.label_drop_merge = QLabel(self.frame_drop_merge)
        self.label_drop_merge.setObjectName(u"label_drop_merge")
        self.label_drop_merge.setMinimumSize(QSize(640, 0))
        self.label_drop_merge.setMaximumSize(QSize(640, 16777215))
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


        self.verticalLayout_24.addWidget(self.frame_main_merge, 0, Qt.AlignTop)

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
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_extract_main = QFrame(self.frame_main_extract)
        self.frame_extract_main.setObjectName(u"frame_extract_main")
        self.frame_extract_main.setMaximumSize(QSize(710, 16777215))
        self.frame_extract_main.setFrameShape(QFrame.StyledPanel)
        self.frame_extract_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_extract_main)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(9, 9, 9, 9)
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
        self.label_description_extract.setFont(font3)
        self.label_description_extract.setStyleSheet(u"")

        self.horizontalLayout_16.addWidget(self.label_description_extract, 0, Qt.AlignLeft)


        self.verticalLayout_20.addWidget(self.frame_description_extract, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.frame_top_page_extract = QFrame(self.frame_extract_main)
        self.frame_top_page_extract.setObjectName(u"frame_top_page_extract")
        self.frame_top_page_extract.setMinimumSize(QSize(690, 0))
        self.frame_top_page_extract.setMaximumSize(QSize(690, 16777215))
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
        self.frame_input_extract.setFont(font4)
        self.frame_input_extract.setStyleSheet(u"border: 0px;")
        self.frame_input_extract.setFrameShape(QFrame.StyledPanel)
        self.frame_input_extract.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_input_extract)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(9, 0, 9, 0)
        self.pushButton_run_extract = QPushButton(self.frame_input_extract)
        self.pushButton_run_extract.setObjectName(u"pushButton_run_extract")
        self.pushButton_run_extract.setMinimumSize(QSize(40, 0))
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
        self.pushButton_run_extract.setIcon(icon3)
        self.pushButton_run_extract.setIconSize(QSize(18, 18))

        self.horizontalLayout_22.addWidget(self.pushButton_run_extract)

        self.pushButton_selectFiles_extract = QPushButton(self.frame_input_extract)
        self.pushButton_selectFiles_extract.setObjectName(u"pushButton_selectFiles_extract")
        self.pushButton_selectFiles_extract.setMinimumSize(QSize(160, 30))
        self.pushButton_selectFiles_extract.setMaximumSize(QSize(150, 16777215))
        self.pushButton_selectFiles_extract.setFont(font)
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

        Ui_MainWindow.lineEdit_outputPath_extract = QLineEdit(self.frame_output_extract)
        self.lineEdit_outputPath_extract.setObjectName(u"lineEdit_outputPath_extract")
        self.lineEdit_outputPath_extract.setMinimumSize(QSize(360, 30))
        self.lineEdit_outputPath_extract.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_outputPath_extract.setFont(font5)
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

        Ui_MainWindow.lineEdit_filename_extract = QLineEdit(self.frame_output_extract)
        self.lineEdit_filename_extract.setObjectName(u"lineEdit_filename_extract")
        self.lineEdit_filename_extract.setMinimumSize(QSize(360, 30))
        self.lineEdit_filename_extract.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_filename_extract.setFont(font5)
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
        self.label_tags_extract.setFont(font6)
        self.label_tags_extract.setStyleSheet(u"color: rgb(112, 117, 125);")

        self.formLayout_5.setWidget(3, QFormLayout.FieldRole, self.label_tags_extract)


        self.horizontalLayout_25.addWidget(self.frame_output_extract, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_20.addWidget(self.frame_top_page_extract, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_13.addWidget(self.frame_extract_main)

        self.frame_options_extract = QFrame(self.frame_main_extract)
        self.frame_options_extract.setObjectName(u"frame_options_extract")
        self.frame_options_extract.setMinimumSize(QSize(690, 0))
        self.frame_options_extract.setStyleSheet(u"background-color:#343A4B;\n"
"border-radius: 7px;")
        self.frame_options_extract.setFrameShape(QFrame.StyledPanel)
        self.frame_options_extract.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_options_extract)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(-1, 5, -1, 5)
        self.frame_pages_extract = QFrame(self.frame_options_extract)
        self.frame_pages_extract.setObjectName(u"frame_pages_extract")
        self.frame_pages_extract.setFrameShape(QFrame.StyledPanel)
        self.frame_pages_extract.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_pages_extract)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(9, 9, 50, 9)
        Ui_MainWindow.comboBox_extractPages = QComboBox(self.frame_pages_extract)
        self.comboBox_extractPages.addItem("")
        self.comboBox_extractPages.addItem("")
        self.comboBox_extractPages.setObjectName(u"comboBox_extractPages")
        self.comboBox_extractPages.setMinimumSize(QSize(0, 0))
        self.comboBox_extractPages.setMaximumSize(QSize(16777215, 33))
        font8 = QFont()
        font8.setFamily(u"Segoe UI")
        font8.setPointSize(9)
        self.comboBox_extractPages.setFont(font8)
        self.comboBox_extractPages.setStyleSheet(u"border: 2px solid rgb(64, 71, 88);\n"
"border-radius: 5px;	\n"
"background-color:#2E3342;")

        self.verticalLayout_23.addWidget(self.comboBox_extractPages)

        Ui_MainWindow.lineEdit_intPages_extract = QLineEdit(self.frame_pages_extract)
        self.lineEdit_intPages_extract.setObjectName(u"lineEdit_intPages_extract")
        self.lineEdit_intPages_extract.setMinimumSize(QSize(200, 28))
        self.lineEdit_intPages_extract.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_intPages_extract.setFont(font6)
        self.lineEdit_intPages_extract.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
"border-radius: 5px;\n"
"border: 2px solid rgb(27, 29, 35);\n"
"padding-left: 10px;")

        self.verticalLayout_23.addWidget(self.lineEdit_intPages_extract)


        self.horizontalLayout_24.addWidget(self.frame_pages_extract, 0, Qt.AlignHCenter)

        Ui_MainWindow.frame__checkbox_extract = QFrame(self.frame_options_extract)
        self.frame__checkbox_extract.setObjectName(u"frame__checkbox_extract")
        self.frame__checkbox_extract.setFrameShape(QFrame.StyledPanel)
        self.frame__checkbox_extract.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame__checkbox_extract)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(9, 9, 50, 9)
        Ui_MainWindow.checkBox_split = QCheckBox(self.frame__checkbox_extract)
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


        self.verticalLayout_13.addWidget(self.frame_options_extract, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_drop_extract = QFrame(self.frame_main_extract)
        self.frame_drop_extract.setObjectName(u"frame_drop_extract")
        self.frame_drop_extract.setMinimumSize(QSize(690, 200))
        self.frame_drop_extract.setMaximumSize(QSize(16777215, 16777215))
        self.frame_drop_extract.setFrameShape(QFrame.StyledPanel)
        self.frame_drop_extract.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_drop_extract)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(5, 20, 5, -1)
        self.label_drop_extract = QLabel(self.frame_drop_extract)
        self.label_drop_extract.setObjectName(u"label_drop_extract")
        self.label_drop_extract.setMinimumSize(QSize(680, 180))
        self.label_drop_extract.setFont(font7)
        self.label_drop_extract.setStyleSheet(u"border: 4px dashed rgb(112, 117, 125);\n"
"color: rgb(112, 117, 125);")
        self.label_drop_extract.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.label_drop_extract)


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
        self.label_description_ocr.setFont(font3)
        self.label_description_ocr.setStyleSheet(u"")

        self.horizontalLayout_27.addWidget(self.label_description_ocr, 0, Qt.AlignLeft)


        self.verticalLayout_27.addWidget(self.frame_description_ocr)

        self.frame_top_page_ocr = QFrame(self.frame_ocr)
        self.frame_top_page_ocr.setObjectName(u"frame_top_page_ocr")
        self.frame_top_page_ocr.setMinimumSize(QSize(0, 150))
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
        self.frame_input_ocr.setFont(font4)
        self.frame_input_ocr.setStyleSheet(u"border: 0px;")
        self.frame_input_ocr.setFrameShape(QFrame.StyledPanel)
        self.frame_input_ocr.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_input_ocr)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(9, 5, 9, 5)
        self.pushButton_selectFiles_ocr = QPushButton(self.frame_input_ocr)
        self.pushButton_selectFiles_ocr.setObjectName(u"pushButton_selectFiles_ocr")
        self.pushButton_selectFiles_ocr.setMinimumSize(QSize(160, 30))
        self.pushButton_selectFiles_ocr.setMaximumSize(QSize(150, 16777215))
        self.pushButton_selectFiles_ocr.setFont(font)
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
        self.pushButton_run_ocr.setMinimumSize(QSize(40, 0))
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
        self.pushButton_run_ocr.setIcon(icon3)
        self.pushButton_run_ocr.setIconSize(QSize(18, 18))

        self.gridLayout_5.addWidget(self.pushButton_run_ocr, 0, 0, 1, 1)


        self.verticalLayout_28.addWidget(self.frame_input_ocr, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_dpi_ocr = QFrame(self.frame_left_ocr)
        self.frame_dpi_ocr.setObjectName(u"frame_dpi_ocr")
        self.frame_dpi_ocr.setMinimumSize(QSize(0, 0))
        self.frame_dpi_ocr.setFont(font4)
        self.frame_dpi_ocr.setFrameShape(QFrame.StyledPanel)
        self.frame_dpi_ocr.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_dpi_ocr)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(17)
        self.gridLayout_2.setContentsMargins(20, 0, 20, 9)
        self.label_intDpi_ocr = QLabel(self.frame_dpi_ocr)
        self.label_intDpi_ocr.setObjectName(u"label_intDpi_ocr")
        self.label_intDpi_ocr.setFont(font)

        self.gridLayout_2.addWidget(self.label_intDpi_ocr, 0, 0, 1, 1, Qt.AlignLeft)

        Ui_MainWindow.lineEdit_intDpi_ocr = QLineEdit(self.frame_dpi_ocr)
        self.lineEdit_intDpi_ocr.setObjectName(u"lineEdit_intDpi_ocr")
        self.lineEdit_intDpi_ocr.setMinimumSize(QSize(0, 30))
        self.lineEdit_intDpi_ocr.setMaximumSize(QSize(50, 16777215))
        self.lineEdit_intDpi_ocr.setFont(font)
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

        self.gridLayout_2.addWidget(self.lineEdit_intDpi_ocr, 0, 1, 1, 1, Qt.AlignRight)


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

        Ui_MainWindow.lineEdit_outputPath_ocr = QLineEdit(self.frame_output_ocr)
        self.lineEdit_outputPath_ocr.setObjectName(u"lineEdit_outputPath_ocr")
        self.lineEdit_outputPath_ocr.setMinimumSize(QSize(0, 30))
        self.lineEdit_outputPath_ocr.setMaximumSize(QSize(360, 16777215))
        self.lineEdit_outputPath_ocr.setFont(font5)
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

        Ui_MainWindow.lineEdit_filename_ocr = QLineEdit(self.frame_output_ocr)
        self.lineEdit_filename_ocr.setObjectName(u"lineEdit_filename_ocr")
        self.lineEdit_filename_ocr.setMinimumSize(QSize(0, 30))
        self.lineEdit_filename_ocr.setMaximumSize(QSize(360, 16777215))
        self.lineEdit_filename_ocr.setFont(font5)
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
        self.label_tags_ocr.setFont(font6)
        self.label_tags_ocr.setStyleSheet(u"color: rgb(112, 117, 125);")

        self.formLayout_6.setWidget(3, QFormLayout.FieldRole, self.label_tags_ocr)


        self.horizontalLayout_28.addWidget(self.frame_output_ocr, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_27.addWidget(self.frame_top_page_ocr, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_15.addWidget(self.frame_ocr, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_drop_ocr = QFrame(self.frame_main_ocr)
        self.frame_drop_ocr.setObjectName(u"frame_drop_ocr")
        self.frame_drop_ocr.setMinimumSize(QSize(0, 200))
        self.frame_drop_ocr.setMaximumSize(QSize(690, 16777215))
        self.frame_drop_ocr.setFrameShape(QFrame.StyledPanel)
        self.frame_drop_ocr.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_drop_ocr)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(5, 0, 5, -1)
        self.label_drop_ocr = QLabel(self.frame_drop_ocr)
        self.label_drop_ocr.setObjectName(u"label_drop_ocr")
        self.label_drop_ocr.setMinimumSize(QSize(680, 0))
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
        self.verticalLayout_12.setContentsMargins(30, 5, 30, 5)
        self.frame_top_page_search = QFrame(self.page_search)
        self.frame_top_page_search.setObjectName(u"frame_top_page_search")
        self.frame_top_page_search.setMinimumSize(QSize(840, 0))
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
        self.label_description_search.setFont(font3)

        self.horizontalLayout_30.addWidget(self.label_description_search, 0, Qt.AlignLeft)


        self.verticalLayout_11.addWidget(self.frame_description_search)

        self.frame_middle = QFrame(self.frame_top_page_search)
        self.frame_middle.setObjectName(u"frame_middle")
        self.frame_middle.setMinimumSize(QSize(840, 0))
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
        Ui_MainWindow.lineEdit_moveto_search = QLineEdit(self.frame_keywords)
        self.lineEdit_moveto_search.setObjectName(u"lineEdit_moveto_search")
        self.lineEdit_moveto_search.setMinimumSize(QSize(0, 30))
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
        self.pushButton_run_search.setMinimumSize(QSize(120, 30))
        self.pushButton_run_search.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_run_search.setFont(font)
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

        Ui_MainWindow.lineEdit_else_search = QLineEdit(self.frame_keywords)
        self.lineEdit_else_search.setObjectName(u"lineEdit_else_search")
        self.lineEdit_else_search.setMinimumSize(QSize(0, 30))
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

        Ui_MainWindow.lineEdit_keywords_search = QLineEdit(self.frame_keywords)
        self.lineEdit_keywords_search.setObjectName(u"lineEdit_keywords_search")
        self.lineEdit_keywords_search.setMinimumSize(QSize(230, 30))
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
        self.frame_top_page.setMinimumSize(QSize(840, 135))
        self.frame_top_page.setMaximumSize(QSize(840, 16777215))
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
        self.frame_input.setMaximumSize(QSize(16777215, 16777215))
        self.frame_input.setFont(font4)
        self.frame_input.setStyleSheet(u"border: 0px;")
        self.frame_input.setFrameShape(QFrame.StyledPanel)
        self.frame_input.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_input)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(9, 5, 5, 5)
        self.pushButton_selectFiles_search = QPushButton(self.frame_input)
        self.pushButton_selectFiles_search.setObjectName(u"pushButton_selectFiles_search")
        self.pushButton_selectFiles_search.setMinimumSize(QSize(0, 30))
        self.pushButton_selectFiles_search.setMaximumSize(QSize(160, 16777215))
        self.pushButton_selectFiles_search.setFont(font)
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


        self.horizontalLayout_13.addWidget(self.frame_input, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame_output = QFrame(self.frame_top_page)
        self.frame_output.setObjectName(u"frame_output")
        self.frame_output.setMinimumSize(QSize(0, 0))
        self.frame_output.setMaximumSize(QSize(300, 16777215))
        self.frame_output.setStyleSheet(u"border: 0px;")
        self.frame_output.setFrameShape(QFrame.StyledPanel)
        self.frame_output.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_output)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(5, 5, 9, 5)
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

        Ui_MainWindow.lineEdit_outputPath_search = QLineEdit(self.frame_output)
        self.lineEdit_outputPath_search.setObjectName(u"lineEdit_outputPath_search")
        self.lineEdit_outputPath_search.setMinimumSize(QSize(220, 30))
        self.lineEdit_outputPath_search.setMaximumSize(QSize(250, 16777215))
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

        Ui_MainWindow.lineEdit_filename_search = QLineEdit(self.frame_output)
        self.lineEdit_filename_search.setObjectName(u"lineEdit_filename_search")
        self.lineEdit_filename_search.setMinimumSize(QSize(230, 30))
        self.lineEdit_filename_search.setMaximumSize(QSize(250, 16777215))
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

        self.label_tags_search = QLabel(self.frame_output)
        self.label_tags_search.setObjectName(u"label_tags_search")
        self.label_tags_search.setMinimumSize(QSize(0, 0))
        self.label_tags_search.setMaximumSize(QSize(16777215, 16777215))
        self.label_tags_search.setFont(font)
        self.label_tags_search.setStyleSheet(u"color: rgb(112, 117, 125);")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.label_tags_search)


        self.horizontalLayout_13.addWidget(self.frame_output, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame_checkBox_ = QFrame(self.frame_top_page)
        self.frame_checkBox_.setObjectName(u"frame_checkBox_")
        self.frame_checkBox_.setMinimumSize(QSize(0, 0))
        self.frame_checkBox_.setMaximumSize(QSize(16777215, 16777215))
        self.frame_checkBox_.setFont(font8)
        self.frame_checkBox_.setStyleSheet(u"border: 0px;")
        self.frame_checkBox_.setFrameShape(QFrame.StyledPanel)
        self.frame_checkBox_.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_checkBox_)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(20)
        self.gridLayout_4.setContentsMargins(5, 5, 9, 5)
        Ui_MainWindow.checkBox_ignoreSpaces_search = QCheckBox(self.frame_checkBox_)
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

        Ui_MainWindow.checkBox_ignorePontuation_search = QCheckBox(self.frame_checkBox_)
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

        Ui_MainWindow.checkBox_ignoreFirstPage_search = QCheckBox(self.frame_checkBox_)
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

        Ui_MainWindow.checkBox_onlyPages_search = QCheckBox(self.frame_checkBox_)
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

        Ui_MainWindow.checkBox_ignoreSpecialChar_search = QCheckBox(self.frame_checkBox_)
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


        self.horizontalLayout_13.addWidget(self.frame_checkBox_, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_12.addWidget(self.frame_top_page, 0, Qt.AlignHCenter)

        self.frame_drop_search = QFrame(self.page_search)
        self.frame_drop_search.setObjectName(u"frame_drop_search")
        self.frame_drop_search.setMinimumSize(QSize(0, 60))
        self.frame_drop_search.setMaximumSize(QSize(16777215, 16777215))
        self.frame_drop_search.setFrameShape(QFrame.StyledPanel)
        self.frame_drop_search.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_drop_search)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_drop_search = QLabel(self.frame_drop_search)
        self.label_drop_search.setObjectName(u"label_drop_search")
        self.label_drop_search.setMinimumSize(QSize(0, 60))
        self.label_drop_search.setMaximumSize(QSize(830, 60))
        self.label_drop_search.setFont(font7)
        self.label_drop_search.setStyleSheet(u"border: 4px dashed rgb(112, 117, 125);\n"
"color: rgb(112, 117, 125);")
        self.label_drop_search.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_drop_search)


        self.verticalLayout_12.addWidget(self.frame_drop_search)

        self.frame_tab = QFrame(self.page_search)
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

        Ui_MainWindow.tabWidget = QTabWidget(self.frame_tab)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setFont(font8)
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
        self.verticalLayout_18.setContentsMargins(5, 5, 5, 5)
        self.frame_zip = QFrame(self.frame_main_zip)
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
        self.label_description_zip.setFont(font3)
        self.label_description_zip.setStyleSheet(u"")

        self.horizontalLayout_21.addWidget(self.label_description_zip, 0, Qt.AlignLeft)


        self.verticalLayout_6.addWidget(self.frame_description_zip)

        self.frame_top_page_zip = QFrame(self.frame_zip)
        self.frame_top_page_zip.setObjectName(u"frame_top_page_zip")
        self.frame_top_page_zip.setMinimumSize(QSize(690, 150))
        self.frame_top_page_zip.setMaximumSize(QSize(815, 16777215))
        self.frame_top_page_zip.setStyleSheet(u"background-color:#343A4B;\n"
"border-radius: 7px;\n"
"border-top: 3px solid rgb(85, 170, 255);")
        self.frame_top_page_zip.setFrameShape(QFrame.StyledPanel)
        self.frame_top_page_zip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_top_page_zip)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(9, 5, 9, 5)
        self.frame_input_zip = QFrame(self.frame_top_page_zip)
        self.frame_input_zip.setObjectName(u"frame_input_zip")
        self.frame_input_zip.setMinimumSize(QSize(0, 0))
        self.frame_input_zip.setMaximumSize(QSize(16777215, 16777215))
        self.frame_input_zip.setFont(font4)
        self.frame_input_zip.setStyleSheet(u"border: 0px;")
        self.frame_input_zip.setFrameShape(QFrame.StyledPanel)
        self.frame_input_zip.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_input_zip)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(9, 5, 9, 5)
        Ui_MainWindow.lineEdit_rootDirectory_zip = QLineEdit(self.frame_input_zip)
        self.lineEdit_rootDirectory_zip.setObjectName(u"lineEdit_rootDirectory_zip")
        self.lineEdit_rootDirectory_zip.setMinimumSize(QSize(260, 30))
        self.lineEdit_rootDirectory_zip.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_rootDirectory_zip.setFont(font5)
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
        self.pushButton_selectRootDirectory_zip.setMinimumSize(QSize(40, 30))
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
        self.formLayout_7.setContentsMargins(9, 5, 9, 5)
        Ui_MainWindow.lineEdit_filename_zip = QLineEdit(self.frame_output_zip)
        self.lineEdit_filename_zip.setObjectName(u"lineEdit_filename_zip")
        self.lineEdit_filename_zip.setMinimumSize(QSize(0, 30))
        self.lineEdit_filename_zip.setMaximumSize(QSize(360, 16777215))
        self.lineEdit_filename_zip.setFont(font5)
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
        self.label_tags_zip.setFont(font6)
        self.label_tags_zip.setStyleSheet(u"color: rgb(112, 117, 125);")

        self.formLayout_7.setWidget(3, QFormLayout.FieldRole, self.label_tags_zip)

        Ui_MainWindow.lineEdit_outputPath_zip = QLineEdit(self.frame_output_zip)
        self.lineEdit_outputPath_zip.setObjectName(u"lineEdit_outputPath_zip")
        self.lineEdit_outputPath_zip.setMinimumSize(QSize(360, 30))
        self.lineEdit_outputPath_zip.setMaximumSize(QSize(360, 16777215))
        self.lineEdit_outputPath_zip.setFont(font5)
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


        self.horizontalLayout_29.addWidget(self.frame_output_zip, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_6.addWidget(self.frame_top_page_zip, 0, Qt.AlignHCenter)


        self.verticalLayout_18.addWidget(self.frame_zip, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame_drop_zip = QFrame(self.frame_main_zip)
        self.frame_drop_zip.setObjectName(u"frame_drop_zip")
        self.frame_drop_zip.setMinimumSize(QSize(600, 200))
        self.frame_drop_zip.setMaximumSize(QSize(690, 16777215))
        self.frame_drop_zip.setFrameShape(QFrame.StyledPanel)
        self.frame_drop_zip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_drop_zip)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(5, 0, 5, -1)

        self.verticalLayout_18.addWidget(self.frame_drop_zip, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_8.addWidget(self.frame_main_zip, 0, Qt.AlignTop)

        self.stackedWidget.addWidget(self.page_zip)
        self.page_credits = QWidget()
        self.page_credits.setObjectName(u"page_credits")
        self.horizontalLayout_12 = QHBoxLayout(self.page_credits)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(30, 20, 30, -1)
        self.plainTextEdit_credits = QPlainTextEdit(self.page_credits)
        self.plainTextEdit_credits.setObjectName(u"plainTextEdit_credits")
        self.plainTextEdit_credits.setFont(font)
        self.plainTextEdit_credits.setStyleSheet(u"QPlainTextEdit{\n"
"	background-color:#343A4B;\n"
"	border-radius: 7px;\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"}\n"
"")
        self.plainTextEdit_credits.setReadOnly(True)
        self.plainTextEdit_credits.setTabStopWidth(81)
        self.plainTextEdit_credits.setCursorWidth(1)
        self.plainTextEdit_credits.setMaximumBlockCount(0)

        self.horizontalLayout_12.addWidget(self.plainTextEdit_credits)

        self.stackedWidget.addWidget(self.page_credits)
        self.page_help = QWidget()
        self.page_help.setObjectName(u"page_help")
        self.horizontalLayout_15 = QHBoxLayout(self.page_help)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(30, 20, 30, -1)
        self.plainTextEdit_help = QPlainTextEdit(self.page_help)
        self.plainTextEdit_help.setObjectName(u"plainTextEdit_help")
        self.plainTextEdit_help.setFont(font)
        self.plainTextEdit_help.setStyleSheet(u"QPlainTextEdit{\n"
"	background-color:#343A4B;\n"
"	border-radius: 7px;\n"
"	border: 2px solid rgb(85, 170, 255);\n"
"}\n"
"")

        self.horizontalLayout_15.addWidget(self.plainTextEdit_help)

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
        self.label_feedback.setFont(font5)

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
        self.label_credits.setFont(font6)
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

        self.stackedWidget.setCurrentIndex(1)
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
        self.pushButton_run_merge.setText("")
        self.pushButton_selectFiles_merge.setText(QCoreApplication.translate("MainWindow", u"Selecionar arquivos", None))
        self.lineEdit_outputPath_merge.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecionar diret\u00f3rio de sa\u00edda", None))
        self.lineEdit_filename_merge.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome do arquivo: #origin", None))
        self.label_tags_merge.setText(QCoreApplication.translate("MainWindow", u"Tags dispon\u00edveis:#year #month #day #time #origin", None))
        self.pushButton_outputPath_merge.setText("")
        self.label_drop_merge.setText(QCoreApplication.translate("MainWindow", u"ARRASTE E SOLTE ARQUIVOS PDF AQUI", None))
        self.label_description_extract.setText(QCoreApplication.translate("MainWindow", u"EXTRAIR P\u00c1GINAS OU DIVIDIR ARQUIVOS PDF", None))
        self.pushButton_run_extract.setText("")
        self.pushButton_selectFiles_extract.setText(QCoreApplication.translate("MainWindow", u"Selecionar arquivos", None))
        self.pushButton_outputPath_extract.setText("")
        self.lineEdit_outputPath_extract.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecionar diret\u00f3rio de sa\u00edda", None))
        self.lineEdit_filename_extract.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome do arquivo: #origin,#pages", None))
        self.label_tags_extract.setText(QCoreApplication.translate("MainWindow", u"Tags dispon\u00edveis: #year #month #day\n"
"#time #pages #origin", None))
        self.comboBox_extractPages.setItemText(0, QCoreApplication.translate("MainWindow", u"P\u00e1ginas indicadas", None))
        self.comboBox_extractPages.setItemText(1, QCoreApplication.translate("MainWindow", u"A cada n p\u00e1ginas", None))

        self.lineEdit_intPages_extract.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ex: 3, 7-8, 11-14", None))
        self.checkBox_split.setText(QCoreApplication.translate("MainWindow", u"Dividir arquivo", None))
        self.checkBox_extract.setText(QCoreApplication.translate("MainWindow", u"Extrair no mesmo arquivo", None))
        self.label_drop_extract.setText(QCoreApplication.translate("MainWindow", u"ARRASTE E SOLTE ARQUIVOS PDF AQUI", None))
        self.label_description_ocr.setText(QCoreApplication.translate("MainWindow", u"ESCANEAR ARQUIVOS PDF", None))
        self.pushButton_selectFiles_ocr.setText(QCoreApplication.translate("MainWindow", u"Selecionar arquivos", None))
        self.pushButton_run_ocr.setText("")
        self.label_intDpi_ocr.setText(QCoreApplication.translate("MainWindow", u"DPI:", None))
        self.lineEdit_intDpi_ocr.setPlaceholderText(QCoreApplication.translate("MainWindow", u"200", None))
        self.pushButton_outputPath_ocr.setText("")
        self.lineEdit_outputPath_ocr.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecionar diret\u00f3rio de sa\u00edda", None))
        self.lineEdit_filename_ocr.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome do arquivo: #origin", None))
        self.label_tags_ocr.setText(QCoreApplication.translate("MainWindow", u"Tags dispon\u00edveis:#year #month #day #time #origin", None))
        self.label_drop_ocr.setText(QCoreApplication.translate("MainWindow", u"ARRASTE E SOLTE ARQUIVOS PDF AQUI", None))
        self.label_description_search.setText(QCoreApplication.translate("MainWindow", u"ORGANIZAR ARQUIVOS PDF PROCURANDO POR EXPRESS\u00d5ES REGULARES", None))
        self.lineEdit_moveto_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ex: Tabela1:2", None))
        self.label_else_search.setText(QCoreApplication.translate("MainWindow", u"Se n\u00e3o encontrar mover para pasta", None))
        self.label_moveto_search.setText(QCoreApplication.translate("MainWindow", u"Mover para pasta", None))
        self.pushButton_run_search.setText(QCoreApplication.translate("MainWindow", u"Executar", None))
        self.lineEdit_else_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ex: N\u00e3o encontrado", None))
        self.label_keywords_search.setText(QCoreApplication.translate("MainWindow", u"Procurar por express\u00f5es", None))
        self.lineEdit_keywords_search.setText("")
        self.lineEdit_keywords_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ex: Tabela1:1, Tabela2:1", None))
        self.pushButton_selectFiles_search.setText(QCoreApplication.translate("MainWindow", u"Selecionar arquivos", None))
        self.pushButton_outputPath_search.setText("")
        self.lineEdit_outputPath_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecionar diret\u00f3rio de sa\u00edda", None))
        self.lineEdit_filename_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome do arquivo: #origin", None))
        self.label_tags_search.setText(QCoreApplication.translate("MainWindow", u"Tags dispon\u00edveis: #year #month #day\n"
"#time #pages #origin", None))
        self.checkBox_ignoreSpaces_search.setText(QCoreApplication.translate("MainWindow", u"Ignorar espa\u00e7os", None))
        self.checkBox_ignorePontuation_search.setText(QCoreApplication.translate("MainWindow", u"Ignorar pontua\u00e7\u00e3o", None))
        self.checkBox_ignoreFirstPage_search.setText(QCoreApplication.translate("MainWindow", u"Ignorar primeira linha", None))
        self.checkBox_onlyPages_search.setText(QCoreApplication.translate("MainWindow", u"Mover apenas p\u00e1ginas", None))
        self.checkBox_ignoreSpecialChar_search.setText(QCoreApplication.translate("MainWindow", u"Ignorar acentos", None))
        self.label_drop_search.setText(QCoreApplication.translate("MainWindow", u"ARRASTE E SOLTE ARQUIVOS PDF AQUI", None))
        self.pushButton_addTable_search.setText("")
        self.pushButton_deleteTable_search.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.label_description_zip.setText(QCoreApplication.translate("MainWindow", u"CRIAR FICHEIRO ZIP DE ARQUIVOS PDF DE UM DIRET\u00d3RIO", None))
        self.lineEdit_rootDirectory_zip.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecionar diret\u00f3rio raiz", None))
        self.pushButton_selectRootDirectory_zip.setText("")
        self.pushButton_run_zip.setText("")
        self.lineEdit_filename_zip.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome do arquivo: #origin", None))
        self.label_tags_zip.setText(QCoreApplication.translate("MainWindow", u"Tags dispon\u00edveis: #year #month #day #time #origin", None))
        self.lineEdit_outputPath_zip.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecionar diret\u00f3rio de sa\u00edda", None))
        self.pushButton_outputPath_zip.setText("")
        self.plainTextEdit_credits.setPlainText(QCoreApplication.translate("MainWindow", u"Ahand: Giving you a hand for automation.\n"
"Copyright (C) 2020  Matheus Melo\n"
"https://github.com/demelomatt\n"
"\n"
"This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.\n"
"\n"
"This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.\n"
"\n"
"<https://www.gnu.org/licenses/>.\n"
"\n"
"User interface created with QT Creator.\n"
"<https://www.qt.io/>.\n"
"Licensed under LGPLv3 conditions.\n"
"\n"
"QT Python binaries by Pyside.\n"
"<https://wiki.qt.io/Qt_for_Python>.\n"
"Licensed under LGPLv3 conditions.\n"
"\n"
"PySide Base by Wanderson Magalhaes.\n"
"<https://github.com/Wanderson-Magalhaes/Simple_PySide_Base>.\n"
"Licensed under MIT License condition"
                        "s.\n"
"\n"
"OCR engine by Tesseract.\n"
"<https://github.com/tesseract-ocr/tesseract>.\n"
"Licensed under Apache License 2.0 conditions.\n"
"\n"
"Tesseract installer for Windows by UB-Mannheim.\n"
"<https://github.com/UB-Mannheim/tesseract/>.\n"
"\n"
"Python-tesseract wrapper by pytesseract .\n"
"<https://github.com/madmaze/pytesseract>.\n"
"Licensed under Apache License 2.0 conditions.\n"
"\n"
"Python Imaging Library by Pillow\n"
"<https://github.com/python-pillow/Pillow>.\n"
"Licensed under the open source PIL Software License conditions.\n"
"\n"
"Convert PDF to a PIL Image object by pdf2image.\n"
"<https://github.com/Belval/pdf2image>.\n"
"Licensed under MIT License conditions.\n"
"\n"
"PDF rendering library by Poppler.\n"
"<https://poppler.freedesktop.org/>.\n"
"Licensed under GPLv3 conditions.\n"
"\n"
"Poppler Windows binaries by oschwartz10612.\n"
"<https://github.com/oschwartz10612/poppler-windows/releases/>.\n"
"\n"
"Python PDF toolkit by PYPDF2.\n"
"<https://github.com/mstamy2/PyPDF2>.\n"
"Licensed un"
                        "der BSD License conditions.\n"
"\n"
"Extracts the text from a PDF page by pdfminer.six.\n"
"<https://github.com/pdfminer/pdfminer.six>.\n"
"Licensed under MIT License conditions.\n"
"\n"
"Sound-playing interface for Windows by winsound.\n"
"<https://docs.python.org/3/library/winsound.html>.\n"
"\n"
"Icons by Flaticon.\n"
"<https://www.flaticon.com/>.\n"
"\n"
"Sound Effects by Freesound.\n"
"<https://freesound.org/>.\n"
"\n"
"Developed with python.\n"
"<https://www.python.org/>.\n"
"Licensed under PSF LICENSE conditions.", None))
        self.plainTextEdit_help.setPlainText(QCoreApplication.translate("MainWindow", u"Preamble\n"
"\n"
"  The GNU General Public License is a free, copyleft license for\n"
"software and other kinds of works.\n"
"\n"
"  The licenses for most software and other practical works are designed\n"
"to take away your freedom to share and change the works.  By contrast,\n"
"the GNU General Public License is intended to guarantee your freedom to\n"
"share and change all versions of a program--to make sure it remains free\n"
"software for all its users.  We, the Free Software Foundation, use the\n"
"GNU General Public License for most of our software; it applies also to\n"
"any other work released this way by its authors.  You can apply it to\n"
"your programs, too.\n"
"\n"
"  When we speak of free software, we are referring to freedom, not\n"
"price.  Our General Public Licenses are designed to make sure that you\n"
"have the freedom to distribute copies of free software (and charge for\n"
"them if you wish), that you receive source code or can get it if you\n"
"want it, that you can change the software "
                        "or use pieces of it in new\n"
"free programs, and that you know you can do these things.\n"
"\n"
"  To protect your rights, we need to prevent others from denying you\n"
"these rights or asking you to surrender the rights.  Therefore, you have\n"
"certain responsibilities if you distribute copies of the software, or if\n"
"you modify it: responsibilities to respect the freedom of others.\n"
"\n"
"  For example, if you distribute copies of such a program, whether\n"
"gratis or for a fee, you must pass on to the recipients the same\n"
"freedoms that you received.  You must make sure that they, too, receive\n"
"or can get the source code.  And you must show them these terms so they\n"
"know their rights.\n"
"\n"
"  Developers that use the GNU GPL protect your rights with two steps:\n"
"(1) assert copyright on the software, and (2) offer you this License\n"
"giving you legal permission to copy, distribute and/or modify it.\n"
"\n"
"  For the developers' and authors' protection, the GPL clearly explains\n"
"that th"
                        "ere is no warranty for this free software.  For both users' and\n"
"authors' sake, the GPL requires that modified versions be marked as\n"
"changed, so that their problems will not be attributed erroneously to\n"
"authors of previous versions.\n"
"\n"
"  Some devices are designed to deny users access to install or run\n"
"modified versions of the software inside them, although the manufacturer\n"
"can do so.  This is fundamentally incompatible with the aim of\n"
"protecting users' freedom to change the software.  The systematic\n"
"pattern of such abuse occurs in the area of products for individuals to\n"
"use, which is precisely where it is most unacceptable.  Therefore, we\n"
"have designed this version of the GPL to prohibit the practice for those\n"
"products.  If such problems arise substantially in other domains, we\n"
"stand ready to extend this provision to those domains in future versions\n"
"of the GPL, as needed to protect the freedom of users.\n"
"\n"
"  Finally, every program is threatened constan"
                        "tly by software patents.\n"
"States should not allow patents to restrict development and use of\n"
"software on general-purpose computers, but in those that do, we wish to\n"
"avoid the special danger that patents applied to a free program could\n"
"make it effectively proprietary.  To prevent this, the GPL assures that\n"
"patents cannot be used to render the program non-free.\n"
"\n"
"  The precise terms and conditions for copying, distribution and\n"
"modification follow.\n"
"\n"
"                       TERMS AND CONDITIONS\n"
"\n"
"  0. Definitions.\n"
"\n"
"  \"This License\" refers to version 3 of the GNU General Public License.\n"
"\n"
"  \"Copyright\" also means copyright-like laws that apply to other kinds of\n"
"works, such as semiconductor masks.\n"
"\n"
"  \"The Program\" refers to any copyrightable work licensed under this\n"
"License.  Each licensee is addressed as \"you\".  \"Licensees\" and\n"
"\"recipients\" may be individuals or organizations.\n"
"\n"
"  To \"modify\" a work means to copy fro"
                        "m or adapt all or part of the work\n"
"in a fashion requiring copyright permission, other than the making of an\n"
"exact copy.  The resulting work is called a \"modified version\" of the\n"
"earlier work or a work \"based on\" the earlier work.\n"
"\n"
"  A \"covered work\" means either the unmodified Program or a work based\n"
"on the Program.\n"
"\n"
"  To \"propagate\" a work means to do anything with it that, without\n"
"permission, would make you directly or secondarily liable for\n"
"infringement under applicable copyright law, except executing it on a\n"
"computer or modifying a private copy.  Propagation includes copying,\n"
"distribution (with or without modification), making available to the\n"
"public, and in some countries other activities as well.\n"
"\n"
"  To \"convey\" a work means any kind of propagation that enables other\n"
"parties to make or receive copies.  Mere interaction with a user through\n"
"a computer network, with no transfer of a copy, is not conveying.\n"
"\n"
"  An interactive"
                        " user interface displays \"Appropriate Legal Notices\"\n"
"to the extent that it includes a convenient and prominently visible\n"
"feature that (1) displays an appropriate copyright notice, and (2)\n"
"tells the user that there is no warranty for the work (except to the\n"
"extent that warranties are provided), that licensees may convey the\n"
"work under this License, and how to view a copy of this License.  If\n"
"the interface presents a list of user commands or options, such as a\n"
"menu, a prominent item in the list meets this criterion.\n"
"\n"
"  1. Source Code.\n"
"\n"
"  The \"source code\" for a work means the preferred form of the work\n"
"for making modifications to it.  \"Object code\" means any non-source\n"
"form of a work.\n"
"\n"
"  A \"Standard Interface\" means an interface that either is an official\n"
"standard defined by a recognized standards body, or, in the case of\n"
"interfaces specified for a particular programming language, one that\n"
"is widely used among developers working in t"
                        "hat language.\n"
"\n"
"  The \"System Libraries\" of an executable work include anything, other\n"
"than the work as a whole, that (a) is included in the normal form of\n"
"packaging a Major Component, but which is not part of that Major\n"
"Component, and (b) serves only to enable use of the work with that\n"
"Major Component, or to implement a Standard Interface for which an\n"
"implementation is available to the public in source code form.  A\n"
"\"Major Component\", in this context, means a major essential component\n"
"(kernel, window system, and so on) of the specific operating system\n"
"(if any) on which the executable work runs, or a compiler used to\n"
"produce the work, or an object code interpreter used to run it.\n"
"\n"
"  The \"Corresponding Source\" for a work in object code form means all\n"
"the source code needed to generate, install, and (for an executable\n"
"work) run the object code and to modify the work, including scripts to\n"
"control those activities.  However, it does not include t"
                        "he work's\n"
"System Libraries, or general-purpose tools or generally available free\n"
"programs which are used unmodified in performing those activities but\n"
"which are not part of the work.  For example, Corresponding Source\n"
"includes interface definition files associated with source files for\n"
"the work, and the source code for shared libraries and dynamically\n"
"linked subprograms that the work is specifically designed to require,\n"
"such as by intimate data communication or control flow between those\n"
"subprograms and other parts of the work.\n"
"\n"
"  The Corresponding Source need not include anything that users\n"
"can regenerate automatically from other parts of the Corresponding\n"
"Source.\n"
"\n"
"  The Corresponding Source for a work in source code form is that\n"
"same work.\n"
"\n"
"  2. Basic Permissions.\n"
"\n"
"  All rights granted under this License are granted for the term of\n"
"copyright on the Program, and are irrevocable provided the stated\n"
"conditions are met.  This Lic"
                        "ense explicitly affirms your unlimited\n"
"permission to run the unmodified Program.  The output from running a\n"
"covered work is covered by this License only if the output, given its\n"
"content, constitutes a covered work.  This License acknowledges your\n"
"rights of fair use or other equivalent, as provided by copyright law.\n"
"\n"
"  You may make, run and propagate covered works that you do not\n"
"convey, without conditions so long as your license otherwise remains\n"
"in force.  You may convey covered works to others for the sole purpose\n"
"of having them make modifications exclusively for you, or provide you\n"
"with facilities for running those works, provided that you comply with\n"
"the terms of this License in conveying all material for which you do\n"
"not control copyright.  Those thus making or running the covered works\n"
"for you must do so exclusively on your behalf, under your direction\n"
"and control, on terms that prohibit them from making any copies of\n"
"your copyrighted material o"
                        "utside their relationship with you.\n"
"\n"
"  Conveying under any other circumstances is permitted solely under\n"
"the conditions stated below.  Sublicensing is not allowed; section 10\n"
"makes it unnecessary.\n"
"\n"
"  3. Protecting Users' Legal Rights From Anti-Circumvention Law.\n"
"\n"
"  No covered work shall be deemed part of an effective technological\n"
"measure under any applicable law fulfilling obligations under article\n"
"11 of the WIPO copyright treaty adopted on 20 December 1996, or\n"
"similar laws prohibiting or restricting circumvention of such\n"
"measures.\n"
"\n"
"  When you convey a covered work, you waive any legal power to forbid\n"
"circumvention of technological measures to the extent such circumvention\n"
"is effected by exercising rights under this License with respect to\n"
"the covered work, and you disclaim any intention to limit operation or\n"
"modification of the work as a means of enforcing, against the work's\n"
"users, your or third parties' legal rights to forbid circu"
                        "mvention of\n"
"technological measures.\n"
"\n"
"  4. Conveying Verbatim Copies.\n"
"\n"
"  You may convey verbatim copies of the Program's source code as you\n"
"receive it, in any medium, provided that you conspicuously and\n"
"appropriately publish on each copy an appropriate copyright notice;\n"
"keep intact all notices stating that this License and any\n"
"non-permissive terms added in accord with section 7 apply to the code;\n"
"keep intact all notices of the absence of any warranty; and give all\n"
"recipients a copy of this License along with the Program.\n"
"\n"
"  You may charge any price or no price for each copy that you convey,\n"
"and you may offer support or warranty protection for a fee.\n"
"\n"
"  5. Conveying Modified Source Versions.\n"
"\n"
"  You may convey a work based on the Program, or the modifications to\n"
"produce it from the Program, in the form of source code under the\n"
"terms of section 4, provided that you also meet all of these conditions:\n"
"\n"
"    a) The work must carry "
                        "prominent notices stating that you modified\n"
"    it, and giving a relevant date.\n"
"\n"
"    b) The work must carry prominent notices stating that it is\n"
"    released under this License and any conditions added under section\n"
"    7.  This requirement modifies the requirement in section 4 to\n"
"    \"keep intact all notices\".\n"
"\n"
"    c) You must license the entire work, as a whole, under this\n"
"    License to anyone who comes into possession of a copy.  This\n"
"    License will therefore apply, along with any applicable section 7\n"
"    additional terms, to the whole of the work, and all its parts,\n"
"    regardless of how they are packaged.  This License gives no\n"
"    permission to license the work in any other way, but it does not\n"
"    invalidate such permission if you have separately received it.\n"
"\n"
"    d) If the work has interactive user interfaces, each must display\n"
"    Appropriate Legal Notices; however, if the Program has interactive\n"
"    interfaces that do not di"
                        "splay Appropriate Legal Notices, your\n"
"    work need not make them do so.\n"
"\n"
"  A compilation of a covered work with other separate and independent\n"
"works, which are not by their nature extensions of the covered work,\n"
"and which are not combined with it such as to form a larger program,\n"
"in or on a volume of a storage or distribution medium, is called an\n"
"\"aggregate\" if the compilation and its resulting copyright are not\n"
"used to limit the access or legal rights of the compilation's users\n"
"beyond what the individual works permit.  Inclusion of a covered work\n"
"in an aggregate does not cause this License to apply to the other\n"
"parts of the aggregate.\n"
"\n"
"  6. Conveying Non-Source Forms.\n"
"\n"
"  You may convey a covered work in object code form under the terms\n"
"of sections 4 and 5, provided that you also convey the\n"
"machine-readable Corresponding Source under the terms of this License,\n"
"in one of these ways:\n"
"\n"
"    a) Convey the object code in, or embodied "
                        "in, a physical product\n"
"    (including a physical distribution medium), accompanied by the\n"
"    Corresponding Source fixed on a durable physical medium\n"
"    customarily used for software interchange.\n"
"\n"
"    b) Convey the object code in, or embodied in, a physical product\n"
"    (including a physical distribution medium), accompanied by a\n"
"    written offer, valid for at least three years and valid for as\n"
"    long as you offer spare parts or customer support for that product\n"
"    model, to give anyone who possesses the object code either (1) a\n"
"    copy of the Corresponding Source for all the software in the\n"
"    product that is covered by this License, on a durable physical\n"
"    medium customarily used for software interchange, for a price no\n"
"    more than your reasonable cost of physically performing this\n"
"    conveying of source, or (2) access to copy the\n"
"    Corresponding Source from a network server at no charge.\n"
"\n"
"    c) Convey individual copies of the "
                        "object code with a copy of the\n"
"    written offer to provide the Corresponding Source.  This\n"
"    alternative is allowed only occasionally and noncommercially, and\n"
"    only if you received the object code with such an offer, in accord\n"
"    with subsection 6b.\n"
"\n"
"    d) Convey the object code by offering access from a designated\n"
"    place (gratis or for a charge), and offer equivalent access to the\n"
"    Corresponding Source in the same way through the same place at no\n"
"    further charge.  You need not require recipients to copy the\n"
"    Corresponding Source along with the object code.  If the place to\n"
"    copy the object code is a network server, the Corresponding Source\n"
"    may be on a different server (operated by you or a third party)\n"
"    that supports equivalent copying facilities, provided you maintain\n"
"    clear directions next to the object code saying where to find the\n"
"    Corresponding Source.  Regardless of what server hosts the\n"
"    Corresponding"
                        " Source, you remain obligated to ensure that it is\n"
"    available for as long as needed to satisfy these requirements.\n"
"\n"
"    e) Convey the object code using peer-to-peer transmission, provided\n"
"    you inform other peers where the object code and Corresponding\n"
"    Source of the work are being offered to the general public at no\n"
"    charge under subsection 6d.\n"
"\n"
"  A separable portion of the object code, whose source code is excluded\n"
"from the Corresponding Source as a System Library, need not be\n"
"included in conveying the object code work.\n"
"\n"
"  A \"User Product\" is either (1) a \"consumer product\", which means any\n"
"tangible personal property which is normally used for personal, family,\n"
"or household purposes, or (2) anything designed or sold for incorporation\n"
"into a dwelling.  In determining whether a product is a consumer product,\n"
"doubtful cases shall be resolved in favor of coverage.  For a particular\n"
"product received by a particular user, \"normally"
                        " used\" refers to a\n"
"typical or common use of that class of product, regardless of the status\n"
"of the particular user or of the way in which the particular user\n"
"actually uses, or expects or is expected to use, the product.  A product\n"
"is a consumer product regardless of whether the product has substantial\n"
"commercial, industrial or non-consumer uses, unless such uses represent\n"
"the only significant mode of use of the product.\n"
"\n"
"  \"Installation Information\" for a User Product means any methods,\n"
"procedures, authorization keys, or other information required to install\n"
"and execute modified versions of a covered work in that User Product from\n"
"a modified version of its Corresponding Source.  The information must\n"
"suffice to ensure that the continued functioning of the modified object\n"
"code is in no case prevented or interfered with solely because\n"
"modification has been made.\n"
"\n"
"  If you convey an object code work under this section in, or with, or\n"
"specifical"
                        "ly for use in, a User Product, and the conveying occurs as\n"
"part of a transaction in which the right of possession and use of the\n"
"User Product is transferred to the recipient in perpetuity or for a\n"
"fixed term (regardless of how the transaction is characterized), the\n"
"Corresponding Source conveyed under this section must be accompanied\n"
"by the Installation Information.  But this requirement does not apply\n"
"if neither you nor any third party retains the ability to install\n"
"modified object code on the User Product (for example, the work has\n"
"been installed in ROM).\n"
"\n"
"  The requirement to provide Installation Information does not include a\n"
"requirement to continue to provide support service, warranty, or updates\n"
"for a work that has been modified or installed by the recipient, or for\n"
"the User Product in which it has been modified or installed.  Access to a\n"
"network may be denied when the modification itself materially and\n"
"adversely affects the operation of the netw"
                        "ork or violates the rules and\n"
"protocols for communication across the network.\n"
"\n"
"  Corresponding Source conveyed, and Installation Information provided,\n"
"in accord with this section must be in a format that is publicly\n"
"documented (and with an implementation available to the public in\n"
"source code form), and must require no special password or key for\n"
"unpacking, reading or copying.\n"
"\n"
"  7. Additional Terms.\n"
"\n"
"  \"Additional permissions\" are terms that supplement the terms of this\n"
"License by making exceptions from one or more of its conditions.\n"
"Additional permissions that are applicable to the entire Program shall\n"
"be treated as though they were included in this License, to the extent\n"
"that they are valid under applicable law.  If additional permissions\n"
"apply only to part of the Program, that part may be used separately\n"
"under those permissions, but the entire Program remains governed by\n"
"this License without regard to the additional permissions.\n"
""
                        "\n"
"  When you convey a copy of a covered work, you may at your option\n"
"remove any additional permissions from that copy, or from any part of\n"
"it.  (Additional permissions may be written to require their own\n"
"removal in certain cases when you modify the work.)  You may place\n"
"additional permissions on material, added by you to a covered work,\n"
"for which you have or can give appropriate copyright permission.\n"
"\n"
"  Notwithstanding any other provision of this License, for material you\n"
"add to a covered work, you may (if authorized by the copyright holders of\n"
"that material) supplement the terms of this License with terms:\n"
"\n"
"    a) Disclaiming warranty or limiting liability differently from the\n"
"    terms of sections 15 and 16 of this License; or\n"
"\n"
"    b) Requiring preservation of specified reasonable legal notices or\n"
"    author attributions in that material or in the Appropriate Legal\n"
"    Notices displayed by works containing it; or\n"
"\n"
"    c) Prohibiting m"
                        "isrepresentation of the origin of that material, or\n"
"    requiring that modified versions of such material be marked in\n"
"    reasonable ways as different from the original version; or\n"
"\n"
"    d) Limiting the use for publicity purposes of names of licensors or\n"
"    authors of the material; or\n"
"\n"
"    e) Declining to grant rights under trademark law for use of some\n"
"    trade names, trademarks, or service marks; or\n"
"\n"
"    f) Requiring indemnification of licensors and authors of that\n"
"    material by anyone who conveys the material (or modified versions of\n"
"    it) with contractual assumptions of liability to the recipient, for\n"
"    any liability that these contractual assumptions directly impose on\n"
"    those licensors and authors.\n"
"\n"
"  All other non-permissive additional terms are considered \"further\n"
"restrictions\" within the meaning of section 10.  If the Program as you\n"
"received it, or any part of it, contains a notice stating that it is\n"
"governed by th"
                        "is License along with a term that is a further\n"
"restriction, you may remove that term.  If a license document contains\n"
"a further restriction but permits relicensing or conveying under this\n"
"License, you may add to a covered work material governed by the terms\n"
"of that license document, provided that the further restriction does\n"
"not survive such relicensing or conveying.\n"
"\n"
"  If you add terms to a covered work in accord with this section, you\n"
"must place, in the relevant source files, a statement of the\n"
"additional terms that apply to those files, or a notice indicating\n"
"where to find the applicable terms.\n"
"\n"
"  Additional terms, permissive or non-permissive, may be stated in the\n"
"form of a separately written license, or stated as exceptions;\n"
"the above requirements apply either way.\n"
"\n"
"  8. Termination.\n"
"\n"
"  You may not propagate or modify a covered work except as expressly\n"
"provided under this License.  Any attempt otherwise to propagate or\n"
"modify "
                        "it is void, and will automatically terminate your rights under\n"
"this License (including any patent licenses granted under the third\n"
"paragraph of section 11).\n"
"\n"
"  However, if you cease all violation of this License, then your\n"
"license from a particular copyright holder is reinstated (a)\n"
"provisionally, unless and until the copyright holder explicitly and\n"
"finally terminates your license, and (b) permanently, if the copyright\n"
"holder fails to notify you of the violation by some reasonable means\n"
"prior to 60 days after the cessation.\n"
"\n"
"  Moreover, your license from a particular copyright holder is\n"
"reinstated permanently if the copyright holder notifies you of the\n"
"violation by some reasonable means, this is the first time you have\n"
"received notice of violation of this License (for any work) from that\n"
"copyright holder, and you cure the violation prior to 30 days after\n"
"your receipt of the notice.\n"
"\n"
"  Termination of your rights under this section does not "
                        "terminate the\n"
"licenses of parties who have received copies or rights from you under\n"
"this License.  If your rights have been terminated and not permanently\n"
"reinstated, you do not qualify to receive new licenses for the same\n"
"material under section 10.\n"
"\n"
"  9. Acceptance Not Required for Having Copies.\n"
"\n"
"  You are not required to accept this License in order to receive or\n"
"run a copy of the Program.  Ancillary propagation of a covered work\n"
"occurring solely as a consequence of using peer-to-peer transmission\n"
"to receive a copy likewise does not require acceptance.  However,\n"
"nothing other than this License grants you permission to propagate or\n"
"modify any covered work.  These actions infringe copyright if you do\n"
"not accept this License.  Therefore, by modifying or propagating a\n"
"covered work, you indicate your acceptance of this License to do so.\n"
"\n"
"  10. Automatic Licensing of Downstream Recipients.\n"
"\n"
"  Each time you convey a covered work, the recip"
                        "ient automatically\n"
"receives a license from the original licensors, to run, modify and\n"
"propagate that work, subject to this License.  You are not responsible\n"
"for enforcing compliance by third parties with this License.\n"
"\n"
"  An \"entity transaction\" is a transaction transferring control of an\n"
"organization, or substantially all assets of one, or subdividing an\n"
"organization, or merging organizations.  If propagation of a covered\n"
"work results from an entity transaction, each party to that\n"
"transaction who receives a copy of the work also receives whatever\n"
"licenses to the work the party's predecessor in interest had or could\n"
"give under the previous paragraph, plus a right to possession of the\n"
"Corresponding Source of the work from the predecessor in interest, if\n"
"the predecessor has it or can get it with reasonable efforts.\n"
"\n"
"  You may not impose any further restrictions on the exercise of the\n"
"rights granted or affirmed under this License.  For example, you "
                        "may\n"
"not impose a license fee, royalty, or other charge for exercise of\n"
"rights granted under this License, and you may not initiate litigation\n"
"(including a cross-claim or counterclaim in a lawsuit) alleging that\n"
"any patent claim is infringed by making, using, selling, offering for\n"
"sale, or importing the Program or any portion of it.\n"
"\n"
"  11. Patents.\n"
"\n"
"  A \"contributor\" is a copyright holder who authorizes use under this\n"
"License of the Program or a work on which the Program is based.  The\n"
"work thus licensed is called the contributor's \"contributor version\".\n"
"\n"
"  A contributor's \"essential patent claims\" are all patent claims\n"
"owned or controlled by the contributor, whether already acquired or\n"
"hereafter acquired, that would be infringed by some manner, permitted\n"
"by this License, of making, using, or selling its contributor version,\n"
"but do not include claims that would be infringed only as a\n"
"consequence of further modification of the contribu"
                        "tor version.  For\n"
"purposes of this definition, \"control\" includes the right to grant\n"
"patent sublicenses in a manner consistent with the requirements of\n"
"this License.\n"
"\n"
"  Each contributor grants you a non-exclusive, worldwide, royalty-free\n"
"patent license under the contributor's essential patent claims, to\n"
"make, use, sell, offer for sale, import and otherwise run, modify and\n"
"propagate the contents of its contributor version.\n"
"\n"
"  In the following three paragraphs, a \"patent license\" is any express\n"
"agreement or commitment, however denominated, not to enforce a patent\n"
"(such as an express permission to practice a patent or covenant not to\n"
"sue for patent infringement).  To \"grant\" such a patent license to a\n"
"party means to make such an agreement or commitment not to enforce a\n"
"patent against the party.\n"
"\n"
"  If you convey a covered work, knowingly relying on a patent license,\n"
"and the Corresponding Source of the work is not available for anyone\n"
""
                        "to copy, free of charge and under the terms of this License, through a\n"
"publicly available network server or other readily accessible means,\n"
"then you must either (1) cause the Corresponding Source to be so\n"
"available, or (2) arrange to deprive yourself of the benefit of the\n"
"patent license for this particular work, or (3) arrange, in a manner\n"
"consistent with the requirements of this License, to extend the patent\n"
"license to downstream recipients.  \"Knowingly relying\" means you have\n"
"actual knowledge that, but for the patent license, your conveying the\n"
"covered work in a country, or your recipient's use of the covered work\n"
"in a country, would infringe one or more identifiable patents in that\n"
"country that you have reason to believe are valid.\n"
"\n"
"  If, pursuant to or in connection with a single transaction or\n"
"arrangement, you convey, or propagate by procuring conveyance of, a\n"
"covered work, and grant a patent license to some of the parties\n"
"receiving the covered"
                        " work authorizing them to use, propagate, modify\n"
"or convey a specific copy of the covered work, then the patent license\n"
"you grant is automatically extended to all recipients of the covered\n"
"work and works based on it.\n"
"\n"
"  A patent license is \"discriminatory\" if it does not include within\n"
"the scope of its coverage, prohibits the exercise of, or is\n"
"conditioned on the non-exercise of one or more of the rights that are\n"
"specifically granted under this License.  You may not convey a covered\n"
"work if you are a party to an arrangement with a third party that is\n"
"in the business of distributing software, under which you make payment\n"
"to the third party based on the extent of your activity of conveying\n"
"the work, and under which the third party grants, to any of the\n"
"parties who would receive the covered work from you, a discriminatory\n"
"patent license (a) in connection with copies of the covered work\n"
"conveyed by you (or copies made from those copies), or (b) primaril"
                        "y\n"
"for and in connection with specific products or compilations that\n"
"contain the covered work, unless you entered into that arrangement,\n"
"or that patent license was granted, prior to 28 March 2007.\n"
"\n"
"  Nothing in this License shall be construed as excluding or limiting\n"
"any implied license or other defenses to infringement that may\n"
"otherwise be available to you under applicable patent law.\n"
"\n"
"  12. No Surrender of Others' Freedom.\n"
"\n"
"  If conditions are imposed on you (whether by court order, agreement or\n"
"otherwise) that contradict the conditions of this License, they do not\n"
"excuse you from the conditions of this License.  If you cannot convey a\n"
"covered work so as to satisfy simultaneously your obligations under this\n"
"License and any other pertinent obligations, then as a consequence you may\n"
"not convey it at all.  For example, if you agree to terms that obligate you\n"
"to collect a royalty for further conveying from those to whom you convey\n"
"the Progra"
                        "m, the only way you could satisfy both those terms and this\n"
"License would be to refrain entirely from conveying the Program.\n"
"\n"
"  13. Use with the GNU Affero General Public License.\n"
"\n"
"  Notwithstanding any other provision of this License, you have\n"
"permission to link or combine any covered work with a work licensed\n"
"under version 3 of the GNU Affero General Public License into a single\n"
"combined work, and to convey the resulting work.  The terms of this\n"
"License will continue to apply to the part which is the covered work,\n"
"but the special requirements of the GNU Affero General Public License,\n"
"section 13, concerning interaction through a network will apply to the\n"
"combination as such.\n"
"\n"
"  14. Revised Versions of this License.\n"
"\n"
"  The Free Software Foundation may publish revised and/or new versions of\n"
"the GNU General Public License from time to time.  Such new versions will\n"
"be similar in spirit to the present version, but may differ in detail to\n"
"a"
                        "ddress new problems or concerns.\n"
"\n"
"  Each version is given a distinguishing version number.  If the\n"
"Program specifies that a certain numbered version of the GNU General\n"
"Public License \"or any later version\" applies to it, you have the\n"
"option of following the terms and conditions either of that numbered\n"
"version or of any later version published by the Free Software\n"
"Foundation.  If the Program does not specify a version number of the\n"
"GNU General Public License, you may choose any version ever published\n"
"by the Free Software Foundation.\n"
"\n"
"  If the Program specifies that a proxy can decide which future\n"
"versions of the GNU General Public License can be used, that proxy's\n"
"public statement of acceptance of a version permanently authorizes you\n"
"to choose that version for the Program.\n"
"\n"
"  Later license versions may give you additional or different\n"
"permissions.  However, no additional obligations are imposed on any\n"
"author or copyright holder as a resul"
                        "t of your choosing to follow a\n"
"later version.\n"
"\n"
"  15. Disclaimer of Warranty.\n"
"\n"
"  THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY\n"
"APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT\n"
"HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM \"AS IS\" WITHOUT WARRANTY\n"
"OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO,\n"
"THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR\n"
"PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM\n"
"IS WITH YOU.  SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF\n"
"ALL NECESSARY SERVICING, REPAIR OR CORRECTION.\n"
"\n"
"  16. Limitation of Liability.\n"
"\n"
"  IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING\n"
"WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR CONVEYS\n"
"THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY\n"
"GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING O"
                        "UT OF THE\n"
"USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF\n"
"DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD\n"
"PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS),\n"
"EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF\n"
"SUCH DAMAGES.\n"
"\n"
"  17. Interpretation of Sections 15 and 16.\n"
"\n"
"  If the disclaimer of warranty and limitation of liability provided\n"
"above cannot be given local legal effect according to their terms,\n"
"reviewing courts shall apply local law that most closely approximates\n"
"an absolute waiver of all civil liability in connection with the\n"
"Program, unless a warranty or assumption of liability accompanies a\n"
"copy of the Program in return for a fee.", None))
        self.label_feedback.setText(QCoreApplication.translate("MainWindow", u"Pesquisando por palavra...", None))
        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://github.com/demelomatt/\"><span style=\" color:#70757d;\">https://github.com/demelomatt/</span></a></p></body></html>", None))
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"v1.1.0", None))
    # retranslateUi

