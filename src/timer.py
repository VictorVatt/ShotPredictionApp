from PySide6 import QtCore
from PySide6.QtCore import QTimer


class Timer:

    def __init__(self, ui):
        self.ui = ui
        self.timer = QTimer()
        self.curr_time = QtCore.QTime(0, 0, 0)
        self.timer.timeout.connect(self.showTime)
        self.ui.startRecord.clicked.connect(self.startTimer)
        self.ui.stopRecord.clicked.connect(self.endTimer)
        self.ui.resetRecord.clicked.connect(self.resetTimer)

    def showTime(self):
        self.curr_time = self.curr_time.addSecs(1)
        time = self.curr_time.toString("hh:mm:ss")
        self.ui.timer_ldc.display(time)

    def startTimer(self):
        self.timer.start(1000)

    def endTimer(self):
        self.timer.stop()

    def resetTimer(self):
        self.curr_time = QtCore.QTime(0, 0, 0)
        time = self.curr_time.toString("hh:mm:ss")
        self.ui.timer_ldc.display(time)