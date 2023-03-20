import sys
from timer import Timer
from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from PySide6.QtCore import QFile, QTimer, QTime, QThread
from ui_app import Ui_mainWindow
from imu_connetion import IMU_connection


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setFixedSize(756, 695)
        self.isRecording = False
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.timer = Timer(self.ui)
        self.thread = QThread()
        self.imu_connection = IMU_connection(self.ui)
        self.imu_connection.moveToThread(self.thread)
        self.ui.connetionBtn_2.clicked.connect(self.imu_connection.run)
        self.thread.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())