import sys
import math
from PyQt5 import QtWidgets, QtCore, QtGui
#from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QTableWidgetItem, QDesktopWidget, QWidget
from PyQt5.QtCore import QDate

from zikkurat001 import Ui_MainWindow 
from Tables import Ui_NewWindow
#TASKS:
#СДЕЛАТЬ ПРОВЕРКУ НА ОТРИЦАТЕЛЬНЫЕ ЧИСЛА ДЛЯ не ЗНАю ЧЕГО

#main window
class mywindow(QtWidgets.QMainWindow):
    k = S = n = s = p1 = z = c = build_time = own_money = 0 
    date_start = QDate.currentDate()
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Build.clicked.connect(self.BuildFunc)
        self.ui.Test.clicked.connect(self.Trying) # для процетиков
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
        ##Написать проверку заполнения при вызове Build_func
        self.mini_table_for_necessary_percents = QtWidgets.QTableWidget(self.ui.centralwidget)
        self.mini_table_for_necessary_percents.setObjectName("mini_table_for_necessary_percents")  
        self.mini_table_for_necessary_percents.move(-3000,-3000) 
        self.mini_table_for_necessary_percents.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.mini_table_for_necessary_percents.resizeColumnsToContents()
        self.mini_table_for_necessary_percents.resizeRowsToContents()
        self.mini_table_for_necessary_percents.setRowCount(1)
        self.mini_table_for_necessary_percents.setColumnCount(10)
        self.mini_table_for_necessary_percents.setVerticalHeaderLabels(["процент потребности в деньгах от стоимости проекта"])
        #сделаем пока автозаполнение процентов
        self.mini_table_for_necessary_percents.setItem(0,0,QTableWidgetItem("9,68508804395618"))
        self.mini_table_for_necessary_percents.setItem(0,1,QTableWidgetItem("11,570903952796"))
        self.mini_table_for_necessary_percents.setItem(0,2,QTableWidgetItem("14,9494931029218"))
        self.mini_table_for_necessary_percents.setItem(0,3,QTableWidgetItem("11,0695162827756"))
        self.mini_table_for_necessary_percents.setItem(0,4,QTableWidgetItem("13,3757296894168"))
        self.mini_table_for_necessary_percents.setItem(0,5,QTableWidgetItem("13,0110106892431"))
        self.mini_table_for_necessary_percents.setItem(0,6,QTableWidgetItem("13,3302211572039"))
        self.mini_table_for_necessary_percents.setItem(0,7,QTableWidgetItem("3,32028347130497"))
        self.mini_table_for_necessary_percents.setItem(0,8,QTableWidgetItem("3,93512861368219"))
        self.mini_table_for_necessary_percents.setItem(0,9,QTableWidgetItem("5,75262499669945")) # по идее тут вместо самой последней 5 должно +3 , т.е 8. Надо было для подсчета нормального так сделать
        ##############################################
        self.ui.Apartments_amount.setText("368")
        self.ui.Average_area_of_apartments.setText("66")
        self.ui.Bulding_duration.setText("30")
        self.ui.Increasing_percentage.setText("2")
        self.ui.Start_money.setText("189082080")
        self.ui.Total_area.setText("24000")
        self.ui.Start_cost.setText("54000")
        self.ui.Self_cost.setText("51900")
        
        
    def show_date(self,date):
        self.date_start = date
        print(QDate.longMonthName(date.month()))
    
        
    def get_dimensions(self):
        l = (self.k,self.S,self.n,self.s,self.p1,self.z,self.build_time,self.own_money,self.c, self.date_start, self.Project_cost)
        return l

    def BuildFunc(self):
        if(self.isnt_field_empty()): 
            if(self.ui.Project_cost.text() == ""):
               tmp = int(self.ui.Self_cost.text())*int(self.ui.Apartments_amount.text()) * int(self.ui.Average_area_of_apartments.text())
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
            self.Project_cost = int(self.ui.Project_cost.text())
            
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
    
    def Trying(self):
        pass
    
