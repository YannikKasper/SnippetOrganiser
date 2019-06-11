from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QListWidget, QListWidgetItem, QMainWindow, QDialog, QMessageBox
from loginGui import Ui_Dialog
from PyQt5 import QtCore
import os
import snippetApi as api
import json

class Login(QDialog):
    

    def __init__(self,parent):
        super().__init__()
        self.parent = parent
        self.design = Ui_Dialog()
        self.design.setupUi(self)
        self.show()
        self.design.buttonBox.accepted.connect(self.checkConnection)

    def checkConnection(self):
        server = self.design.textServer.text()
        token = self.design.textToken.text()
        res = api.checkConnection(server,token)
        if res is not False:
            with open("C:\\ProgramData\\snippetOrganiser\\config.txt","w") as conf:
                json.dump({"server":server,"token":token},conf)
            api.readConfig()
            self.close()
            self.parent.refresh()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Wrong Server or token")
            msg.setWindowTitle("Wrong Server or token")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.show()
            msg.exec_()

    def writeConfig(self):
        print("Test")
        
