from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QListWidget, QListWidgetItem, QMainWindow, QDialog, QMessageBox
from addSnippetGui import Ui_Dialog
import snippetApi as api
from style import getStyleAll
import PyQt5.QtCore
class Dialog(QDialog):
    def __init__(self,id=None,parent=None):
        super().__init__()
        self.design = Ui_Dialog()
        self.design.setupUi(self)
        self.parent = parent
        self.id=id
        print(parent.generalFolders)
        self.design.textFolder.addItems(parent.generalFolders)
        ##with open("style.stylesheet") as sh:
            #self.setStyleSheet(sh.read())
        self.setStyleSheet(getStyleAll())
        self.show()
        self.design.buttonBox.accepted.connect(self.acceptSnippet)
        if id is not None:
            self.fillBoxes(id)
        else:
            self.design.textFolder.setCurrentText("")

    def closeEvent(self, QCloseEvent):
        self.parent.refresh()

    def acceptSnippet(self):
        if "." in self.design.textFileName.toPlainText():
            if self.id==None:
                api.postSnippet(self.design.textTitle.toPlainText(),
                                self.design.textFileName.toPlainText(),
                                self.design.textFolder.currentText(),
                                self.design.textDescription.toPlainText(),
                                self.design.textSnippet.toPlainText())
            else:
                api.updateSnippet(self.id,
                                self.design.textTitle.toPlainText(),
                                self.design.textFileName.toPlainText(),
                                self.design.textFolder.currentText(),
                                self.design.textDescription.toPlainText(),
                                self.design.textSnippet.toPlainText())
            self.parent.refresh()
            self.accept()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Plase enter a valid file type")
            msg.setWindowTitle("Invalid file")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.show()
            msg.exec_()

    def fillBoxes(self, id):
      
        snippet = api.singleSnippetMeta(id)
        raw = api.singleSnippetApi(id)
        self.design.textSnippet.setPlainText(raw)
        index = self.design.textFolder.findText(snippet["description"].split("\n")[0], PyQt5.QtCore.Qt.MatchFixedString)
        if index >= 0:
            self.design.textFolder.setCurrentIndex(index)
        self.design.textTitle.setPlainText(snippet["title"])
        if "\n" in snippet["description"]:
            self.design.textDescription.setPlainText(snippet["description"].split("\n",1)[1])
        self.design.textFileName.setPlainText(snippet["file_name"])
    