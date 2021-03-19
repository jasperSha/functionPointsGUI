from generated_ui.NewProjectWindow import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp
from PyQt5 import QtGui


class MyNewProjectWindow(Ui_NewProjectWindow):
    def __init__(self, window):
        self.setupUi(window)
        self.projectParams = {}

        self.projectNameBox.selectAll()
        self.projectNameBox.setFocus()

        self.buttonBox.buttons()[0].setDisabled(True)
        self.projectNameBox.textChanged.connect(self.nonEmptyField)
        
        self.buttonBox.accepted.connect(self.create_new)
    
    def nonEmptyField(self):
        if len(self.projectNameBox.text()) > 0:
            self.buttonBox.buttons()[0].setDisabled(False)
        if len(self.projectNameBox.text()) == 0:
            self.buttonBox.buttons()[0].setDisabled(True)
        
    
    def create_new(self):
        self.projectParams['projectName'] = self.projectNameBox.text()
        self.projectParams['productName'] = self.productNameBox.toPlainText()
        self.projectParams['creator'] = self.creatorNameBox.toPlainText()
        self.projectParams['comments'] = self.commentBox.toPlainText()
        
    def getNewProjectParams(self):
        return self.projectParams
    
