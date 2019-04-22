import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

# Subclass QMainWindow to customise your application's main window
class Window(QWidget):

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)

        self.setWindowTitle("My Awesome App")

        self.__init_data()

        # set layout
        self.__layout()

        self.add_result_label()
        self.add_left_comboBox()
        self.add_plus_label()
        self.add_right_comboBox()

    def __init_data(self):
        '''
        init global datas for the app.
        '''
        self.ls = [str(i) for i in range(10)]
        self.left = 0
        self.right = 0

    def __layout(self):
        self.grid = QGridLayout()
        self.grid.setSpacing(20)
        self.setLayout(self.grid)
    
    def add_plus_label(self):
        self.grid.addWidget(QLabel('+'), 0, 1)

    def add_left_comboBox(self):
        self.left_combo_box = QComboBox()
        self.grid.addWidget(self.left_combo_box, 0, 0)
        self.left_combo_box.currentTextChanged.connect(
            lambda i: self.__combobox_clicked(i, 'left')
        )
        self.left_combo_box.addItems(self.ls)
    
    def add_right_comboBox(self):
        self.right_combo_box = QComboBox()
        self.grid.addWidget(self.right_combo_box, 0, 2)
        self.right_combo_box.currentTextChanged.connect(
            lambda i: self.__combobox_clicked(i, 'right')
        )
        self.right_combo_box.addItems(self.ls)
    
    def add_result_label(self):
        self.result_label = QLabel()
        self.grid.addWidget(self.result_label, 2, 1)

    def __combobox_clicked(self, val, name):
        if name == 'left':
            self.left = int(val)
        elif name == 'right':
            self.right = int(val)
        self.result_label.setText('{}'.format(self.left + self.right))
        
        

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    app.exec_()