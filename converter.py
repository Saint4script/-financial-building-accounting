import sys

from PyQt5 import QtWidgets 
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from zikkurat001 import Ui_MainWindow 
from Tables import Ui_NewWindow


class mywindow(QtWidgets.QMainWindow):
    k = 0
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Build.clicked.connect(self.BuildFunc)
        self.ui.Test.clicked.connect(self.Kappa)
        
    def BuildFunc(self):
        if(self.ui.Project_cost.text() == ""):
           tmp = int(self.ui.Self_cost.text())*int(self.ui.Total_area.text())
           self.ui.Project_cost.setText(str(tmp))
            
        start_money = int(self.ui.Start_money.text())
        self_cost = int(self.ui.Self_cost.text())
        total_area = int(self.ui.Total_area.text())
        if(start_money < total_area * self_cost * 0.1):     
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage("Здесь.Не.Строят")
            error_dialog.exec_()
        else:
             self.k = total_area * self_cost - start_money
       
    def Kappa(self):
        self.ui.Apartments_amount.setText(str(self.k))
                  

'''class newwindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(newwindow, self).__init__()
        self.ui = Ui_NewWindow()
        self.ui.setupUi(self)'''


        
'''def Trying(app):
    app.hide()
    application = newwindow()
    application.show()'''

app = QtWidgets.QApplication([])
application = mywindow()
application.show()

#Ui_MainWindow.Test.clicked.connect(Trying(application))
sys.exit(app.exec())