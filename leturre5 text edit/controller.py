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
        self.ui.textEdit.textChanged.connect(self.textEditTextChanged)
        self.ui.plainTextEdit.textChanged.connect(self.plainEditTextChanged)
        self.ui.btn_ClearLblPlain.clicked.connect(self.BtnClearClicked)
    
    def buttonClicked(self):
        msg = self.ui.line_Input.text()
        self.ui.lbl_Display.setText(msg)
        
    def textEditTextChanged(self):
        msg = self.ui.textEdit.toPlainText()
        self.ui.lbl_TextEdit.setText(msg)
        
    def plainEditTextChanged(self):
        msg = self.ui.plainTextEdit.toPlainText()
        self.ui.lbl_PlainEdit.setText(msg)
        
    def BtnClearClicked(self):
        self.ui.lbl_PlainEdit.clear()