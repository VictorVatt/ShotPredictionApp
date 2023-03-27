from PySide6.QtCharts import (QAreaSeries, QBarSet, QChart, QChartView,
                              QLineSeries, QPieSeries, QScatterSeries,
                              QSplineSeries, QStackedBarSeries, QPieSlice, QBarSeries)
from PySide6.QtWidgets import (QApplication, QMainWindow, QSizePolicy,
                               QWidget)
from PySide6.QtGui import QBrush, QColor, QPainter, QFont
from random import random, uniform
from PySide6.QtCore import QPointF, Qt
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


class Plot:
    def __init__(self, ui, shots):
        self.ui = ui
        self.typeofshots = shots
        self.ax1 = None
        self.ax2 = None

    def create_charts(self):
        plt.style.use("dark_background")

        for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
            plt.rcParams[param] = '0.9'  # very light grey

        for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
            plt.rcParams[param] = '#212946'  # bluish dark grey

        colors = [
            '#08F7FE',  # teal/cyan
            '#FE53BB',  # pink
            '#F5D300',  # yellow
            '#00ff41',  # matrix green
        ]
        # Create a DataFrame
        df = pd.DataFrame({"TypeOfShots": self.typeofshots})
        mapping = {0: "Serve", 1: "Forehand", 2: "Backhand", 3: "Forehand Volley", 4: "Backhand Volley"}
        df["TypeOfShots"] = df["TypeOfShots"].replace(mapping, regex=True)
        # Count the number of each type
        shot_counts = df['TypeOfShots'].value_counts()
        print(shot_counts)

        # Création du graphique en barres
        fig, (self.ax1, self.ax2) = plt.subplots(1, 2, figsize=(8.71, 2.11))
        self.ax1.bar(shot_counts.index, shot_counts.values, color=colors)

        plt.title('Distribution of the different shots')
        plt.ylabel('Number of shots')

        # Ajout du nombre de coups sur chaque barre
        for i, v in enumerate(shot_counts.values):
            self.ax1.text(i, v, str(v), ha='center', va='bottom', )

        # Création du graphique circulaire
        self.ax2.pie(shot_counts.values, labels=shot_counts.index, autopct='%1.1f%%', colors=colors)
        plt.show()

