import json
import sys
import os
from snippetGui import Ui_MainWindow
import snippetApi as api
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QListWidget, QListWidgetItem, QMainWindow, QDialog, QMessageBox
from PyQt5.QtCore import QTimer
import os
import pyperclip
from addSnippetGui import Ui_Dialog
from addSnippet import Dialog
from style import getStyle


class Form(QMainWindow):
    def __init__(self):
        self.snippets = {}
        self.snippetKeys = []
        self.selectedLanguage = ""
        self.selectedFolder = ""
        self.selectedSnippet = ""
        self.selectedSnippetID = ""
        self.selectedList = "language"
        super().__init__()
        self.timer = QTimer()
        self.timer.setInterval(250)
        self.timer.setSingleShot(True)
        self.snippetOrganiserform = Ui_MainWindow()
        self.snippetOrganiserform.setupUi(self)
        self.setStyleSheet(getStyle())
        self.show()
        self.snippetOrganiserform.languageList.itemClicked.connect(self.listClicked)
        self.timer.timeout.connect(self.singleClick)
        self.snippetOrganiserform.clipButton.clicked.connect(self.clipClicked)
        self.snippetOrganiserform.addButton.clicked.connect(self.addSnippet)
        self.snippetOrganiserform.btnDelete.clicked.connect(self.deleteSnippet)
        self.snippetOrganiserform.btnBack.clicked.connect(self.back)
        self.refresh()
        
    def back(self):
        if self.selectedList =="folder":
            self.selectedList = "language"
            self.snippetOrganiserform.btnBack.setVisible(False)
        elif self.selectedList == "snippet":
            self.selectedList = "folder"
        self.showList()

    def clipClicked(self):
        pyperclip.copy(self.snippetOrganiserform.textSnippet.toPlainText())

    def addSnippet(self,task):
        self.dialog = Dialog(None,self)
     
    def deleteSnippet(self):
        api.deleteSnippet(self.snippets[self.selectedLanguage][self.selectedFolder][self.selectedSnippet]["id"])
        self.refresh()

    def listClicked(self,item):

        text = item.text()
        
        if self.selectedList =="language":
            self.selectedList = "folder"
            self.selectedLanguage= text
            self.showList()
            
        elif self.selectedList =="folder":
            self.selectedFolder = text
            self.selectedList="snippet"
            self.showList()

        elif self.selectedList =="snippet":
            self.snippetClickDetection(text)

    def snippetClickDetection(self, item):
        if not self.timer.isActive():
            self.timer.start()
            print(item)
            self.clickedItem = item
            return
        else:
            self.timer.stop()
            self.dialog = Dialog(self.snippets[self.selectedLanguage][self.selectedFolder][item]["id"],self)
            
   
    def singleClick(self):
        snippetID = self.snippets[self.selectedLanguage][self.selectedFolder][self.clickedItem]["id"]
        self.snippetOrganiserform.textEditSnippet.setText(api.singleSnippetApi(snippetID))
        if "\n" in self.snippets[self.selectedLanguage][self.selectedFolder][self.clickedItem]["description"]:
            self.snippetOrganiserform.textDescription.setText(self.snippets[self.selectedLanguage][self.selectedFolder][self.clickedItem]["description"].split("\n",1)[1])
        self.selectedSnippet =self.clickedItem
        self.selectedSnippetID = snippetID
        self.snippetOrganiserform.labelSnippetPath.setText(self.selectedLanguage + "\\" +self.selectedFolder +"\\" + self.selectedSnippet)
 

    def refresh(self):
        self.snippets = api.snippetAPI()
        self.snippetKeys = self.snippets.keys()
        self.snippetOrganiserform.textDescription.clear()
        self.snippetOrganiserform.textEditSnippet.clear()
        self.selectedList="language"
        self.snippetOrganiserform.labelSnippetPath.clear()
        self.showList()


    def showList(self):
        self.snippetOrganiserform.languageList.clear()

        if self.selectedList=="language":
            self.snippetOrganiserform.label.setText("Programming Language")
            for snippetKey in self.snippetKeys:
                item = QListWidgetItem(snippetKey)
                self.snippetOrganiserform.languageList.addItem(item)
                self.snippetOrganiserform.languageList.sortItems()

        elif self.selectedList=="folder":
            
            self.snippetOrganiserform.label.setText("Folder")
            self.snippetOrganiserform.btnBack.setVisible(True)
            folderList=[]
            for folder in self.snippets[self.selectedLanguage]:
                if folder not in folderList:
                    folderList.append(folder)
                    self.snippetOrganiserform.languageList.addItem(QListWidgetItem(folder))

        elif self.selectedList=="snippet":
            self.snippetOrganiserform.label.setText("Snippets")
            for snippetName in self.snippets[self.selectedLanguage][self.selectedFolder]:
                self.snippetOrganiserform.languageList.addItem(QListWidgetItem(snippetName))

if __name__ == "__main__":
    app = QApplication([])
    form = Form()
    sys.exit(app.exec())
