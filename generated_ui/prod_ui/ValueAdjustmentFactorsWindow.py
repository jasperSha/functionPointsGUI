# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ValueAdjustmentFactorsWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ValueAdjustmentFactorsWindow(object):
    def setupUi(self, ValueAdjustmentFactorsWindow):
        self.vafWin = ValueAdjustmentFactorsWindow

        ValueAdjustmentFactorsWindow.setObjectName("ValueAdjustmentFactorsWindow")
        ValueAdjustmentFactorsWindow.setWindowModality(QtCore.Qt.WindowModal)
        ValueAdjustmentFactorsWindow.resize(763, 486)
        self.buttonBox = QtWidgets.QDialogButtonBox(ValueAdjustmentFactorsWindow)
        self.buttonBox.setGeometry(QtCore.QRect(70, 440, 156, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(ValueAdjustmentFactorsWindow)
        self.label.setGeometry(QtCore.QRect(160, 20, 451, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.formLayoutWidget = QtWidgets.QWidget(ValueAdjustmentFactorsWindow)
        self.formLayoutWidget.setGeometry(QtCore.QRect(70, 60, 666, 371))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.label_12 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_14 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.label_15 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.label_13 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.first = QtWidgets.QComboBox(self.formLayoutWidget)
        self.first.setMaxVisibleItems(6)
        self.first.setMaxCount(6)
        self.first.setObjectName("first")
        self.first.addItem("")
        self.first.addItem("")
        self.first.addItem("")
        self.first.addItem("")
        self.first.addItem("")
        self.first.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.first)
        self.second = QtWidgets.QComboBox(self.formLayoutWidget)
        self.second.setMaxVisibleItems(6)
        self.second.setMaxCount(6)
        self.second.setObjectName("second")
        self.second.addItem("")
        self.second.addItem("")
        self.second.addItem("")
        self.second.addItem("")
        self.second.addItem("")
        self.second.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.second)
        self.third = QtWidgets.QComboBox(self.formLayoutWidget)
        self.third.setMaxVisibleItems(6)
        self.third.setMaxCount(6)
        self.third.setObjectName("third")
        self.third.addItem("")
        self.third.addItem("")
        self.third.addItem("")
        self.third.addItem("")
        self.third.addItem("")
        self.third.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.third)
        self.fourth = QtWidgets.QComboBox(self.formLayoutWidget)
        self.fourth.setMaxVisibleItems(6)
        self.fourth.setMaxCount(6)
        self.fourth.setObjectName("fourth")
        self.fourth.addItem("")
        self.fourth.addItem("")
        self.fourth.addItem("")
        self.fourth.addItem("")
        self.fourth.addItem("")
        self.fourth.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.fourth)
        self.fifth = QtWidgets.QComboBox(self.formLayoutWidget)
        self.fifth.setMaxVisibleItems(6)
        self.fifth.setMaxCount(6)
        self.fifth.setObjectName("fifth")
        self.fifth.addItem("")
        self.fifth.addItem("")
        self.fifth.addItem("")
        self.fifth.addItem("")
        self.fifth.addItem("")
        self.fifth.addItem("")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.fifth)
        self.sixth = QtWidgets.QComboBox(self.formLayoutWidget)
        self.sixth.setMaxVisibleItems(6)
        self.sixth.setMaxCount(6)
        self.sixth.setObjectName("sixth")
        self.sixth.addItem("")
        self.sixth.addItem("")
        self.sixth.addItem("")
        self.sixth.addItem("")
        self.sixth.addItem("")
        self.sixth.addItem("")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.sixth)
        self.seventh = QtWidgets.QComboBox(self.formLayoutWidget)
        self.seventh.setMaxVisibleItems(6)
        self.seventh.setMaxCount(6)
        self.seventh.setObjectName("seventh")
        self.seventh.addItem("")
        self.seventh.addItem("")
        self.seventh.addItem("")
        self.seventh.addItem("")
        self.seventh.addItem("")
        self.seventh.addItem("")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.seventh)
        self.eighth = QtWidgets.QComboBox(self.formLayoutWidget)
        self.eighth.setMaxVisibleItems(6)
        self.eighth.setMaxCount(6)
        self.eighth.setObjectName("eighth")
        self.eighth.addItem("")
        self.eighth.addItem("")
        self.eighth.addItem("")
        self.eighth.addItem("")
        self.eighth.addItem("")
        self.eighth.addItem("")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.eighth)
        self.ninth = QtWidgets.QComboBox(self.formLayoutWidget)
        self.ninth.setMaxVisibleItems(6)
        self.ninth.setMaxCount(6)
        self.ninth.setObjectName("ninth")
        self.ninth.addItem("")
        self.ninth.addItem("")
        self.ninth.addItem("")
        self.ninth.addItem("")
        self.ninth.addItem("")
        self.ninth.addItem("")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.ninth)
        self.tenth = QtWidgets.QComboBox(self.formLayoutWidget)
        self.tenth.setMaxVisibleItems(6)
        self.tenth.setMaxCount(6)
        self.tenth.setObjectName("tenth")
        self.tenth.addItem("")
        self.tenth.addItem("")
        self.tenth.addItem("")
        self.tenth.addItem("")
        self.tenth.addItem("")
        self.tenth.addItem("")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.tenth)
        self.eleventh = QtWidgets.QComboBox(self.formLayoutWidget)
        self.eleventh.setMaxVisibleItems(6)
        self.eleventh.setMaxCount(6)
        self.eleventh.setObjectName("eleventh")
        self.eleventh.addItem("")
        self.eleventh.addItem("")
        self.eleventh.addItem("")
        self.eleventh.addItem("")
        self.eleventh.addItem("")
        self.eleventh.addItem("")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.eleventh)
        self.twelfth = QtWidgets.QComboBox(self.formLayoutWidget)
        self.twelfth.setMaxVisibleItems(6)
        self.twelfth.setMaxCount(6)
        self.twelfth.setObjectName("twelfth")
        self.twelfth.addItem("")
        self.twelfth.addItem("")
        self.twelfth.addItem("")
        self.twelfth.addItem("")
        self.twelfth.addItem("")
        self.twelfth.addItem("")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.twelfth)
        self.thirteenth = QtWidgets.QComboBox(self.formLayoutWidget)
        self.thirteenth.setMaxVisibleItems(6)
        self.thirteenth.setMaxCount(6)
        self.thirteenth.setObjectName("thirteenth")
        self.thirteenth.addItem("")
        self.thirteenth.addItem("")
        self.thirteenth.addItem("")
        self.thirteenth.addItem("")
        self.thirteenth.addItem("")
        self.thirteenth.addItem("")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.thirteenth)
        self.fourteenth = QtWidgets.QComboBox(self.formLayoutWidget)
        self.fourteenth.setMaxVisibleItems(6)
        self.fourteenth.setMaxCount(6)
        self.fourteenth.setObjectName("fourteenth")
        self.fourteenth.addItem("")
        self.fourteenth.addItem("")
        self.fourteenth.addItem("")
        self.fourteenth.addItem("")
        self.fourteenth.addItem("")
        self.fourteenth.addItem("")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.fourteenth)

        self.retranslateUi(ValueAdjustmentFactorsWindow)
        self.first.setCurrentIndex(0)
        self.second.setCurrentIndex(0)
        self.third.setCurrentIndex(0)
        self.fourth.setCurrentIndex(0)
        self.fifth.setCurrentIndex(0)
        self.sixth.setCurrentIndex(0)
        self.seventh.setCurrentIndex(0)
        self.eighth.setCurrentIndex(0)
        self.ninth.setCurrentIndex(0)
        self.tenth.setCurrentIndex(0)
        self.eleventh.setCurrentIndex(0)
        self.twelfth.setCurrentIndex(0)
        self.thirteenth.setCurrentIndex(0)
        self.fourteenth.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ValueAdjustmentFactorsWindow)

    def retranslateUi(self, ValueAdjustmentFactorsWindow):
        _translate = QtCore.QCoreApplication.translate
        ValueAdjustmentFactorsWindow.setWindowTitle(_translate("ValueAdjustmentFactorsWindow", "Value Adjustment Factors"))
        self.label.setText(_translate("ValueAdjustmentFactorsWindow", "Assign a value from 0 to 5 for each of the following Value Adjustment Factors"))
        self.label_2.setText(_translate("ValueAdjustmentFactorsWindow", "Does the system require reliable backup and recovery processes?"))
        self.label_4.setText(_translate("ValueAdjustmentFactorsWindow", "Are specialized data communications required to transfer information to or from the application?"))
        self.label_9.setText(_translate("ValueAdjustmentFactorsWindow", "Are there distributed processing functions?"))
        self.label_12.setText(_translate("ValueAdjustmentFactorsWindow", "Is performance critical?"))
        self.label_5.setText(_translate("ValueAdjustmentFactorsWindow", "Will the system run in an existing, heavily utilized operational environment?"))
        self.label_14.setText(_translate("ValueAdjustmentFactorsWindow", "Does the system require online data entry?"))
        self.label_15.setText(_translate("ValueAdjustmentFactorsWindow", "Does the online data entry require the input transaction to be built over multiple screens or operations?"))
        self.label_13.setText(_translate("ValueAdjustmentFactorsWindow", "Are the internal logical files updated online?"))
        self.label_10.setText(_translate("ValueAdjustmentFactorsWindow", "Are the input, output, files or inquiries complex?"))
        self.label_11.setText(_translate("ValueAdjustmentFactorsWindow", "Is the internal processing complex?"))
        self.label_8.setText(_translate("ValueAdjustmentFactorsWindow", "Is the code designed to be reusable?"))
        self.label_7.setText(_translate("ValueAdjustmentFactorsWindow", "Are conversion and installation included in the design?"))
        self.label_6.setText(_translate("ValueAdjustmentFactorsWindow", "Is the system designed for multiple installations in differnet organizations?"))
        self.label_3.setText(_translate("ValueAdjustmentFactorsWindow", "Is the application designed to facilitate change and ease of use by the user?"))
        self.first.setItemText(0, _translate("ValueAdjustmentFactorsWindow", "0"))
        self.first.setItemText(1, _translate("ValueAdjustmentFactorsWindow", "1"))
        self.first.setItemText(2, _translate("ValueAdjustmentFactorsWindow", "2"))
        self.first.setItemText(3, _translate("ValueAdjustmentFactorsWindow", "3"))
        self.first.setItemText(4, _translate("ValueAdjustmentFactorsWindow", "4"))
        self.first.setItemText(5, _translate("ValueAdjustmentFactorsWindow", "5"))
        self.second.setItemText(0, _translate("ValueAdjustmentFactorsWindow", "0"))
        self.second.setItemText(1, _translate("ValueAdjustmentFactorsWindow", "1"))
        self.second.setItemText(2, _translate("ValueAdjustmentFactorsWindow", "2"))
        self.second.setItemText(3, _translate("ValueAdjustmentFactorsWindow", "3"))
        self.second.setItemText(4, _translate("ValueAdjustmentFactorsWindow", "4"))
        self.second.setItemText(5, _translate("ValueAdjustmentFactorsWindow", "5"))
        self.third.setItemText(0, _translate("ValueAdjustmentFactorsWindow", "0"))
        self.third.setItemText(1, _translate("ValueAdjustmentFactorsWindow", "1"))
        self.third.setItemText(2, _translate("ValueAdjustmentFactorsWindow", "2"))
        self.third.setItemText(3, _translate("ValueAdjustmentFactorsWindow", "3"))
        self.third.setItemText(4, _translate("ValueAdjustmentFactorsWindow", "4"))
        self.third.setItemText(5, _translate("ValueAdjustmentFactorsWindow", "5"))
        self.fourth.setItemText(0, _translate("ValueAdjustmentFactorsWindow", "0"))
        self.fourth.setItemText(1, _translate("ValueAdjustmentFactorsWindow", "1"))
        self.fourth.setItemText(2, _translate("ValueAdjustmentFactorsWindow", "2"))
        self.fourth.setItemText(3, _translate("ValueAdjustmentFactorsWindow", "3"))
        self.fourth.setItemText(4, _translate("ValueAdjustmentFactorsWindow", "4"))
        self.fourth.setItemText(5, _translate("ValueAdjustmentFactorsWindow", "5"))
        self.fifth.setItemText(0, _translate("ValueAdjustmentFactorsWindow", "0"))
        self.fifth.setItemText(1, _translate("ValueAdjustmentFactorsWindow", "1"))
        self.fifth.setItemText(2, _translate("ValueAdjustmentFactorsWindow", "2"))
        self.fifth.setItemText(3, _translate("ValueAdjustmentFactorsWindow", "3"))
        self.fifth.setItemText(4, _translate("ValueAdjustmentFactorsWindow", "4"))
        self.fifth.setItemText(5, _translate("ValueAdjustmentFactorsWindow", "5"))
        self.sixth.setItemText(0, _translate("ValueAdjustmentFactorsWindow", "0"))
        self.sixth.setItemText(1, _translate("ValueAdjustmentFactorsWindow", "1"))
        self.sixth.setItemText(2, _translate("ValueAdjustmentFactorsWindow", "2"))
        self.sixth.setItemText(3, _translate("ValueAdjustmentFactorsWindow", "3"))
        self.sixth.setItemText(4, _translate("ValueAdjustmentFactorsWindow", "4"))
        self.sixth.setItemText(5, _translate("ValueAdjustmentFactorsWindow", "5"))
        self.seventh.setItemText(0, _translate("ValueAdjustmentFactorsWindow", "0"))
        self.seventh.setItemText(1, _translate("ValueAdjustmentFactorsWindow", "1"))
        self.seventh.setItemText(2, _translate("ValueAdjustmentFactorsWindow", "2"))
        self.seventh.setItemText(3, _translate("ValueAdjustmentFactorsWindow", "3"))
        self.seventh.setItemText(4, _translate("ValueAdjustmentFactorsWindow", "4"))
        self.seventh.setItemText(5, _translate("ValueAdjustmentFactorsWindow", "5"))
        self.eighth.setItemText(0, _translate("ValueAdjustmentFactorsWindow", "0"))
        self.eighth.setItemText(1, _translate("ValueAdjustmentFactorsWindow", "1"))
        self.eighth.setItemText(2, _translate("ValueAdjustmentFactorsWindow", "2"))
        self.eighth.setItemText(3, _translate("ValueAdjustmentFactorsWindow", "3"))
        self.eighth.setItemText(4, _translate("ValueAdjustmentFactorsWindow", "4"))
        self.eighth.setItemText(5, _translate("ValueAdjustmentFactorsWindow", "5"))
        self.ninth.setItemText(0, _translate("ValueAdjustmentFactorsWindow", "0"))
        self.ninth.setItemText(1, _translate("ValueAdjustmentFactorsWindow", "1"))
        self.ninth.setItemText(2, _translate("ValueAdjustmentFactorsWindow", "2"))
        self.ninth.setItemText(3, _translate("ValueAdjustmentFactorsWindow", "3"))
        self.ninth.setItemText(4, _translate("ValueAdjustmentFactorsWindow", "4"))
        self.ninth.setItemText(5, _translate("ValueAdjustmentFactorsWindow", "5"))
        self.tenth.setItemText(0, _translate("ValueAdjustmentFactorsWindow", "0"))
        self.tenth.setItemText(1, _translate("ValueAdjustmentFactorsWindow", "1"))
        self.tenth.setItemText(2, _translate("ValueAdjustmentFactorsWindow", "2"))
        self.tenth.setItemText(3, _translate("ValueAdjustmentFactorsWindow", "3"))
        self.tenth.setItemText(4, _translate("ValueAdjustmentFactorsWindow", "4"))
        self.tenth.setItemText(5, _translate("ValueAdjustmentFactorsWindow", "5"))
        self.eleventh.setItemText(0, _translate("ValueAdjustmentFactorsWindow", "0"))
        self.eleventh.setItemText(1, _translate("ValueAdjustmentFactorsWindow", "1"))
        self.eleventh.setItemText(2, _translate("ValueAdjustmentFactorsWindow", "2"))
        self.eleventh.setItemText(3, _translate("ValueAdjustmentFactorsWindow", "3"))
        self.eleventh.setItemText(4, _translate("ValueAdjustmentFactorsWindow", "4"))
        self.eleventh.setItemText(5, _translate("ValueAdjustmentFactorsWindow", "5"))
        self.twelfth.setItemText(0, _translate("ValueAdjustmentFactorsWindow", "0"))
        self.twelfth.setItemText(1, _translate("ValueAdjustmentFactorsWindow", "1"))
        self.twelfth.setItemText(2, _translate("ValueAdjustmentFactorsWindow", "2"))
        self.twelfth.setItemText(3, _translate("ValueAdjustmentFactorsWindow", "3"))
        self.twelfth.setItemText(4, _translate("ValueAdjustmentFactorsWindow", "4"))
        self.twelfth.setItemText(5, _translate("ValueAdjustmentFactorsWindow", "5"))
        self.thirteenth.setItemText(0, _translate("ValueAdjustmentFactorsWindow", "0"))
        self.thirteenth.setItemText(1, _translate("ValueAdjustmentFactorsWindow", "1"))
        self.thirteenth.setItemText(2, _translate("ValueAdjustmentFactorsWindow", "2"))
        self.thirteenth.setItemText(3, _translate("ValueAdjustmentFactorsWindow", "3"))
        self.thirteenth.setItemText(4, _translate("ValueAdjustmentFactorsWindow", "4"))
        self.thirteenth.setItemText(5, _translate("ValueAdjustmentFactorsWindow", "5"))
        self.fourteenth.setItemText(0, _translate("ValueAdjustmentFactorsWindow", "0"))
        self.fourteenth.setItemText(1, _translate("ValueAdjustmentFactorsWindow", "1"))
        self.fourteenth.setItemText(2, _translate("ValueAdjustmentFactorsWindow", "2"))
        self.fourteenth.setItemText(3, _translate("ValueAdjustmentFactorsWindow", "3"))
        self.fourteenth.setItemText(4, _translate("ValueAdjustmentFactorsWindow", "4"))
        self.fourteenth.setItemText(5, _translate("ValueAdjustmentFactorsWindow", "5"))
