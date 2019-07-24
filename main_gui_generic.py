# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_gui_generic.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(516, 604)
        MainWindow.setStyleSheet("QWidget#footer QToolButton, QWidget#header QToolButton{\n"
"    border: 0px solid black;\n"
"    border-radius: 12px\n"
"}\n"
"\n"
"\n"
"QWidget#footer QToolButton{\n"
"    padding: 5px\n"
"}\n"
"\n"
"QWidget#footer QToolButton:hover{\n"
"    padding: 0px\n"
"}\n"
"\n"
"QLabel#img_label{\n"
"    border: 2px solid rgb(238, 238, 238)\n"
"}\n"
"\n"
"QWidget#header QLabel{\n"
"    font-size: 14px;\n"
"    color: black\n"
"}\n"
"\n"
"QWidget#footer QLabel, QWidget#footer QCheckBox{\n"
"    font-size: 12px;\n"
"    /*color: rgb(230, 155, 3)*/\n"
"}\n"
"\n"
"\n"
"\n"
"QWidget#centralwidget{\n"
"    background-color: qlineargradient(spread:pad, x1:0.528409, y1:0, x2:0.534591, y2:1, stop:0 rgba(255, 255, 255, 255), stop:0.971591 rgba(245, 247, 250, 255), stop:1 rgba(245, 247, 250, 255))\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.img_label = QtWidgets.QLabel(self.centralwidget)
        self.img_label.setObjectName("img_label")
        self.gridLayout.addWidget(self.img_label, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.header = QtWidgets.QWidget(self.centralwidget)
        self.header.setMaximumSize(QtCore.QSize(16777215, 50))
        self.header.setObjectName("header")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.header)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.name_label = QtWidgets.QLabel(self.header)
        self.name_label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.name_label.setObjectName("name_label")
        self.horizontalLayout_2.addWidget(self.name_label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.remember_button = QtWidgets.QToolButton(self.header)
        self.remember_button.setFocusPolicy(QtCore.Qt.NoFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("files/note.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.remember_button.setIcon(icon)
        self.remember_button.setIconSize(QtCore.QSize(25, 25))
        self.remember_button.setObjectName("remember_button")
        self.horizontalLayout_2.addWidget(self.remember_button)
        self.gridLayout.addWidget(self.header, 1, 0, 1, 1)
        self.footer = QtWidgets.QWidget(self.centralwidget)
        self.footer.setMaximumSize(QtCore.QSize(16777215, 161))
        self.footer.setObjectName("footer")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.footer)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget = QtWidgets.QWidget(self.footer)
        self.widget.setMinimumSize(QtCore.QSize(0, 79))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 66))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pos_count_label = QtWidgets.QLabel(self.widget)
        self.pos_count_label.setMinimumSize(QtCore.QSize(120, 12))
        self.pos_count_label.setObjectName("pos_count_label")
        self.verticalLayout.addWidget(self.pos_count_label)
        self.neg_count_label = QtWidgets.QLabel(self.widget)
        self.neg_count_label.setMinimumSize(QtCore.QSize(120, 12))
        self.neg_count_label.setObjectName("neg_count_label")
        self.verticalLayout.addWidget(self.neg_count_label)
        self.other_count_label = QtWidgets.QLabel(self.widget)
        self.other_count_label.setMinimumSize(QtCore.QSize(120, 12))
        self.other_count_label.setObjectName("other_count_label")
        self.verticalLayout.addWidget(self.other_count_label)
        self.gridLayout_2.addWidget(self.widget, 4, 1, 3, 1)
        self.widget_2 = QtWidgets.QWidget(self.footer)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(86, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.neg_button = QtWidgets.QToolButton(self.widget_2)
        self.neg_button.setMinimumSize(QtCore.QSize(55, 55))
        self.neg_button.setMaximumSize(QtCore.QSize(55, 55))
        self.neg_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.neg_button.setStyleSheet("QToolButton{\n"
"    qproperty-icon: url(\"D:/programming/tinder_analysis/files/nope.png\")\n"
"}\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("files/left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.neg_button.setIcon(icon1)
        self.neg_button.setIconSize(QtCore.QSize(50, 50))
        self.neg_button.setObjectName("neg_button")
        self.horizontalLayout.addWidget(self.neg_button)
        self.other_button = QtWidgets.QToolButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.other_button.sizePolicy().hasHeightForWidth())
        self.other_button.setSizePolicy(sizePolicy)
        self.other_button.setMinimumSize(QtCore.QSize(50, 50))
        self.other_button.setMaximumSize(QtCore.QSize(50, 605050))
        self.other_button.setFocusPolicy(QtCore.Qt.NoFocus)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("files/down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.other_button.setIcon(icon2)
        self.other_button.setIconSize(QtCore.QSize(45, 45))
        self.other_button.setObjectName("other_button")
        self.horizontalLayout.addWidget(self.other_button, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.pos_button = QtWidgets.QToolButton(self.widget_2)
        self.pos_button.setMinimumSize(QtCore.QSize(55, 55))
        self.pos_button.setMaximumSize(QtCore.QSize(55, 55))
        self.pos_button.setFocusPolicy(QtCore.Qt.NoFocus)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("files/right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pos_button.setIcon(icon3)
        self.pos_button.setIconSize(QtCore.QSize(50, 50))
        self.pos_button.setObjectName("pos_button")
        self.horizontalLayout.addWidget(self.pos_button)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.gridLayout_2.addWidget(self.widget_2, 2, 1, 2, 3)
        self.undo_button = QtWidgets.QToolButton(self.footer)
        self.undo_button.setMinimumSize(QtCore.QSize(35, 35))
        self.undo_button.setMaximumSize(QtCore.QSize(35, 35))
        self.undo_button.setFocusPolicy(QtCore.Qt.NoFocus)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("files/undo2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.undo_button.setIcon(icon4)
        self.undo_button.setIconSize(QtCore.QSize(30, 30))
        self.undo_button.setObjectName("undo_button")
        self.gridLayout_2.addWidget(self.undo_button, 5, 2, 1, 1)
        self.grayscale_checkbox = QtWidgets.QCheckBox(self.footer)
        self.grayscale_checkbox.setMouseTracking(False)
        self.grayscale_checkbox.setTabletTracking(False)
        self.grayscale_checkbox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.grayscale_checkbox.setStyleSheet("QCheckBox::indicator:unchecked{\n"
"    image: url(./files/flame.png);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    image: url(./files/flame_gray.png);\n"
"}\n"
"")
        self.grayscale_checkbox.setText("")
        self.grayscale_checkbox.setChecked(False)
        self.grayscale_checkbox.setObjectName("grayscale_checkbox")
        self.gridLayout_2.addWidget(self.grayscale_checkbox, 6, 3, 1, 1, QtCore.Qt.AlignRight)
        self.gridLayout.addWidget(self.footer, 4, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setStyleSheet("QProgressBar:horizontal {\n"
"border: 1px solid rgb(100, 100, 100);\n"
"border-radius: 3px;\n"
"background: white;\n"
"padding: 2px;\n"
"text-align: right;\n"
"margin-right: 0ex;\n"
"}\n"
"QProgressBar::chunk:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0  rgba(8,208,255,255), stop: 1 rgba(64,170,255,255));\n"
"margin-right: 2px; /* space */\n"
"border-radius: 3px;\n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setFormat("")
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.img_label.setText(_translate("MainWindow", "image"))
        self.name_label.setText(_translate("MainWindow", "name"))
        self.remember_button.setText(_translate("MainWindow", "..."))
        self.pos_count_label.setText(_translate("MainWindow", "pos count"))
        self.neg_count_label.setText(_translate("MainWindow", "neg count"))
        self.other_count_label.setText(_translate("MainWindow", "other count"))
        self.neg_button.setText(_translate("MainWindow", "..."))
        self.other_button.setText(_translate("MainWindow", "..."))
        self.pos_button.setText(_translate("MainWindow", "..."))
        self.undo_button.setText(_translate("MainWindow", "..."))

