from generated_ui.FPPaneNameInput import *
from PyQt5.QtWidgets import *

class MyFPPaneNameDialog(Ui_FPPaneNameInputWindow):
    def __init__(self, window):
        self.setupUi(window)
        self.fpInputBox.selectAll()
        self.fpInputBox.setFocus()

        self.buttonBox.buttons()[0].setDisabled(True)
        self.fpInputBox.textChanged.connect(self.nonEmptyField)
        
        self.buttonBox.accepted.connect(self.createPane)
    
    def nonEmptyField(self):
        if len(self.fpInputBox.text()) > 0:
            self.buttonBox.buttons()[0].setDisabled(False)
        if len(self.fpInputBox.text()) == 0:
            self.buttonBox.buttons()[0].setDisabled(True)
    
    def createPane(self):
        self.fpPaneName = self.fpInputBox.text()
        
    def getPaneName(self):
        return self.fpPaneName