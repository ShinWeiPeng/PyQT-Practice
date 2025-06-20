from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QFileDialog

from UI import Ui_MainWindow

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        self.ui.btnOpenFile.clicked.connect(self.open_file) 
        self.ui.btnOpenFolder.clicked.connect(self.open_folder)

    def open_file(self):
        filename, filetype = QFileDialog.getOpenFileName(self,
                  "Open file",
                  "./")                 # start path
        print(filename, filetype)
        self.ui.lblShowFilePath.setText(filename)

    def open_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self,
                  "Open folder",
                  "./")                 # start path
        print(folder_path)
        self.ui.lblShowFolderPath.setText(folder_path)