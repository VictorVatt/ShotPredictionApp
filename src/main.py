import sys
from timer import Timer
from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile, QTimer, QTime
from ui import Ui_mainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setFixedSize(756, 695)
        self.isRecording = False
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.timer = Timer(self.ui)



if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())