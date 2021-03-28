class UseCasePane:
    def __init__(self, paneID):
        '''
            Pane that holds UCP data:
                technical complexity factors

                environment complexity factors

                unadjusted use case points


                fields:
                    productivity factor: default:20
                    LOC/PM: default: 700
                    LOC/UCP default: 100

                    Output:
                        total UCP
                        estimated hours
                        estimated LOC
                        estimated PM
        '''
        self.paneID = paneID

        self.tcfWeights = {
                            "2.0": '',
                            "1.0": '',
                            "1.0": '',
                            "1.0": '',
                            "1.0": '',
                            "0.5": '',
                            "0.5": '',
                            "2.0": '',
                            "1.0": '',
                            "1.0": '',
                            "1.0": '',
                            "1.0": '',
                            "1.0": ''
        }

        self.ecfWeights = [
                                1.5,
                                0.5,
                                1.0,
                                0.5,
                                1.0,
                                2.0,
                                -1.0,
                                2.0
                        ]

        self.uucw = {
            'simple': 5.0,
            'average': 10.0,
            'complex': 15.0
        }

        self.uaw = {
            'simple': 1.0,
            'average': 2.0,
            'complex': 3.0
        }

        self.tcfTotalFactors = 0
        self.tcf = 0 # tcf = 0.6 * (.01*techFactors)

        self.ecfTotalFactors = 0
        self.ecf = 0 # ecf = 1.4 + (-0.03 * envFactors)

        self.uucwTotal = 0
        self.uawTotal = 0
        self.uucp = 0 # uucp = uaw + uucw

        
        self.PF = 0
        self.ucp = 0 # ucp = tcf * ecf * uucp * PF

        self.locucp = 0 # loc per UCP
        self.locPM = 0 # loc per programmer month

        self.estLOC = 0 # estLOC = locucp * ucp
        self.estPM = 0 # estPM = estLOC / locPM
        self.estHours = 0 # estHours = estPM * 1600 (40 hour weeks, 4 weeks/month)
        self.output = [self.ucp, self.estHours, self.estLOC, self.estPM]
    
    def __repr__(self):
        return f"{self.paneID}"

    def get_ID(self):
        return self.paneID
    
    def get_tcfTotalFactors(self):
        return self.tcfTotalFactors
    
    def set_tcfTotalFactors(self, tcfFactors):
        self.tcfTotalFactors = tcfFactors
    
    def get_tcf(self):
        return self.tcf
    
    def set_tcf(self, tcf):
        self.tcf = tcf
    
    def get_ecfTotalFactors(self):
        return self.ecfTotalFactors
    
    def set_ecfTotalFactors(self, ecfFactors):
        self.ecfTotalFactors = ecfFactors

    def get_ecf(self):
        return self.ecf
    
    def set_ecf(self, ecf):
        self.ecf = ecf
    
    def get_uucwTotal(self):
        return self.uucwTotal
    
    def set_uucwTotal(self, uucwTotal):
        self.uucwTotal = uucwTotal
    
    def get_uawTotal(self):
        return self.uawTotal
    
    def set_uawTotal(self, uawTotal):
        self.uawTotal = uawTotal
    
    def get_uucp(self):
        return self.uucp

    def set_uucp(self, uucp):
        self.uucp = uucp
    
    def get_PF(self):
        return self.PF
    
    def set_PF(self, pf):
        self.PF = pf
    
    def get_UCP(self):
        return self.ucp
    
    def set_UCP(self, ucp):
        self.ucp = ucp

    def get_locucp(self):
        return self.locucp

    def set_locucp(self, locucp):
        self.locucp = locucp

    def get_locPM(self):
        return self.locPM
    
    def set_locPM(self, locpm):
        self.locPM = locpm
    
    def get_estLOC(self):
        return self.estLOC
    
    def set_estLOC(self, estloc):
        self.estLOC = estloc
    
    def get_estPM(self):
        return self.estPM
    
    def set_estPM(self, estpm):
        self.estPM = estpm

    def get_estHours(self):
        return self.estHours
    
    def set_estHours(self, esthours):
        self.estHours = esthours
    
    def get_output(self):
        return self.output
    
    def set_output(self, output):
        self.output = output

    
    

