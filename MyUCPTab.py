from generated_ui.dev_ui.UCPTab import *

from PyQt5.QtWidgets import *

class MyUCPTab(QWidget, Ui_UCPTab):
    def __init__(self, window, pane, loaded=False):
        QWidget.__init__(self, window)
        self.setupUi(window)

        self.paneName = pane.get_ID()

        self.tcfWeights = pane.get_tcfWeights()
        self.ecfWeights = pane.get_ecfWeights()

        self.tcfTotalFactors = pane.get_tcfTotalFactors()
        self.tcf = pane.get_tcf()
        self.ecfTotalFactors = pane.get_ecfTotalFactors()
        self.ecf = pane.get_ecf()

        self.uucw = pane.get_uucw()
        self.uaw = pane.get_uaw()

        self.uucwTotal = pane.get_uucwTotal()
        self.uawTotal = pane.get_uawTotal()
        self.uucp = pane.get_uucp()

        self.pf = pane.get_PF()
        self.ucp = pane.get_UCP()

        self.locucp = pane.get_locucp()
        self.locPM = pane.get_locPM()

        self.estLOC = pane.get_estLOC()
        self.estPM = pane.get_estPM()
        self.estHours = pane.get_estHours()

        self.output = pane.get_output()

        if loaded:
            pass # load saved data
        
        self.uucwSimple.valueChanged.connect(self.computeUUCW)
        self.uucwAvg.valueChanged.connect(self.computeUUCW)
        self.uucwComplex.valueChanged.connect(self.computeUUCW)
        
        self.uawSimple.valueChanged.connect(self.computeUAW)
        self.uawAvg.valueChanged.connect(self.computeUAW)
        self.uawComplex.valueChanged.connect(self.computeUAW)

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
