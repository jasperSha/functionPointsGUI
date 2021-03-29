from generated_ui.dev_ui.tcfWindow import *
from PyQt5.QtWidgets import *

import copy

class MyTCFWindow(QDialog, Ui_TCFWindow):
    def __init__(self, window, tcfFactors: list):
        QDialog.__init__(self, window)
        self.setupUi(window)

        #setting from prior values
        self.prevFactors = copy.deepcopy(tcfFactors)
        self.tcfFactors = copy.deepcopy(tcfFactors)
        self.currFactors = copy.deepcopy(tcfFactors)

        self.totalFactors = 0

        self.weights = [
            2.0,
            1.0,
            1.0,
            1.0,
            1.0,
            0.5,
            0.5,
            2.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
        ]



        items = (self.inputItems.itemAt(i).widget() for i in range(self.inputItems.count()))
        for i, widget in enumerate(items):
            widget.setCurrentText(str(int(tcfFactors[i])))
            widget.activated.connect(self.tcf_input)
        
        outItems = (self.outputItems.itemAt(i).widget() for i in range(self.outputItems.count()))
        for i, widget in enumerate(outItems):
            weightedFactor = tcfFactors[i] * self.weights[i]
            self.totalFactors += weightedFactor
            widget.setText(str(weightedFactor))
        
        self.buttonBox.accepted.connect(self.accept_tcf)
        self.buttonBox.rejected.connect(self.cancel_tcf)

    def accept_tcf(self):
        items = (self.inputItems.itemAt(i).widget() for i in range(self.inputItems.count()))
        for i, widget in enumerate(items):
            factor = widget.currentText()
            self.tcfFactors[i] = float(factor)
    
    def cancel_tcf(self):
        items = (self.inputItems.itemAt(i).widget() for i in range(self.inputItems.count()))
        for i, widget in enumerate(items):
            widget.setCurrentText(str(self.prevFactors[i]))
            self.tcfFactors[i] = self.prevFactors[i]
        
    
    def tcf_input(self):
        button = self.tcfwin.sender()
        inputIndex = int(button.objectName()[1:-5]) #retrieves the t int as a proxy for weight index

        weightedFactor = float(button.currentText()) * self.weights[inputIndex-1]

        # get matching output label name
        tcfOutName = "t" + str(inputIndex) + "out"
        items = (self.outputItems.itemAt(i).widget() for i in range(self.outputItems.count()))
        for i, widget in enumerate(items):
            if widget.objectName() == tcfOutName:
                self.tcfFactors[i] = int(button.currentText())
                widget.setText(str(weightedFactor))

    def retrieve_tcf(self):
        totalFactors = 0
        outItems = (self.outputItems.itemAt(i).widget() for i in range(self.outputItems.count()))
        for item in outItems:
            totalFactors += float(item.text())

        self.tcf = round(0.6 + (0.01 * totalFactors), 3)
        return self.tcf

    def get_tcfFactors(self):
        return self.tcfFactors
    
