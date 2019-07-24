# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'specify_folders.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Folders(object):
    def setupUi(self, Folders):
        Folders.setObjectName("Folders")
        Folders.resize(400, 425)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Folders.sizePolicy().hasHeightForWidth())
        Folders.setSizePolicy(sizePolicy)
        Folders.setMinimumSize(QtCore.QSize(400, 425))
        Folders.setStyleSheet("QWidget#Folders{\n"
" background-color: white\n"
"}\n"
"QLabel#heading{\n"
" color: rgb(181, 92, 149)\n"
"}\n"
"QPushButton{\n"
"    border: 2px  solid  black;\n"
"}\n"
"QToolButton{\n"
"    border: 2px  solid   rgb(181, 92, 149);\n"
"     background-color: white;\n"
"    font-size: 10pt;\n"
"    color:   rgb(140, 60, 114);\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Folders)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.remember_checkBox = QtWidgets.QCheckBox(Folders)
        self.remember_checkBox.setObjectName("remember_checkBox")
        self.gridLayout.addWidget(self.remember_checkBox, 4, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 6, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 3, 1, 1)
        self.heading = QtWidgets.QLabel(Folders)
        self.heading.setMinimumSize(QtCore.QSize(0, 80))
        self.heading.setMaximumSize(QtCore.QSize(16777215, 100))
        self.heading.setObjectName("heading")
        self.gridLayout.addWidget(self.heading, 0, 0, 1, 4)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.source_label = QtWidgets.QLabel(Folders)
        self.source_label.setObjectName("source_label")
        self.gridLayout_2.addWidget(self.source_label, 1, 0, 1, 1)
        self.neg_label = QtWidgets.QLabel(Folders)
        self.neg_label.setObjectName("neg_label")
        self.gridLayout_2.addWidget(self.neg_label, 7, 0, 1, 1)
        self.line_edit_pos = QtWidgets.QLineEdit(Folders)
        self.line_edit_pos.setObjectName("line_edit_pos")
        self.gridLayout_2.addWidget(self.line_edit_pos, 6, 0, 1, 1)
        self.line_edit_source = QtWidgets.QLineEdit(Folders)
        self.line_edit_source.setMinimumSize(QtCore.QSize(320, 0))
        self.line_edit_source.setObjectName("line_edit_source")
        self.gridLayout_2.addWidget(self.line_edit_source, 3, 0, 1, 1)
        self.pos_label = QtWidgets.QLabel(Folders)
        self.pos_label.setObjectName("pos_label")
        self.gridLayout_2.addWidget(self.pos_label, 5, 0, 1, 1)
        self.other_label = QtWidgets.QLabel(Folders)
        self.other_label.setObjectName("other_label")
        self.gridLayout_2.addWidget(self.other_label, 9, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 12, 1, 1, 1)
        self.line_edit_other = QtWidgets.QLineEdit(Folders)
        self.line_edit_other.setObjectName("line_edit_other")
        self.gridLayout_2.addWidget(self.line_edit_other, 11, 0, 1, 1)
        self.line_edit_neg = QtWidgets.QLineEdit(Folders)
        self.line_edit_neg.setObjectName("line_edit_neg")
        self.gridLayout_2.addWidget(self.line_edit_neg, 8, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 4, 0, 1, 1)
        self.source_fc_button = QtWidgets.QToolButton(Folders)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.source_fc_button.sizePolicy().hasHeightForWidth())
        self.source_fc_button.setSizePolicy(sizePolicy)
        self.source_fc_button.setMinimumSize(QtCore.QSize(10, 0))
        self.source_fc_button.setMaximumSize(QtCore.QSize(25, 20))
        self.source_fc_button.setObjectName("source_fc_button")
        self.gridLayout_2.addWidget(self.source_fc_button, 3, 1, 1, 1)
        self.neg_fc_button = QtWidgets.QToolButton(Folders)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.neg_fc_button.sizePolicy().hasHeightForWidth())
        self.neg_fc_button.setSizePolicy(sizePolicy)
        self.neg_fc_button.setMinimumSize(QtCore.QSize(10, 0))
        self.neg_fc_button.setMaximumSize(QtCore.QSize(25, 20))
        self.neg_fc_button.setObjectName("neg_fc_button")
        self.gridLayout_2.addWidget(self.neg_fc_button, 8, 1, 1, 1)
        self.other_fc_button = QtWidgets.QToolButton(Folders)
        self.other_fc_button.setMaximumSize(QtCore.QSize(25, 20))
        self.other_fc_button.setObjectName("other_fc_button")
        self.gridLayout_2.addWidget(self.other_fc_button, 11, 1, 1, 1)
        self.pos_fc_button = QtWidgets.QToolButton(Folders)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pos_fc_button.sizePolicy().hasHeightForWidth())
        self.pos_fc_button.setSizePolicy(sizePolicy)
        self.pos_fc_button.setMinimumSize(QtCore.QSize(10, 0))
        self.pos_fc_button.setMaximumSize(QtCore.QSize(25, 20))
        self.pos_fc_button.setObjectName("pos_fc_button")
        self.gridLayout_2.addWidget(self.pos_fc_button, 6, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 2, 0, 1, 4)
        self.start_button = QtWidgets.QToolButton(Folders)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(56)
        sizePolicy.setHeightForWidth(self.start_button.sizePolicy().hasHeightForWidth())
        self.start_button.setSizePolicy(sizePolicy)
        self.start_button.setMinimumSize(QtCore.QSize(110, 0))
        self.start_button.setObjectName("start_button")
        self.gridLayout.addWidget(self.start_button, 6, 1, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Folders)
        QtCore.QMetaObject.connectSlotsByName(Folders)

    def retranslateUi(self, Folders):
        _translate = QtCore.QCoreApplication.translate
        Folders.setWindowTitle(_translate("Folders", "Form"))
        self.remember_checkBox.setText(_translate("Folders", "Remember choice"))
        self.heading.setText(_translate("Folders", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Please choose folders</span></p></body></html>"))
        self.source_label.setText(_translate("Folders", "<html><head/><body><p><span style=\" font-size:10pt;\">Source:</span></p></body></html>"))
        self.neg_label.setText(_translate("Folders", "<html><head/><body><p><span style=\" font-size:10pt;\">Negative</span></p></body></html>"))
        self.pos_label.setText(_translate("Folders", "<html><head/><body><p><span style=\" font-size:10pt;\">Positive:</span></p></body></html>"))
        self.other_label.setText(_translate("Folders", "<html><head/><body><p><span style=\" font-size:10pt;\">Other:</span></p></body></html>"))
        self.source_fc_button.setText(_translate("Folders", "..."))
        self.neg_fc_button.setText(_translate("Folders", "..."))
        self.other_fc_button.setText(_translate("Folders", "..."))
        self.pos_fc_button.setText(_translate("Folders", "..."))
        self.start_button.setText(_translate("Folders", "Start"))

