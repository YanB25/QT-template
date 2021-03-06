import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from components.plot_canvas import PlotCanvas
from components.demo import ComboxDemo

# Subclass QMainWindow to customise your application's main window
class Window(QMainWindow):

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
        
        self.add_inputbox()
        self.add_new_dialog_button()

        self.add_open_file_button()

        # self.add_matplotlib_figure()

        # self.add_local_image()

        self.add_combox_demo()

    def __init_data(self):
        '''
        init global datas for the app.
        '''
        self.ls = [str(i) for i in range(10)]
        self.left = 0
        self.right = 0

    def __layout(self):
        '''
        set the global layout of the window.
        window.setLayout is not valid, so add a middleware `main_frame`
        '''
        self.grid = QGridLayout()
        self.grid.setSpacing(20)
        main_frame = QWidget()
        main_frame.setLayout(self.grid)
        self.setCentralWidget(main_frame)    

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

    def add_inputbox(self):
        self.middle_inputbox = QLineEdit()
        self.grid.addWidget(self.middle_inputbox, 1, 1)
        # below first one handle the `Enter` pressed.
        # the second one handle when content changed.
        # self.middle_inputbox.returnPressed.connect(self.__middle_inputbox_pressed)
        self.middle_inputbox.textChanged.connect(self.__middle_inputbox_pressed)
    
    def add_open_file_button(self):
        self.open_file_button = QPushButton('open file')
        self.grid.addWidget(self.open_file_button, 3, 1)
        self.open_file_button.clicked.connect(self.show_open_file_dialog)

    def add_new_dialog_button(self):
        self.new_dialog_button = QPushButton('new dialog')
        self.grid.addWidget(self.new_dialog_button, 4, 1)
        self.new_dialog_button.clicked.connect(self.__show_new_dialog)
    
    def show_open_file_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, 'QFileDialog.getOpenFileName()', '', 'All Files (*);;CSV (*.csv)', options=options)
        if fileName:
            print(fileName)

    
    def add_matplotlib_figure(self):
        self.figure = PlotCanvas(self)
        self.grid.addWidget(self.figure, 5, 1)
    
    def add_local_image(self):
        self.image_label = QLabel()
        pixmap = QPixmap('example.png')
        pixmap = pixmap.scaled(64, 64)
        self.image_label.setPixmap(pixmap)
        self.grid.addWidget(self.image_label, 10, 1)
        print(self.image_label.width())
    
    def add_combox_demo(self):
        self.combox_demo = ComboxDemo()
        self.grid.addWidget(self.combox_demo, 6, 1)

    def __combobox_clicked(self, val, name):
        if name == 'left':
            self.left = int(val)
        elif name == 'right':
            self.right = int(val)
        self.result_label.setText('{}'.format(self.left + self.right))
    def __slot_open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, 'Open File', '/home/yanbin/')
    

    def __slot_show_open_file_dialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')
        print(fname)

    def __middle_inputbox_pressed(self):
        print('INPUT BOX GET: {}'.format(self.middle_inputbox.text()))

    def __show_new_dialog(self):
        QMessageBox.about(self, "Title", "You click me!")
        
        

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    app.exec_()
