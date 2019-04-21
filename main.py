import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

# Subclass QMainWindow to customise your application's main window
class Window(QWidget):

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)

        self.init()

        self.result = QLabel('')

        self.setWindowTitle("My Awesome App")

        self.grid = QGridLayout()
        self.grid.setSpacing(3)

        self.cb = QComboBox()
        self.cb2 = QComboBox()
        self.cb.currentIndexChanged.connect(self.select)
        self.cb2.currentIndexChanged.connect(self.select2)

        self.grid.addWidget(self.cb, 0, 0)
        self.grid.addWidget(QLabel('+'), 0, 1)
        self.grid.addWidget(self.cb2, 0, 2)
        self.grid.addWidget(self.result, 2, 1)

        self.setLayout(self.grid)


        self.initCB()
        self.initCB2()


    def init(self):
        self.left = 0
        self.right = 0
        self.ls = [str(i) for i in range(10)]

    def initCB(self):
        self.cb.addItems(self.ls)
        self.cb.currentIndexChanged.connect(self.select)
    def initCB2(self):
        self.cb2.addItems(self.ls)
        self.cb2.currentIndexChanged.connect(self.select)
    def select(self, i):
        self.left = i
        print(i)
        self.onchange()
    def select2(self, i):
        self.right = i
        print(i)
        self.onchange()
    def onchange(self):
        self.result.setText('{}'.format(int(self.left) + int(self.right)))

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    app.exec_()
