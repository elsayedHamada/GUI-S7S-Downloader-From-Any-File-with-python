# Import needed modules 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.uic import *
import sys
import os
import urllib.request

# load the UI file
FORM_CLASS, _ = loadUiType(os.path.join(os.path.dirname(__file__), "DesignDownloader.ui"))

# create the main loop
class MainLoop(QMainWindow, FORM_CLASS):
    def __init__(self, parent=None):
        super(MainLoop, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.ui_handler()
        self.buttons_handler()

    def ui_handler(self):
        self.setWindowTitle("S7S Downloader")

    def buttons_handler(self):
        self.pushButton_2.clicked.connect(self.download)
        self.pushButton.clicked.connect(self.browse_handler)
        self.pushButton_3.clicked.connect(quit)

    def browse_handler(self):
        pass

    def progress_handler(self):
        pass

    def download(self):
        url = self.lineEdit.text()
        location = self.lineEdit_2.text()
        


def main():
    app = QApplication(sys.argv)
    window = MainLoop()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()