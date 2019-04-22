from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import random
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=3, height=3):
        fig = Figure(figsize=(width, height))

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()
    
    # 如果数据太过复杂，可以把这个函数注释掉，然后在外部指挥画图
    def plot(self):
        data = [random.random() for i in range(25)]
        ax = self.figure.add_subplot(211)
        ax.plot(data, 'r-')
        ax.set_title('PyQt Matplotlib Example')

        ax = self.figure.add_subplot(212)
        ax.plot(data, 'r+')
        ax.set_title('hello')

        self.draw()

