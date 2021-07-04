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
        super(MainLoop).__init(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)


def main():
    app = QApplication(sys.argv)
    window = MainLoop()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()