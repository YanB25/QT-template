import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
class ComboxDemo(QWidget):
    def __init__(self, parent=None):
        super(ComboxDemo, self).__init__(parent)
        self.layout = QVBoxLayout()
        self.lbl = QLabel("abc")

        self.cb = QComboBox()
        self.cb.addItems(["C", "C++", "C#", "Java"])
        self.cb.currentIndexChanged.connect(self.selectionchange)

        self.layout.addWidget(self.lbl)
        self.layout.addWidget(self.cb)
        self.setLayout(self.layout)
        
    def selectionchange(self, i):
        self.lbl.setText(self.cb.currentText())
