import pickle
import sys
from copy import deepcopy

from Project import Project
from Pane import Pane
from UseCasePane import UseCasePane
from SMIPane import SMIPane

from generated_ui.prod_ui.MainWindow import *

from MysmiErrorWindow import MysmiErrorWindow
from MyNewProjectWindow import MyNewProjectWindow
from MyWeightFactorsTab import MyWeightFactorsTab
from MySMITab import MySMITab
from MyUCPTab import MyUCPTab
from MyFPPaneNameInput import MyFPPaneNameDialog
from MyUCPPaneNameInput import MyUCPPaneNameInput
from MySelectLanguageWindow import MySelectLanguageWindow

from PyQt5.QtWidgets import QFileDialog, QTabWidget, QVBoxLayout, QWidget, QMainWindow, QMessageBox
from PyQt5.QtCore import QSettings, QCoreApplication
from PyQt5.QtGui import QCloseEvent

ORGANIZATION_NAME = 'Developers At Work'
ORGANIZATION_DOMAIN = 'Masters of CS'
APPLICATION_NAME = 'Function Points Calculator'
SETTINGS_TRAY = 'settings/tray'


class App(QMainWindow, QWidget, Ui_MainWindow):
    #initialize data params for save file
    currentProject = Project('init')
    def __init__(self, window):
        # QWidget.__init__(self, window)
        QMainWindow.__init__(self, window)
        self.setupUi(window)
        self.currentTitle = self.win.windowTitle()
        self.settings = QSettings('MyApp', 'GUIApp')
        self.languagePreference = self.settings.value('language preference')

        self.mainLayout = QVBoxLayout(self.centralwidget)
        
        self.layout = QVBoxLayout()
        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.remove_tab)
        self.layout.addWidget(self.tabs)

        self.mainLayout.addLayout(self.layout)
        self.smiIndex = None
        self.smiTabOpened = False
        self.newProject = False
        
        #connect new project
        self.actionNew.triggered.connect(self.new_project)

        #save project
        self.actionSave.triggered.connect(self.save_project)

        #open saved project
        self.actionOpen.triggered.connect(self.open_project)

        #set language preference
        self.changeLanguageButton.triggered.connect(self.set_language_preference)

        #enter FP data
        self.enterFPDataButton.triggered.connect(self.enter_function_points)

        #calculate use case points
        self.enterUseCasePoints.triggered.connect(self.calculate_ucp)

        #calculate SMI
        # self.enterSMI.setEnabled(True)
        self.enterSMI.triggered.connect(self.calculate_smi)

        
        self.actionExit_2.triggered.connect(self.close)
        self.win.closeEvent = self.closeEvent
        
    
    def closeEvent(self, event: QCloseEvent):
        if self.newProject:
            msg = QMessageBox.question(self, "Exit Program", "Save before Quitting?",
            QMessageBox.Ok | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Cancel)

            if msg == QMessageBox.Ok:
                self.save_project()
            elif msg == QMessageBox.No:
                QtWidgets.qApp.quit()
            elif msg == QMessageBox.Cancel:
                event.ignore()
        else:
            QtWidgets.qApp.quit()
    
    def set_language_preference(self):
        self.window = QtWidgets.QDialog()
        self.ui = MySelectLanguageWindow(self.window, preferredLanguage=self.languagePreference)
        self.window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.window.show()
        rsp = self.window.exec_()

        if rsp == QtWidgets.QDialog.Accepted:
            self.languagePreference = self.ui.get_language()
            self.settings.setValue('language preference', self.languagePreference)
            self.settings.sync()


    def remove_tab(self, index):
        widget = self.tabs.widget(index)
        if widget is not None:
            if widget.objectName() == "SMIForm":
                self.enterSMI.setEnabled(True)
                self.smiTabOpened = False
            App.currentProject.remove_pane(index)
            widget.deleteLater()
        self.tabs.removeTab(index)


    def calculate_ucp(self):
        self.window = QtWidgets.QDialog()
        self.ui = MyUCPPaneNameInput(self.window)
        self.window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.window.show()
        rsp = self.window.exec_()

        if rsp == QtWidgets.QDialog.Accepted:
            paneName = self.ui.getPaneName()

            ucpPane = UseCasePane(paneID=paneName)
            tab = QWidget()
            App.currentProject.add_pane_tab(MyUCPTab(tab, pane=ucpPane))
            App.currentProject.add_pane(ucpPane)

            index = self.tabs.addTab(tab, paneName)
            self.tabs.setCurrentIndex(index)

    def calculate_smi(self):
        # if the tab is closed early without saving we reset the smitabopened variable
        if self.smiTabOpened:
            self.errorWindow = QtWidgets.QDialog()
            self.ui = MysmiErrorWindow(self.errorWindow)
            self.errorWindow.setWindowModality(QtCore.Qt.ApplicationModal)
            self.errorWindow.show()
            rsp = self.errorWindow.exec_()
            return
        
        defaultSMIPane = SMIPane("SMI")
        tab = QWidget()
        App.currentProject.add_pane_tab(MySMITab(tab, pane=defaultSMIPane))
        App.currentProject.add_pane(defaultSMIPane)

        index = self.tabs.addTab(tab, "SMI")
        self.tabs.setCurrentIndex(index)

        self.smiIndex = index # when we close the tab at this index, reset the smiTabopened variable
        self.smiTabOpened = True

    def enter_function_points(self):
        self.window = QtWidgets.QDialog()
        self.ui = MyFPPaneNameDialog(self.window)
        self.window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.window.show()
        rsp = self.window.exec_()

        if rsp == QtWidgets.QDialog.Accepted:
            paneName = self.ui.getPaneName()

            defaultPane = Pane(paneName=paneName)
            
            tab = QWidget()
            App.currentProject.add_pane_tab(MyWeightFactorsTab(tab, pane=defaultPane, languagePreference=self.languagePreference))
            App.currentProject.add_pane(defaultPane)

            index = self.tabs.addTab(tab, paneName)
            self.tabs.setCurrentIndex(index)


    def new_project(self):
        self.window = QtWidgets.QDialog()
        ui = MyNewProjectWindow(self.window)
        self.window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.window.show()
        rsp = self.window.exec_()

        if rsp == QtWidgets.QDialog.Accepted:
            App.currentProject.reset()
            self.enterFPDataButton.setEnabled(True)
            self.enterUseCasePoints.setEnabled(True)
            self.enterSMI.setEnabled(True)
            self.newProject = True
            projectDetails = ui.getNewProjectParams()

            App.currentProject.set_project_name(projectDetails['projectName'])
            App.currentProject.set_product_name(projectDetails['productName'])
            App.currentProject.set_creator_name(projectDetails['creator'])
            App.currentProject.set_comments(projectDetails['comments'])

            # must set self.win = MainWindow in UI file manually for this to work
            self.win.setWindowTitle(self.currentTitle + ' - ' + projectDetails['projectName'])

    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget() is not None:
                    child.widget().setParent(None)
                elif child.layout() is not None:
                    self.clearLayout(child.layout())

    def open_project(self):
        openDlg = QFileDialog()
        openDlg.setWindowTitle("Open File")
        openDlg.setAcceptMode(QFileDialog.AcceptOpen)
        openDlg.setNameFilter('MS Files (*.ms)')

        if openDlg.exec_() == QFileDialog.Accepted:
            #reset current project and layout
            self.clearLayout(self.mainLayout)
            App.currentProject.reset()

            #if user opening project from fresh run
            self.enterFPDataButton.setEnabled(True)
            self.enterUseCasePoints.setEnabled(True)

            self.layout = QVBoxLayout()
            self.tabs = QTabWidget()
            self.tabs.setTabsClosable(True)
            self.tabs.tabCloseRequested.connect(self.remove_tab)
            self.layout.addWidget(self.tabs)

            self.mainLayout.addLayout(self.layout)
            self.newProject = True

            filename = openDlg.selectedFiles()[0]
            with open(filename, 'rb') as f:
                loadProject = pickle.load(f)
            
            #set project details
            App.currentProject.set_project_name(loadProject.get_project_name())
            App.currentProject.set_product_name(loadProject.get_product_name())
            App.currentProject.set_creator_name(loadProject.get_creator_name())
            App.currentProject.set_comments(loadProject.get_comments())

            #get pane objects (not the tabs)
            for loadPane in loadProject.get_panes():
                if isinstance(loadPane, UseCasePane):
                    newPane = UseCasePane(loadPane.get_ID())
                    newPane.set_tcfFactors(loadPane.get_tcfFactors())
                    newPane.set_ecfFactors(loadPane.get_ecfFactors())
                    newPane.set_uucw(loadPane.get_uucw())
                    newPane.set_uaw(loadPane.get_uaw())
                    newPane.set_tcf(loadPane.get_tcf())
                    newPane.set_ecf(loadPane.get_ecf())
                    newPane.set_uucwTotal(loadPane.get_uucwTotal())
                    newPane.set_uawTotal(loadPane.get_uawTotal())
                    newPane.set_uucp(loadPane.get_uucp())
                    newPane.set_PF(loadPane.get_PF())
                    newPane.set_UCP(loadPane.get_UCP())
                    newPane.set_locucp(loadPane.get_locucp())
                    newPane.set_locPM(loadPane.get_locPM())
                    newPane.set_estLOC(loadPane.get_estLOC())
                    newPane.set_estPM(loadPane.get_estPM())
                    newPane.set_estHours(loadPane.get_estHours())
                elif isinstance(loadPane, Pane):      
                    newPane = Pane(loadPane.get_name())
                    newPane.set_inputValues(loadPane.get_inputValues())
                    newPane.set_inputWeights(loadPane.get_inputWeights())
                    newPane.set_outputValues(loadPane.get_outputValues())
                    newPane.set_VAF(loadPane.get_VAF())
                    newPane.set_totalCount(loadPane.get_totalCount())
                    newPane.set_computedFP(loadPane.get_computedFP())
                    newPane.set_selectedLanguage(loadPane.get_selectedLanguage())
                    newPane.set_codeSize(loadPane.get_codeSize())
                else: # smi pane
                    newPane = SMIPane(loadPane.paneID)
                    newPane.SMI = loadPane.SMI
                    newPane.MA = loadPane.MA
                    newPane.MC = loadPane.MC
                    newPane.MD = loadPane.MD
                    newPane.TM = loadPane.TM


                tab = QWidget()
                if isinstance(newPane, UseCasePane):
                    App.currentProject.add_pane_tab(MyUCPTab(tab, loaded=True, pane=newPane))
                    name = newPane.get_ID()
                    index = self.tabs.addTab(tab, name)
                    self.tabs.setCurrentIndex(index)
                elif isinstance(newPane, Pane):
                    App.currentProject.add_pane_tab(MyWeightFactorsTab(tab, loaded=True, pane=newPane))
                    name = newPane.get_name()
                    index = self.tabs.addTab(tab, name)
                    self.tabs.setCurrentIndex(index)
                else: # smi pane
                    App.currentProject.add_pane_tab(MySMITab(tab, loaded=True, pane=newPane))
                    name = newPane.paneID
                    index = self.tabs.addTab(tab, name)
                    self.smiIndex = index
                    self.tabs.setCurrentIndex(index)
                
            self.win.setWindowTitle('CECS 543 Metrics Suite - ' + App.currentProject.get_project_name())
    
        
    def save_project(self):
        save_dialog = QFileDialog()
        save_dialog.setWindowTitle("Save File")
        save_dialog.setAcceptMode(QFileDialog.AcceptSave)
        save_dialog.setNameFilter('MS Files (*.ms)')
        save_dialog.setDefaultSuffix('ms')

        if save_dialog.exec_() == QFileDialog.Accepted:

            savedTabs = []

            #get pane TAB objects (not the panes, need to pull info from these, convert to regular panes for pickle)
            allPaneTabs = App.currentProject.get_pane_tabs()
            for paneTab in allPaneTabs:
                if isinstance(paneTab, MyUCPTab):
                    savePane = UseCasePane(paneTab.get_ID())
                    savePane.set_tcfFactors(paneTab.get_tcfFactors())
                    savePane.set_ecfFactors(paneTab.get_ecfFactors())
                    savePane.set_uucw(paneTab.get_uucw())
                    savePane.set_uaw(paneTab.get_uaw())
                    savePane.set_tcf(paneTab.get_tcf())
                    savePane.set_ecf(paneTab.get_ecf())
                    savePane.set_uucwTotal(paneTab.get_uucwTotal())
                    savePane.set_uawTotal(paneTab.get_uawTotal())
                    savePane.set_uucp(paneTab.get_uucp())
                    savePane.set_PF(paneTab.get_PF())
                    savePane.set_UCP(paneTab.get_UCP())
                    savePane.set_locucp(paneTab.get_locucp())
                    savePane.set_locPM(paneTab.get_locPM())
                    savePane.set_estLOC(paneTab.get_estLOC())
                    savePane.set_estPM(paneTab.get_estPM())
                    savePane.set_estHours(paneTab.get_estHours())
                elif isinstance(paneTab, MyWeightFactorsTab):
                    savePane = Pane(paneTab.get_name())
                    savePane.set_inputValues(paneTab.get_inputValues())
                    savePane.set_inputWeights(paneTab.get_inputWeights())
                    savePane.set_outputValues(paneTab.get_outputValues())
                    savePane.set_VAF(paneTab.get_VAF())
                    savePane.set_totalCount(paneTab.get_totalCount())
                    savePane.set_computedFP(paneTab.get_computedFP())
                    savePane.set_selectedLanguage(paneTab.get_selectedLanguage())
                    savePane.set_codeSize(paneTab.get_codeSize())
                else: # smi tab
                    savePane = SMIPane(paneTab.paneID)
                    saveInfo = paneTab.get_table()
                    
                    savePane.SMI = saveInfo['smi']
                    savePane.MA = saveInfo['ma']
                    savePane.MC = saveInfo['mc']
                    savePane.MD = saveInfo['md']
                    savePane.TM = saveInfo['tm']

                savedTabs.append(savePane)
            
            saveProject = Project(App.currentProject.get_project_name())
            saveProject.set_creator_name(App.currentProject.get_creator_name())
            saveProject.set_product_name(App.currentProject.get_product_name())
            saveProject.set_comments(App.currentProject.get_comments())

            #saving pane objects
            saveProject.save_panes(savedTabs)

            filename = save_dialog.selectedFiles()[0]
            with open(filename, 'wb') as f:
                pickle.dump(saveProject, f, -1)





if __name__ == '__main__':
    QCoreApplication.setOrganizationName(ORGANIZATION_NAME)
    QCoreApplication.setOrganizationDomain(ORGANIZATION_DOMAIN)
    QCoreApplication.setApplicationName(APPLICATION_NAME)

    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    
    ui = App(main_window)
    
    main_window.show()

    app.exec_()