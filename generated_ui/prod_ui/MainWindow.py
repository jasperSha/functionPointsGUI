# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.win = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(946, 668)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 946, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuPreferences = QtWidgets.QMenu(self.menubar)
        self.menuPreferences.setObjectName("menuPreferences")
        self.menuMetrics = QtWidgets.QMenu(self.menubar)
        self.menuMetrics.setObjectName("menuMetrics")
        self.menuFunction_Points = QtWidgets.QMenu(self.menuMetrics)
        self.menuFunction_Points.setObjectName("menuFunction_Points")
        self.menuUse_Case_Points = QtWidgets.QMenu(self.menuMetrics)
        self.menuUse_Case_Points.setObjectName("menuUse_Case_Points")
        self.menuSMI = QtWidgets.QMenu(self.menuMetrics)
        self.menuSMI.setObjectName("menuSMI")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.changeLanguageButton = QtWidgets.QAction(MainWindow)
        self.changeLanguageButton.setObjectName("changeLanguageButton")
        self.enterFPDataButton = QtWidgets.QAction(MainWindow)
        self.enterFPDataButton.setEnabled(False)
        self.enterFPDataButton.setObjectName("enterFPDataButton")
        self.actionExit_2 = QtWidgets.QAction(MainWindow)
        self.actionExit_2.setObjectName("actionExit_2")
        self.enterUseCasePoints = QtWidgets.QAction(MainWindow)
        self.enterUseCasePoints.setEnabled(False)
        self.enterUseCasePoints.setObjectName("enterUseCasePoints")
        self.enterSMI = QtWidgets.QAction(MainWindow)
        self.enterSMI.setObjectName("enterSMI")
        self.enterSMI.setEnabled(False)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit_2)
        self.menuPreferences.addAction(self.changeLanguageButton)
        self.menuFunction_Points.addAction(self.enterFPDataButton)
        self.menuUse_Case_Points.addAction(self.enterUseCasePoints)
        self.menuSMI.addAction(self.enterSMI)
        self.menuMetrics.addAction(self.menuFunction_Points.menuAction())
        self.menuMetrics.addAction(self.menuUse_Case_Points.menuAction())
        self.menuMetrics.addAction(self.menuSMI.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuPreferences.menuAction())
        self.menubar.addAction(self.menuMetrics.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CECS 543 Metrics Suite"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuPreferences.setTitle(_translate("MainWindow", "Preferences"))
        self.menuMetrics.setTitle(_translate("MainWindow", "Metrics"))
        self.menuFunction_Points.setTitle(_translate("MainWindow", "Function Points"))
        self.menuUse_Case_Points.setTitle(_translate("MainWindow", "Use Case Points"))
        self.menuSMI.setTitle(_translate("MainWindow", "SMI"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.changeLanguageButton.setText(_translate("MainWindow", "Language"))
        self.enterFPDataButton.setText(_translate("MainWindow", "Enter FP Data"))
        self.actionExit_2.setText(_translate("MainWindow", "Exit"))
        self.enterUseCasePoints.setText(_translate("MainWindow", "Enter Use Case Data"))
        self.enterSMI.setText(_translate("MainWindow", "Calculate SMI"))
