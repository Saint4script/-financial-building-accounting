import sys

from PyQt5 import QtWidgets 
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from zikkurat001 import Ui_MainWindow 
from Tables import Ui_NewWindow


class mywindow(QtWidgets.QMainWindow):
    k = S = n = s = p1 = z = c = 0 
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Build.clicked.connect(self.BuildFunc)
        self.ui.Test.clicked.connect(self.Trying)
        
        self.ui.Total_area.editingFinished.connect(lambda field = self.ui.Total_area: self.CheckerForFields(field))
        self.ui.Apartments_amount.editingFinished.connect(lambda field = self.ui.Apartments_amount: self.CheckerForFields(field))
        self.ui.Average_area_of_apartments.editingFinished.connect(lambda field = self.ui.Average_area_of_apartments: self.CheckerForFields(field))
        self.ui.Start_cost.editingFinished.connect(lambda field = self.ui.Start_cost: self.CheckerForFields(field))
        self.ui.Increasing_percentage.editingFinished.connect(lambda field = self.ui.Increasing_percentage: self.CheckerForFields(field))
        self.ui.Bulding_duration.editingFinished.connect(lambda field = self.ui.Bulding_duration: self.CheckerForFields(field))
        self.ui.Start_money.editingFinished.connect(lambda field = self.ui.Start_money: self.CheckerForFields(field))
        self.ui.Self_cost.editingFinished.connect(lambda field = self.ui.Self_cost: self.CheckerForFields(field))
        
        
    def BuildFunc(self):
        if(self.ui.Project_cost.text() == ""):
           tmp = int(self.ui.Self_cost.text())*int(self.ui.Total_area.text())
           self.ui.Project_cost.setText(str(tmp))
         
        start_money = int(self.ui.Start_money.text())
        self_cost = self.c = int(self.ui.Self_cost.text())
        total_area = self.S = int(self.ui.Total_area.text())
        self.n = int(self.ui.Apartments_amount.text())
        self.s = int(self.ui.Average_area_of_apartments.text())
        self.p1 = int(self.ui.Start_cost.text())
        self.z = int(self.ui.Increasing_percentage.text())
        
        if(start_money < total_area * self_cost * 0.1):     
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage("Здесь.Не.Строят")
            error_dialog.exec_()
        else:
             self.k = total_area * self_cost - start_money
             application = newwindow(self)
             application.show()
             self.hide()

    def CheckerForFields(self, field): #Проверка заполнения полей, чтобы не вводили что-то кроме чисел

        if(field.text() != ""): #Если не писать это условие, прога вообще не запускается _-_
            try:
                int(field.text())
            except ValueError:
                error = QtWidgets.QErrorMessage()
                error.showMessage("Это не число")
                error.exec_()
                field.setText("")
    
    def Trying(self):
        if(self.ui.Total_area.text() != "" and self.ui.Self_cost.text() != ""):
            tmp = int(self.ui.Self_cost.text())*int(self.ui.Total_area.text())
            self.ui.Project_cost.setText(str(tmp))
        
        
#Это теперь дочерний класс класса mywindow
class newwindow(QtWidgets.QMainWindow):
    def __init__(self, parent):
        super(newwindow, self).__init__(parent)
        self.ui = Ui_NewWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.bp)
    
    def bp(self):
        self.parent().show()
        self.close()
        
        
app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())