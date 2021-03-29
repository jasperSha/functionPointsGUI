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

        self.tcfFactors = [
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
        ]

        self.ecfFactors = [
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
        ]

        self.uucw = [
            0.0,
            0.0,
            0.0,
        ]

        self.uaw = [
            0.0,
            0.0,
            0.0,
        ]


        self.tcf = 0.0 # tcf = 0.6 * (.01*techFactors)
        self.ecf = 0.0 # ecf = 1.4 + (-0.03 * envFactors)

        self.uucwTotal = 0.0
        self.uawTotal = 0.0
        self.uucp = 0.0 # uucp = uaw + uucw

        self.PF = 0.0
        self.ucp = 0.0 # ucp = tcf * ecf * uucp * PF

        self.locucp = 0.0 # loc per UCP
        self.locPM = 0.0 # loc per programmer month

        self.estLOC = 0.0 # estLOC = locucp * ucp
        self.estPM = 0.0 # estPM = estLOC / locPM
        self.estHours = 0.0 # estHours = estPM * 1600 (40 hour weeks, 4 weeks/month)
    
    def __repr__(self):
        return f"{self.paneID}"
    
    def is_ucp_pane(self):
        return True

    def get_ID(self):
        return self.paneID
    
    def get_tcfFactors(self):
        return self.tcfFactors
    
    def set_tcfFactors(self, tcffactors):
        self.tcfFactors = tcffactors

    def get_ecfFactors(self):
        return self.ecfFactors

    def set_ecfFactors(self, ecffactors):
        self.ecfFactors = ecffactors

    def get_uucw(self):
        return self.uucw
    
    def set_uucw(self, uucw):
        self.uucw = uucw
    
    def get_uaw(self):
        return self.uaw
    
    def set_uaw(self, uaw):
        self.uaw = uaw
    
    def get_tcf(self):
        return self.tcf
    
    def set_tcf(self, tcf):
        self.tcf = tcf
    
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
    
