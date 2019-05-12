# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'snippet.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1219, 771)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setScaledContents(True)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.textEditSnippet = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditSnippet.setGeometry(QtCore.QRect(540, 70, 641, 621))
        self.textEditSnippet.setObjectName("textEditSnippet")
        self.languageList = QtWidgets.QListWidget(self.centralwidget)
        self.languageList.setGeometry(QtCore.QRect(10, 70, 141, 621))
        self.languageList.setObjectName("languageList")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(510, 700, 91, 31))
        self.addButton.setObjectName("addButton")
        self.changeButton = QtWidgets.QPushButton(self.centralwidget)
        self.changeButton.setGeometry(QtCore.QRect(620, 700, 91, 31))
        self.changeButton.setObjectName("changeButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(540, 30, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(True)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.folderList = QtWidgets.QListWidget(self.centralwidget)
        self.folderList.setGeometry(QtCore.QRect(160, 70, 171, 621))
        self.folderList.setObjectName("folderList")
        self.snippetList = QtWidgets.QListWidget(self.centralwidget)
        self.snippetList.setGeometry(QtCore.QRect(340, 70, 171, 621))
        self.snippetList.setObjectName("snippetList")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 10, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setScaledContents(True)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(340, 10, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setScaledContents(True)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Programming Languages"))
        self.addButton.setText(_translate("MainWindow", "Add snippet"))
        self.changeButton.setText(_translate("MainWindow", "changeSnippet"))
        self.label_2.setText(_translate("MainWindow", "Your Snippet"))
        self.label_3.setText(_translate("MainWindow", "Folder"))
        self.label_4.setText(_translate("MainWindow", "Snippets"))


