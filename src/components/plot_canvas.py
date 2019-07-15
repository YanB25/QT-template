from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import random
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import seaborn as sns
import pandas as pd
import numpy as np

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=12, height=9):
    # def __init__(self, parent=None, width=4, height=3):
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
        # 下面被注释掉的例子是使用原生matplotlib画图
        # data = [random.random() for i in range(25)]
        # ax = self.figure.add_subplot(211)
        # ax.plot(data, 'r-')
        # ax.set_title('PyQt Matplotlib Example')

        # ax = self.figure.add_subplot(212)
        # ax.plot(data, 'r+')
        # ax.set_title('hello')

        ax = self.figure.add_subplot(2, 1, 1)
        data = pd.DataFrame()
        x = np.random.randint(0, 100, (100,))
        y = np.random.randint(0, 100, (100,))
        gender = np.random.choice(['Male', 'Female'], (100, ))
        data['x'] = x
        data['y'] = y
        data['gender'] = gender
        sns.relplot(data=data, x='x', y='y', style='gender', hue='gender', ax=ax)
        ax.set_title('example using seaborn')
        ax.set_ylabel('this is y label')
        # self.draw()

        ax = self.figure.add_subplot(2, 1, 2)
        data = pd.DataFrame()
        x = np.random.randint(0, 100, (100,))
        y = np.random.randint(0, 100, (100,))
        gender = np.random.choice(['Male', 'Female'], (100, ))
        data['time'] = x
        data['value'] = y
        data['gender'] = gender
        sns.relplot(data=data, x='time', y='value', style='gender', hue='gender', ax=ax, kind='line')
        ax.set_ylabel('this is y label')
        self.draw()

