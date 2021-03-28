import pickle
import sys

from Project import Project
from Pane import Pane

from generated_ui.prod_ui.MainWindow import *

from MyNewProjectWindow import MyNewProjectWindow
from MyWeightFactorsTab import MyWeightFactorsTab
from MyFPPaneNameInput import MyFPPaneNameDialog
from MySelectLanguageWindow import MySelectLanguageWindow

from PyQt5.QtWidgets import QFileDialog, QTabWidget, QVBoxLayout, QWidget, QMainWindow
from PyQt5.QtCore import QSettings, QCoreApplication

ORGANIZATION_NAME = 'Developers At Work'
ORGANIZATION_DOMAIN = 'Masters of CS'
APPLICATION_NAME = 'Function Points Calculator'
SETTINGS_TRAY = 'settings/tray'


class App(QMainWindow, Ui_MainWindow):
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
    
    def set_language_preference(self):
        self.window = QtWidgets.QDialog()
        self.ui = MySelectLanguageWindow(self.window, preferredLanguage=self.languagePreference)
        self.window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.window.show()
        rsp = self.window.exec_()

        if rsp == 0:
            self.languagePreference = self.ui.get_language()
            self.settings.setValue('language preference', self.languagePreference)
            self.settings.sync()


    def remove_tab(self, index):
        widget = self.tabs.widget(index)
        if widget is not None:
            App.currentProject.remove_pane(index)
            widget.deleteLater()
        self.tabs.removeTab(index)

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

            self.layout = QVBoxLayout()
            self.tabs = QTabWidget()
            self.tabs.setTabsClosable(True)
            self.tabs.tabCloseRequested.connect(self.remove_tab)
            self.layout.addWidget(self.tabs)

            self.mainLayout.addLayout(self.layout)

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
                newPane = Pane(loadPane.get_name())
                newPane.set_VAF(loadPane.get_VAF())
                newPane.set_codeSize(loadPane.get_codeSize())
                newPane.set_totalCount(loadPane.get_totalCount())
                newPane.set_computedFP(loadPane.get_computedFP())
                newPane.set_inputValues(loadPane.get_inputValues())
                newPane.set_outputValues(loadPane.get_outputValues())
                newPane.set_selectedLanguage(loadPane.get_selectedLanguage())
                newPane.set_inputWeights(loadPane.get_inputWeights())                

                tab = QWidget()
                App.currentProject.add_pane_tab(MyWeightFactorsTab(tab, loaded=True, pane=newPane))
                
                name = newPane.get_name()
                index = self.tabs.addTab(tab, name)
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
                savePane = Pane(paneTab.get_paneName())
                savePane.set_inputValues(paneTab.get_inputValues())
                savePane.set_inputWeights(paneTab.get_inputWeights())
                savePane.set_outputValues(paneTab.get_outputValues())
                savePane.set_VAF(paneTab.get_VAF())
                savePane.set_totalCount(paneTab.get_totalCount())
                savePane.set_computedFP(paneTab.get_computedFP())
                savePane.set_selectedLanguage(paneTab.get_selectedLanguage())
                savePane.set_codeSize(paneTab.get_codeSize())

                savedTabs.append(savePane)

            saveProject = Project(App.currentProject.get_project_name())
            saveProject.set_creator_name(App.currentProject.get_creator_name())
            saveProject.set_product_name(App.currentProject.get_product_name())
            saveProject.set_comments(App.currentProject.get_comments())

            saveProject.save_panes(savedTabs)

            filename = save_dialog.selectedFiles()[0]
            with open(filename, 'wb') as f:
                pickle.dump(saveProject, f, -1)
            print(filename)





if __name__ == '__main__':
    QCoreApplication.setOrganizationName(ORGANIZATION_NAME)
    QCoreApplication.setOrganizationDomain(ORGANIZATION_DOMAIN)
    QCoreApplication.setApplicationName(APPLICATION_NAME)

    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    
    ui = App(main_window)
    
    main_window.show()
    app.exec_()