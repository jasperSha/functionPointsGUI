# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SelectLanguageWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SelectLanguageWindow(object):
    def setupUi(self, SelectLanguageWindow):
        self.slwwin = SelectLanguageWindow
        SelectLanguageWindow.setObjectName("SelectLanguageWindow")
        SelectLanguageWindow.setWindowModality(QtCore.Qt.WindowModal)
        SelectLanguageWindow.resize(259, 570)
        SelectLanguageWindow.setWindowTitle("")
        self.confirmationBox = QtWidgets.QDialogButtonBox(SelectLanguageWindow)
        self.confirmationBox.setGeometry(QtCore.QRect(10, 500, 181, 41))
        self.confirmationBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.confirmationBox.setObjectName("confirmationBox")

        self.confirmationBox.accepted.connect(SelectLanguageWindow.close)
        self.confirmationBox.rejected.connect(SelectLanguageWindow.close)

        self.label = QtWidgets.QLabel(SelectLanguageWindow)
        self.label.setGeometry(QtCore.QRect(30, 20, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(SelectLanguageWindow)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 60, 161, 441))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioAssembler = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioAssembler.setFont(font)
        self.radioAssembler.setObjectName("radioAssembler")
        self.languageGroup = QtWidgets.QButtonGroup(SelectLanguageWindow)
        self.languageGroup.setObjectName("languageGroup")
        self.languageGroup.addButton(self.radioAssembler)
        self.verticalLayout.addWidget(self.radioAssembler)
        self.radioAda95 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioAda95.setFont(font)
        self.radioAda95.setObjectName("radioAda95")
        self.languageGroup.addButton(self.radioAda95)
        self.verticalLayout.addWidget(self.radioAda95)
        self.radioC = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioC.setFont(font)
        self.radioC.setObjectName("radioC")
        self.languageGroup.addButton(self.radioC)
        self.verticalLayout.addWidget(self.radioC)
        self.radioCPlusPlus = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioCPlusPlus.setFont(font)
        self.radioCPlusPlus.setObjectName("radioCPlusPlus")
        self.languageGroup.addButton(self.radioCPlusPlus)
        self.verticalLayout.addWidget(self.radioCPlusPlus)
        self.radioCSharp = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioCSharp.setFont(font)
        self.radioCSharp.setObjectName("radioCSharp")
        self.languageGroup.addButton(self.radioCSharp)
        self.verticalLayout.addWidget(self.radioCSharp)
        self.radioCOBOL = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioCOBOL.setFont(font)
        self.radioCOBOL.setObjectName("radioCOBOL")
        self.languageGroup.addButton(self.radioCOBOL)
        self.verticalLayout.addWidget(self.radioCOBOL)
        self.radioFORTRAN = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioFORTRAN.setFont(font)
        self.radioFORTRAN.setObjectName("radioFORTRAN")
        self.languageGroup.addButton(self.radioFORTRAN)
        self.verticalLayout.addWidget(self.radioFORTRAN)
        self.radioHTML = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioHTML.setFont(font)
        self.radioHTML.setObjectName("radioHTML")
        self.languageGroup.addButton(self.radioHTML)
        self.verticalLayout.addWidget(self.radioHTML)
        self.radioJava = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioJava.setFont(font)
        self.radioJava.setObjectName("radioJava")
        self.languageGroup.addButton(self.radioJava)
        self.verticalLayout.addWidget(self.radioJava)
        self.radioJavaScript = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioJavaScript.setFont(font)
        self.radioJavaScript.setObjectName("radioJavaScript")
        self.languageGroup.addButton(self.radioJavaScript)
        self.verticalLayout.addWidget(self.radioJavaScript)
        self.radioVBScript = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioVBScript.setFont(font)
        self.radioVBScript.setObjectName("radioVBScript")
        self.languageGroup.addButton(self.radioVBScript)
        self.verticalLayout.addWidget(self.radioVBScript)
        self.radioVisualBasic = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioVisualBasic.setFont(font)
        self.radioVisualBasic.setObjectName("radioVisualBasic")
        self.languageGroup.addButton(self.radioVisualBasic)
        self.verticalLayout.addWidget(self.radioVisualBasic)

        self.retranslateUi(SelectLanguageWindow)
        QtCore.QMetaObject.connectSlotsByName(SelectLanguageWindow)

    def retranslateUi(self, SelectLanguageWindow):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("SelectLanguageWindow", "Select one language"))
        self.radioAssembler.setText(_translate("SelectLanguageWindow", "Assembler"))
        self.radioAda95.setText(_translate("SelectLanguageWindow", "Ada 95"))
        self.radioC.setText(_translate("SelectLanguageWindow", "C"))
        self.radioCPlusPlus.setText(_translate("SelectLanguageWindow", "C++"))
        self.radioCSharp.setText(_translate("SelectLanguageWindow", "C#"))
        self.radioCOBOL.setText(_translate("SelectLanguageWindow", "COBOL"))
        self.radioFORTRAN.setText(_translate("SelectLanguageWindow", "FORTRAN"))
        self.radioHTML.setText(_translate("SelectLanguageWindow", "HTML"))
        self.radioJava.setText(_translate("SelectLanguageWindow", "Java"))
        self.radioJavaScript.setText(_translate("SelectLanguageWindow", "JavaScript"))
        self.radioVBScript.setText(_translate("SelectLanguageWindow", "VBScript"))
        self.radioVisualBasic.setText(_translate("SelectLanguageWindow", "Visual Basic"))
