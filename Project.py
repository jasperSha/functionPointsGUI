from Pane import Pane
class Project:
    def __init__(self, name):
        self.projectName = name
        self.productName = ''
        self.creator = ''
        self.comments = ''

        self.panes = [] #holds list of Panes


        self.paneTabs = [] #holds list of tab objects
    
    def __repr__(self):
        return "Project Name: %s\nProduct Name: %s\nCreator: %s\nComments: %s" % (self.projectName, 
                                                                                self.productName,
                                                                                self.creator,
                                                                                self.comments)

    def add_pane_tab(self, paneTab):
        self.paneTabs.append(paneTab)

    def get_pane_tabs(self):
        return self.paneTabs
    
    def add_pane(self, pane):
        self.panes.append(pane)

    def save_panes(self, savePanes):
        self.panes = savePanes
    
    def get_panes(self):
        return self.panes

    def set_project_name(self, projectName):
        self.projectName = projectName
    
    def get_project_name(self):
        return self.projectName

    def set_product_name(self, productName):
        self.productName = productName
    
    def get_product_name(self):
        return self.productName
    
    def set_creator_name(self, creatorName):
        self.creator = creatorName
    
    def get_creator_name(self):
        return self.creator
    
    def set_comments(self, comments):
        self.comments = comments
    
    def get_comments(self):
        return self.comments

    def remove_pane(self, paneIndex):
        if self.panes:
            self.panes.pop(paneIndex)
        if self.paneTabs:
            self.paneTabs.pop(paneIndex)

    def reset(self):
        if self.paneTabs:
            self.paneTabs = []
        if self.panes:
            self.panes = []
        if self.projectName:
            self.projectName = ''
        if self.creator:
            self.creator = ''
        if self.comments:
            self.comments = ''
    
    