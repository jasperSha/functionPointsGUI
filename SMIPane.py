class SMIPane:
    def __init__(self, paneID):
        '''
            Pane that holds SMI data:
            
            @params:
                SMI: list
                MA: list
                MC: list
                MD: list
                TM: list

        '''
        self.paneID = paneID

        self.SMI = []
        self.MA = []
        self.MC = []
        self.MD = []
        self.TM = []

    def __repr__(self):
        return f'SMI={self.SMI}\nmodules added={self.MA}\nmod changed={self.MC}\nmod del={self.MD}\ntotal modules={self.TM}'
