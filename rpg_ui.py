# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rpg.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1008, 685)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pages = QStackedWidget(self.centralwidget)
        self.pages.setObjectName(u"pages")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page_home.sizePolicy().hasHeightForWidth())
        self.page_home.setSizePolicy(sizePolicy)
        self.label = QLabel(self.page_home)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-7, -170, 1024, 1024))
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMaximumSize(QSize(1041, 1024))
        font = QFont()
        font.setFamily(u"Papyrus")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTabletTracking(False)
        self.label.setFocusPolicy(Qt.TabFocus)
        self.label.setStyleSheet(u"QLabel{\n"
"   .img{\n"
"		height: 100%;\n"
"		width:100%;\n"
"		object-fit: cover;\n"
"    }\n"
"}")
        self.label.setFrameShape(QFrame.NoFrame)
        self.label.setFrameShadow(QFrame.Raised)
        self.label.setLineWidth(10)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setIndent(0)
        self.label.setOpenExternalLinks(False)
        self.frame = QFrame(self.page_home)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(250, 430, 341, 271))
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy2)
        self.frame.setMinimumSize(QSize(341, 241))
        font1 = QFont()
        font1.setFamily(u"MS Serif")
        font1.setPointSize(7)
        font1.setKerning(False)
        self.frame.setFont(font1)
        self.frame.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color:wheat;\n"
