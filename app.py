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
        save_location = str(QFileDialog.getSaveFileName(self, caption="Save To", directory=".", filter="All files (*.*"))
        text_location = save_location[2:].split(",")[0][0:-1]
        self.lineEdit_2.setText(text_location)

    def progress_handler(self, blocknum, blocksize, totalsize):
        downloaded_size = blocknum * blocksize
        percent = downloaded_size * 100 / totalsize
        self.progressBar.setValue(int(percent))
        QApplication.processEvents()

    def download(self):
        url = self.lineEdit.text()
        location = self.lineEdit_2.text()
        try:
            urllib.request.urlretrieve(url, location, self.progress_handler)
            QMessageBox.information(self, "S7S Downloader", f"Download Completed\n save to >> {location}")
        except Exception:
            QMessageBox.warning(self, "S7S Downloader", "Check If the Url Or The Loocation Is Not Right.")
            
        self.progressBar.setValue(0)
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")


def main():
    app = QApplication(sys.argv)
    window = MainLoop()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()

# D:\Coding\Python\Python_Projects\Remake\S7S Downloader\setup.exe
# https://download.sublimetext.com/sublime_text_build_4107_x64_setup.exe