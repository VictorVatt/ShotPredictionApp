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
        self.device = None
        self.portInfo = None
        self.version = None
        self.ui = ui
        self.orientationResetDone = False

        self.timer = QtCore.QTimer(self, timeout = self.record)



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
            self.portInfo = portInfo
            address = portInfo.bluetoothAddress()
            self.ui.listWidget.addItem(address)
            print(f"Opening DOT with address: @ {address}")
            if not self.manager.openPort(self.portInfo): # open port to the select dot
                print(f"Connection to Device {address} failed, retrying...")
                print(f"Device {address} retry connected:")
                if not self.manager.openPort(self.portInfo):
                    print(f"Could not open DOT. Reason: {self.manager.lastResultText()}")
                    continue

            self.ui.message_connexion.setText(f"IMU : {address} Connecté") # set the connection message
            self.device = self.manager.device(portInfo.deviceId()) #create the device with the manager

            # connect the start button for recording to the method
            # allowed user to start a recording
            self.ui.startRecord.clicked.connect(self.startPressed)

    def record(self):
        if self.callback.packetsAvailable():
            s = ""
                # Retrieve a packet
            packet = self.callback.getNextPacket(self.device.portInfo().bluetoothAddress())

            if packet.containsOrientation():
                euler = packet.orientationEuler()
                s += f"Roll:{euler.x():7.2f}, Pitch:{euler.y():7.2f}, Yaw:{euler.z():7.2f}| "

            print("%s\r" % s, end="", flush=True)

            if not self.orientationResetDone:
                print(f"\nResetting heading for device {self.device.portInfo().bluetoothAddress()}: ", end="", flush=True)
                if self.device.resetOrientation(xsensdot_pc_sdk.XRM_Heading):
                    print("OK", end="", flush=True)
                else:
                    print(f"NOK: {self.device.lastResultText()}", end="", flush=True)
            print("\n", end="", flush=True)
            self.orientationResetDone = True
    def startPressed(self):
        if self.device.setOnboardFilterProfile("General"):
            print("Successfully set profile to General")
        self.device.setLogOptions(xsensdot_pc_sdk.XSO_Calibrate)

        logFileName = "logfile_" + self.portInfo.bluetoothAddress().replace(':', '-') + ".csv"
        print(f"Enable logging to: {logFileName}")
        if not self.device.enableLogging(logFileName):
            print(f"Failed to enable logging. Reason: {self.manager.lastResultText()}")
        print("Putting device into measurement mode.")
        if not self.device.startMeasurement(xsensdot_pc_sdk.XsPayloadMode_HighFidelity):
            print(f"Could not put device into measurement mode. Reason: {self.manager.lastResultText()}")
        s = ""
        s += f"{self.device.portInfo().bluetoothAddress():42}"
        print("%s" % s, flush=True)

        self.ui.stopRecord.clicked.connect(self.pausePressed)
        QtCore.QTimer.singleShot(0, self.record)
        self.timer.start()
        # allow user to stop recording

    def pausePressed(self):
        print(f"\nResetting heading to default for device {self.device.portInfo().bluetoothAddress()}: ", end="", flush=True)
        if self.device.resetOrientation(xsensdot_pc_sdk.XRM_DefaultAlignment):
            print("OK", end="", flush=True)
        else:
            print(f"NOK: {self.device.lastResultText()}", end="", flush=True)
        print("\n", end="", flush=True)

        print("\nStopping measurement...")
        if not self.device.stopMeasurement():
            print("Failed to stop measurement.")
        if not self.device.disableLogging():
                print("Failed to disable logging.")

        print("Closing ports...")
        self.manager.close()

        print("Successful exit.")
        self.timer.stop()
















