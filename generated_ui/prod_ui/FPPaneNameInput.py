# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FPPaneNameInput.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FPPaneNameInputWindow(object):
    def setupUi(self, FPPaneNameInputWindow):
        FPPaneNameInputWindow.setObjectName("FPPaneNameInputWindow")
        FPPaneNameInputWindow.resize(308, 140)
        self.buttonBox = QtWidgets.QDialogButtonBox(FPPaneNameInputWindow)
        self.buttonBox.setGeometry(QtCore.QRect(-90, 80, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(FPPaneNameInputWindow)
        self.label.setGeometry(QtCore.QRect(90, 10, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.fpInputBox = QtWidgets.QLineEdit(FPPaneNameInputWindow)
        self.fpInputBox.setGeometry(QtCore.QRect(50, 50, 201, 20))
        self.fpInputBox.setObjectName("fpInputBox")

        self.retranslateUi(FPPaneNameInputWindow)
        self.buttonBox.accepted.connect(FPPaneNameInputWindow.accept)
        self.buttonBox.rejected.connect(FPPaneNameInputWindow.reject)
        QtCore.QMetaObject.connectSlotsByName(FPPaneNameInputWindow)

    def retranslateUi(self, FPPaneNameInputWindow):
        _translate = QtCore.QCoreApplication.translate
        FPPaneNameInputWindow.setWindowTitle(_translate("FPPaneNameInputWindow", "Input"))
        self.label.setText(_translate("FPPaneNameInputWindow", "Name of this FP"))
