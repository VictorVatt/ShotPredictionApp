from PySide6.QtCharts import (QAreaSeries, QBarSet, QChart, QChartView,
                              QLineSeries, QPieSeries, QScatterSeries,
                              QSplineSeries, QStackedBarSeries, QPieSlice, QBarSeries)
from PySide6.QtWidgets import (QApplication, QMainWindow, QSizePolicy,
    QWidget)
from PySide6.QtGui import QBrush, QColor, QPainter, QFont
from random import random, uniform
from PySide6.QtCore import QPointF, Qt
import pandas as pd

class Plot():
        def __init__(self, ui, shots):
            self.ui = ui
            self.shots = shots
            self.data_shots = pd.DataFrame({'typeofshot': shots})
            mapping = {0: 'Serve', 1: 'Forehand', 2: 'Backhand', 3: 'Forehand Volley', 4: 'Backhand volley'}
            self.data_shots['typeofshot'] = self.data_shots['typeofshot'].replace(mapping, regex=True)
            print(self.data_shots)

            chart_view = QChartView(self.create_pie_chart())
            self.ui.gridLayout.addWidget(chart_view, 0, 0, 1, 2)
            chart_view.chart().setBackgroundBrush(QBrush(QColor("transparent")))
            chart_view = QChartView(self.create_bar_chart())
            self.ui.gridLayout.addWidget(chart_view, 0, 2, 1, 2)
            chart_view.chart().setBackgroundBrush(QBrush(QColor("transparent")))

        def create_pie_chart(self):
            category_count = self.data_shots["typeofshot"].value_counts()

            # Création de la série de données pour le PieChart
            series = QPieSeries()

            # Ajout des fréquences de chaque catégorie au PieChart
            for index, value in category_count.items():
                label = str(index)
                series.append(label, value)

            series.setPieSize(1)
            # Création du PieChart
            chart = QChart()
            legend = chart.legend()
            font = QFont()
            font.setPointSize(11)  # set font size to 14
            legend.setFont(font)  # apply new font size to legend
            chart.addSeries(series)
            chart.setTitle("Titre")
            chart.legend().setAlignment(Qt.AlignLeft)


            return chart

        def create_bar_chart(self):
            category_count = self.data_shots["typeofshot"].value_counts()
            barSeries = QBarSeries()
            for index, value in category_count.items():
                label = str(index)
                barSeries.append(value)

            chart = QChart()
            chart.addSeries(barSeries)
            chart.setTitle('Exemple de graphique à barres')

            axisX = chart.createDefaultAxes()
            axisY = chart.createDefaultAxes()
            axisY.setTitleText('Valeurs')

            return chart
    #def plot_shot_distribution(self):
        # Create a DataFrame
        #df = pd.DataFrame({"TypeOfShots": self.typeofshots})
        #mapping = {0: "Serve", 1: "Forehand", 2: "Backhand", 3: "Forehand Volley", 4 : "Backhand Volley"}
        #df["TypeOfShots"] = df["TypeOfShots"].replace(mapping, regex=True)
        # Count the number of each type
        #shot_counts = df['TypeOfShots'].value_counts()
        #print(shot_counts)
        #colors = ['green', 'orange', 'grey', 'purple', 'red']

        # Création du graphique en barres
        #fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.71, 2.11))
        #ax1.bar(shot_counts.index, shot_counts.values, color=colors)
        #plt.title('Distribution of the different shots')
        #plt.ylabel('Number of shots')

        # Ajout du nombre de coups sur chaque barre
        #for i, v in enumerate(shot_counts.values):
            #ax1.text(i, v, str(v), ha='center', va='bottom', )

        # Création du graphique circulaire
        #ax2.pie(shot_counts.values, labels=shot_counts.index, autopct='%1.1f%%', colors=colors)
        #self.ui.results_graph(fig)

