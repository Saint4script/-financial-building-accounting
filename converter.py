import sys
import math
import PyQt5.QtGui
from PyQt5 import QtWidgets 
#from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QTableWidgetItem
from PyQt5.QtCore import QDate
from zikkurat001 import Ui_MainWindow 
from Tables import Ui_NewWindow
#TASKS:
#СДЕЛАТЬ ПРОВЕРКУ НА ОТРИЦАТЕЛЬНЫЕ ЧИСЛА ДЛЯ ХУЙ ЗНАЕТ ЧЕГО

#main window
class mywindow(QtWidgets.QMainWindow):
    k = S = n = s = p1 = z = c = build_time = own_money = 0 
    date_start = QDate.currentDate()
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Build.clicked.connect(self.BuildFunc)
        #self.ui.Test.clicked.connect(self.Trying) # для тестов
        self.ui.Total_area.editingFinished.connect(lambda field = self.ui.Total_area: self.CheckerForFields(field))
        self.ui.Apartments_amount.editingFinished.connect(lambda field = self.ui.Apartments_amount: self.CheckerForFields(field))
        self.ui.Average_area_of_apartments.editingFinished.connect(lambda field = self.ui.Average_area_of_apartments: self.CheckerForFields(field))
        self.ui.Start_cost.editingFinished.connect(lambda field = self.ui.Start_cost: self.CheckerForFields(field))
        self.ui.Increasing_percentage.editingFinished.connect(lambda field = self.ui.Increasing_percentage: self.CheckerForFields(field))
        self.ui.Bulding_duration.editingFinished.connect(lambda field = self.ui.Bulding_duration: self.CheckerForFields(field))
        self.ui.Start_money.editingFinished.connect(lambda field = self.ui.Start_money: self.CheckerForFields(field))
        self.ui.Self_cost.editingFinished.connect(lambda field = self.ui.Self_cost: self.CheckerForFields(field))
        self.ui.calendarWidget.clicked[QDate].connect(self.show_date)

        ##############################################
        self.ui.Apartments_amount.setText("368")
        self.ui.Average_area_of_apartments.setText("12")
        self.ui.Bulding_duration.setText("30")
        self.ui.Increasing_percentage.setText("2")
        self.ui.Start_money.setText("12312313")
        self.ui.Total_area.setText("12")
        self.ui.Start_cost.setText("54000")
        self.ui.Self_cost.setText("12")
        
        
    def show_date(self,date):
        self.date_start = date
        #print(QDate.longMonthName(date.month()))
    
        
    def get_dimensions(self):
        l = (self.k,self.S,self.n,self.s,self.p1,self.z,self.build_time,self.own_money,self.c, self.date_start)
        return l
    def BuildFunc(self):
        if(self.isnt_field_empty()): 
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
            self.build_time = int(self.ui.Bulding_duration.text())
            self.own_money = int(self.ui.Start_money.text())
            
            if(start_money < total_area * self_cost * 0.1):     
                error_dialog = QtWidgets.QErrorMessage()
                error_dialog.showMessage("Здесь.Не.Строят")
                error_dialog.exec_()
            else:
                 self.k = total_area * self_cost - start_money
                 application = newwindow(self)
                 application.show()
                 self.hide()
    
    
    def isnt_field_empty(self):
        lineEdits = self.ui.centralwidget.findChildren(QtWidgets.QLineEdit)
        checker = True
        for lineEdit in lineEdits:
            if(lineEdit.text() == ""):
                if (lineEdit != self.ui.Project_cost):
                    lineEdit.setStyleSheet("background-color:yellow;")
                    checker = False
            else:
                lineEdit.setStyleSheet("background-color:none;")
        self.ui.Project_cost.setStyleSheet("background-color:none;")
        if(not checker):
            warning = QtWidgets.QMessageBox()
            warning.setWindowTitle("Empty field")
            warning.setText("Fill all the fields")
            warning.setIcon(QtWidgets.QMessageBox.Critical)
            warning.exec_() 
        return checker
                
                
    def CheckerForFields(self, field): #Проверка заполнения полей, чтобы не вводили что-то кроме чисел
        if(field.text() != ""): #Если не писать это условие, прога вообще не запускается _-_
            try:
                int(field.text())
            except ValueError:
                error = QtWidgets.QErrorMessage()
                error.showMessage("Это не число")
                error.exec_()
                field.setText("")
    
    
    '''
    def Trying(self):
        if(self.ui.Total_area.text() != "" and self.ui.Self_cost.text() != ""):
            tmp = int(self.ui.Self_cost.text())*int(self.ui.Total_area.text())
            self.ui.Project_cost.setText(str(tmp))
    '''
        
        