"border-radius: 8px;\n"
"align-self: center;\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetFixedSize)
        self.pb_start = QPushButton(self.frame)
        self.pb_start.setObjectName(u"pb_start")
        self.pb_start.setMinimumSize(QSize(321, 39))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(245, 222, 179, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(213, 127, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(191, 63, 255, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(85, 0, 127, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(113, 0, 170, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush6 = QBrush(QColor(255, 255, 255, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        brush7 = QBrush(QColor(212, 127, 255, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        brush8 = QBrush(QColor(255, 255, 220, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        brush9 = QBrush(QColor(170, 0, 255, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        self.pb_start.setPalette(palette)
        font2 = QFont()
        font2.setFamily(u"Papyrus")
        font2.setPointSize(19)
        self.pb_start.setFont(font2)

        self.verticalLayout_2.addWidget(self.pb_start, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.pb_instruct = QPushButton(self.frame)
        self.pb_instruct.setObjectName(u"pb_instruct")
        self.pb_instruct.setMinimumSize(QSize(321, 39))
        self.pb_instruct.setFont(font)
        self.pb_instruct.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.pb_instruct.setToolTipDuration(7)
        self.pb_instruct.setAutoFillBackground(False)

        self.verticalLayout_2.addWidget(self.pb_instruct, 0, Qt.AlignHCenter)

        self.pb_exit = QPushButton(self.frame)
        self.pb_exit.setObjectName(u"pb_exit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pb_exit.sizePolicy().hasHeightForWidth())
        self.pb_exit.setSizePolicy(sizePolicy3)
        self.pb_exit.setMinimumSize(QSize(321, 39))
        font3 = QFont()
        font3.setFamily(u"Papyrus")
        font3.setPointSize(19)
        font3.setBold(True)
        font3.setWeight(75)
        font3.setStrikeOut(False)
        font3.setKerning(False)
        self.pb_exit.setFont(font3)
        self.pb_exit.setAutoRepeatInterval(100)

        self.verticalLayout_2.addWidget(self.pb_exit, 0, Qt.AlignHCenter)

        self.txt_title = QTextBrowser(self.page_home)
        self.txt_title.setObjectName(u"txt_title")
        self.txt_title.setGeometry(QRect(40, 50, 601, 111))
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.txt_title.sizePolicy().hasHeightForWidth())
        self.txt_title.setSizePolicy(sizePolicy4)
        font4 = QFont()
        font4.setFamily(u"Macondo")
        font4.setPointSize(28)
        self.txt_title.setFont(font4)
        self.txt_title.setAutoFillBackground(True)
        self.txt_title.setStyleSheet(u"background-color: transparent;")
        self.txt_title.setFrameShape(QFrame.NoFrame)
        self.txt_title.setLineWidth(0)
        self.textBrowser = QTextBrowser(self.page_home)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(100, 130, 351, 192))
        font5 = QFont()
        font5.setFamily(u"Vollkorn SC")
        font5.setPointSize(22)
        self.textBrowser.setFont(font5)
        self.textBrowser.setStyleSheet(u"background-color: transparent;")
        self.textBrowser.setFrameShape(QFrame.NoFrame)
        self.pages.addWidget(self.page_home)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label_14 = QLabel(self.page)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(-20, -290, 1041, 1024))
        self.label_14.setMaximumSize(QSize(1041, 1024))
        self.label_14.setFont(font)
        self.label_14.setTabletTracking(False)
        self.label_14.setFocusPolicy(Qt.TabFocus)
        self.label_14.setStyleSheet(u"QLabel{\n"
"   .img{\n"
"		height: 100%;\n"
"		width:100%;\n"
"		object-fit: cover;\n"
"    }\n"
"}")
        self.label_14.setFrameShape(QFrame.NoFrame)
        self.label_14.setFrameShadow(QFrame.Raised)
        self.label_14.setLineWidth(10)
        self.label_14.setAlignment(Qt.AlignCenter)
        self.label_14.setIndent(0)
        self.label_14.setOpenExternalLinks(False)
        self.textBrowser_10 = QTextBrowser(self.page)
        self.textBrowser_10.setObjectName(u"textBrowser_10")
        self.textBrowser_10.setGeometry(QRect(220, 20, 591, 101))
        self.textBrowser_10.setFont(font4)
        self.pushButton_29 = QPushButton(self.page)
        self.pushButton_29.setObjectName(u"pushButton_29")
        self.pushButton_29.setGeometry(QRect(440, 510, 161, 51))
        font6 = QFont()
        font6.setFamily(u"Papyrus")
        font6.setPointSize(16)
        self.pushButton_29.setFont(font6)
        self.pages.addWidget(self.page)
        self.page_instr = QWidget()
        self.page_instr.setObjectName(u"page_instr")
        self.frame_2 = QFrame(self.page_instr)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(-20, -10, 951, 951))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(30, 120, 851, 591))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(8, -111, 1031, 741))
        self.txt_instructr = QTextBrowser(self.frame_3)
        self.txt_instructr.setObjectName(u"txt_instructr")
        self.txt_instructr.setGeometry(QRect(196, 60, 541, 431))
        font7 = QFont()
        font7.setFamily(u"Papyrus")
        font7.setPointSize(15)
        font7.setKerning(False)
        self.txt_instructr.setFont(font7)
        self.txt_instructr.setStyleSheet(u"QTextBrowser{\n"
"\n"
"background: transparent;\n"
"justify-text: center;\n"
"border-radius: 10px 10px;\n"
"\n"
"}\n"
"QLabel{\n"
"\n"
"background-color: grey;\n"
"opacity:0.5;\n"
"\n"
"border-radius: 10px 10px;\n"
"}\n"
"")
        self.txt_instructr.setFrameShadow(QFrame.Raised)
        self.txt_instructr.setLineWidth(5)
        self.pb_back = QPushButton(self.frame_3)
        self.pb_back.setObjectName(u"pb_back")
        self.pb_back.setGeometry(QRect(380, 412, 181, 41))
        font8 = QFont()
        font8.setFamily(u"Papyrus")
        font8.setPointSize(14)
        self.pb_back.setFont(font8)
        self.pb_back.setStyleSheet(u"background-color:wheat;\n"
"border-radius:10px;")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(42, -278, 1153, 950))
        self.label_3.setStyleSheet(u"background:transparent;")
        self.label_3.raise_()
        self.frame_3.raise_()
        self.pages.addWidget(self.page_instr)
        self.Hall = QWidget()
        self.Hall.setObjectName(u"Hall")
        self.Hall.setEnabled(True)
        self.label_2 = QLabel(self.Hall)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(-50, -200, 1024, 1024))
        self.label_2.setMaximumSize(QSize(1041, 1024))
        self.label_2.setFont(font)
        self.label_2.setTabletTracking(False)
        self.label_2.setFocusPolicy(Qt.TabFocus)
        self.label_2.setStyleSheet(u"QLabel{\n"
"   .img{\n"
"		height: 100%;\n"
"		width:100%;\n"
"		object-fit: cover;\n"
"    }\n"
"}")
        self.label_2.setFrameShape(QFrame.NoFrame)
        self.label_2.setFrameShadow(QFrame.Raised)
        self.label_2.setLineWidth(10)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setIndent(0)
        self.label_2.setOpenExternalLinks(False)
        self.textBrowser_2 = QTextBrowser(self.Hall)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setGeometry(QRect(40, 30, 321, 71))
        sizePolicy.setHeightForWidth(self.textBrowser_2.sizePolicy().hasHeightForWidth())
        self.textBrowser_2.setSizePolicy(sizePolicy)
        font9 = QFont()
        font9.setFamily(u"Macondo")
        font9.setPointSize(22)
        self.textBrowser_2.setFont(font9)
        self.pb_dr = QPushButton(self.Hall)
        self.pb_dr.setObjectName(u"pb_dr")
        self.pb_dr.setGeometry(QRect(30, 340, 101, 23))
        self.pb_a = QPushButton(self.Hall)
        self.pb_a.setObjectName(u"pb_a")
        self.pb_a.setGeometry(QRect(850, 340, 75, 23))
        self.lineEdit = QLineEdit(self.Hall)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(160, 499, 141, 31))
        self.lineEdit.setStyleSheet(u"border-radius: 10px;")
        self.pushButton = QPushButton(self.Hall)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(310, 500, 75, 31))
        sizePolicy5 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy5)
        font10 = QFont()
        font10.setFamily(u"Papyrus")
        font10.setPointSize(10)
        self.pushButton.setFont(font10)
        self.pushButton.setStyleSheet(u"background-color: black;\n"
"color: white;\n"
"border-radius:10px;\n"
"")
        self.label_12 = QLabel(self.Hall)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(180, 480, 71, 16))
        self.label_12.setStyleSheet(u"background-color:white;")
        self.pages.addWidget(self.Hall)
        self.dining_room = QWidget()
        self.dining_room.setObjectName(u"dining_room")
        self.label_5 = QLabel(self.dining_room)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(-53, -254, 1041, 1024))
        self.label_5.setMaximumSize(QSize(1041, 1024))
        self.label_5.setFont(font)
        self.label_5.setTabletTracking(False)
        self.label_5.setFocusPolicy(Qt.TabFocus)
        self.label_5.setStyleSheet(u"QLabel{\n"
"   .img{\n"
"		height: 100%;\n"
"		width:100%;\n"
"		object-fit: cover;\n"
"    }\n"
"}")
        self.label_5.setFrameShape(QFrame.NoFrame)
        self.label_5.setFrameShadow(QFrame.Raised)
        self.label_5.setLineWidth(10)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setIndent(0)
        self.label_5.setOpenExternalLinks(False)
        self.textBrowser_3 = QTextBrowser(self.dining_room)
        self.textBrowser_3.setObjectName(u"textBrowser_3")
        self.textBrowser_3.setGeometry(QRect(50, 60, 231, 61))
        self.textBrowser_3.setFont(font4)
        self.label_13 = QLabel(self.dining_room)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(700, 320, 47, 13))
        self.pb_k = QPushButton(self.dining_room)
        self.pb_k.setObjectName(u"pb_k")
        self.pb_k.setGeometry(QRect(880, 350, 75, 23))
        self.pb_h = QPushButton(self.dining_room)
        self.pb_h.setObjectName(u"pb_h")
        self.pb_h.setGeometry(QRect(70, 320, 75, 23))
        self.lineEdit_2 = QLineEdit(self.dining_room)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(150, 520, 191, 41))
        self.lineEdit_2.setStyleSheet(u"border-radius:10px;")
        self.pushButton_2 = QPushButton(self.dining_room)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(350, 530, 75, 23))
        self.pushButton_2.setStyleSheet(u"background-color: black;\n"
"color: white;\n"
"border-radius:10px;\n"
"")
        self.pages.addWidget(self.dining_room)
        self.kitchen = QWidget()
        self.kitchen.setObjectName(u"kitchen")
        self.label_6 = QLabel(self.kitchen)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(-10, -260, 1041, 1024))
        self.label_6.setMaximumSize(QSize(1041, 1024))
        self.label_6.setFont(font)
        self.label_6.setTabletTracking(False)
        self.label_6.setFocusPolicy(Qt.TabFocus)
        self.label_6.setStyleSheet(u"QLabel{\n"
"   .img{\n"
"		height: 100%;\n"
"		width:100%;\n"
"		object-fit: cover;\n"
"    }\n"
"}")
        self.label_6.setFrameShape(QFrame.NoFrame)
        self.label_6.setFrameShadow(QFrame.Raised)
        self.label_6.setLineWidth(10)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setIndent(0)
        self.label_6.setOpenExternalLinks(False)
        self.textBrowser_4 = QTextBrowser(self.kitchen)
        self.textBrowser_4.setObjectName(u"textBrowser_4")
        self.textBrowser_4.setGeometry(QRect(80, 80, 151, 61))
        self.textBrowser_4.setFont(font4)
        self.pb_dr_2 = QPushButton(self.kitchen)
        self.pb_dr_2.setObjectName(u"pb_dr_2")
        self.pb_dr_2.setGeometry(QRect(70, 360, 111, 23))
        self.pb_pan = QPushButton(self.kitchen)
        self.pb_pan.setObjectName(u"pb_pan")
        self.pb_pan.setGeometry(QRect(850, 350, 75, 23))
        self.pb_inv_3 = QPushButton(self.kitchen)
        self.pb_inv_3.setObjectName(u"pb_inv_3")
        self.pb_inv_3.setGeometry(QRect(230, 510, 75, 23))
        self.pb_take_2 = QPushButton(self.kitchen)
        self.pb_take_2.setObjectName(u"pb_take_2")
        self.pb_take_2.setGeometry(QRect(670, 510, 75, 23))
        self.pages.addWidget(self.kitchen)
        self.saladearmas = QWidget()
        self.saladearmas.setObjectName(u"saladearmas")
        self.label_7 = QLabel(self.saladearmas)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(25, -208, 1041, 1024))
        self.label_7.setMaximumSize(QSize(1041, 1024))
        self.label_7.setFont(font)
        self.label_7.setTabletTracking(False)
        self.label_7.setFocusPolicy(Qt.TabFocus)
        self.label_7.setStyleSheet(u"QLabel{\n"
"   .img{\n"
"		height: 100%;\n"
"		width:100%;\n"
"		object-fit: cover;\n"
"    }\n"
"}")
        self.label_7.setFrameShape(QFrame.NoFrame)
        self.label_7.setFrameShadow(QFrame.Raised)
        self.label_7.setLineWidth(10)
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_7.setIndent(0)
        self.label_7.setOpenExternalLinks(False)
        self.textBrowser_5 = QTextBrowser(self.saladearmas)
        self.textBrowser_5.setObjectName(u"textBrowser_5")
        self.textBrowser_5.setGeometry(QRect(80, 50, 251, 61))
        self.textBrowser_5.setFont(font4)
        self.pb_hall = QPushButton(self.saladearmas)
        self.pb_hall.setObjectName(u"pb_hall")
        self.pb_hall.setGeometry(QRect(70, 340, 75, 23))
        self.pb_tes = QPushButton(self.saladearmas)
        self.pb_tes.setObjectName(u"pb_tes")
        self.pb_tes.setGeometry(QRect(850, 340, 75, 23))
        self.pb_inv_4 = QPushButton(self.saladearmas)
        self.pb_inv_4.setObjectName(u"pb_inv_4")
        self.pb_inv_4.setGeometry(QRect(330, 510, 75, 23))
        self.pb_take_3 = QPushButton(self.saladearmas)
        self.pb_take_3.setObjectName(u"pb_take_3")
        self.pb_take_3.setGeometry(QRect(630, 510, 75, 23))
        self.pb_trono = QPushButton(self.saladearmas)
        self.pb_trono.setObjectName(u"pb_trono")
        self.pb_trono.setGeometry(QRect(600, 310, 81, 31))
        self.pages.addWidget(self.saladearmas)
        self.treasure_room = QWidget()
        self.treasure_room.setObjectName(u"treasure_room")
        self.label_8 = QLabel(self.treasure_room)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(-5, -345, 1041, 1024))
        self.label_8.setMaximumSize(QSize(1041, 1024))
        self.label_8.setFont(font)
        self.label_8.setTabletTracking(False)
        self.label_8.setFocusPolicy(Qt.TabFocus)
        self.label_8.setStyleSheet(u"QLabel{\n"
"   .img{\n"
"		height: 100%;\n"
"		width:100%;\n"
"		object-fit: cover;\n"
"    }\n"
"}")
        self.label_8.setFrameShape(QFrame.NoFrame)
        self.label_8.setFrameShadow(QFrame.Raised)
        self.label_8.setLineWidth(10)
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_8.setIndent(0)
        self.label_8.setOpenExternalLinks(False)
        self.textBrowser_6 = QTextBrowser(self.treasure_room)
        self.textBrowser_6.setObjectName(u"textBrowser_6")
        self.textBrowser_6.setGeometry(QRect(50, 90, 261, 61))
        self.textBrowser_6.setFont(font4)
        self.pb_arm = QPushButton(self.treasure_room)
        self.pb_arm.setObjectName(u"pb_arm")
        self.pb_arm.setGeometry(QRect(70, 320, 111, 23))
        self.pb_lib = QPushButton(self.treasure_room)
        self.pb_lib.setObjectName(u"pb_lib")
        self.pb_lib.setGeometry(QRect(870, 330, 75, 23))
        self.pages.addWidget(self.treasure_room)
        self.biblioteca = QWidget()
        self.biblioteca.setObjectName(u"biblioteca")
        self.label_9 = QLabel(self.biblioteca)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(-20, -370, 1024, 1024))
        self.label_9.setMaximumSize(QSize(1041, 1024))
        self.label_9.setFont(font)
        self.label_9.setTabletTracking(False)
        self.label_9.setFocusPolicy(Qt.TabFocus)
        self.label_9.setStyleSheet(u"QLabel{\n"
"   .img{\n"
"		height: 100%;\n"
"		width:100%;\n"
"		object-fit: cover;\n"
"    }\n"
"}")
        self.label_9.setFrameShape(QFrame.NoFrame)
        self.label_9.setFrameShadow(QFrame.Raised)
        self.label_9.setLineWidth(10)
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_9.setIndent(0)
        self.label_9.setOpenExternalLinks(False)
        self.textBrowser_7 = QTextBrowser(self.biblioteca)
        self.textBrowser_7.setObjectName(u"textBrowser_7")
        self.textBrowser_7.setGeometry(QRect(70, 70, 171, 61))
        self.textBrowser_7.setFont(font4)
        self.pb_tes_2 = QPushButton(self.biblioteca)
        self.pb_tes_2.setObjectName(u"pb_tes_2")
        self.pb_tes_2.setGeometry(QRect(60, 300, 131, 23))
        self.pb_sm = QPushButton(self.biblioteca)
        self.pb_sm.setObjectName(u"pb_sm")
        self.pb_sm.setGeometry(QRect(440, 440, 111, 23))
        self.pb_sm_2 = QPushButton(self.biblioteca)
        self.pb_sm_2.setObjectName(u"pb_sm_2")
        self.pb_sm_2.setGeometry(QRect(830, 300, 111, 23))
        self.pages.addWidget(self.biblioteca)
        self.sala_trono = QWidget()
        self.sala_trono.setObjectName(u"sala_trono")
        self.label_10 = QLabel(self.sala_trono)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(30, -150, 1041, 1021))
        self.label_10.setMaximumSize(QSize(1041, 1024))
        self.label_10.setFont(font)
        self.label_10.setTabletTracking(False)
        self.label_10.setFocusPolicy(Qt.TabFocus)
        self.label_10.setStyleSheet(u"QLabel{\n"
"   .img{\n"
"		height: 100%;\n"
"		width:100%;\n"
"		object-fit: cover;\n"
"    }\n"
"}")
        self.label_10.setFrameShape(QFrame.NoFrame)
        self.label_10.setFrameShadow(QFrame.Raised)
        self.label_10.setLineWidth(10)
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_10.setIndent(0)
        self.label_10.setOpenExternalLinks(False)
        self.trono = QTextBrowser(self.sala_trono)
        self.trono.setObjectName(u"trono")
        self.trono.setGeometry(QRect(100, 70, 261, 61))
        self.trono.setFont(font4)
        self.pb_arm_2 = QPushButton(self.sala_trono)
        self.pb_arm_2.setObjectName(u"pb_arm_2")
        self.pb_arm_2.setGeometry(QRect(70, 340, 121, 23))
        self.pb_sm_3 = QPushButton(self.sala_trono)
        self.pb_sm_3.setObjectName(u"pb_sm_3")
        self.pb_sm_3.setGeometry(QRect(860, 340, 75, 23))
        self.pages.addWidget(self.sala_trono)
        self.saladomago = QWidget()
        self.saladomago.setObjectName(u"saladomago")
        self.label_11 = QLabel(self.saladomago)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(30, -310, 1041, 1024))
        self.label_11.setMaximumSize(QSize(1041, 1024))
        self.label_11.setFont(font)
        self.label_11.setTabletTracking(False)
        self.label_11.setFocusPolicy(Qt.TabFocus)
        self.label_11.setStyleSheet(u"QLabel{\n"
"   .img{\n"
"		height: 100%;\n"
"		width:100%;\n"
"		object-fit: cover;\n"
"    }\n"
"}")
        self.label_11.setFrameShape(QFrame.NoFrame)
        self.label_11.setFrameShadow(QFrame.Raised)
        self.label_11.setLineWidth(10)
        self.label_11.setAlignment(Qt.AlignCenter)
        self.label_11.setIndent(0)
        self.label_11.setOpenExternalLinks(False)
        self.textBrowser_9 = QTextBrowser(self.saladomago)
        self.textBrowser_9.setObjectName(u"textBrowser_9")
        self.textBrowser_9.setGeometry(QRect(80, 50, 291, 61))
        self.textBrowser_9.setFont(font4)
        self.pb_trono_2 = QPushButton(self.saladomago)
        self.pb_trono_2.setObjectName(u"pb_trono_2")
        self.pb_trono_2.setGeometry(QRect(90, 290, 75, 23))
        self.pb_se = QPushButton(self.saladomago)
        self.pb_se.setObjectName(u"pb_se")
        self.pb_se.setGeometry(QRect(840, 300, 75, 23))
        self.pb_inv_5 = QPushButton(self.saladomago)
        self.pb_inv_5.setObjectName(u"pb_inv_5")
        self.pb_inv_5.setGeometry(QRect(320, 510, 75, 23))
        self.pb_take_4 = QPushButton(self.saladomago)
        self.pb_take_4.setObjectName(u"pb_take_4")
        self.pb_take_4.setGeometry(QRect(630, 520, 75, 23))
        self.pages.addWidget(self.saladomago)

        self.verticalLayout.addWidget(self.pages)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/icons/imagens/_760734f2-5482-431a-9f76-3bbe66665458.jpeg\"\n"
