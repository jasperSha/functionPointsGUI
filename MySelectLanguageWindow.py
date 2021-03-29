from generated_ui.prod_ui.SelectLanguageWindow import *
from PyQt5.QtWidgets import *

class MySelectLanguageWindow(QDialog, Ui_SelectLanguageWindow):
    def __init__(self, window, setLanguage=None, preferredLanguage=None):
        QDialog.__init__(self, window)
        self.setupUi(window)
        self.lang = ''

        if preferredLanguage:
            self.lang = preferredLanguage
            for btn in self.languageGroup.buttons():
                if btn.objectName() == self.lang:
                    btn.setChecked(True)
        else:
            self.lang = setLanguage
            for btn in self.languageGroup.buttons():
                if btn.objectName() == self.lang:
                    btn.setChecked(True)

        self.confirmationBox.accepted.connect(self.set_language)
        self.confirmationBox.rejected.connect(self.cancel)

    def cancel(self):
        for btn in self.languageGroup.buttons():
            if btn.objectName() == self.lang:
                btn.setChecked(True)

    def set_language(self):
        for btn in self.languageGroup.buttons():
            if btn.isChecked():
                self.lang = btn.objectName()

    def get_language(self):
        return self.lang

        
        