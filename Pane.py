
class Pane:
    def __init__(self, paneName):
        self.name = paneName

        self.inputValues = { 
            'externalInputsInput': 0,
            'externalOutputsInput': 0,
            'externalInquiriesInput': 0,
            'externalInterfaceFilesInput': 0,
            'internalLogicalFilesInput': 0
        }

        self.inputWeights = { #default is average complexity
            'externalInputsInput': 4,
            'externalOutputsInput': 5,
            'externalInquiriesInput': 4,
            'externalInterfaceFilesInput': 10,
            'internalLogicalFilesInput': 7
        }

        self.VAF = [0]*14 

        self.outputValues = {
            'ei_factor': 0,
            'eo_factor': 0,
            'eInq_factor': 0,
            'eInf_factor': 0,
            'intLog_factor': 0
        }

        self.computedFP = 0 
        self.totalCount = 0
        self.codeSize = 0
        self.selectedLanguage = ''
    
    def __repr__(self):
        return f"{self.paneID}\nVAF={self.VAF}\nFP={self.computedFP}\ninputValues={self.inputValues}\noutput={self.outputValues}\ntotalcount={self.totalCount}\nlang={self.language}\n"

    def get_name(self):
        return self.name
    
    def set_codeSize(self, codeSize):
        self.codeSize = codeSize
    
    def get_codeSize(self):
        return self.codeSize

    def set_totalCount(self, totalCount: int):
        self.totalCount = totalCount
    
    def get_totalCount(self):
        return self.totalCount
    
    def set_VAF(self, vaf: list):
        self.VAF = vaf
    
    def get_VAF(self):
        return self.VAF
    
    def set_inputValues(self, inputValues: dict):
        self.inputValues = inputValues
    
    def get_inputValues(self):
        return self.inputValues

    def set_inputWeights(self, inputWeights: dict):
        self.inputWeights = inputWeights
    
    def get_inputWeights(self):
        return self.inputWeights
    
    def set_outputValues(self, outputValues: dict):
        self.outputValues = outputValues
    
    def get_outputValues(self):
        return self.outputValues
    
    def set_computedFP(self, computedFP: int):
        self.computedFP = computedFP
    
    def get_computedFP(self):
        return self.computedFP
    
    def set_selectedLanguage(self, selectedLanguage: str):
        self.selectedLanguage = selectedLanguage
    
    def get_selectedLanguage(self):
        return self.selectedLanguage
    
    