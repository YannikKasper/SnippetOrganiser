# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addSnippet.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1124, 679)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(780, 50, 181, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.textAddSnippt = QtWidgets.QPlainTextEdit(Dialog)
        self.textAddSnippt.setGeometry(QtCore.QRect(20, 50, 641, 601))
        self.textAddSnippt.setObjectName("textAddSnippt")
        self.textFileName = QtWidgets.QTextEdit(Dialog)
        self.textFileName.setGeometry(QtCore.QRect(690, 160, 411, 31))
        self.textFileName.setObjectName("textFileName")
        self.textDescription = QtWidgets.QTextEdit(Dialog)
        self.textDescription.setGeometry(QtCore.QRect(690, 330, 401, 321))
        self.textDescription.setObjectName("textDescription")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 10, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(690, 110, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(690, 280, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.textFileName_2 = QtWidgets.QTextEdit(Dialog)
        self.textFileName_2.setGeometry(QtCore.QRect(690, 240, 411, 31))
        self.textFileName_2.setObjectName("textFileName_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(690, 200, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add Snippet"))
        self.label.setText(_translate("Dialog", "Snippet"))
        self.label_2.setText(_translate("Dialog", "File Name"))
        self.label_3.setText(_translate("Dialog", "Description"))
        self.label_4.setText(_translate("Dialog", "Folder"))


