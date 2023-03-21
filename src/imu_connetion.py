import xsensdot_pc_sdk
from PySide6 import QtCore
from PySide6.QtCore import QThread, QTimer
from CallbackHandler import CallbackHandler
import time

class IMU_connection(QThread):
    def __init__(self, ui):
        super().__init__()
        self.manager = xsensdot_pc_sdk.XsDotConnectionManager()
        self.callback = CallbackHandler()
        self.version = None
        self.ui = ui

        self.timer = QtCore.QTimer(self, timeout = self.dosomething)



    def run(self):
        # recover the SDK version
        self.version = xsensdot_pc_sdk.XsVersion()
        xsensdot_pc_sdk.xsdotsdkDllVersion(self.version)
        self.ui.sdk_version.setText(f"Version SDK : {self.version.toXsString()} ")

        # attach the callback handler to connection manager
        self.manager.addXsDotCallbackHandler(self.callback)

        # enable the xsensdot detection
        self.manager.enableDeviceDetection()
        startTime = xsensdot_pc_sdk.XsTimeStamp_nowMs()

        # research xsensdot for 2 secondes
        while not self.callback.errorReceived() and xsensdot_pc_sdk.XsTimeStamp_nowMs() - startTime <= 2000:
            time.sleep(0.1)

        #desable xsensdot detection
        self.manager.disableDeviceDetection()
        print("Stopped scanning for devices.")
        self.manager.disableDeviceDetection()

        # if no xsens dot detected
        if len(self.callback.getDetectedDots()) == 0:
            print("No Xsens DOT device(s) found. Aborting.")

        # connection to xsensdot
        for portInfo in self.callback.getDetectedDots():
            address = portInfo.bluetoothAddress()
            self.ui.listWidget.addItem(address)
            print(f"Opening DOT with address: @ {address}")
            if not self.manager.openPort(portInfo): # open port to the select dot
                print(f"Connection to Device {address} failed, retrying...")
                print(f"Device {address} retry connected:")
                if not self.manager.openPort(portInfo):
                    print(f"Could not open DOT. Reason: {self.manager.lastResultText()}")
                    continue

            self.ui.message_connexion.setText(f"IMU : {address} Connecté") # set the connection message
            device = self.manager.device(portInfo.deviceId()) #create the device with the manager

            # connect the start button for recording to the method
            # allowed user to start a recording
            self.ui.startRecord.clicked.connect(self.startPressed)

    def dosomething(self):
        print("Hello")
    def startPressed(self):
        QtCore.QTimer.singleShot(0, self.dosomething)
        self.timer.start()
        # allow user to stop recording
        self.ui.stopRecord.clicked.connect(self.pausePressed)

    def pausePressed(self):
        self.timer.stop()
















