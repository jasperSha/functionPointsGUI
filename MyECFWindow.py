from generated_ui.prod_ui.ecfWindow import *
from PyQt5.QtWidgets import *
import copy

class MyECFWindow(QDialog, Ui_ECFWindow):
    def __init__(self, window, ecfFactors: list):
        QDialog.__init__(self, window)
        self.setupUi(window)

        self.prevFactors = copy.deepcopy(ecfFactors)
        self.ecfFactors = copy.deepcopy(ecfFactors)
        self.currFactors = copy.deepcopy(ecfFactors)

        self.totalFactors = 0

        self.weights = [
            1.5,
            0.5,
            1.0,
            0.5,
            1.0,
            2.0,
            -1.0,
            2.0,
        ]

        items = (self.inputItems.itemAt(i).widget() for i in range(self.inputItems.count()))
        for i, widget in enumerate(items):
            widget.setCurrentText(str(int(ecfFactors[i])))
            widget.activated.connect(self.ecf_input)
        
        outItems = (self.outputItems.itemAt(i).widget() for i in range(self.outputItems.count()))
        for i, widget in enumerate(outItems):
            weightedFactor = ecfFactors[i] * self.weights[i]
            self.totalFactors += weightedFactor
            widget.setText(str(weightedFactor))
        
        self.buttonBox.accepted.connect(self.accept_ecf)
        self.buttonBox.rejected.connect(self.cancel_ecf)

    def accept_ecf(self):
        items = (self.inputItems.itemAt(i).widget() for i in range(self.inputItems.count()))
        for i, widget in enumerate(items):
            factor = widget.currentText()
            self.ecfFactors[i] = float(factor)
    
    def cancel_ecf(self):
        items = (self.inputItems.itemAt(i).widget() for i in range(self.inputItems.count()))
        for i, widget in enumerate(items):
            widget.setCurrentText(str(self.prevFactors[i]))
            self.ecfFactors[i] = self.prevFactors[i]

    def ecf_input(self):
        button = self.ecfwin.sender()
        inputIndex = int(button.objectName()[1:-2])  #retrieves the t int as a proxy for weight index

        weightedFactor = float(button.currentText()) * self.weights[inputIndex-1]

        # get matching output label name
        tcfOutName = "e" + str(inputIndex) + "out"
        items = (self.outputItems.itemAt(i).widget() for i in range(self.outputItems.count()))
        for i, widget in enumerate(items):
            if widget.objectName() == tcfOutName:
                self.ecfFactors[i] = int(button.currentText())
                widget.setText(str(weightedFactor))


    def retrieve_ecf(self):
        totalFactors = 0
        outItems = (self.outputItems.itemAt(i).widget() for i in range(self.outputItems.count()))
        for item in outItems:
            totalFactors += float(item.text())

        # self.totalFactors = totalFactors
        self.ecf = round(1.4 + (-0.03 * totalFactors), 3)
        return self.ecf

    def get_ecfFactors(self):
        return self.ecfFactors

