from generated_ui.prod_ui.ValueAdjustmentFactorsWindow import *
from PyQt5.QtWidgets import *


class MyValueAdjustmentFactorsWindow(QDialog, Ui_ValueAdjustmentFactorsWindow):
    def __init__(self, window, vaf):
        QDialog.__init__(self, window)
        self.setupUi(window)

        # these are copies only after one level (the elements share mem address until mutated)
        self.prevVAF = list(vaf)
        self.currVAF = list(vaf)
        
        self.first.setCurrentText(str(vaf[0]))
        self.second.setCurrentText(str(vaf[1]))
        self.third.setCurrentText(str(vaf[2]))
        self.fourth.setCurrentText(str(vaf[3]))
        self.fifth.setCurrentText(str(vaf[4]))
        self.sixth.setCurrentText(str(vaf[5]))
        self.seventh.setCurrentText(str(vaf[6]))
        self.eighth.setCurrentText(str(vaf[7]))
        self.ninth.setCurrentText(str(vaf[8]))
        self.tenth.setCurrentText(str(vaf[9]))
        self.eleventh.setCurrentText(str(vaf[10]))
        self.twelfth.setCurrentText(str(vaf[11]))
        self.thirteenth.setCurrentText(str(vaf[12]))
        self.fourteenth.setCurrentText(str(vaf[13]))

        self.first.activated.connect(self.fp_input)
        self.second.activated.connect(self.fp_input)
        self.third.activated.connect(self.fp_input)
        self.fourth.activated.connect(self.fp_input)
        self.fifth.activated.connect(self.fp_input)
        self.sixth.activated.connect(self.fp_input)
        self.seventh.activated.connect(self.fp_input)
        self.eighth.activated.connect(self.fp_input)
        self.ninth.activated.connect(self.fp_input)
        self.tenth.activated.connect(self.fp_input)
        self.eleventh.activated.connect(self.fp_input)
        self.twelfth.activated.connect(self.fp_input)
        self.thirteenth.activated.connect(self.fp_input)
        self.fourteenth.activated.connect(self.fp_input)
        
        self.buttonBox.rejected.connect(self.cancel)

        self.buttonBox.accepted.connect(self.vafWin.accept)
        self.buttonBox.rejected.connect(self.vafWin.reject)
        

    def get_newVAF(self):
        return self.currVAF
    
    def get_oldVAF(self):
        return self.prevVAF
    
    def cancel(self):
        self.first.setCurrentText(str(self.prevVAF[0]))
        self.second.setCurrentText(str(self.prevVAF[1]))
        self.third.setCurrentText(str(self.prevVAF[2]))
        self.fourth.setCurrentText(str(self.prevVAF[3]))
        self.fifth.setCurrentText(str(self.prevVAF[4]))
        self.sixth.setCurrentText(str(self.prevVAF[5]))
        self.seventh.setCurrentText(str(self.prevVAF[6]))
        self.eighth.setCurrentText(str(self.prevVAF[7]))
        self.ninth.setCurrentText(str(self.prevVAF[8]))
        self.tenth.setCurrentText(str(self.prevVAF[9]))
        self.eleventh.setCurrentText(str(self.prevVAF[10]))
        self.twelfth.setCurrentText(str(self.prevVAF[11]))
        self.thirteenth.setCurrentText(str(self.prevVAF[12]))
        self.fourteenth.setCurrentText(str(self.prevVAF[13]))


    def fp_input(self):
        # # must set self.wftab = WeightFactorsTab in UI file manually for this to work
        button = self.vafWin.sender()
        buttonName = button.objectName()

        if buttonName == 'first':
            self.index0 = int(button.currentText())
            self.currVAF[0] = self.index0
        elif buttonName == 'second':
            self.index1 = int(button.currentText())
            self.currVAF[1] = self.index1
        elif buttonName == 'third':
            self.index2 = int(button.currentText())
            self.currVAF[2] = self.index2
        elif buttonName == 'fourth':
            self.index3 = int(button.currentText())
            self.currVAF[3] = self.index3
        elif buttonName == 'fifth':
            self.index4 = int(button.currentText())
            self.currVAF[4] = self.index4
        elif buttonName == 'sixth':
            self.index5 = int(button.currentText())
            self.currVAF[5] = self.index5
        elif buttonName == 'seventh':
            self.index6 = int(button.currentText())
            self.currVAF[6] = self.index6
        elif buttonName == 'eighth':
            self.index7 = int(button.currentText())
            self.currVAF[7] = self.index7
        elif buttonName == 'ninth':
            self.index8 = int(button.currentText())
            self.currVAF[8] = self.index8
        elif buttonName == 'tenth':
            self.index9 = int(button.currentText())
            self.currVAF[9] = self.index9
        elif buttonName == 'eleventh':
            self.index10 = int(button.currentText())
            self.currVAF[10] = self.index10
        elif buttonName == 'twelfth':
            self.index11 = int(button.currentText())
            self.currVAF[11] = self.index11
        elif buttonName == 'thirteenth':
            self.index12 = int(button.currentText())
            self.currVAF[12] = self.index12
        elif buttonName == 'fourteenth':
            self.index13 = int(button.currentText())
            self.currVAF[13] = self.index13
            