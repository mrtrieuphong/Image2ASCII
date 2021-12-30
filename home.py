# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1020, 604)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QMainWindow {\n"
"    background-color: #000;\n"
"}\n"
"  \n"
"")
        MainWindow.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget {\n"
"    background-color: #121313;\n"
"}\n"
"  \n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.Group1 = QtWidgets.QGroupBox(self.centralwidget)
        self.Group1.setGeometry(QtCore.QRect(20, 60, 381, 161))
        self.Group1.setStyleSheet("QGroupBox#Group1{\n"
"    background-color: #242526;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"}\n"
"  \n"
"")
        self.Group1.setTitle("")
        self.Group1.setObjectName("Group1")
        self.Browser = QtWidgets.QPushButton(self.Group1)
        self.Browser.setGeometry(QtCore.QRect(20, 20, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Browser.setFont(font)
        self.Browser.setStyleSheet("QPushButton#Browser:hover:!pressed\n"
"{\n"
"      background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0.306818 rgba(63, 0, 64, 255), stop:0.886364 rgba(0, 27, 68, 255));\n"
"}\n"
"QPushButton#Browser {\n"
"     background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0.306818 rgba(143, 0, 146, 255), stop:0.886364 rgba(0, 100, 245, 255));\n"
"    border: none; \n"
"    color: white;\n"
"    border-radius: 25px;\n"
"}\n"
"")
        self.Browser.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("static/folder-open-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Browser.setIcon(icon)
        self.Browser.setIconSize(QtCore.QSize(24, 24))
        self.Browser.setObjectName("Browser")
        self.Filename = QtWidgets.QLabel(self.Group1)
        self.Filename.setGeometry(QtCore.QRect(20, 20, 341, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(11)
        self.Filename.setFont(font)
        self.Filename.setStyleSheet("QLabel#Filename {\n"
"      background-color: #3A3B3C;\n"
"      border: none; \n"
"    color: white;\n"
"    border-radius: 25px;\n"
"}")
        self.Filename.setScaledContents(False)
        self.Filename.setWordWrap(False)
        self.Filename.setIndent(60)
        self.Filename.setObjectName("Filename")
        self.I2T = QtWidgets.QPushButton(self.Group1)
        self.I2T.setGeometry(QtCore.QRect(20, 90, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.I2T.setFont(font)
        self.I2T.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.I2T.setStyleSheet("QPushButton#I2T:disabled {\n"
"     background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0.306818 rgba(63, 0, 64, 255), stop:0.886364 rgba(0, 27, 68, 255));\n"
"}\n"
"QPushButton#I2T:hover:!pressed\n"
"{\n"
"      background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0.306818 rgba(63, 0, 64, 255), stop:0.886364 rgba(0, 27, 68, 255));\n"
"}\n"
"QPushButton#I2T {\n"
"     background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0.306818 rgba(143, 0, 146, 255), stop:0.886364 rgba(0, 100, 245, 255));\n"
"    border: none; \n"
"    color: white;\n"
"    border-radius: 20px;\n"
"}\n"
"")
        self.I2T.setIconSize(QtCore.QSize(24, 24))
        self.I2T.setAutoRepeat(False)
        self.I2T.setAutoExclusive(False)
        self.I2T.setFlat(False)
        self.I2T.setObjectName("I2T")
        self.I2I = QtWidgets.QPushButton(self.Group1)
        self.I2I.setGeometry(QtCore.QRect(200, 90, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.I2I.setFont(font)
        self.I2I.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.I2I.setStyleSheet("QPushButton#I2I:disabled {\n"
"     background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0.306818 rgba(63, 0, 64, 255), stop:0.886364 rgba(0, 27, 68, 255));\n"
"}\n"
"QPushButton#I2I:hover:!pressed\n"
"{\n"
"  background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0.306818 rgba(63, 0, 64, 255), stop:0.886364 rgba(0, 27, 68, 255));\n"
"}\n"
"QPushButton#I2I {\n"
"     background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0.306818 rgba(143, 0, 146, 255), stop:0.886364 rgba(0, 100, 245, 255));\n"
"    border: none; \n"
"    color: white;\n"
"    border-radius: 20px;\n"
"}\n"
"")
        self.I2I.setIconSize(QtCore.QSize(24, 24))
        self.I2I.setAutoRepeat(False)
        self.I2I.setAutoExclusive(False)
        self.I2I.setFlat(False)
        self.I2I.setObjectName("I2I")
        self.Filename.raise_()
        self.Browser.raise_()
        self.I2T.raise_()
        self.I2I.raise_()
        self.Group2 = QtWidgets.QGroupBox(self.centralwidget)
        self.Group2.setGeometry(QtCore.QRect(20, -10, 981, 51))
        self.Group2.setStyleSheet("QGroupBox#Group2{\n"
"    background-color: #242526;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"}\n"
"  \n"
"")
        self.Group2.setTitle("")
        self.Group2.setObjectName("Group2")
        self.Appname = QtWidgets.QLabel(self.Group2)
        self.Appname.setEnabled(True)
        self.Appname.setGeometry(QtCore.QRect(30, 20, 331, 21))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Appname.setFont(font)
        self.Appname.setAutoFillBackground(False)
        self.Appname.setStyleSheet("QLabel#Appname {\n"
"    color: white;\n"
"    background-color: #242526;\n"
"}")
        self.Appname.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.Appname.setObjectName("Appname")
        self.Close = QtWidgets.QPushButton(self.Group2)
        self.Close.setGeometry(QtCore.QRect(950, 20, 21, 21))
        self.Close.setStyleSheet("QPushButton#Close:hover:!pressed\n"
"{\n"
"      background-color: rgb(167, 30, 30);\n"
"}\n"
"QPushButton#Close {\n"
"    background-color: rgb(220, 60, 60);\n"
"    border: none; \n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.Close.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("static/times-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Close.setIcon(icon1)
        self.Close.setObjectName("Close")
        self.Minimun = QtWidgets.QPushButton(self.Group2)
        self.Minimun.setGeometry(QtCore.QRect(920, 20, 21, 21))
        self.Minimun.setStyleSheet("QPushButton#Minimun:hover:!pressed\n"
"{\n"
"      background-color: rgb(72, 72, 72);\n"
"}\n"
"QPushButton#Minimun {\n"
"    background-color: rgb(140, 140, 140);\n"
"    border: none; \n"
"    color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.Minimun.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("static/minimum-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Minimun.setIcon(icon2)
        self.Minimun.setObjectName("Minimun")
        self.Group3 = QtWidgets.QGroupBox(self.centralwidget)
        self.Group3.setGeometry(QtCore.QRect(20, 240, 381, 321))
        self.Group3.setStyleSheet("QGroupBox#Group3{\n"
"    background-color: #242526;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"}\n"
"  \n"
"")
        self.Group3.setTitle("")
        self.Group3.setObjectName("Group3")
        self.Image = QtWidgets.QLabel(self.Group3)
        self.Image.setGeometry(QtCore.QRect(10, 20, 361, 291))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(16)
        self.Image.setFont(font)
        self.Image.setStyleSheet("QLabel#Image {\n"
"    color: gray;\n"
"    background-color: none;\n"
"}")
        self.Image.setAlignment(QtCore.Qt.AlignCenter)
        self.Image.setObjectName("Image")
        self.Author = QtWidgets.QLabel(self.centralwidget)
        self.Author.setGeometry(QtCore.QRect(40, 230, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Rowdies")
        font.setPointSize(14)
        self.Author.setFont(font)
        self.Author.setStyleSheet("QLabel#Author {\n"
"    color: white;\n"
"    background-color: none;\n"
"}")
        self.Author.setObjectName("Author")
        self.Upload = QtWidgets.QLabel(self.centralwidget)
        self.Upload.setGeometry(QtCore.QRect(40, 50, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Rowdies")
        font.setPointSize(14)
        self.Upload.setFont(font)
        self.Upload.setStyleSheet("QLabel#Upload {\n"
"    color: white;\n"
"    background-color: none;\n"
"}")
        self.Upload.setObjectName("Upload")
        self.Group4 = QtWidgets.QGroupBox(self.centralwidget)
        self.Group4.setGeometry(QtCore.QRect(420, 60, 521, 501))
        self.Group4.setStyleSheet("QGroupBox#Group4{\n"
"    background-color: #242526;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"}\n"
"  \n"
"")
        self.Group4.setTitle("")
        self.Group4.setObjectName("Group4")
        self.Result = QtWidgets.QLabel(self.Group4)
        self.Result.setGeometry(QtCore.QRect(6, 12, 511, 481))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(1)
        self.Result.setFont(font)
        self.Result.setStyleSheet("QLabel#Result {\n"
"    color: white;\n"
"    background-color: none;\n"
"}")
        self.Result.setText("")
        self.Result.setAlignment(QtCore.Qt.AlignCenter)
        self.Result.setObjectName("Result")
        self.Export = QtWidgets.QPushButton(self.centralwidget)
        self.Export.setEnabled(True)
        self.Export.setGeometry(QtCore.QRect(950, 130, 51, 51))
        self.Export.setStyleSheet("QPushButton#Export:disabled {\n"
"     background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0.306818 rgba(63, 0, 64, 255), stop:0.886364 rgba(0, 27, 68, 255));\n"
"}\n"
"QPushButton#Export:hover:!pressed\n"
"{\n"
"      background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0.306818 rgba(63, 0, 64, 255), stop:0.886364 rgba(0, 27, 68, 255));\n"
"}\n"
"QPushButton#Export {\n"
"     background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0.306818 rgba(143, 0, 146, 255), stop:0.886364 rgba(0, 100, 245, 255));\n"
"    border: none; \n"
"    color: white;\n"
"    border-radius: 25px;\n"
"}\n"
"")
        self.Export.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("static/file-code-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Export.setIcon(icon3)
        self.Export.setIconSize(QtCore.QSize(24, 24))
        self.Export.setObjectName("Export")
        self.Info = QtWidgets.QPushButton(self.centralwidget)
        self.Info.setGeometry(QtCore.QRect(950, 60, 51, 51))
        self.Info.setStyleSheet("\n"
"QPushButton#Info:hover:!pressed\n"
"{\n"
"  background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0.306818 rgba(63, 0, 64, 255), stop:0.886364 rgba(0, 27, 68, 255));\n"
"}\n"
"QPushButton#Info {\n"
"     background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0.306818 rgba(143, 0, 146, 255), stop:0.886364 rgba(0, 100, 245, 255));\n"
"    border: none; \n"
"    color: white;\n"
"    border-radius: 25px;\n"
"}\n"
"")
        self.Info.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("static/user-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Info.setIcon(icon4)
        self.Info.setIconSize(QtCore.QSize(24, 24))
        self.Info.setObjectName("Info")
        self.Save = QtWidgets.QPushButton(self.centralwidget)
        self.Save.setGeometry(QtCore.QRect(950, 200, 51, 51))
        self.Save.setStyleSheet("QPushButton#Save:disabled {\n"
"     background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0.306818 rgba(63, 0, 64, 255), stop:0.886364 rgba(0, 27, 68, 255));\n"
"}\n"
"QPushButton#Save:hover:!pressed\n"
"{\n"
"      background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0.306818 rgba(63, 0, 64, 255), stop:0.886364 rgba(0, 27, 68, 255));\n"
"}\n"
"QPushButton#Save {\n"
"     background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0.306818 rgba(143, 0, 146, 255), stop:0.886364 rgba(0, 100, 245, 255));\n"
"    border: none; \n"
"    color: white;\n"
"    border-radius: 25px;\n"
"}\n"
"")
        self.Save.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("static/save-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Save.setIcon(icon5)
        self.Save.setIconSize(QtCore.QSize(24, 24))
        self.Save.setObjectName("Save")
        self.Height = QtWidgets.QSlider(self.centralwidget)
        self.Height.setGeometry(QtCore.QRect(960, 340, 31, 191))
        self.Height.setAutoFillBackground(True)
        self.Height.setStyleSheet("QSlider::sub-page:vertical:disabled {\n"
"background: green;\n"
"border-color: none;\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0.306818 rgba(143, 0, 146, 255), stop:0.886364 rgba(0, 100, 245, 255));\n"
"    border: nonne;;\n"
"    border-radius: 5px;\n"
"    }")
        self.Height.setMinimum(500)
        self.Height.setMaximum(5000)
        self.Height.setSingleStep(100)
        self.Height.setPageStep(100)
        self.Height.setSliderPosition(1000)
        self.Height.setOrientation(QtCore.Qt.Vertical)
        self.Height.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.Height.setTickInterval(500)
        self.Height.setObjectName("Height")
        self.Display = QtWidgets.QLabel(self.centralwidget)
        self.Display.setGeometry(QtCore.QRect(950, 270, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        self.Display.setFont(font)
        self.Display.setStyleSheet("QLabel#Display {\n"
"    color: white;\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0.306818 rgba(143, 0, 146, 255), stop:0.886364 rgba(0, 100, 245, 255));\n"
"    border: none;\n"
"    border-radius: 25px;\n"
"}")
        self.Display.setAlignment(QtCore.Qt.AlignCenter)
        self.Display.setIndent(-1)
        self.Display.setObjectName("Display")
        self.Height_label = QtWidgets.QLabel(self.centralwidget)
        self.Height_label.setGeometry(QtCore.QRect(940, 540, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Rowdies")
        font.setPointSize(8)
        self.Height_label.setFont(font)
        self.Height_label.setStyleSheet("QLabel#Height_label {\n"
"    color: white;\n"
"    background-color: none;\n"
"}")
        self.Height_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Height_label.setObjectName("Height_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Filename.setText(_translate("MainWindow", "Browser your image here..."))
        self.I2T.setText(_translate("MainWindow", "Image to ASCII"))
        self.I2I.setText(_translate("MainWindow", "ACSII with Color"))
        self.Appname.setText(_translate("MainWindow", "Image to ASCII - nguyentrieuphong.com"))
        self.Image.setText(_translate("MainWindow", "nothing to show"))
        self.Author.setText(_translate("MainWindow", "Review"))
        self.Upload.setText(_translate("MainWindow", "Upload"))
        self.Export.setToolTip(_translate("MainWindow", "<html><head/><body><p>Open in notepad</p></body></html>"))
        self.Export.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.Info.setToolTip(_translate("MainWindow", "<html><head/><body><p>About author</p></body></html>"))
        self.Display.setText(_translate("MainWindow", "1000"))
        self.Height_label.setText(_translate("MainWindow", "resolution"))

