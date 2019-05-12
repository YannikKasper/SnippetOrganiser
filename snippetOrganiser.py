import json
import sys
import os
from snippetGui import Ui_MainWindow
import snippetApi as api
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QListWidget, QListWidgetItem, QMainWindow, QDialog, QMessageBox
from PyQt5.QtCore import QTimer
import os
import pyperclip
from addSnippet import Ui_Dialog


class Form(QMainWindow):
    def __init__(self):
        self.snippets = {}
        self.snippetKeys = []
        self.selectedLanguage = ""
        self.selectedFolder = ""
        self.selectedSnippet = ""
        self.selectedSnippetID = ""
        super().__init__()
        self.timer = QTimer()
        self.timer.setInterval(250)
        self.timer.setSingleShot(True)
        self.snippetOrganiserform = Ui_MainWindow()
        self.snippetOrganiserform.setupUi(self)
        self.show()
        self.refresh()
        

    def acceptSnippet(self):
        if "." in self.dialog.textFileName.toPlainText():
            api.postSnippet(self.dialog.textTitle.toPlainText(),
                            self.dialog.textFileName.toPlainText(),
                            self.dialog.textFolder.toPlainText(),
                            self.dialog.textDescription.toPlainText(),
                            self.dialog.textSnippet.toPlainText())
            self.refresh()
            self.addForm.accept()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Plase enter a valid file type")
            msg.setWindowTitle("Invalid file")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.show()
            msg.exec_()


    
    def clipClicked(self):
        pyperclip.copy(self.snippetOrganiserform.textSnippet.toPlainText())

    def addSnippet(self,task):
        self.addForm = QDialog()
        self.dialog = Ui_Dialog()
        self.dialog.setupUi(self.addForm)
        self.addForm.show()
        self.dialog.buttonBox.accepted.connect(self.acceptSnippet)
    
    def deleteSnippet(self):
        api.deleteSnippet(self.snippets[self.selectedLanguage][self.selectedFolder][self.selectedSnippet])
        self.refresh()

    def languageClicked(self, item):
        item = QListWidgetItem(item)
        lang = item.text()
        self.snippetOrganiserform.snippetList.clear()
        self.snippetOrganiserform.folderList.clear()
        self.selectedLanguage = lang
        folderList=[]
        for folder in self.snippets[lang]:
            if folder not in folderList:
                folderList.append(folder)
                self.snippetOrganiserform.folderList.addItem(QListWidgetItem(folder))

    def folderClicked(self, item):
        item = QListWidgetItem(item)
        snippetName = ""
        self.snippetOrganiserform.snippetList.clear()
        self.selectedFolder = item.text()
        for snippetName in self.snippets[self.selectedLanguage][item.text()]:
            self.snippetOrganiserform.snippetList.addItem(
                QListWidgetItem(snippetName))

    def snippetClickDetection(self, item):
        if not self.timer.isActive():
            self.timer.start()
            self.clickedItem = item
            return
        else:
            self.timer.stop()
            self.addForm = QDialog()
            self.dialog = Ui_Dialog()
            self.dialog.setupUi(self.addForm)
            self.addForm.show()
            self.dialog.buttonBox.accepted.connect(self.acceptSnippet)
            
   
    def singleClick(self):
        snippetID = self.snippets[self.selectedLanguage][self.selectedFolder][self.clickedItem.text()]
        self.snippetOrganiserform.textEditSnippet.setText(api.singleSnippetApi(snippetID))
        self.selectedSnippet =self.clickedItem.text()
        self.selectedSnippetID = snippetID

    def refresh(self):
        self.snippets = api.snippetAPI()
        self.snippetKeys = self.snippets.keys()
      
        self.snippetOrganiserform.languageList.clear()
        self.snippetOrganiserform.folderList.clear()
        self.snippetOrganiserform.snippetList.clear()
        for snippetKey in self.snippetKeys:
            item = QListWidgetItem(snippetKey)
            self.snippetOrganiserform.languageList.addItem(item)

        self.snippetOrganiserform.languageList.itemClicked.connect(self.languageClicked)
        self.snippetOrganiserform.folderList.itemClicked.connect(self.folderClicked)
        self.snippetOrganiserform.snippetList.itemClicked.connect(self.snippetClickDetection)
        self.timer.timeout.connect(self.singleClick)
        self.snippetOrganiserform.clipButton.clicked.connect(self.clipClicked)
        self.snippetOrganiserform.addButton.clicked.connect(self.addSnippet)
        self.snippetOrganiserform.btnDelete.clicked.connect(self.deleteSnippet)


if __name__ == "__main__":
    app = QApplication([])
    form = Form()
    sys.exit(app.exec())
