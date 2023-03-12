from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtWidgets import (QApplication, QFrame, QGraphicsView, QGroupBox,
    QLCDNumber, QLabel, QPushButton, QRadioButton,
    QSizePolicy, QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(1200, 854)
        mainWindow.setMinimumSize(QSize(1200, 854))
        mainWindow.setMaximumSize(QSize(1200, 854))
        mainWindow.setAutoFillBackground(False)
        mainWindow.setStyleSheet(u"background-color: rgb(22, 27, 34);")
        self.laterality = QGroupBox(mainWindow)
        self.laterality.setObjectName(u"laterality")
        self.laterality.setGeometry(QRect(20, 120, 271, 91))
        self.laterality.setStyleSheet(u"color: rgb(255, 255, 255);\n""font: 75 16pt \"Sharp Sans Display No2\";")
        self.rightHanded = QRadioButton(self.laterality)
        self.rightHanded.setObjectName(u"rightHanded")
        self.rightHanded.setGeometry(QRect(150, 30, 101, 51))
        self.rightHanded.setStyleSheet(u"font: 75 8pt \"Sharp Sans Display No2\";\n""font: 75 14pt \"Sharp Sans Display No2\";")
        self.leftHanded = QRadioButton(self.laterality)
        self.leftHanded.setObjectName(u"leftHanded")
        self.leftHanded.setGeometry(QRect(10, 30, 111, 51))
        self.leftHanded.setStyleSheet(u"font: 75 8pt \"Sharp Sans Display No2\";\n""font: 75 14pt \"Sharp Sans Display No2\";")
        self.title = QLabel(mainWindow)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(400, 20, 441, 71))
        self.title.setStyleSheet(u"font: 75 36pt \"Sharp Sans Display No2\";\n""color: rgb(213, 220, 60);")
        self.IMUinformations = QGroupBox(mainWindow)
        self.IMUinformations.setObjectName(u"IMUinformations")
        self.IMUinformations.setGeometry(QRect(310, 120, 871, 371))
        self.IMUinformations.setStyleSheet(u"font: 75 14pt \"Sharp Sans Display No2\";\n""color: rgb(255, 255, 255);")
        self.connexion_statut = QLabel(self.IMUinformations)
        self.connexion_statut.setObjectName(u"connexion_statut")
        self.connexion_statut.setGeometry(QRect(340, 130, 251, 101))
        self.connexion_statut.setStyleSheet(u"color: rgb(193, 78, 78);")
        self.results_label = QLabel(mainWindow)
        self.results_label.setObjectName(u"results_label")
        self.results_label.setGeometry(QRect(310, 510, 211, 41))
        self.results_label.setStyleSheet(u"color: rgb(255, 255, 255);\n""font: 75 20pt \"Sharp Sans Display No2\";\n""")
        self.results_graph = QGraphicsView(mainWindow)
        self.results_graph.setObjectName(u"results_graph")
        self.results_graph.setGeometry(QRect(310, 560, 871, 211))
        self.results_graph.setStyleSheet(u"border: 1px solid rgb(255, 255, 255);")
        self.openGLWidget = QOpenGLWidget(mainWindow)
        self.openGLWidget.setObjectName(u"openGLWidget")
        self.openGLWidget.setGeometry(QRect(20, 230, 271, 261))
        self.openGLWidget.setStyleSheet(u"")
        self.startRecord = QPushButton(mainWindow)
        self.startRecord.setObjectName(u"startRecord")
        self.startRecord.setGeometry(QRect(310, 780, 271, 61))
        self.startRecord.setStyleSheet(u"color:rgb(255, 255, 255);\n""background-color: rgb(213, 220, 60);\n""font: 22pt \"MS Shell Dlg 2\";")
        self.resetRecord = QPushButton(mainWindow)
        self.resetRecord.setObjectName(u"resetRecord")
        self.resetRecord.setGeometry(QRect(910, 780, 271, 61))
        self.resetRecord.setStyleSheet(u"color:rgb(255, 255, 255);\n""background-color: rgb(213, 220, 60);\n""font: 22pt \"MS Shell Dlg 2\";")
        self.stopRecord = QPushButton(mainWindow)
        self.stopRecord.setObjectName(u"stopRecord")
        self.stopRecord.setGeometry(QRect(610, 780, 271, 61))
        self.stopRecord.setStyleSheet(u"color:rgb(255, 255, 255);\n""background-color: rgb(213, 220, 60);\n""font: 22pt \"MS Shell Dlg 2\";")
        self.timer_container = QFrame(mainWindow)
        self.timer_container.setObjectName(u"timer_container")
        self.timer_container.setGeometry(QRect(20, 560, 271, 141))
        self.timer_container.setStyleSheet(u"border: 1px solid rgb(255, 255, 255);")
        self.timer_container.setFrameShape(QFrame.StyledPanel)
        self.timer_container.setFrameShadow(QFrame.Raised)
        self.timer_ldc = QLCDNumber(self.timer_container)
        self.timer_ldc.setObjectName(u"timer_ldc")
        self.timer_ldc.setGeometry(QRect(10, 60, 251, 71))
        self.timer_ldc.setStyleSheet(u"color: rgb(213, 220, 60);\n""")
        self.timer_ldc.setProperty("value", 0.000000000000000)
        self.timer_label = QLabel(self.timer_container)
        self.timer_label.setObjectName(u"timer_label")
        self.timer_label.setGeometry(QRect(10, 10, 251, 41))
        self.timer_label.setStyleSheet(u"color: rgb(255, 255, 255);\n""font: 75 20pt \"Sharp Sans Display No2\";\n""font: 14pt \"MS Shell Dlg 2\";")

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"Form", None))
        self.laterality.setTitle(QCoreApplication.translate("mainWindow", u"Lat\u00e9ralit\u00e9", None))
        self.rightHanded.setText(QCoreApplication.translate("mainWindow", u"Droitier", None))
        self.leftHanded.setText(QCoreApplication.translate("mainWindow", u"Gaucher", None))
        self.title.setText(QCoreApplication.translate("mainWindow", u"TennisPrediction", None))
#if QT_CONFIG(tooltip)
        self.IMUinformations.setToolTip(QCoreApplication.translate("mainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sharp Sans Display No2'; font-size:14pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#aa0000;\">Informations g\u00e9n\u00e9rale sur l'IMU connect\u00e9</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.IMUinformations.setTitle(QCoreApplication.translate("mainWindow", u"Informations IMU", None))
        self.connexion_statut.setText(QCoreApplication.translate("mainWindow", u"Aucun IMU connect\u00e9 ...", None))
        self.results_label.setText(QCoreApplication.translate("mainWindow", u"Resultats", None))
        self.startRecord.setText(QCoreApplication.translate("mainWindow", u"Start recording", None))
        self.resetRecord.setText(QCoreApplication.translate("mainWindow", u"Reset recording", None))
        self.stopRecord.setText(QCoreApplication.translate("mainWindow", u"Stop recording", None))
        self.timer_label.setText(QCoreApplication.translate("mainWindow", u"Timer ", None))
    # retranslateUi

