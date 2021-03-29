from generated_ui.dev_ui.UCPTab import *
from MyTCFWindow import MyTCFWindow
from MyECFWindow import MyECFWindow

from PyQt5.QtWidgets import *

class MyUCPTab(QWidget, Ui_UCPTab):
    def __init__(self, window, pane, loaded=False):
        QWidget.__init__(self, window)
        self.setupUi(window)

        self.paneName = pane.get_ID()

        self.tcfFactors = pane.get_tcfFactors()
        self.ecfFactors = pane.get_ecfFactors()

        self.tcf = pane.get_tcf()
        self.ecf = pane.get_ecf()

        self.uucw = pane.get_uucw()
        self.uaw = pane.get_uaw()

        self.uucwTotal = pane.get_uucwTotal()
        self.uawTotal = pane.get_uawTotal()
        self.uucp = pane.get_uucp()

        self.pf = 20
        self.locucp = 100
        self.locPM = 700

        self.ucp = pane.get_UCP()
        self.estLOC = pane.get_estLOC()
        self.estPM = pane.get_estPM()
        self.estHours = pane.get_estHours()

        if loaded:
            self.pf = pane.get_PF()
            self.locucp = pane.get_locucp()
            self.locPM = pane.get_locPM()
            self.load_data()
        
        self.uucwSimple.valueChanged.connect(self.computeUUCW)
        self.uucwAvg.valueChanged.connect(self.computeUUCW)
        self.uucwComplex.valueChanged.connect(self.computeUUCW)
        
        self.uawSimple.valueChanged.connect(self.computeUAW)
        self.uawAvg.valueChanged.connect(self.computeUAW)
        self.uawComplex.valueChanged.connect(self.computeUAW)

        self.computeTCF.clicked.connect(self.retrieve_TCF)
        self.computeECF.clicked.connect(self.retrieve_ECF)

        self.PFInput.valueChanged.connect(self.compute_PF)
        self.LOCPMInput.valueChanged.connect(self.compute_LOCPM)
        self.LOCUCPInput.valueChanged.connect(self.compute_LOCUCP)

        self.computeFullEst.clicked.connect(self.full_estimate)

    def get_estHours(self):
        return self.estHours
    
    def get_estPM(self):
        return self.estPM
    
    def get_estLOC(self):
        return self.estLOC
    
    def get_UCP(self):
        return self.ucp

    def get_locucp(self):
        return self.locucp
    def get_locPM(self):
        return self.locPM
    
    def get_PF(self):
        return self.pf
    
    def get_uucp(self):
        return self.uucp

    def get_uawTotal(self):
        return self.uawTotal
    
    def get_uucwTotal(self):
        return self.uucwTotal

    def get_uaw(self):
        return self.uaw

    def get_tcf(self):
        return self.tcf
    
    def get_ecf(self):
        return self.ecf
    
    def get_uucw(self):
        return self.uucw
    
    def get_ecfFactors(self):
        return self.ecfFactors

    def get_tcfFactors(self):
        return self.tcfFactors

    def get_ID(self):
        return self.paneName

    def is_ucp_pane(self):
        return True

    def full_estimate(self):
        uucp = self.uucp
        tcf = self.tcf
        ecf = self.ecf
        pf = self.pf

        self.ucp = round(tcf * ecf * uucp, 3)
        self.totalUCPOutput.setText(str(self.ucp))

        self.estHours = round(self.ucp * pf, 3)
        self.estHoursOutput.setText(str(self.estHours))

        self.estLOC = round(self.ucp * self.locucp, 3)
        self.estLOCOutput.setText(str(self.estLOC))

        self.estPM = round(self.estLOC / self.locPM, 3)
        self.estPMOutput.setText(str(self.estPM))

    def compute_LOCPM(self):
        v = self.LOCPMInput.value()
        self.locPM = v
        
    def compute_LOCUCP(self):
        v = self.LOCUCPInput.value()
        self.locucp = v
    
    def compute_PF(self):
        v = self.PFInput.value()
        self.pf = v

    def load_data(self):
        self.uucwSimple.setValue(self.uucw[0])
        self.uucwAvg.setValue(self.uucw[1])
        self.uucwComplex.setValue(self.uucw[2])
        self.uucwOutput.setText(str(self.uucwTotal))

        self.uawSimple.setValue(self.uaw[0])
        self.uawAvg.setValue(self.uaw[1])
        self.uawComplex.setValue(self.uaw[2])
        self.uawOutput.setText(str(self.uawTotal))

        uucp = self.uucwTotal + self.uawTotal
        self.uucpOutput.setText(str(uucp))

        self.tcfOutput.setText(str(self.tcf))
        self.ecfOutput.setText(str(self.ecf))

        self.PFInput.setValue(self.pf)
        self.LOCPMInput.setValue(self.locPM)
        self.LOCUCPInput.setValue(self.locucp)

        self.totalUCPOutput.setText(str(self.ucp))
        self.estHoursOutput.setText(str(self.estHours))
        self.estLOCOutput.setText(str(self.estLOC))
        self.estPMOutput.setText(str(self.estPM))
    
    def retrieve_TCF(self):
        self.window = QtWidgets.QDialog()
        self.ui = MyTCFWindow(self.window, tcfFactors=self.tcfFactors)
        self.window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.window.show()
        rsp = self.window.exec_()

        if rsp == 1:
            self.tcfFactors = self.ui.get_tcfFactors()
            self.tcf = self.ui.retrieve_tcf()
            self.tcfOutput.setText(str(self.tcf))
            
    def retrieve_ECF(self):
        self.window = QtWidgets.QDialog()
        self.ui = MyECFWindow(self.window, ecfFactors=self.ecfFactors)
        self.window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.window.show()
        rsp = self.window.exec_()

        if rsp == 1:
            self.ecfFactors = self.ui.get_ecfFactors()
            self.ecf = self.ui.retrieve_ecf()
            self.ecfOutput.setText(str(self.ecf))

    def get_uucw(self):
        return self.uucw

    def get_uaw(self):
        return self.uaw

    def computeUUCW(self):
        v1 = self.uucwSimple.value()
        self.uucw[0] = v1

        v2 = self.uucwAvg.value()
        self.uucw[1] = v2

        v3 = self.uucwComplex.value()
        self.uucw[2] = v3

        #apply weights
        uucwTotal = (v1 * 5) + (v2 * 10) + (v3 * 15)
        self.uucwTotal = uucwTotal

        self.uucwOutput.setText(str(self.uucwTotal))

        self.uucp = self.uucwTotal + self.uawTotal
        self.uucpOutput.setText(str(self.uucp))

    def computeUAW(self):
        v1 = self.uawSimple.value()
        self.uaw[0] = v1

        v2 = self.uawAvg.value()
        self.uaw[1] = v2

        v3 = self.uawComplex.value()
        self.uaw[2] = v3

        #apply weights
        uawTotal = (v1 * 1) + (v2 * 2) + (v3 * 3)
        self.uawTotal = uawTotal
        self.uawOutput.setText(str(self.uawTotal))

        self.uucp = self.uucwTotal + self.uawTotal
        self.uucpOutput.setText(str(self.uucp))

    
