from PyQt5 import QtWidgets, QtGui, QtCore

from UI import Ui_MainWindow

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        # TODO
        # qpushbutton doc: https://doc.qt.io/qt-5/qpushbutton.html
        self.ui.btn_Change.setText('Print message!')
        self.ui.btn_Change.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        msg = self.ui.line_Input.text()
        self.ui.lbl_Display.setText(msg)