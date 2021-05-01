from generated_ui.dev_ui.SMITab import *

from PyQt5.QtWidgets import *
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator

class NumericDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        editor = super(NumericDelegate, self).createEditor(parent, option, index)
        if isinstance(editor, QLineEdit):
            reg_ex = QRegExp("^(0|[1-9][0-9]*)")
            validator = QRegExpValidator(reg_ex, editor)
            editor.setValidator(validator)
        return editor

class MySMITab(QWidget, Ui_SMIForm):
    def __init__(self, window, pane, loaded=False):
        QWidget.__init__(self, window)
        self.setupUi(window)
        self.paneID = pane.paneID
        self.rowCount = 0
        self.rowIndex = 0

        # numeric, no leading zeroes validation for input
        delegate = NumericDelegate(self.modulesTable)
        self.modulesTable.setItemDelegate(delegate)

        # for reference only
        self.columns = ["SMI", "MA", "MC", "MD", "TM"]
        self.columnCount = 5

        # columns that cannot be edited by user
        self.SMI_COLUMN = 0
        self.TM_COLUMN = 4

        if loaded:
            smi = pane.SMI
            ma = pane.MA
            mc = pane.MC
            md = pane.MD
            tm = pane.TM

            

            self.rowCount = len(smi) # for reading rows
            self.rowIndex = len(smi) # for row insertion
            for row in range(self.rowIndex):
                self.modulesTable.insertRow(row)
                self.modulesTable.setRowHeight(row, 15)
                self.modulesTable.setColumnWidth(5, 142)

                smiItem = QTableWidgetItem(str(smi[row]))
                maItem = QTableWidgetItem(str(ma[row]))
                mcItem = QTableWidgetItem(str(mc[row]))
                mdItem = QTableWidgetItem(str(md[row]))
                tmItem = QTableWidgetItem(str(tm[row]))

                smiItem.setFlags(smiItem.flags() ^ QtCore.Qt.ItemIsEditable)
                tmItem.setFlags(tmItem.flags() ^ QtCore.Qt.ItemIsEditable)
        
                # modules cannot be deleted/changed in first row
                if row == 0:
                    mcItem.setFlags(mcItem.flags() ^ QtCore.Qt.ItemIsEditable)
                    mdItem.setFlags(mdItem.flags() ^ QtCore.Qt.ItemIsEditable)

                self.modulesTable.setItem(row, 0, smiItem)
                self.modulesTable.setItem(row, 1, maItem)
                self.modulesTable.setItem(row, 2, mcItem)
                self.modulesTable.setItem(row, 3, mdItem)
                self.modulesTable.setItem(row, 4, tmItem)
        else:
            # insert initial row
            self.modulesTable.insertRow(self.rowIndex)
            self.modulesTable.setRowHeight(self.rowIndex, 15)
            self.modulesTable.setColumnWidth(self.columnCount, 142)

            maItem = QTableWidgetItem(str(0))
            self.modulesTable.setItem(self.rowIndex, 1, maItem)

            # modules cannot be deleted or changed in the first row
            mcItem = QTableWidgetItem(str(0))
            mcItem.setFlags(mcItem.flags() ^ QtCore.Qt.ItemIsEditable)

            mdItem = QTableWidgetItem(str(0))
            mdItem.setFlags(mdItem.flags() ^ QtCore.Qt.ItemIsEditable)

            self.modulesTable.setItem(self.rowIndex, 2, mcItem)
            self.modulesTable.setItem(self.rowIndex, 3, mdItem)

            # SMI and total modules cannot be modified by user
            smiItem = QTableWidgetItem(str(0))
            smiItem.setFlags(smiItem.flags() ^ QtCore.Qt.ItemIsEditable)
            self.modulesTable.setItem(self.rowIndex, self.SMI_COLUMN, smiItem)

            tmItem = QTableWidgetItem(str(0))
            tmItem.setFlags(tmItem.flags() ^ QtCore.Qt.ItemIsEditable)
            self.modulesTable.setItem(self.rowIndex, self.TM_COLUMN, tmItem)

            # current row done, now increment index (for future insertions)
            self.rowIndex += 1

            # add to row count
            self.rowCount += 1

        self.computeIndexButton.clicked.connect(self.compute_index)
        self.computeIndexButton.clicked.connect(self.get_table)
        self.addRowButton.clicked.connect(self.add_row)




    def compute_index(self):

        # first row
        ma = int(self.modulesTable.item(0, 1).text())
        tmItem = QTableWidgetItem(str(ma))
        self.modulesTable.setItem(0, 4, tmItem)

        table = self.modulesTable
        for row in range(1, self.rowCount):
            prevTM = int(table.item(row-1, 4).text())
            # if '0' in [table.item(row, 1).text(), table.item(row, 2).text(), table.item(row, 3).text()]:
            #     return
            ma = int(table.item(row, 1).text())
            mc = int(table.item(row, 2).text())
            md = int(table.item(row, 3).text())

            tm = prevTM + ma - md
            tmItem = QTableWidgetItem(str(tm))
            self.modulesTable.setItem(row, 4, tmItem)

            smi = (tm - (ma + mc + md)) / tm
            smiItem = QTableWidgetItem(str(smi))
            self.modulesTable.setItem(row, 0, smiItem)

                    

    def add_row(self):
        self.modulesTable.insertRow(self.rowIndex)
        self.modulesTable.setRowHeight(self.rowIndex, 15)
        self.modulesTable.setColumnWidth(self.columnCount, 142)

        # SMI and total modules cannot be modified by user
        smiItem = QTableWidgetItem(str(0))
        smiItem.setFlags(smiItem.flags() ^ QtCore.Qt.ItemIsEditable)
        self.modulesTable.setItem(self.rowIndex, self.SMI_COLUMN, smiItem)

        maItem = QTableWidgetItem(str(0))
        self.modulesTable.setItem(self.rowIndex, 1, maItem)

        mcItem = QTableWidgetItem(str(0))
        self.modulesTable.setItem(self.rowIndex, 2, mcItem)

        mdItem = QTableWidgetItem(str(0))
        self.modulesTable.setItem(self.rowIndex, 3, mdItem)

        tmItem = QTableWidgetItem(str(0))
        tmItem.setFlags(tmItem.flags() ^ QtCore.Qt.ItemIsEditable)
        self.modulesTable.setItem(self.rowIndex, self.TM_COLUMN, tmItem)

        self.rowIndex += 1 # for future insertions
        self.rowCount += 1 # added a row

    
    def get_table(self):
        table = self.modulesTable

        smi, ma, mc, md, tm = ([] for i in range(5))

        for row in range(self.rowCount):
            smi.append(float(table.item(row, 0).text()))
            ma.append(int(table.item(row, 1).text()))
            mc.append(int(table.item(row, 2).text()))
            md.append(int(table.item(row, 3).text()))
            tm.append(int(table.item(row, 4).text()))

        return {'smi': smi, 'ma': ma, 'mc': mc, 'md': md, 'tm': tm}

