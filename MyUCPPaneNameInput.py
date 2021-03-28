from generated_ui.dev_ui.UCPPaneNameInput import *
from PyQt5.QtWidgets import *

class MyUCPPaneNameInput(Ui_UCPPaneNameInput):
    def __init__(self, window):
        self.setupUi(window)

        self.ucpinput.selectAll()
        self.ucpinput.setFocus()

        self.acceptreject.buttons()[0].setDisabled(True)
        self.ucpinput.textChanged.connect(self.nonEmptyField)

        self.acceptreject.accepted.connect(self.createPane)

    def nonEmptyField(self):
        if len(self.ucpinput.text()) > 0:
            self.acceptreject.buttons()[0].setDisabled(False)
        if len(self.ucpinput.text()) == 0:
            self.acceptreject.buttons()[0].setDisabled(True)

    def createPane(self):
        self.ucpPaneName = self.ucpinput.text()

    def getPaneName(self):
        return self.ucpPaneName