#Это теперь дочерний класс класса mywindow
class newwindow(QtWidgets.QMainWindow):
    
    def __init__(self, parent):
        
        super(newwindow, self).__init__(parent)
        self.ui = Ui_NewWindow()
        self.ui.setupUi(self)

        self.k, self.S, self.n, self.s, self.p1,self.z, self.build_time, self.own_money, self.c, self.date_start = mywindow.get_dimensions(self.parent())
        list_of_tables = []

        self.ui.TableWidget = QtWidgets.QTableWidget(self.ui.centralwidget)
        self.ui.TableWidget.setObjectName("Table_decade")
        self.ui.TableWidget.move(0,120) 
        self.ui.TableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.ui.TableWidget.resizeColumnsToContents()
        self.ui.TableWidget.resizeRowsToContents()
        self.ui.pushButton.clicked.connect(self._exit)
        self.fill_table()

        self.ui.Table_with_flat_sell_plan = QtWidgets.QTableWidget(self.ui.centralwidget)
        self.ui.Table_with_flat_sell_plan.setObjectName("Table_with_flat_sell_plan")  
        self.ui.Table_with_flat_sell_plan.move(0,300) 
        self.ui.Table_with_flat_sell_plan.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.ui.Table_with_flat_sell_plan.resizeColumnsToContents()
        self.ui.Table_with_flat_sell_plan.resizeRowsToContents()
        self.fill_table_with_flat_sell_plan()
        

        list_of_tables.append(self.ui.TableWidget)
        list_of_tables.append(self.ui.Table_with_flat_sell_plan)
        for elem in list_of_tables:
            self.ui.comboBox.addItem("")

        
    def _exit(self):
        self.parent().show()
        self.close()
        
    def fill_table(self):  
        decades = math.ceil(self.build_time/3)
        
        self.ui.TableWidget.setRowCount(2)
        self.ui.TableWidget.setColumnCount(decades + 1)
        labels_decades = []
        new_date = self.date_start.month()
        price  = self.p1
        avg_sum1 = avg_sum2 = avg_sum3 = total_avg = 0
        self.pointer = [math.floor(decades/3),decades - math.floor(decades/3)*2]

        def toFixed(numObj, digits=0):    #some magic code from StackOverflow
            return f"{numObj:.{digits}f}"
        
        for i in range(decades):
            month = QDate.longMonthName(new_date)
            day = str(self.date_start.day())
            tempStr = F"{day} {month}"
            labels_decades.append(tempStr)
            new_date = new_date + 3

            if(new_date > 12):
                new_date -= 12
            cell_info = QTableWidgetItem(str(price))
                
            if(i < math.floor(decades/3)):
                avg_sum1 += price
                self.ui.TableWidget.setHorizontalHeader
            elif(i < decades - math.floor(decades/3)):
                avg_sum2 += price
            else:
                avg_sum3 += price
            
            total_avg += price
            self.ui.TableWidget.setItem(0 , i, cell_info)
            price = price * (1 + self.z/100)
            price = float(toFixed(price, 2))
        
        avg_sum1 = toFixed(avg_sum1 / self.pointer[0], 2)
        avg_sum2 = toFixed(avg_sum2 / self.pointer[1], 2)
        avg_sum3 = toFixed(avg_sum3 / self.pointer[0], 2)
        self.ui.TableWidget.setItem(1 , 0, QTableWidgetItem(avg_sum1))
        self.ui.TableWidget.setItem(1 , self.pointer[0], QTableWidgetItem(avg_sum2))
        self.ui.TableWidget.setItem(1 , self.pointer[0] + self.pointer[1], QTableWidgetItem(avg_sum3))

        total_avg = toFixed(total_avg / decades, 2)               
        self.ui.TableWidget.setItem(1, decades, QTableWidgetItem(total_avg))    
        labels_decades.append("Средняя цена") 
        Tlabels_decades = tuple(labels_decades)
        self.ui.TableWidget.setHorizontalHeaderLabels(Tlabels_decades)
        self.ui.TableWidget.setVerticalHeaderLabels(tuple([F"цена 1 кв.м. - каждый квартал увеличивается на {self.z}%", "средняя цена 1 кв.м"]))

    def fill_table_with_flat_sell_plan(self): # план продаж в количестве квартир
 
        decades = math.ceil(self.build_time/3)
        self.ui.Table_with_flat_sell_plan.setRowCount(14)
        self.ui.Table_with_flat_sell_plan.setColumnCount(decades)
        self.ui.Table_with_flat_sell_plan.setHorizontalHeaderLabels(["" for i in range(decades)])
        self.ui.Table_with_flat_sell_plan.setVerticalHeaderLabels([ "по стратегии 1 - в начале",
                                                                    "по стратегии 2 - в середине",
                                                                    "по стратегии 3 - в конце",
                                                                    "по стратегии 4 - равномерно",
                                                                    "план продаж в руб. по ценам:",
                                                                    "по стратегии 1 - в начале",
                                                                    "по стратегии 2 - в середине",
                                                                    "по стратегии 3 - в конце",
                                                                    "по стратегии 4 - равномерно",
                                                                    "количество денег на эскроу счетах:",
                                                                    "по стратегии 1 - в начале",
                                                                    "по стратегии 2 - в середине",
                                                                    "по стратегии 3 - в конце",
                                                                    "по стратегии 4 - равномерно"])


        def fill_cells(row, point):
            flat_amount = self.n
            avg_flat_area = self.s
            one_meter_cost = self.p1
            flats = []
            sum1 = 0

            for i in range(point):
                flats.append(math.ceil(flat_amount / (point - i)))
                flat_amount -= flats[i]

            for i, flat in enumerate(flats):
                tmp = flat*(one_meter_cost^i)*avg_flat_area # план продаж
                sum1 += tmp # количество денег на отдельном эскроу-счете
                if(row == 1):
                    self.ui.Table_with_flat_sell_plan.setItem(row, i + self.pointer[0], QTableWidgetItem(str(flat)))
                    self.ui.Table_with_flat_sell_plan.setItem(row+5, i + self.pointer[0], QTableWidgetItem(str(tmp)))
                    self.ui.Table_with_flat_sell_plan.setItem(row+10, i + self.pointer[0], QTableWidgetItem(str(sum1)))
                elif(row == 2):
                    self.ui.Table_with_flat_sell_plan.setItem(row, i + self.pointer[0] + self.pointer[1], QTableWidgetItem(str(flat)))
                    self.ui.Table_with_flat_sell_plan.setItem(row+5, i + self.pointer[0] + self.pointer[1], QTableWidgetItem(str(tmp)))
                    self.ui.Table_with_flat_sell_plan.setItem(row+10, i + self.pointer[0], QTableWidgetItem(str(sum1)))
                else:
                    self.ui.Table_with_flat_sell_plan.setItem(row, i, QTableWidgetItem(str(flat)))
                    self.ui.Table_with_flat_sell_plan.setItem(row+5, i, QTableWidgetItem(str((tmp))))
                    self.ui.Table_with_flat_sell_plan.setItem(row+10, i, QTableWidgetItem(str(sum1)))

        fill_cells(0, self.pointer[0])
        fill_cells(1, self.pointer[1])
        fill_cells(2, self.pointer[0])
        fill_cells(3, decades) # хз, почема decades, мне это больно осознавать, но главное - работает правильно


app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())


