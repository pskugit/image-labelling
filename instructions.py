# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'instructions.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Instructions(object):
    def setupUi(self, Instructions):
        Instructions.setObjectName("Instructions")
        Instructions.resize(400, 425)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Instructions.sizePolicy().hasHeightForWidth())
        Instructions.setSizePolicy(sizePolicy)
        Instructions.setMinimumSize(QtCore.QSize(400, 425))
        Instructions.setStyleSheet("QWidget#Instructions{\n"
"  background-color: white\n"
"}\n"
"QLabel#heading{\n"
" color: rgb(127, 152, 197)\n"
"}\n"
"QPushButton{\n"
"    border: 2px  solid  black;\n"
"}\n"
"QToolButton{\n"
"     background-color: white;\n"
"    border: 2px  solid    rgb(127, 152, 197);\n"
"    font-size: 10pt;\n"
"    color:  rgb(64, 90, 140);\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Instructions)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 1)
        self.noshow_checkBox = QtWidgets.QCheckBox(Instructions)
        self.noshow_checkBox.setObjectName("noshow_checkBox")
        self.gridLayout.addWidget(self.noshow_checkBox, 2, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label = QtWidgets.QLabel(Instructions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(340, 240))
        self.label.setStyleSheet(" padding-left: 20px;")
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 3)
        self.heading = QtWidgets.QLabel(Instructions)
        self.heading.setMinimumSize(QtCore.QSize(0, 80))
        self.heading.setMaximumSize(QtCore.QSize(16777215, 100))
        self.heading.setStyleSheet("")
        self.heading.setObjectName("heading")
        self.gridLayout.addWidget(self.heading, 0, 0, 1, 3)
        self.continue_button = QtWidgets.QToolButton(Instructions)
        self.continue_button.setMinimumSize(QtCore.QSize(110, 0))
        self.continue_button.setObjectName("continue_button")
        self.gridLayout.addWidget(self.continue_button, 4, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Instructions)
        QtCore.QMetaObject.connectSlotsByName(Instructions)

    def retranslateUi(self, Instructions):
        _translate = QtCore.QCoreApplication.translate
        Instructions.setWindowTitle(_translate("Instructions", "Form"))
        self.noshow_checkBox.setText(_translate("Instructions", "Do not show again"))
        self.label.setText(_translate("Instructions", "<html><head/><body><p align=\"justify\"><span style=\" font-size:10pt;\">Welcome to the label machiene. </span></p><p align=\"justify\"><span style=\" font-size:10pt;\">Please classify the pictures you will be shown! </span></p><p align=\"justify\"><span style=\" font-size:10pt;\">Use the </span><span style=\" font-size:10pt; font-weight:600;\">arrow keys</span></p><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Right arrow: Move file to &quot;positive&quot; folder.</span></li><li align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Left arrow: Move file to &quot;negative&quot; folder.</span></li><li align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Down arrow: Move file to &quot;other&quot; folder.</span></li></ul><p align=\"justify\"><span style=\" font-size:10pt;\">Use the </span><span style=\" font-size:10pt; font-weight:600;\">space bar</span><span style=\" font-size:10pt;\"> to undo the previous choice. </span></p><p align=\"justify\"><span style=\" font-size:10pt;\">Use the symbol in the top right corner to </span><span style=\" font-size:10pt; font-weight:600;\">save</span><span style=\" font-size:10pt;\"> a name.</span></p><p align=\"justify\"><span style=\" font-size:10pt;\">Use the symbol in the bottom right corner to toggle </span><span style=\" font-size:10pt; font-weight:600;\">color</span><span style=\" font-size:10pt;\">.<br/></span></p><p align=\"justify\"><br/></p></body></html>"))
        self.heading.setText(_translate("Instructions", "<html><head/><body><p align=\"center\"><span style=\" font-size:xx-large; font-weight:600;\">Instructions</span></p></body></html>"))
        self.continue_button.setText(_translate("Instructions", "Specify folders"))

