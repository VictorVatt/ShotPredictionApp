import sys
from timer import Timer
from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile, QTimer, QTime
from src import interface


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setFixedSize(756, 695)
        self.isRecording = False
        self.ui = interface.Ui_mainWindow()
        self.ui.setupUi(self)
        self.timer = Timer(self.ui)
        self.ui.recordButton.clicked.connect(self.timer.startTimer)

    def handleRecording(self):


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())