#Это теперь дочерний класс класса mywindow
class newwindow(QtWidgets.QMainWindow):
    
    def __init__(self, parent):
        super(newwindow, self).__init__(parent)
        self.ui = Ui_NewWindow()
        self.ui.setupUi(self)

        self.k, self.S, self.n, self.s, self.p1,self.z, self.build_time, self.own_money, self.c, self.date_start, self.project_cost = mywindow.get_dimensions(self.parent())
        self.decades = math.ceil(self.build_time / 3)
        cp = QDesktopWidget().availableGeometry().center()
        self.move(int(round(cp.x() - self.width() / 2)), int(round(cp.y() - self.height() / 2 - 20)))
    
        self.credit_money = self.project_cost - self.own_money #заемные средства 

        #делаем все ячейки в таблицe read-only
        def read_only_tables(table):
            for i in range(table.rowCount()):
                for j in range(table.columnCount()):
                    if(table.item(i, j) != None): # Если не сделать проверку на None(NULL), то когда он пытается обратиться к пустой ячейке, он падает, 
                                                  #т.к она NoneType -_-
                        table.item(i, j).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                    else:
                        table.setItem(i, j, QTableWidgetItem(""))  #Поэтому надо положить в нее хотя бы пустую строку
                        table.item(i, j).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        def align_items(table):
            for i in range(table.rowCount()):
                for j in range(table.columnCount()):
                    if(table.item(i, j) != None): # Если не сделать проверку на None(NULL), то когда он пытается обратиться к пустой ячейке, он падает, 
                                                  #т.к она NoneType -_-
                        table.item(i, j).setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                    else:
                        table.setItem(i, j, QTableWidgetItem(""))  #Поэтому надо положить в нее хотя бы пустую строку
                        table.item(i, j).setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        
        self.TableWidget = QtWidgets.QTableWidget(self.ui.centralwidget)
        self.TableWidget.setObjectName("Table_decade")
        self.TableWidget.move(-3000,-3000) 
        self.TableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.TableWidget.resizeColumnsToContents()
        self.TableWidget.resizeRowsToContents()
        self.fill_table()
        self.fill_horizontal_headers(self.TableWidget)
        self.TableWidget.setHorizontalHeaderItem( self.decades, QTableWidgetItem("Средняя цена"))
        read_only_tables(self.TableWidget)
        align_items(self.TableWidget)
        
        #self.TableWidget.setStyleSheet("QTableCornerButton::section{border-image:url(Corner.png)}")

        self.Table_with_flat_sell_plan = QtWidgets.QTableWidget(self.ui.centralwidget)
        self.Table_with_flat_sell_plan.setObjectName("Table_with_flat_sell_plan")  
        self.Table_with_flat_sell_plan.move(-3000,-3000) 
        self.Table_with_flat_sell_plan.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.Table_with_flat_sell_plan.resizeColumnsToContents()
        self.Table_with_flat_sell_plan.resizeRowsToContents()
        self.fill_table_with_flat_sell_plan()
        self.fill_horizontal_headers(self.Table_with_flat_sell_plan)
        self.Table_with_flat_sell_plan.setHorizontalHeaderItem(math.ceil(self.build_time / 3), QTableWidgetItem("Итого"))
        self.Table_with_flat_sell_plan.setHorizontalHeaderItem(math.ceil(self.build_time / 3 + 1), QTableWidgetItem("потеря прибыли у строительной организации"))
        self.Table_with_flat_sell_plan.setColumnWidth(self.decades + 1, 200)
        self.Table_with_flat_sell_plan.setHorizontalHeaderItem( self.decades+ 2, QTableWidgetItem("рентабильность активов"))
        self.Table_with_flat_sell_plan.setColumnWidth( self.decades + 2, 150)

        read_only_tables(self.Table_with_flat_sell_plan)
        align_items(self.Table_with_flat_sell_plan)

        self.escrow_rate = QtWidgets.QTableWidget(self.ui.centralwidget)
        self.escrow_rate.setObjectName("escrow_rate")  
        self.escrow_rate.move(-3000,-3000) 
        self.escrow_rate.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.escrow_rate.resizeColumnsToContents()
        self.escrow_rate.resizeRowsToContents()
        self.fill_escrow_rate()
        
        read_only_tables(self.escrow_rate)
        align_items(self.escrow_rate)
        

        self.credit_is_got_fully_at_the_beginning = QtWidgets.QTableWidget(self.ui.centralwidget)
        self.credit_is_got_fully_at_the_beginning.setObjectName("credit_is_got_fully_atThe_beginning")  
        self.credit_is_got_fully_at_the_beginning.move(-3000,-3000) 
        self.credit_is_got_fully_at_the_beginning.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.credit_is_got_fully_at_the_beginning.resizeColumnsToContents()
        self.credit_is_got_fully_at_the_beginning.resizeRowsToContents()
    
        self.fill_credit_is_got_fully_at_the_beginning()
        read_only_tables(self.credit_is_got_fully_at_the_beginning)
        align_items(self.credit_is_got_fully_at_the_beginning)

        self.credit_line_chooses_evenly = QtWidgets.QTableWidget(self.ui.centralwidget)
        self.credit_line_chooses_evenly.setObjectName("credit_line_chooses_evenly")  
        self.credit_line_chooses_evenly.move(-3000,-3000) 
        self.credit_line_chooses_evenly.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.credit_line_chooses_evenly.resizeColumnsToContents()
        self.credit_line_chooses_evenly.resizeRowsToContents()
    
        self.fill_credit_line_chooses_evenly()
        read_only_tables(self.credit_line_chooses_evenly)
        align_items(self.credit_line_chooses_evenly)


        # self.mini_table_for_necessary_percents = QtWidgets.QTableWidget(self.ui.centralwidget)
        # self.mini_table_for_necessary_percents.setObjectName("mini_table_for_necessary_percents")  
        # self.mini_table_for_necessary_percents.move(-3000,-3000) 
        # self.mini_table_for_necessary_percents.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        # self.mini_table_for_necessary_percents.resizeColumnsToContents()
        # self.mini_table_for_necessary_percents.resizeRowsToContents()
        # self.mini_table_for_necessary_percents.setRowCount(1)
        # self.mini_table_for_necessary_percents.setColumnCount(self.decades)
        # self.mini_table_for_necessary_percents.setVerticalHeaderLabels(["процент потребности в деньгах от стоимости проекта"])
        # #сделаем пока автозаполнение процентов
        # self.mini_table_for_necessary_percents.setItem(0,0,QTableWidgetItem("9,68508804395618"))
        # self.mini_table_for_necessary_percents.setItem(0,1,QTableWidgetItem("11,570903952796"))
        # self.mini_table_for_necessary_percents.setItem(0,2,QTableWidgetItem("14,9494931029218"))
        # self.mini_table_for_necessary_percents.setItem(0,3,QTableWidgetItem("11,0695162827756"))
        # self.mini_table_for_necessary_percents.setItem(0,4,QTableWidgetItem("13,3757296894168"))
        # self.mini_table_for_necessary_percents.setItem(0,5,QTableWidgetItem("13,0110106892431"))
        # self.mini_table_for_necessary_percents.setItem(0,6,QTableWidgetItem("13,3302211572039"))
        # self.mini_table_for_necessary_percents.setItem(0,7,QTableWidgetItem("3,32028347130497"))
        # self.mini_table_for_necessary_percents.setItem(0,8,QTableWidgetItem("3,93512861368219"))
        # self.mini_table_for_necessary_percents.setItem(0,9,QTableWidgetItem("5,75262499669945")) # по идее тут вместо самой последней 5 должно +3 , т.е 8. Надо было для подсчета нормального так сделать
        # align_items(self.mini_table_for_necessary_percents)

        self.main_table_necessary_percents = QtWidgets.QTableWidget(self.ui.centralwidget)
        self.main_table_necessary_percents.setObjectName("main_table_necessary_percents")  
        self.main_table_necessary_percents.move(-3000,-3000) 
        self.main_table_necessary_percents.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.main_table_necessary_percents.resizeColumnsToContents()
        self.main_table_necessary_percents.resizeRowsToContents()
        self.main_table_necessary_percents.setRowCount(7)
        self.main_table_necessary_percents.setColumnCount(self.decades + 5)
        self.main_table_necessary_percents.setVerticalHeaderLabels(["потребность в денежныж средствах для реализации проекта", 
                                                                    "заемных средств, которые нужно взять у банка", 
                                                                    "количество заемных средств",
                                                                    "по 1 стратегии - в начале",
                                                                    "по 2 стратегии - в середине", 
                                                                    "по 3 стратегии - в конце", 
                                                                    "по 4 стратегии - равномерно"])
        self.fill_horizontal_headers(self.main_table_necessary_percents)
        self.main_table_necessary_percents.setHorizontalHeaderItem(self.decades, QTableWidgetItem("Сумма платежей"))
        self.main_table_necessary_percents.setHorizontalHeaderItem(self.decades + 1, QTableWidgetItem("Средневзвешенная процентная ставка"))
        self.main_table_necessary_percents.setHorizontalHeaderItem(self.decades + 2, QTableWidgetItem("Эффект финансового рычага"))
        self.main_table_necessary_percents.setHorizontalHeaderItem(self.decades + 3, QTableWidgetItem("Рентабильность собственного капиатала"))
        self.main_table_necessary_percents.setHorizontalHeaderItem(self.decades + 4, QTableWidgetItem("Итого"))
        self.main_table_necessary_percents.setColumnWidth(self.decades + 1, 230)
        self.main_table_necessary_percents.setColumnWidth(self.decades + 2, 180)
        self.main_table_necessary_percents.setColumnWidth(self.decades + 3, 240)
        self.fill_main_table_necessary_percents()
        align_items(self.main_table_necessary_percents)
        read_only_tables(self.main_table_necessary_percents)


        #14. Прибыль до налогообложения строительной организации при различных стратегиях
        #продаж с использованием заемных средств в объеме 85 % от стоимости проекта.
        #таблица №2 из статьи, задание 14
        self.table_85_percent_debt_money = QtWidgets.QTableWidget(self.ui.centralwidget)
        self.table_85_percent_debt_money.setObjectName("table_85_percent_debt_money")  
        self.table_85_percent_debt_money.move(-3000,-3000) 
        self.table_85_percent_debt_money.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table_85_percent_debt_money.resizeColumnsToContents()
        self.table_85_percent_debt_money.resizeRowsToContents()
        self.table_85_percent_debt_money.setRowCount(3)
        self.table_85_percent_debt_money.setColumnCount(4)
        self.table_85_percent_debt_money.setVerticalHeaderLabels(["в начале строительства", "равномерно в течение строительства", "по мере необходимости"])
        self.table_85_percent_debt_money.setHorizontalHeaderLabels(["в начале", "в середине", "в конце", "равномерно"])
        self.fill_table_85_percent_debt_money()
        align_items(self.table_85_percent_debt_money)
        read_only_tables(self.table_85_percent_debt_money)

        #15.	
        #Расчет эффект финансового рычага строительной организации при 
        #различных стратегиях продаж с использованием заемных средств
        self.table_financial_leverage_with_debt = QtWidgets.QTableWidget(self.ui.centralwidget)
        self.table_financial_leverage_with_debt.setObjectName("table_financial_leverage_with_debt")  
        self.table_financial_leverage_with_debt.move(-3000,-3000) 
        self.table_financial_leverage_with_debt.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table_financial_leverage_with_debt.resizeColumnsToContents()
        self.table_financial_leverage_with_debt.resizeRowsToContents()
        self.table_financial_leverage_with_debt.setRowCount(3)
        self.table_financial_leverage_with_debt.setColumnCount(4)
        self.table_financial_leverage_with_debt.setVerticalHeaderLabels(["в начале строительства", "равномерно в течение строительства", "по мере необходимости"])
        self.table_financial_leverage_with_debt.setHorizontalHeaderLabels(["в начале", "в середине", "в конце", "равномерно"])
        self.fill_table_financial_leverage_with_debt()
        align_items(self.table_financial_leverage_with_debt)
        read_only_tables(self.table_financial_leverage_with_debt)

        self.general_table_bank_position = QtWidgets.QTableWidget(self.ui.centralwidget)
        self.general_table_bank_position.setObjectName("general_table_bank_position")  
        self.general_table_bank_position.move(-3000,-3000) 
        self.general_table_bank_position.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.general_table_bank_position.resizeColumnsToContents()
        self.general_table_bank_position.resizeRowsToContents()
        self.general_table_bank_position.setRowCount(3)
        self.general_table_bank_position.setColumnCount(4)
        self.general_table_bank_position.setVerticalHeaderLabels(["в начале строительства", "равномерно в течение строительства", "по мере необходимости"])
        self.general_table_bank_position.setHorizontalHeaderLabels(["в начале", "в середине", "в конце", "равномерно"])
        self.fill_general_table_bank_position()


        #16.
        #Рентабельность собственного капитала строительной организации
        #при различных стратегиях продаж с использованием заемных средств
        #в объеме 85 % от стоимости проекта, в процентах.
        self.table_profitability_of_own_money = QtWidgets.QTableWidget(self.ui.centralwidget)
        self.table_profitability_of_own_money.setObjectName("table_profitability_of_own_money")  
        self.table_profitability_of_own_money.move(-3000,-3000) 
        self.table_profitability_of_own_money.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table_profitability_of_own_money.resizeColumnsToContents()
        self.table_profitability_of_own_money.resizeRowsToContents()
        self.table_profitability_of_own_money.setRowCount(3)
        self.table_profitability_of_own_money.setColumnCount(4)
        self.table_profitability_of_own_money.setVerticalHeaderLabels(["в начале строительства", "равномерно в течение строительства", "по мере необходимости"])
        self.table_profitability_of_own_money.setHorizontalHeaderLabels(["в начале", "в середине", "в конце", "равномерно"])
        self.fill_table_profitability_of_own_money()


        #17
        #Количество денежных средств, которые получит банк за предоставления кредита в размере 85%
        #от стоимости проекта за весь срок строительства
        self.table_bank_money_all_time = QtWidgets.QTableWidget(self.ui.centralwidget)
        self.table_bank_money_all_time.setObjectName("table_bank_money_all_time")  
        self.table_bank_money_all_time.move(-3000,-3000) 
        self.table_bank_money_all_time.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table_bank_money_all_time.resizeColumnsToContents()
        self.table_bank_money_all_time.resizeRowsToContents()
        self.table_bank_money_all_time.setRowCount(3)
        self.table_bank_money_all_time.setColumnCount(4)
        self.table_bank_money_all_time.setVerticalHeaderLabels(["в начале строительства", "равномерно в течение строительства", "по мере необходимости"])
        self.table_bank_money_all_time.setHorizontalHeaderLabels(["в начале", "в середине", "в конце", "равномерно"])
        self.fill_table_bank_money_all_time()


        #18
        #Расчет средневзвешенной процентной ставки по заемному капиталу строительной организации при кредитовании 

        self.table_average_weighted_rate = QtWidgets.QTableWidget(self.ui.centralwidget)
        self.table_average_weighted_rate.setObjectName("table_average_weighted_rate")  
        self.table_average_weighted_rate.move(-3000,-3000) 
        self.table_average_weighted_rate.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table_average_weighted_rate.resizeColumnsToContents()
        self.table_average_weighted_rate.resizeRowsToContents()
        self.table_average_weighted_rate.setRowCount(3)
        self.table_average_weighted_rate.setColumnCount(4)
        self.table_average_weighted_rate.setVerticalHeaderLabels(["в начале строительства", "равномерно в течение строительства", "по мере необходимости"])
        self.table_average_weighted_rate.setHorizontalHeaderLabels(["в начале", "в середине", "в конце", "равномерно"])
        self.fill_table_average_weighted_rate()


        #19.
        #Увеличение себестоимости 1м2 при различных видах кредитования и времени пополнения
        #счетов эскроу при кредитовании строительной организации
        self.table_encrease_owncost_area = QtWidgets.QTableWidget(self.ui.centralwidget)
        self.table_encrease_owncost_area.setObjectName("table_encrease_owncost_area")  
        self.table_encrease_owncost_area.move(-3000,-3000) 
        self.table_encrease_owncost_area.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table_encrease_owncost_area.resizeColumnsToContents()
        self.table_encrease_owncost_area.resizeRowsToContents()
        self.table_encrease_owncost_area.setRowCount(3)
        self.table_encrease_owncost_area.setColumnCount(4)
        self.table_encrease_owncost_area.setVerticalHeaderLabels(["в начале строительства", "равномерно в течение строительства", "по мере необходимости"])
        self.table_encrease_owncost_area.setHorizontalHeaderLabels(["в начале", "в середине", "в конце", "равномерно"])
        self.fill_table_encrease_owncost_area()


        #20
        #Увеличение себестоимости 1м2 при различных видах кредитования и времени пополнения
        #счетов эскроу при кредитовании строительной организации, %
        self.table_encrease_owncost_area_percentage = QtWidgets.QTableWidget(self.ui.centralwidget)
        self.table_encrease_owncost_area_percentage.setObjectName("table_encrease_owncost_area_percentage")  
        self.table_encrease_owncost_area_percentage.move(-3000,-3000) 
        self.table_encrease_owncost_area_percentage.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table_encrease_owncost_area_percentage.resizeColumnsToContents()
        self.table_encrease_owncost_area_percentage.resizeRowsToContents()
        self.table_encrease_owncost_area_percentage.setRowCount(3)
        self.table_encrease_owncost_area_percentage.setColumnCount(4)
        self.table_encrease_owncost_area_percentage.setVerticalHeaderLabels(["в начале строительства", "равномерно в течение строительства", "по мере необходимости"])
        self.table_encrease_owncost_area_percentage.setHorizontalHeaderLabels(["в начале", "в середине", "в конце", "равномерно"])
        self.fill_table_encrease_owncost_area_percentage()


        #21
        #Прикидка поступления денежных средств в бюджет за счет налоговых отчислений
        #от строительной организации и банка при кредитовании строительной организации 
        self.table_budget_money_income = QtWidgets.QTableWidget(self.ui.centralwidget)
        self.table_budget_money_income.setObjectName("table_budget_money_income")  
        self.table_budget_money_income.move(-3000,-3000) 
        self.table_budget_money_income.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table_budget_money_income.resizeColumnsToContents()
        self.table_budget_money_income.resizeRowsToContents()
        self.table_budget_money_income.setRowCount(3)
        self.table_budget_money_income.setColumnCount(4)
        self.table_budget_money_income.setVerticalHeaderLabels(["в начале строительства", "равномерно в течение строительства", "по мере необходимости"])
        self.table_budget_money_income.setHorizontalHeaderLabels(["в начале", "в середине", "в конце", "равномерно"])
        self.fill_table_budget_money_income()

        self.ui.pushButton.clicked.connect(self._exit)
        self.ui.show_tables.clicked.connect(self.choose_tables)
        self.ui.clear_tables.clicked.connect(self.clear_tables)



    #КОРОЧЕ. ТУТ ВСЕ СОСТОИТ ИЗ КОСТЫЛЕЙ. КOГДА ВСЕ СДЕЛАЕМ, НАДО СПРОСИТЬ ПАРУ МОМЕНТОВ И ЗАПОЛНЯТЬ ЕЕ НОРМАЛЬНО
    # ЕЩЕ ВАЖНЫЙ КОМЕНТ!!!!!!! ТУТ СУММИРОВАНИЕ ИДЕТ НЕ ПО ВСЕМ СТОБЦАМ ТАБЛИЦЫ, А ТОЛЬКО КОНКРЕТНЫЕ ПЛАТЕЖИ!!!!
    #НАДО ПОТОМ СПРОСИТЬ КАК ПРАВИЛЬНО, ЩАС ПРОСТО ОСТАВИМ ТАК, ЧТОБЫ ЧИСЛА СХОДИЛИСЬ!!!!!!!!!!!!
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    def fill_main_table_necessary_percents(self):
        
        percents_sum = 0
        for i in range(self.parent().mini_table_for_necessary_percents.columnCount()):
            if(self.parent().mini_table_for_necessary_percents.item(0, i) == None):
                message = 'Вы не заполнили все ячейки'
                QtWidgets.QMessageBox.warning(self, 'Уведомление', message,
                                                        QtWidgets.QMessageBox.Ok)
                return
            else:
                percent = float(self.parent().mini_table_for_necessary_percents.item(0, i).text().replace(',', '.'))
                # percent = int(percent * 100)
                # print(percent)
                percents_sum += percent
                # print(percents_sum)
        
        if(percents_sum != 100):
            message = f'Сумма процентов не равна 100 ({percents_sum})'
            QtWidgets.QMessageBox.warning(self, 'Уведомление', message,
                                                        QtWidgets.QMessageBox.Ok)
            return
        
        for i in range(self.parent().mini_table_for_necessary_percents.columnCount()):
            TableItem = self.parent().mini_table_for_necessary_percents.item(0, i).text().replace(',', '.') #это надо из-за того, что дробные числа в питоне пишутся через точку, а ввести могут с запятыми 
            cell_info = self.project_cost * float(TableItem) / 100
            self.main_table_necessary_percents.setItem(0, i, QTableWidgetItem(str(cell_info)))
            self.main_table_necessary_percents.setItem(1, i, QTableWidgetItem(str(cell_info)))

        self.main_table_necessary_percents.setItem(1, 0, QTableWidgetItem('0'))
        self.main_table_necessary_percents.setItem(1, 1, QTableWidgetItem('78859731.95'))
        
        self.main_table_necessary_percents.update()
        tmp_sum = 0
        for i in range(self.parent().mini_table_for_necessary_percents.columnCount()):
            tmp_sum += float(self.main_table_necessary_percents.item(1, i).text())
            self.main_table_necessary_percents.setItem(2, i, QTableWidgetItem(str(tmp_sum)))

        for i in range(4):
            row_sum = 0
            for j in range(1, self.decades):
                tmp = float(self.main_table_necessary_percents.item(2, j).text())
                percent = float(self.escrow_rate.item(i,j).text())
                row_sum += tmp * percent / 4
                self.main_table_necessary_percents.setItem(i + 3, j, QTableWidgetItem(str(tmp *percent / 4 )))
            self.main_table_necessary_percents.setItem(i + 3, self.decades, QTableWidgetItem(str(row_sum)))
            self.main_table_necessary_percents.setItem(i + 3, self.decades + 1, QTableWidgetItem(str(round(row_sum / self.credit_money * 100 , 2))))
        
        for i in range(4):
            rent = float(self.Table_with_flat_sell_plan.item(i + 5, self.decades + 2).text())
            rate = float(self.main_table_necessary_percents.item(i + 3, self.decades + 1).text())
            effect = 0.8 * (rent - rate / 100) * self.credit_money / self.own_money
            self.main_table_necessary_percents.setItem(i + 3, self.decades + 2, QTableWidgetItem(str(effect))) # Эффект финансового рычага
            self.main_table_necessary_percents.setItem(i + 3, self.decades + 3, QTableWidgetItem(str(0.8 * rent + effect))) # Рентабильность собственного капитала
            
        for i in range(4):
            total_sum = 0
            for j in range(2,self.decades):
                total_sum += float(self.main_table_necessary_percents.item(i + 3, j).text())
            
            total_sum += self.credit_money + self.own_money
            self.main_table_necessary_percents.setItem(i + 3, self.decades + 4, QTableWidgetItem(str(round(total_sum, 2)))) #Итого
        
        #self.fill_general_table_bank_position()
 
    def clear_tables(self):
        tables = self.ui.centralwidget.findChildren(QtWidgets.QTableWidget)
        for table in tables:
            table.move(-3000,-3000)

    def choose_tables(self):

        current_height = 100
        tables = self.ui.centralwidget.findChildren(QtWidgets.QTableWidget)
        #self.show_main_table.move(-3000, -3000)
        for table in tables:
            table.move(-3000,-3000)
        selected_items = self.ui.listWidget.selectedItems()

        def check_height(height):
            if(height > 1000):
                message = 'Слишком много таблиц'
                QtWidgets.QMessageBox.warning(self, 'Уведомление', message,
                                                        QtWidgets.QMessageBox.Ok)
                
                return False
            return True

        for elem in selected_items:
            if(elem.text() == 'Цена 1м^2'):
                if(check_height(current_height + self.TableWidget.height() + 10)):
                    self.TableWidget.move(0,current_height)
                    current_height += self.TableWidget.height() + 10
                    self.TableWidget.resize(1600, self.TableWidget.height())
                else:
                    break
            elif(elem.text() == 'План продаж'):
                if(check_height(current_height + self.Table_with_flat_sell_plan.height() + 10)):
                    self.Table_with_flat_sell_plan.move(0,current_height)
                    current_height += self.Table_with_flat_sell_plan.height() + 10
                    self.Table_with_flat_sell_plan.resize(1600, self.Table_with_flat_sell_plan.height())
                else:
                    break
            elif(elem.text() == 'Определение процентной ставки на эскроу'):
                if(check_height(current_height + self.escrow_rate.height() + 10)):
                    self.escrow_rate.move(0,current_height)
                    current_height += self.escrow_rate.height() + 10
                    self.escrow_rate.resize(1600, self.escrow_rate.height())
                else:
                    break
            elif(elem.text() == "если кредит получен единовременно в начале, то платежи по процентам за пользование заемными средствами в конце периода"):
                if(check_height(current_height + self.credit_is_got_fully_at_the_beginning.height() + 10)):
                    self.credit_is_got_fully_at_the_beginning.move(0, current_height)
                    current_height += self.credit_is_got_fully_at_the_beginning.height() + 10
                    self.credit_is_got_fully_at_the_beginning.resize(1600, self.credit_is_got_fully_at_the_beginning.height())
                else:
                    break
            elif(elem.text() == "если кредитная линия выбирается равномерно в течении срока строительства, то платежи по процентам за пользование заемными средствами в конце периода"):
                if(check_height(current_height + self.credit_line_chooses_evenly.height() + 10)):
                    self.credit_line_chooses_evenly.move(0, current_height)
                    current_height += self.credit_line_chooses_evenly.height() + 10
                    self.credit_line_chooses_evenly.resize(1600, self.credit_line_chooses_evenly.height())
                else:
                    break
            elif(elem.text() == "если кредитная линия выбирается по мере необходимости строительного процесса, то платежи по процентам за пользование заемными средствами в конце периода"):
                if(check_height(current_height + 10 + self.main_table_necessary_percents.height() + 10)):
                    #self.mini_table_for_necessary_percents.move(0, current_height)
                    #self.mini_table_for_necessary_percents.resize(1300, self.mini_table_for_necessary_percents.height())
                    #self.show_main_table.move(10, current_height)
                    #current_height += self.mini_table_for_necessary_percents.height() + 10
                    

                    self.main_table_necessary_percents.move(0, current_height)
                    self.main_table_necessary_percents.resize(1600, self.main_table_necessary_percents.height())
                    current_height += self.main_table_necessary_percents.height() + 10
                else:
                    break
            elif(elem.text() == "Процентные выплаты, которые получит банк"):
                if(check_height(current_height + self.general_table_bank_position.height() + 10 )):
                    self.general_table_bank_position.move(0, current_height)
                    self.general_table_bank_position.resize(800, self.general_table_bank_position.height())
                    current_height += self.general_table_bank_position.height() + 10
                else:
                    break
            elif(elem.text() == "Прибыль с использованием заемных средств в объеме 85 % от стоимости проекта"):
                if(check_height(current_height + self.table_85_percent_debt_money.height() + 10 )):
                    self.table_85_percent_debt_money.move(0, current_height)
                    self.table_85_percent_debt_money.resize(800, self.table_85_percent_debt_money.height())
                    current_height += self.table_85_percent_debt_money.height() + 10
                else:
                    break
            elif(elem.text() == "Финансовый рычаг при различных стратегиях продаж с использованием заемных средств"):
                if(check_height(current_height + self.table_financial_leverage_with_debt.height() + 10 )):
                    self.table_financial_leverage_with_debt.move(0, current_height)
                    self.table_financial_leverage_with_debt.resize(800, self.table_financial_leverage_with_debt.height())
                    current_height += self.table_financial_leverage_with_debt.height() + 10
                else:
                    break
            elif(elem.text() == "Рентабельность собственного капитала при различных стратегиях продаж с использованием заемных средств"):
                if(check_height(current_height + self.table_profitability_of_own_money.height() + 10 )):
                    self.table_profitability_of_own_money.move(0, current_height)
                    self.table_profitability_of_own_money.resize(800, self.table_profitability_of_own_money.height())
                    current_height += self.table_profitability_of_own_money.height() + 10
                else:
                    break
            elif(elem.text() == "Процентные выплаты, получаемые банком за предоставление кредита"):
                if(check_height(current_height + self.table_bank_money_all_time.height() + 10 )):
                    self.table_bank_money_all_time.move(0, current_height)
                    self.table_bank_money_all_time.resize(800, self.table_bank_money_all_time.height())
                    current_height += self.table_bank_money_all_time.height() + 10
                else:
                    break
            elif(elem.text() == "Средневзвешенная процентная ставка по заемному капиталу строительной организации"):
                if(check_height(current_height + self.table_average_weighted_rate.height() + 10 )):
                    self.table_average_weighted_rate.move(0, current_height)
                    self.table_average_weighted_rate.resize(800, self.table_average_weighted_rate.height())
                    current_height += self.table_average_weighted_rate.height() + 10
                else:
                    break
            elif(elem.text() == "Увеличение себестоимости 1м2  при кредитовании строительной организации"):
                if(check_height(current_height + self.table_encrease_owncost_area.height() + 10 )):
                    self.table_encrease_owncost_area.move(0, current_height)
                    self.table_encrease_owncost_area.resize(800, self.table_encrease_owncost_area.height())
                    current_height += self.table_encrease_owncost_area.height() + 10
                else:
                    break
            elif(elem.text() == "Увеличение себестоимости 1м2  при кредитовании строительной организации в %"):
                if(check_height(current_height + self.table_encrease_owncost_area_percentage.height() + 10 )):
                    self.table_encrease_owncost_area_percentage.move(0, current_height)
                    self.table_encrease_owncost_area_percentage.resize(800, self.table_encrease_owncost_area_percentage.height())
                    current_height += self.table_encrease_owncost_area_percentage.height() + 10
                else:
                    break
            elif(elem.text() == "Прикидка поступления денежных средств в бюджет за счет налоговых отчислений от строительной организации и банка"):
                if(check_height(current_height + self.table_budget_money_income.height() + 10 )):
                    self.table_budget_money_income.move(0, current_height)
                    self.table_budget_money_income.resize(800, self.table_budget_money_income.height())
                    current_height += self.table_budget_money_income.height() + 10
                else:
                    break
            
    def _exit(self):
        self.parent().show()
        self.close()
        
    def fill_table(self):  
        decades = math.ceil(self.build_time/3)
        self.TableWidget.setRowCount(2)
        self.TableWidget.setColumnCount(decades + 1)
        price  = self.p1
        avg_sum1 = avg_sum2 = avg_sum3 = total_avg = 0
        self.pointer = [math.floor(decades/3),decades - math.floor(decades/3)*2]

        def toFixed(numObj, digits=0):    #some magic code from StackOverflow
            return f"{numObj:.{digits}f}"
        
        #Объявим тут несколько глобальных массивов, которые понадобятся нам в будущем
        self.Array_of_avg_flat_prices = []
        self.Array_of_flat_prices = []
        for i in range(decades):
            self.Array_of_flat_prices.append(price)
            cell_info = QTableWidgetItem(str(round(price, 2)))
                
            if(i < math.floor(decades/3)):
                avg_sum1 += price
            elif(i < decades - math.floor(decades/3)):
                avg_sum2 += price
            else:
                avg_sum3 += price
            
            total_avg += price
            self.TableWidget.setItem(0 , i, cell_info)
            price = price * (1 + self.z/100)
        
        avg_sum1 = avg_sum1 / self.pointer[0]
        avg_sum2 = avg_sum2 / self.pointer[1]
        avg_sum3 = avg_sum3 / self.pointer[0]
        self.TableWidget.setItem(1 , 0, QTableWidgetItem(str(round(avg_sum1,2))))
        self.TableWidget.setItem(1 , self.pointer[0], QTableWidgetItem(str(round(avg_sum2,2))))
        self.TableWidget.setItem(1 , self.pointer[0] + self.pointer[1], QTableWidgetItem(str(round(avg_sum3,2))))

        total_avg = total_avg / decades   
        self.Array_of_avg_flat_prices = [avg_sum1, avg_sum2 , avg_sum3, total_avg]   #Да, я переопределил тут массив, но мне пофиг, там хотя бы видно, зачем он создан
          
        self.TableWidget.setItem(1, decades, QTableWidgetItem(str(round(total_avg,2))))    

        
        self.TableWidget.setVerticalHeaderLabels([F"цена 1 кв.м. - каждый квартал увеличивается на {self.z}%", "средняя цена 1 кв.м"])

    def fill_table_with_flat_sell_plan(self): # план продаж в количестве квартир
        self.iterator = 0
        decades = math.ceil(self.build_time/3)
        self.Table_with_flat_sell_plan.setRowCount(14)
        self.Table_with_flat_sell_plan.setColumnCount(decades + 3)
        self.Table_with_flat_sell_plan.setHorizontalHeaderLabels(["" for i in range(decades)])
        self.Table_with_flat_sell_plan.setVerticalHeaderLabels([ "по стратегии 1 - в начале",
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

        #Определяем тут глобальные массивы, которые понадобятся в будущем
        self.flats_amount_first_three_strategies = []
        self.flats_amount_fourth_strategy = []
        self.sell_plan_in_rub_first_three_strategies = []
        self.sell_plan_in_rub_fourth_strategy = []
        self.escrow_amount_of_money_first_three_strategies = []
        self.escrow_amount_of_money_fourth_strategy = []
        #Переменные для хранения сумм
        self.sell_plan_sum_of_each_str  = [0, 0, 0, 0]

        def fill_cells(row, point):
            flat_amount = self.n
            avg_flat_area = self.s
            flats = []
            sum1 = 0

            for i in range(point):
                amount = math.ceil(flat_amount / (point - i))
                if(row < 3):
                    self.flats_amount_first_three_strategies.append(amount)
                else:
                    self.flats_amount_fourth_strategy.append(amount)
                 
                flats.append(amount)
                flat_amount -= flats[i]
    
            for i, flat in enumerate(flats):
                perc = self.Array_of_flat_prices[self.iterator]
                tmp = flat*(perc)*avg_flat_area # план продаж
                self.iterator += 1
                sum1 += tmp # количество денег на отдельном эскроу-счете

                if(row < 3):
                    self.sell_plan_in_rub_first_three_strategies.append(tmp)
                    self.escrow_amount_of_money_first_three_strategies.append(sum1)
                else:
                    self.sell_plan_in_rub_fourth_strategy.append(tmp)
                    self.escrow_amount_of_money_fourth_strategy.append(sum1)

                if(row == 1):
                    self.Table_with_flat_sell_plan.setItem(row, i + self.pointer[0], QTableWidgetItem(str(flat)))
                    self.Table_with_flat_sell_plan.setItem(row+5, i + self.pointer[0], QTableWidgetItem(str(round(tmp,1))))
                    self.Table_with_flat_sell_plan.setItem(row+10, i + self.pointer[0], QTableWidgetItem(str(round(sum1,1))))
                elif(row == 2):
                    self.Table_with_flat_sell_plan.setItem(row, i + self.pointer[0] + self.pointer[1], QTableWidgetItem(str(flat)))
                    self.Table_with_flat_sell_plan.setItem(row+5, i + self.pointer[0] + self.pointer[1], QTableWidgetItem(str(round(tmp,1))))
                    self.Table_with_flat_sell_plan.setItem(row+10, i + self.pointer[0] + self.pointer[1], QTableWidgetItem(str(round(sum1,1))))
                else:
                    self.Table_with_flat_sell_plan.setItem(row, i, QTableWidgetItem(str(flat)))
                    self.Table_with_flat_sell_plan.setItem(row+5, i, QTableWidgetItem(str((round(tmp,1)))))
                    self.Table_with_flat_sell_plan.setItem(row+10, i, QTableWidgetItem(str(round(sum1,1))))
        
        
        fill_cells(0, self.pointer[0])
        fill_cells(1, self.pointer[1])
        fill_cells(2, self.pointer[0])
        self.iterator = 0
        fill_cells(3, decades)
        #Заполняем сумму по квартирам в каждой стратегии 
        self.Table_with_flat_sell_plan.setItem(0, decades, QTableWidgetItem(str(sum(self.flats_amount_first_three_strategies[: self.pointer[0]]))))
        self.Table_with_flat_sell_plan.setItem(1, decades, QTableWidgetItem(str(sum(self.flats_amount_first_three_strategies[self.pointer[0]: decades - self.pointer[0]]))))
        self.Table_with_flat_sell_plan.setItem(2, decades, QTableWidgetItem(str(sum(self.flats_amount_first_three_strategies[-self.pointer[0] : ]))))
        self.Table_with_flat_sell_plan.setItem(3, decades, QTableWidgetItem(str(sum(self.flats_amount_fourth_strategy))))
        #Заполняем сумму по плану продаж 
        self.sell_plan_sum_of_each_str[0] = sum(self.sell_plan_in_rub_first_three_strategies[: self.pointer[0]])
        self.Table_with_flat_sell_plan.setItem(5, decades, QTableWidgetItem(str(round( self.sell_plan_sum_of_each_str[0], 2))))

        self.sell_plan_sum_of_each_str[1] = sum(self.sell_plan_in_rub_first_three_strategies[self.pointer[0]: decades - self.pointer[0]])
        self.Table_with_flat_sell_plan.setItem(6, decades, QTableWidgetItem(str(round(self.sell_plan_sum_of_each_str[1], 2))))

        self.sell_plan_sum_of_each_str[2] = sum(self.sell_plan_in_rub_first_three_strategies[-self.pointer[0] : ])
        self.Table_with_flat_sell_plan.setItem(7, decades, QTableWidgetItem(str(round(self.sell_plan_sum_of_each_str[2], 2))))

        self.sell_plan_sum_of_each_str[3] = sum(self.sell_plan_in_rub_fourth_strategy)
        self.Table_with_flat_sell_plan.setItem(8, decades, QTableWidgetItem(str(round(self.sell_plan_sum_of_each_str[3], 2))))

        #Заполним рентабилность активов 
        for i in range(4):
            value = (self.sell_plan_sum_of_each_str[i] - self.S * self.c) / (self.own_money + self.credit_money)
            self.Table_with_flat_sell_plan.setItem(i + 5, decades + 2, QTableWidgetItem(str(value)))
    
    def fill_escrow_rate(self):
        decades = math.ceil(self.build_time / 3)
        new_date = self.date_start.month()
        self.escrow_rate.setRowCount(4)
        self.escrow_rate.setColumnCount(decades)
        self.escrow_rate.setVerticalHeaderLabels([ "по стратегии 1 - в начале",
                                                            "по стратегии 2 - в середине",
                                                            "по стратегии 3 - в конце",
                                                            "по стратегии 4 - равномерно"])



        #ЗАПОЛНЯЕМ ПЕРВУЮ СТРОЧКУ
        for i in range(decades):
            if(self.escrow_amount_of_money_first_three_strategies[i] < self.credit_money / 2 and i < self.pointer[0]):
                cell_info = QTableWidgetItem("0.12")
                self.escrow_rate.setItem(0, i, cell_info)

            elif(self.escrow_amount_of_money_first_three_strategies[i] < self.credit_money * 0.75 and i < self.pointer[0]):
                cell_info = QTableWidgetItem("0.09")
                self.escrow_rate.setItem(0, i, cell_info)

            elif(self.escrow_amount_of_money_first_three_strategies[i] < self.credit_money  and i < self.pointer[0]):
                cell_info = QTableWidgetItem("0.06")
                self.escrow_rate.setItem(0, i, cell_info)

            elif(self.escrow_amount_of_money_first_three_strategies[i] < self.credit_money * 1.5 or i >= self.pointer[0]):
                cell_info = QTableWidgetItem("0.03")
                self.escrow_rate.setItem(0, i, cell_info)     

        #ЗАПОЛНЯЕМ ВТОРУЮ СТРОЧКУ
        for i in range(self.pointer[0]):
            cell_info = QTableWidgetItem("0.12")
            self.escrow_rate.setItem(1, i, cell_info)

        for i in range(self.pointer[0], decades - self.pointer[0]):
            if(self.escrow_amount_of_money_first_three_strategies[i] < self.credit_money / 2 ):
                cell_info = QTableWidgetItem("0.12")
                self.escrow_rate.setItem(1, i, cell_info) 
            elif(self.escrow_amount_of_money_first_three_strategies[i] < self.credit_money * 0.75):
                cell_info = QTableWidgetItem("0.09")
                self.escrow_rate.setItem(1, i, cell_info)
            elif(self.escrow_amount_of_money_first_three_strategies[i] < self.credit_money):
                cell_info = QTableWidgetItem("0.06")
                self.escrow_rate.setItem(1, i, cell_info)
            elif(self.escrow_amount_of_money_first_three_strategies[i] < self.credit_money * 1.5):
                cell_info = QTableWidgetItem("0.03")
                self.escrow_rate.setItem(1, i, cell_info)  
        
        for i in range(decades - self.pointer[0], decades):
            cell_info = QTableWidgetItem("0.03")
            self.escrow_rate.setItem(1, i, cell_info)

        #ЗАПОЛНЯЕМ ТРЕТЬЮ СТРОЧКУ

        for i in range(decades - self.pointer[0]):
            cell_info = QTableWidgetItem("0.12")
            self.escrow_rate.setItem(2, i, cell_info)
        
        for i in range(decades - self.pointer[0], decades):
            if(self.escrow_amount_of_money_first_three_strategies[i] < self.credit_money / 2 ):
                cell_info = QTableWidgetItem("0.12")
                self.escrow_rate.setItem(2, i, cell_info) 
            elif(self.escrow_amount_of_money_first_three_strategies[i] < self.credit_money * 0.75):
                cell_info = QTableWidgetItem("0.09")
                self.escrow_rate.setItem(2, i, cell_info)
            elif(self.escrow_amount_of_money_first_three_strategies[i] < self.credit_money):
                cell_info = QTableWidgetItem("0.06")
                self.escrow_rate.setItem(2, i, cell_info)
            elif(self.escrow_amount_of_money_first_three_strategies[i] < self.credit_money * 1.5):
                cell_info = QTableWidgetItem("0.03")
                self.escrow_rate.setItem(2, i, cell_info) 
             
        #ЗАПОЛНЯЕМ ЧЕТВЕРТУЮ СТРОЧКУ
        labels_names = []
        for i in range(decades):
            month = QDate.longMonthName(new_date)
            day = str(self.date_start.day())
            tempStr = F"{day} {month}"
            labels_names.append(tempStr)
            new_date = new_date + 3
            if(new_date > 12):
                new_date -= 12

            if(self.escrow_amount_of_money_fourth_strategy[i] < self.credit_money / 2 ):
                cell_info = QTableWidgetItem("0.12")
                self.escrow_rate.setItem(3, i, cell_info) 
            elif(self.escrow_amount_of_money_fourth_strategy[i] < self.credit_money * 0.75):
                cell_info = QTableWidgetItem("0.09")
                self.escrow_rate.setItem(3, i, cell_info)
            elif(self.escrow_amount_of_money_fourth_strategy[i] < self.credit_money):
                cell_info = QTableWidgetItem("0.06")
                self.escrow_rate.setItem(3, i, cell_info)
            elif(self.escrow_amount_of_money_fourth_strategy[i] < self.credit_money * 1.5):
                cell_info = QTableWidgetItem("0.03")
                self.escrow_rate.setItem(3, i, cell_info)

        self.escrow_rate.setHorizontalHeaderLabels(labels_names)

    def fill_horizontal_headers(self,table):
        decades = math.ceil(self.build_time / 3)
        new_date = self.date_start.month()
        labels_names = []
        for j in range(decades):
            month = QDate.longMonthName(new_date)
            day = str(self.date_start.day())
            tempStr = F"{day} {month}"
            labels_names.append(tempStr)
            new_date = new_date + 3
            if(new_date > 12):
                new_date -= 12
        table.setHorizontalHeaderLabels(labels_names)

    def fill_credit_is_got_fully_at_the_beginning(self):
        #Объявим несколько массивов
        self.first_strategy_payment = []
        self.second_strategy_payment = []
        self.third_strategy_payment = []
        self.fourth_strategy_payment = []

        decades = math.ceil(self.build_time / 3)
        new_date = self.date_start.month()
        self.credit_is_got_fully_at_the_beginning.setRowCount(4)
        self.credit_is_got_fully_at_the_beginning.setColumnCount(decades + 5)
        self.credit_is_got_fully_at_the_beginning.setVerticalHeaderLabels([ "по стратегии 1 - в начале",
                                                                            "по стратегии 2 - в середине",
                                                                            "по стратегии 3 - в конце",
                                                                            "по стратегии 4 - равномерно"])

        labels_names = []
        for i in range(4):
            for j in range(decades):
                if(i == 0):
                    month = QDate.longMonthName(new_date)
                    day = str(self.date_start.day())
                    tempStr = F"{day} {month}"
                    labels_names.append(tempStr)
                    new_date = new_date + 3
                    if(new_date > 12):
                        new_date -= 12
                
                cell_info = self.credit_money  / 4 * float(self.escrow_rate.item(i, j).text())
                self.credit_is_got_fully_at_the_beginning.setItem(i, j, QTableWidgetItem(str(round(cell_info, 2))))
                if(i == 0):
                    self.first_strategy_payment.append(cell_info)
                elif(i == 1):
                    self.second_strategy_payment.append(cell_info)
                elif(i == 2):
                    self.third_strategy_payment.append(cell_info)
                elif(i == 3):
                    self.fourth_strategy_payment.append(cell_info)
        
        self.credit_is_got_fully_at_the_beginning.setItem(0, decades, QTableWidgetItem(str(round(sum(self.first_strategy_payment), 2))))
        self.credit_is_got_fully_at_the_beginning.setItem(1, decades, QTableWidgetItem(str(round(sum(self.second_strategy_payment), 2))))
        self.credit_is_got_fully_at_the_beginning.setItem(2, decades, QTableWidgetItem(str(round(sum(self.third_strategy_payment), 2))))
        self.credit_is_got_fully_at_the_beginning.setItem(3, decades, QTableWidgetItem(str(round(sum(self.fourth_strategy_payment), 2))))

        self.credit_is_got_fully_at_the_beginning.setItem(0, decades + 1, QTableWidgetItem(str(round(sum(self.first_strategy_payment) / self.credit_money * 100, 2))))
        self.credit_is_got_fully_at_the_beginning.setItem(1, decades + 1, QTableWidgetItem(str(round(sum(self.second_strategy_payment) / self.credit_money * 100, 2))))
        self.credit_is_got_fully_at_the_beginning.setItem(2, decades + 1, QTableWidgetItem(str(round(sum(self.third_strategy_payment) / self.credit_money * 100, 2))))
        self.credit_is_got_fully_at_the_beginning.setItem(3, decades + 1, QTableWidgetItem(str(round(sum(self.fourth_strategy_payment) / self.credit_money * 100, 2))))


        for i in range(4):
            rent = float(self.Table_with_flat_sell_plan.item(i + 5, decades + 2).text())
            rate = float(self.credit_is_got_fully_at_the_beginning.item(i, decades + 1).text())
            effect = 0.8 * (rent - rate / 100) * self.credit_money / self.own_money
            self.credit_is_got_fully_at_the_beginning.setItem(i, decades + 2, QTableWidgetItem(str(effect))) # Эффект финансового рычага
            self.credit_is_got_fully_at_the_beginning.setItem(i, decades + 3, QTableWidgetItem(str(0.8 * rent + effect))) # Рентабильность собственного капитала
            
        for i in range(4):
            total_sum = 0
            for j in range(decades + 3):
                total_sum += float(self.credit_is_got_fully_at_the_beginning.item(i, j).text())
            
            total_sum += self.credit_money + self.own_money
            self.credit_is_got_fully_at_the_beginning.setItem(i, decades + 4, QTableWidgetItem(str(round(total_sum, 2)))) #Итого

        labels_names.append("Сумма платежей")
        labels_names.append("средневзвешенная процентная ставка")
        labels_names.append("Эффект финансового рычага")
        labels_names.append("Рентабильность собственного капитала")
        labels_names.append("Итого")
        self.credit_is_got_fully_at_the_beginning.setColumnWidth(decades + 1, 230)
        self.credit_is_got_fully_at_the_beginning.setColumnWidth(decades + 2, 180)
        self.credit_is_got_fully_at_the_beginning.setColumnWidth(decades + 3, 230)
        self.credit_is_got_fully_at_the_beginning.setHorizontalHeaderLabels(labels_names)

    def fill_credit_line_chooses_evenly(self):
         #Объявим несколько массивов
        self.first_strategy_credit_line = []
        self.second_strategy_credit_line = []
        self.third_strategy_credit_line = []
        self.fourth_strategy_credit_line = []

        decades = math.ceil(self.build_time / 3)
        new_date = self.date_start.month()
        self.credit_line_chooses_evenly.setRowCount(4)
        self.credit_line_chooses_evenly.setColumnCount(decades + 5)
        self.credit_line_chooses_evenly.setVerticalHeaderLabels([ "по стратегии 1 - в начале",
                                                            "по стратегии 2 - в середине",
                                                            "по стратегии 3 - в конце",
                                                            "по стратегии 4 - равномерно"])

        labels_names = []
        for i in range(4):
            for j in range(decades):
                if(i == 0):
                    month = QDate.longMonthName(new_date)
                    day = str(self.date_start.day())
                    tempStr = F"{day} {month}"
                    labels_names.append(tempStr)
                    new_date = new_date + 3
                    if(new_date > 12):
                        new_date -= 12
                
                cell_info = self.credit_money  / (2.5 * 4) * float(self.escrow_rate.item(i, j).text()) 
                self.credit_line_chooses_evenly.setItem(i, j, QTableWidgetItem(str(round(cell_info, 2))))
                if(i == 0):
                    self.first_strategy_credit_line.append(cell_info)
                elif(i == 1):
                    self.second_strategy_credit_line.append(cell_info)
                elif(i == 2):
                    self.third_strategy_credit_line.append(cell_info)
                elif(i == 3):
                    self.fourth_strategy_credit_line.append(cell_info)
        
        self.credit_line_chooses_evenly.setItem(0, decades, QTableWidgetItem(str(round(sum(self.first_strategy_credit_line), 2))))
        self.credit_line_chooses_evenly.setItem(1, decades, QTableWidgetItem(str(round(sum(self.second_strategy_credit_line), 2))))
        self.credit_line_chooses_evenly.setItem(2, decades, QTableWidgetItem(str(round(sum(self.third_strategy_credit_line), 2))))
        self.credit_line_chooses_evenly.setItem(3, decades, QTableWidgetItem(str(round(sum(self.fourth_strategy_credit_line), 2))))

        self.credit_line_chooses_evenly.setItem(0, decades + 1, QTableWidgetItem(str(round(sum(self.first_strategy_credit_line) / self.credit_money * 100, 2))))
        self.credit_line_chooses_evenly.setItem(1, decades + 1, QTableWidgetItem(str(round(sum(self.second_strategy_credit_line) / self.credit_money * 100, 2))))
        self.credit_line_chooses_evenly.setItem(2, decades + 1, QTableWidgetItem(str(round(sum(self.third_strategy_credit_line) / self.credit_money * 100, 2))))
        self.credit_line_chooses_evenly.setItem(3, decades + 1, QTableWidgetItem(str(round(sum(self.fourth_strategy_credit_line) / self.credit_money * 100, 2))))

        for i in range(4):
            rent = float(self.Table_with_flat_sell_plan.item(i + 5, decades + 2).text())
            rate = float(self.credit_line_chooses_evenly.item(i, decades + 1).text())
            effect = 0.8 * (rent - rate / 100) * self.credit_money / self.own_money
            self.credit_line_chooses_evenly.setItem(i, decades + 2, QTableWidgetItem(str(effect))) # Эффект финансового рычага
            self.credit_line_chooses_evenly.setItem(i, decades + 3, QTableWidgetItem(str(0.8 * rent + effect))) # Рентабильность собственного капитала
            
        for i in range(4):
            total_sum = 0
            for j in range(decades + 3):
                total_sum += float(self.credit_line_chooses_evenly.item(i, j).text())
            
            total_sum += self.credit_money + self.own_money
            self.credit_line_chooses_evenly.setItem(i, decades + 4, QTableWidgetItem(str(round(total_sum, 2)))) #Итого




        self.credit_line_chooses_evenly.setColumnWidth(decades + 1, 230)
        self.credit_line_chooses_evenly.setColumnWidth(decades + 2, 180)
        self.credit_line_chooses_evenly.setColumnWidth(decades + 3, 240)

        labels_names.append("Сумма платежей")
        labels_names.append("Средневзвешенная процентная ставка")
        labels_names.append("Эффект финансового рычага")
        labels_names.append("Рентабильность собственного капиатала")
        labels_names.append("Итого")
        self.credit_line_chooses_evenly.setHorizontalHeaderLabels(labels_names)

    def fill_general_table_bank_position(self):
        self.general_table_bank_position.setItem(0, 0, QTableWidgetItem(str(round(sum(self.first_strategy_payment),2))))
        self.general_table_bank_position.setItem(0, 1, QTableWidgetItem(str(round(sum(self.second_strategy_payment),2))))
        self.general_table_bank_position.setItem(0, 2, QTableWidgetItem(str(round(sum(self.third_strategy_payment),2))))
        self.general_table_bank_position.setItem(0, 3, QTableWidgetItem(str(round(sum(self.fourth_strategy_payment),2))))

        self.general_table_bank_position.setItem(1, 0, QTableWidgetItem(str(round(sum(self.first_strategy_credit_line),2))))
        self.general_table_bank_position.setItem(1, 1, QTableWidgetItem(str(round(sum(self.second_strategy_credit_line),2))))
        self.general_table_bank_position.setItem(1, 2, QTableWidgetItem(str(round(sum(self.third_strategy_credit_line),2))))
        self.general_table_bank_position.setItem(1, 3, QTableWidgetItem(str(round(sum(self.fourth_strategy_credit_line),2))))

        self.general_table_bank_position.setItem(2, 0, QTableWidgetItem(self.main_table_necessary_percents.item(3, self.decades).text()))
        self.general_table_bank_position.setItem(2, 1, QTableWidgetItem(self.main_table_necessary_percents.item(4, self.decades).text()))
        self.general_table_bank_position.setItem(2, 2, QTableWidgetItem(self.main_table_necessary_percents.item(5, self.decades).text()))
        self.general_table_bank_position.setItem(2, 3, QTableWidgetItem(self.main_table_necessary_percents.item(6, self.decades).text()))

    def fill_table_financial_leverage_with_debt(self):

        #заполняем первую строку
        for i in range(4):
            item = QTableWidgetItem(str(round(float(self.credit_is_got_fully_at_the_beginning.item(i, self.decades+2).text())*100, 2)))
            self.table_financial_leverage_with_debt.setItem(0, i, item)
        #заполняем вторую строку
        for i in range(4):
           item = QTableWidgetItem(str(round(float(self.credit_line_chooses_evenly.item(i, self.decades+2).text())*100, 2)))
           self.table_financial_leverage_with_debt.setItem(1, i, item)
        #заполняем третью строку
        for i in range(4):
            item = QTableWidgetItem(str(round(float(self.main_table_necessary_percents.item(i+3, self.decades+2).text())*100, 2)))
            self.table_financial_leverage_with_debt.setItem(2, i, item)
        
    def fill_table_85_percent_debt_money(self):
        #заполняем первую строку
        for i in range(4):
            item1 = float(self.Table_with_flat_sell_plan.item(i+5, self.decades).text())
            item2 = float(self.credit_is_got_fully_at_the_beginning.item(i, self.decades + 4).text())
            res = QTableWidgetItem(str((item1 - item2)))
            self.table_85_percent_debt_money.setItem(0, i, res)
        #заполняем вторую строку
        for i in range(4):
            item1 = float(self.Table_with_flat_sell_plan.item(i+5, self.decades).text())
            item2 = float(self.credit_line_chooses_evenly.item(i, self.decades + 4).text())
            res = QTableWidgetItem(str((item1 - item2)))
            self.table_85_percent_debt_money.setItem(1, i, res)
        #заполняем третью строку
        for i in range(4):
            pass
            item1 = float(self.Table_with_flat_sell_plan.item(i+5, self.decades).text())
            item2 = float(self.main_table_necessary_percents.item(i+3, self.decades + 4).text())
            res = QTableWidgetItem(str((item1 - item2)))
            self.table_85_percent_debt_money.setItem(2, i, res)

    def fill_table_profitability_of_own_money(self):
        #заполняем первую строку
        for i in range(4):
            item = QTableWidgetItem(str(round(float(self.credit_is_got_fully_at_the_beginning.item(i, self.decades+3).text())*100, 2)))
            self.table_profitability_of_own_money.setItem(0, i, item)
        #заполняем вторую строку
        for i in range(4):
           item = QTableWidgetItem(str(round(float(self.credit_line_chooses_evenly.item(i, self.decades+3).text())*100, 2)))
           self.table_profitability_of_own_money.setItem(1, i, item)
        #заполняем третью строку
        for i in range(4):
            item = QTableWidgetItem(str(round(float(self.main_table_necessary_percents.item(i+3, self.decades+3).text())*100, 2)))
            self.table_profitability_of_own_money.setItem(2, i, item)
    
    def fill_table_bank_money_all_time(self):
        #заполняем первую строку
        for i in range(4):
            item = QTableWidgetItem(str(round(float(self.credit_is_got_fully_at_the_beginning.item(i, self.decades).text()), 2)))
            self.table_bank_money_all_time.setItem(0, i, item)
        #заполняем вторую строку
        for i in range(4):
           item = QTableWidgetItem(str(round(float(self.credit_line_chooses_evenly.item(i, self.decades).text()), 2)))
           self.table_bank_money_all_time.setItem(1, i, item)
        #заполняем третью строку
        for i in range(4):
            item = QTableWidgetItem(str(round(float(self.main_table_necessary_percents.item(i+3, self.decades).text()), 2)))
            self.table_bank_money_all_time.setItem(2, i, item)

    def fill_table_average_weighted_rate(self):
        #заполняем первую строку
        for i in range(4):
            item = QTableWidgetItem(str(round(float(self.credit_is_got_fully_at_the_beginning.item(i, self.decades+1).text()), 2)))
            self.table_average_weighted_rate.setItem(0, i, item)
        #заполняем вторую строку
        for i in range(4):
           item = QTableWidgetItem(str(round(float(self.credit_line_chooses_evenly.item(i, self.decades+1).text()), 2)))
           self.table_average_weighted_rate.setItem(1, i, item)
        #заполняем третью строку
        for i in range(4):
            item = QTableWidgetItem(str(round(float(self.main_table_necessary_percents.item(i+3, self.decades+1).text()), 2)))
            self.table_average_weighted_rate.setItem(2, i, item)

    def fill_table_encrease_owncost_area(self):
        tmp = self.s*self.n
        for i in range(3):
            for j in range(4):
                item = float(self.table_bank_money_all_time.item(i,j).text())
                self.table_encrease_owncost_area.setItem(i, j, QTableWidgetItem(str(round(float(item/tmp)))))

    def fill_table_encrease_owncost_area_percentage(self):
        for i in range(3):
            for j in range(4):
                item = float(self.table_encrease_owncost_area.item(i,j).text())
                print(self.c, " ",item," ",str(float(item/self.c)))
                self.table_encrease_owncost_area_percentage.setItem(i, j, QTableWidgetItem(str(round(float(item/self.c*100),1))))

    def fill_table_budget_money_income(self):
        pass
app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())
