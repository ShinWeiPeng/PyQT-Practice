from PyQt6 import QtWidgets, uic
import pyqtgraph as pg
import numpy as np
from scipy.stats import norm
import sys
from main_ui import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):
 
    def __init__(self):
        super().__init__()
 
        #Load the UI Page by PyQt6
        # uic.loadUi('main.ui', self)
        self.setWindowTitle('PyQtGraph shows normal distribution')
        self.pdfcdf_status = 1
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Signals
        self.ui.pdfcdf.clicked.connect(self.update_plot)
        self.ui.checkBox_Grid.stateChanged.connect(self.gridon)
        self.ui.lineEdit_x.returnPressed.connect(self.comp_cdf)
        self.ui.lineEdit_cdfx.returnPressed.connect(self.comp_invcdf)
        self.ui.hSlider_x.valueChanged.connect(self.sliderMove)
        self.ui.hSlider_x.sliderMoved.connect(self.sliderMove)
        self.update_plot()
         
    # Slots
    def update_plot(self):
        self.ui.graphWidget.clear() # clear current plot before plotting
        x = np.linspace(-5, 5, 1000)
        if self.pdfcdf_status == 1:
            y = norm.pdf(x)
            titlename = "PDF"
        else:
            y = norm.cdf(x)
            titlename = "CDF"
        pen = pg.mkPen(color=(255, 0, 0), width = 10) # Qt.DotLine, Qt.DashDotLine and Qt.DashDotDotLine
     
        cur1 = self.ui.graphWidget.plot(x, y, pen = pen, name = 'Demo')
        cur2 = self.ui.graphWidget.plot(x, np.zeros(len(y)))
        # add color patch under curve
        patchcur = pg.FillBetweenItem(curve1 = cur1, curve2 = cur2, brush = 'g')
        if self.pdfcdf_status == 1:
            self.ui.graphWidget.addItem(patchcur)
         
        self.ui.graphWidget.setBackground('w')
        self.ui.graphWidget.setTitle(titlename, color="b", size="14pt")
        styles = {'color':'green', 'font-size':'16px'}
        self.ui.graphWidget.setLabel('left', 'Y', **styles)
        self.ui.graphWidget.setLabel('bottom', 'X', **styles)
        self.ui.graphWidget.showGrid(x=False, y=False)
        self.pdfcdf_status = -self.pdfcdf_status
 
    def gridon(self, s):
        # print(self.checkBox_Grid.checkState())
        if s == 2: # 0 : unchecked; 2 : checked
            self.ui.graphWidget.showGrid(x = True, y = True)   
        else:
            self.ui.graphWidget.showGrid(x = False, y = False)   
 
    def comp_cdf(self):
        cdf = norm.cdf(float(self.ui.lineEdit_x.displayText()))    
        self.ui.lineEdit_cdfx.setText(str(round(cdf, 4)))
        self.ui.hSlider_x.setValue(int(float(self.ui.lineEdit_x.displayText())))
 
    def comp_invcdf(self):
        x = norm.ppf(float(self.ui.lineEdit_cdfx.displayText()))
        self.ui.lineEdit_x.setText(str(round(x,4)))
     
    def sliderMove(self, x):
        self.ui.lineEdit_x.setText(str(round(x,4)))
        self.ui.lineEdit_cdfx.setText(str(round(norm.cdf(x), 4)))
 
def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())
 
if __name__ == '__main__':
    main()