from Pane import Pane

from generated_ui.WeightFactorsTab import *

from MyValueAdjustmentFactorsWindow import MyValueAdjustmentFactorsWindow
from MySelectLanguageWindow import MySelectLanguageWindow

from PyQt5.QtWidgets import *

    

class MyWeightFactorsTab(QWidget, Ui_WeightFactorsTab):
    def __init__(self, window, pane, loaded=False, languagePreference=None):
        QWidget.__init__(self, window)
        self.setupUi(window)
        self.languageLOCPerFP = {
            'radioAssembler': 337,
            'radioAda95': 154,
            'radioC': 148,
            'radioCOBOL': 80,
            'radioCPlusPlus': 59,
            'radioCSharp': 58,
            'radioFORTRAN': 90,
            'radioHTML': 43,
            'radioJava': 55,
            'radioJavaScript': 54,
            'radioVBScript': 38,
            'radioVisualBasic': 50
        }


        self.paneName = pane.get_name()
        self.inputValues = pane.get_inputValues()
        self.inputWeights = pane.get_inputWeights()
        self.VAF = pane.get_VAF()
        self.outputValues = pane.get_outputValues()
        self.totalCount = pane.get_totalCount()
        self.computedFP = pane.get_computedFP()
        self.selectedLanguage = pane.get_selectedLanguage()
        self.codeSize = pane.get_codeSize()
        
        if loaded:
            self.load_data()

        if languagePreference and not loaded:
            self.selectedLanguage = languagePreference
            displayLang = languagePreference.replace('radio', '')

            if displayLang == 'CPlusPlus':
                displayLang = 'C++'
            elif displayLang == 'CSharp':
                displayLang = 'C#'
            self.currentLanguageOutput.setText(displayLang)
        
        if not self.selectedLanguage:
            self.currentLanguageOutput.setText("None")

        self.externalInputsInput.valueChanged.connect(self.computeEI)
        self.simple3.toggled.connect(self.computeEI)
        self.average4.toggled.connect(self.computeEI)
        self.complex6.toggled.connect(self.computeEI)

        self.externalOutputsInput.valueChanged.connect(self.computeEO)
        self.simple4.toggled.connect(self.computeEO)
        self.average5.toggled.connect(self.computeEO)
        self.complex7.toggled.connect(self.computeEO)

        self.externalInquiriesInput.valueChanged.connect(self.computeEInq)
        self.simple3_2.toggled.connect(self.computeEInq)
        self.average4_2.toggled.connect(self.computeEInq)
        self.complex6_2.toggled.connect(self.computeEInq)

        self.externalInterfaceFilesInput.valueChanged.connect(self.computeEInf)
        self.simple7.toggled.connect(self.computeEInf)
        self.average10.toggled.connect(self.computeEInf)
        self.complex15.toggled.connect(self.computeEInf)
 
        self.internalLogicalFilesInput.valueChanged.connect(self.computeLogic)
        self.simple5.toggled.connect(self.computeLogic)
        self.average7.toggled.connect(self.computeLogic)
        self.complex10.toggled.connect(self.computeLogic)
 

        self.currentLanguageOutput.textChanged.connect(self.compute_code_size)
        
        self.computeFunctionPointsButton.clicked.connect(self.compute_fp)
        self.valueAdjustmentsButton.clicked.connect(self.retrieve_vaf)
        self.computeCodeSizeButton.clicked.connect(self.compute_code_size)
        self.changeLanguageButton.clicked.connect(self.change_language)

    def load_data(self):
        ei_input = self.inputValues['externalInputsInput']
        eo_input = self.inputValues['externalOutputsInput']
        einq_input = self.inputValues['externalInquiriesInput']
        einf_input = self.inputValues['externalInterfaceFilesInput']
        inlog_input = self.inputValues['internalLogicalFilesInput']

        self.externalInputsInput.setValue(ei_input)
        self.externalOutputsInput.setValue(eo_input)
        self.externalInquiriesInput.setValue(einq_input)
        self.externalInterfaceFilesInput.setValue(einf_input)
        self.internalLogicalFilesInput.setValue(inlog_input)

        ei_weight = self.inputWeights['externalInputsInput']
        eo_weight = self.inputWeights['externalOutputsInput']
        einq_weight = self.inputWeights['externalInquiriesInput']
        einf_weight = self.inputWeights['externalInterfaceFilesInput']
        inlog_weight = self.inputWeights['internalLogicalFilesInput']

        for btn in self.externalInputsGroup.buttons():
            if btn.text() == str(ei_weight):
                btn.setChecked(True)

        for btn in self.externalOutputsGroup.buttons():
            if btn.text() == str(eo_weight):
                btn.setChecked(True)

        for btn in self.externalInquiriesGroup.buttons():
            if btn.text() == str(einq_weight):
                btn.setChecked(True)

        for btn in self.externalInterfaceGroup.buttons():
            if btn.text() == str(einf_weight):
                btn.setChecked(True)

        for btn in self.internalLogicalGroup.buttons():
            if btn.text() == str(inlog_weight):
                btn.setChecked(True)

        ei_out = self.outputValues['ei_factor']
        eo_out = self.outputValues['eo_factor']
        einq_out = self.outputValues['eInq_factor']
        einf_out = self.outputValues['eInf_factor']
        inlog_out = self.outputValues['intLog_factor']

        self.externalInputOutput.setText(str(ei_out))
        self.externalOutputsOutput.setText(str(eo_out))
        self.externalInquiriesOutput.setText(str(einq_out))
        self.externalInterfaceFilesOutput.setText(str(einf_out))
        self.internalLogicalFilesOutput.setText(str(inlog_out))

        totalcount = self.totalCount
        computedfp = self.computedFP
        codeSize = self.codeSize
        vaf = self.VAF

        self.totalCountOutput.setText(str(totalcount))
        self.totalFunctionPointsOutput.setText(str(computedfp))
        self.computeCodeSizeOutput.setText(str(codeSize))
        self.valueAdjustmentsOutput.setText(str(sum(vaf)))

        selectedLanguage = self.selectedLanguage
        displayLang = selectedLanguage.replace('radio', '')
        if displayLang == 'CPlusPlus':
            displayLang = 'C++'
        elif displayLang == 'CSharp':
            displayLang = 'C#'
        self.currentLanguageOutput.setText(displayLang)

    def get_paneName(self):
        return self.paneName

    def get_inputValues(self):
        return self.inputValues
    
    def get_inputWeights(self):
        return self.inputWeights
    
    def get_VAF(self):
        return self.VAF

    def get_outputValues(self):
        return self.outputValues
    
    def get_totalCount(self):
        return self.totalCount
    
    def get_computedFP(self):
        return self.computedFP
    
    def get_selectedLanguage(self):
        return self.selectedLanguage
    
    def get_codeSize(self):
        return self.codeSize
    
    
    def computeEI(self):
        v = self.externalInputsInput.value()
        self.inputValues['externalInputsInput'] = v

        for btn in self.externalInputsGroup.buttons():
            if btn.isChecked():
                self.inputWeights['externalInputsInput'] = int(btn.text())
        ei_factor = v * self.inputWeights['externalInputsInput']
        self.outputValues['ei_factor'] = ei_factor
        self.compute_total()

    def computeEO(self):
        v = self.externalOutputsInput.value()
        self.inputValues['externalOutputsInput'] = v

        for btn in self.externalOutputsGroup.buttons():
            if btn.isChecked():
                self.inputWeights['externalOutputsInput'] = int(btn.text())
        eo_factor = v * self.inputWeights['externalOutputsInput']
        self.outputValues['eo_factor'] = eo_factor
        self.compute_total()

    def computeEInq(self):
        v = self.externalInquiriesInput.value()
        self.inputValues['externalInquiriesInput'] = v

        for btn in self.externalInquiriesGroup.buttons():
            if btn.isChecked():
                self.inputWeights['externalInquiriesInput'] = int(btn.text())
        eInq_factor = v * self.inputWeights['externalInquiriesInput']
        self.outputValues['eInq_factor'] = eInq_factor
        self.compute_total()

    def computeEInf(self):
        v = self.externalInterfaceFilesInput.value()
        self.inputValues['externalInterfaceFilesInput'] = v

        for btn in self.externalInterfaceGroup.buttons():
            if btn.isChecked():
                self.inputWeights['externalInterfaceFilesInput'] = int(btn.text())
        eInf_factor = v * self.inputWeights['externalInterfaceFilesInput']
        self.outputValues['eInf_factor'] = eInf_factor
        self.compute_total()

    def computeLogic(self):
        v = self.internalLogicalFilesInput.value()
        self.inputValues['internalLogicalFilesInput'] = v

        for btn in self.internalLogicalGroup.buttons():
            if btn.isChecked():
                self.inputWeights['internalLogicalFilesInput'] = int(btn.text())
        intLog_factor = v * self.inputWeights['internalLogicalFilesInput']
        self.outputValues['intLog_factor'] = intLog_factor
        self.compute_total()
    
    def compute_total(self):
        self.totalCount = 0
        ei = self.outputValues['ei_factor']
        eo = self.outputValues['eo_factor']
        einq = self.outputValues['eInq_factor']
        einf = self.outputValues['eInf_factor']
        intlog = self.outputValues['intLog_factor']

        self.totalCount = ei + eo + einq + einf + intlog
        caf = 0.01*sum(self.VAF) + 0.65
        self.computedFP = round(caf * self.totalCount, 2)

    
    def retrieve_vaf(self):
        self.window = QtWidgets.QDialog()
        self.ui = MyValueAdjustmentFactorsWindow(self.window, self.VAF)
        self.window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.window.show()
        rsp = self.window.exec_()
        
        if rsp == 0:
            self.VAF = self.ui.get_VAF()
            self.valueAdjustmentsOutput.setText(str(sum(self.VAF)))

    def change_language(self):
        self.window = QtWidgets.QDialog()
        self.ui = MySelectLanguageWindow(self.window, setLanguage=self.selectedLanguage)
        self.window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.window.show()
        rsp = self.window.exec_()

        if rsp == 0:
            self.selectedLanguage = self.ui.get_language()
            displayLang = self.selectedLanguage.replace('radio', '')
            if displayLang == 'CPlusPlus':
                displayLang = 'C++'
            elif displayLang == 'CSharp':
                displayLang = 'C#'
            self.currentLanguageOutput.setText(displayLang)

    def compute_code_size(self):
        currLang = self.selectedLanguage
        if currLang and self.computedFP != 0:
            self.codeSize = round(self.languageLOCPerFP[currLang] * self.computedFP, 2)

            self.computeCodeSizeOutput.setText(str(self.codeSize))


    def fp_input(self):
        # must set self.wftab = WeightFactorsTab in UI file manually for this to work
        button = self.wftab.sender()
        buttonName = button.objectName()
        self.inputValues[buttonName] = button.value()


    def compute_fp(self):
        caf = 0.01*sum(self.VAF) + 0.65
        self.computedFP = round(caf * self.totalCount, 2)

        self.externalInputOutput.setText(str(self.outputValues['ei_factor']))
        self.externalOutputsOutput.setText(str(self.outputValues['eo_factor']))
        self.externalInquiriesOutput.setText(str(self.outputValues['eInq_factor']))
        self.externalInterfaceFilesOutput.setText(str(self.outputValues['eInf_factor']))
        self.internalLogicalFilesOutput.setText(str(self.outputValues['intLog_factor']))

        self.totalCountOutput.setText(str(self.totalCount))
        self.totalFunctionPointsOutput.setText(str(self.computedFP))
        self.valueAdjustmentsOutput.setText(str(sum(self.VAF)))

