import os
import sys
import ctypes
import webbrowser
from PIL.ImageQt import ImageQt
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QPixmap
from home import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QFileDialog, QLabel, QMainWindow

from image_to_text import saveAsText
from image_to_ASCII_image import saveAsImage

myapp_id = 'www.nguyentrieuphong.com'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myapp_id)
ROOT_DIR = os.path.abspath(os.curdir)
ICON_PATH = os.path.join(ROOT_DIR, 'static/icon.png')


class Dialog(QMainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(ICON_PATH))
        self.openFileNameLabel = QLabel()
        self.saveFileNameLabel = QLabel()
        self.ui.Browser.clicked.connect(self.setOpenFileName)
        self.ui.I2T.clicked.connect(self.convert_to_text)
        self.ui.I2I.clicked.connect(self.convert_to_image)
        self.ui.Info.clicked.connect(self.open_webbrowser)
        self.ui.Close.clicked.connect(self.close)
        self.ui.Minimun.clicked.connect(self.showMinimized)
        self.ui.I2T.setDisabled(True)
        self.ui.I2I.setDisabled(True)
        self.ui.Export.setDisabled(True)
        self.ui.Save.setDisabled(True)
        self.ui.Height.valueChanged[int].connect(self.setImageSize)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.fileDir = None
        self.ascii = None
        self.ascii_image = None
        self.new_height = 1000

    def setOpenFileName(self):
        self.fileDir, _ = QFileDialog.getOpenFileName(
            self,
            "Open image", self.openFileNameLabel.text(),
            "Images (*.jpg *.jpeg *.png)"
        )
        fileName = QUrl.fromLocalFile(self.fileDir).fileName()

        if self.fileDir:
            self.ui.I2T.setEnabled(True)
            self.ui.I2I.setEnabled(True)
            stringNum = len(fileName)
            if stringNum > 15:
                fileName = fileName[0:8] + "..."
            self.ui.Filename.setText(fileName)
            pixmap = QPixmap(self.fileDir)
            if pixmap.width() >= pixmap.height():
                pixmap = pixmap.scaledToWidth(361)
            else:
                pixmap = pixmap.scaledToHeight(291)
            self.ui.Image.setPixmap(pixmap)
            self.ui.Image.show()

    def setImageSize(self, new_height):
        self.new_height = new_height
        self.ui.Display.setText("{height}".format(height=self.new_height))

    def convert_to_text(self):
        self.ui.Export.setEnabled(True)
        self.ascii = saveAsText(self.fileDir)
        self.ui.Result.setText(self.ascii)
        self.ui.Export.clicked.connect(self.export_txt)

    def export_txt(self):
        fileName, _ = QFileDialog.getSaveFileName(self,
                                                  "Save ASCII as",
                                                  self.saveFileNameLabel.text(),
                                                  "Documents (*.txt)")
        if fileName:
            with open(fileName, "w") as f:
                f.write(self.ascii)
        os.startfile(fileName)

    def convert_to_image(self):
        self.ui.Save.setEnabled(True)
        self.ui.Save.clicked.connect(self.save_image)
        self.ascii_image = saveAsImage(self.fileDir, self.new_height)
        qim = ImageQt(self.ascii_image)
        pixmap = QtGui.QPixmap.fromImage(qim)
        if pixmap.width() >= pixmap.height():
            pixmap = pixmap.scaledToWidth(511)
        else:
            pixmap = pixmap.scaledToHeight(481)
        self.ui.Result.setPixmap(pixmap)
        self.ui.Result.show()

    def save_image(self):
        fileName, _ = QFileDialog.getSaveFileName(self,
                                                  "Save image as",
                                                  self.saveFileNameLabel.text(),
                                                  "Images (*.jpg)")
        if fileName:
            self.ascii_image.save(fileName)
            os.startfile(fileName)

    def open_webbrowser(self):
        webbrowser.open('https://www.nguyentrieuphong.com')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Dialog()
    dialog.setFixedSize(1020, 600)
    dialog.show()
    sys.exit(app.exec_())
