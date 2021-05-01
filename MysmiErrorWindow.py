from generated_ui.prod_ui.smiERRORWindow import *
from PyQt5.QtWidgets import *

class MysmiErrorWindow(QDialog, Ui_Dialog):
    def __init__(self, window):
        QDialog.__init__(self, window)
        self.setupUi(window)