"background-size = \"100% 100% \" /></p></body></html>", None))
        self.pb_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pb_instruct.setText(QCoreApplication.translate("MainWindow", u"Instru\u00e7\u00f5es", None))
        self.pb_exit.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
        self.txt_title.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Macondo'; font-size:28pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:48pt; color:#005500;\">Automata Quest</span></p></body></html>", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Vollkorn SC'; font-size:22pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Vollkorn SC semibold';\">Castle of Illusions</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Papyrus'; font-size:19pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/icons/imagens/_f599d019-ba86-46e7-839b-2df4b3a11421.jpeg\" /></p></body></html>", None))
        self.textBrowser_10.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Macondo'; font-size:28pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Parab\u00e9ns! Voc\u00ea saiu do Castelo das Ilus\u00f5es!</p></body></html>", None))
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u"Voltar ao Menu", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/icons/imagens/imgbin-paper-parchment-scroll-papyrus-pina-colada-cocktail-eanyVe3gtFaDjqn3X5VbGHwnG-removebg-preview.png\"\n"
"\n"
"width = \"900\"\n"
"height = \"700\"/></p></body></html>", None))
        self.txt_instructr.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Papyrus'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Instru\u00e7\u00f5es</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">O jogador atravessar\u00e1 uma s\u00e9rie de c\u00e2maras e tomar\u00e1 decis\u00f5es, sendo elas, mudar de sala (go), olhar (look), ver invent\u00e1rio (inventory) e"
                        " pegar (take). Para ganhar, a sequ\u00eancia de decis\u00f5es , que \u00e9 lida como uma palavra, deve ser aceita pelo aut\u00f4mato, chegando ao estado de aceita\u00e7\u00e3o (que \u00e9 a sa\u00edda do castelo). Algumas salas precisam de itens espec\u00edficos para entrar, ent\u00e3o observe bem seu redor.</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Boa Jornada!</p></body></html>", None))
        self.pb_back.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/icons/imagens/_54c07ec3-fc12-4eb3-8d48-c1daefbfa04b.jpeg\" <style = height = \"100%\", width=\"100%\", object-fit= \"cover\"/>/></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Papyrus'; font-size:19pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/icons/imagens/_5d272f6b-a435-48e3-8543-db017f8de360.jpeg\" /></p></body></html>", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Macondo'; font-size:22pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt;\">Hall de Entrada</span></p></body></html>", None))
        self.pb_dr.setText(QCoreApplication.translate("MainWindow", u"Sala de jantar (DR)", None))
        self.pb_a.setText(QCoreApplication.translate("MainWindow", u"Armaria(A)", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"confirmar", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Comandos:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Papyrus'; font-size:19pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/icons/imagens/_89a8adbf-04e2-47dd-866e-ab9d9dcbb655.jpeg\" /><img src=\":/icons/imagens/_760734f2-5482-431a-9f76-3bbe66665458.jpeg\" /></p></body></html>", None))
        self.textBrowser_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Macondo'; font-size:28pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Sala de Jantar</p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pb_k.setText(QCoreApplication.translate("MainWindow", u"cozinha(K)", None))
        self.pb_h.setText(QCoreApplication.translate("MainWindow", u"Hall(EH)", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"confirmar", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Papyrus'; font-size:19pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/icons/imagens/_294a131b-d5e5-4e73-ac50-5b609055e7e6.jpeg\" /></p></body></html>", None))
        self.textBrowser_4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Macondo'; font-size:28pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Cozinha</p></body></html>", None))
        self.pb_dr_2.setText(QCoreApplication.translate("MainWindow", u"sala de jantar", None))
        self.pb_pan.setText(QCoreApplication.translate("MainWindow", u"despensa", None))
        self.pb_inv_3.setText(QCoreApplication.translate("MainWindow", u"inventario", None))
        self.pb_take_2.setText(QCoreApplication.translate("MainWindow", u"pegar", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Papyrus'; font-size:19pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/icons/imagens/_54c07ec3-fc12-4eb3-8d48-c1daefbfa04b.jpeg\" /></p></body></html>", None))
        self.textBrowser_5.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Macondo'; font-size:28pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Sala de Armas</p></body></html>", None))
        self.pb_hall.setText(QCoreApplication.translate("MainWindow", u"Hall", None))
        self.pb_tes.setText(QCoreApplication.translate("MainWindow", u"Sala Tesouro", None))
        self.pb_inv_4.setText(QCoreApplication.translate("MainWindow", u"inventario", None))
        self.pb_take_3.setText(QCoreApplication.translate("MainWindow", u"pegar", None))
        self.pb_trono.setText(QCoreApplication.translate("MainWindow", u"Sala do trono", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Papyrus'; font-size:19pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/icons/imagens/Imagem do WhatsApp de 2023-12-03 \u00e0(s) 23.35.04_fcaa6d31.jpg\" /></p></body></html>", None))
        self.textBrowser_6.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Macondo'; font-size:28pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Sala do tesouro</p></body></html>", None))
        self.pb_arm.setText(QCoreApplication.translate("MainWindow", u"Sala de Armas", None))
        self.pb_lib.setText(QCoreApplication.translate("MainWindow", u"Biblioteca", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Papyrus'; font-size:19pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/icons/imagens/Imagem do WhatsApp de 2023-12-03 \u00e0(s) 23.35.03_d2866627.jpg\" /></p></body></html>", None))
        self.textBrowser_7.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Macondo'; font-size:28pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Biblioteca</p></body></html>", None))
        self.pb_tes_2.setText(QCoreApplication.translate("MainWindow", u"Sala do tesouro (TR)", None))
        self.pb_sm.setText(QCoreApplication.translate("MainWindow", u"sa\u00edda secreta(SE)", None))
        self.pb_sm_2.setText(QCoreApplication.translate("MainWindow", u"Sala de Magia(WS)", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Papyrus'; font-size:19pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/icons/imagens/Imagem do WhatsApp de 2023-12-03 \u00e0(s) 23.35.03_44b85b81.jpg\" /></p></body></html>", None))
        self.trono.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Macondo'; font-size:28pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Sala do Trono</p></body></html>", None))
        self.pb_arm_2.setText(QCoreApplication.translate("MainWindow", u"Sala de Armas", None))
        self.pb_sm_3.setText(QCoreApplication.translate("MainWindow", u"Sala de Magia", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Papyrus'; font-size:19pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/icons/imagens/Imagem do WhatsApp de 2023-12-03 \u00e0(s) 23.35.05_4f56fd68.jpg\" /></p></body></html>", None))
        self.textBrowser_9.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Macondo'; font-size:28pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Sala do Feiticeiro</p></body></html>", None))
        self.pb_trono_2.setText(QCoreApplication.translate("MainWindow", u"Sala do trono", None))
        self.pb_se.setText(QCoreApplication.translate("MainWindow", u"Sa\u00edda secreta", None))
        self.pb_inv_5.setText(QCoreApplication.translate("MainWindow", u"inventario", None))
        self.pb_take_4.setText(QCoreApplication.translate("MainWindow", u"pegar", None))
    # retranslateUi

