import sys
import math
from PyQt5 import QtWidgets, QtCore, QtGui
#from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QTableWidgetItem, QDesktopWidget, QWidget
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
        self.ui.Average_area_of_apartments.setText("66")
        self.ui.Bulding_duration.setText("30")
        self.ui.Increasing_percentage.setText("2")
        self.ui.Start_money.setText("1231231399")
        self.ui.Total_area.setText("24000")
        self.ui.Start_cost.setText("54000")
        self.ui.Self_cost.setText("51900")
        
        
    def show_date(self,date):
        self.date_start = date
        #print(QDate.longMonthName(date.month()))
    
        
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

        self.k, self.S, self.n, self.s, self.p1,self.z, self.build_time, self.own_money, self.c, self.date_start, self.project_cost = mywindow.get_dimensions(self.parent())
    
        cp = QDesktopWidget().availableGeometry().center()
        self.move(int(round(cp.x() - self.width() / 2)), int(round(cp.y() - self.height() / 2 - 20)))
    
        self.credit_money = self.project_cost * 0.85 #заемные средства !!!!!!!!!!!!!!!!!!!!!!!!!! FIX IT !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        def read_only_tables(table):
            for i in range(table.rowCount()):
                for j in range(table.columnCount()):
                    if(table.item(i, j) != None): # Если не сделать проверку на None(NULL), то когда он пытается обратиться к пустой ячейке, он падает, т.к она NoneType -_-
                        table.item(i, j).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                    else:
                        table.setItem(i, j, QTableWidgetItem(""))  #Поэтому надо положить в нее хотя бы пустую строку
                        table.item(i, j).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        self.TableWidget = QtWidgets.QTableWidget(self.ui.centralwidget)
        self.TableWidget.setObjectName("Table_decade")
        self.TableWidget.move(-3000,-3000) 
        self.TableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.TableWidget.resizeColumnsToContents()
        self.TableWidget.resizeRowsToContents()
        self.fill_table()

        read_only_tables(self.TableWidget)
        

        self.Table_with_flat_sell_plan = QtWidgets.QTableWidget(self.ui.centralwidget)
        self.Table_with_flat_sell_plan.setObjectName("Table_with_flat_sell_plan")  
        self.Table_with_flat_sell_plan.move(-3000,-3000) 
        self.Table_with_flat_sell_plan.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.Table_with_flat_sell_plan.resizeColumnsToContents()
        self.Table_with_flat_sell_plan.resizeRowsToContents()
        self.fill_table_with_flat_sell_plan()

        read_only_tables(self.Table_with_flat_sell_plan)

        self.escrow_rate = QtWidgets.QTableWidget(self.ui.centralwidget)
        self.escrow_rate.setObjectName("escrow_rate")  
        self.escrow_rate.move(-3000,-3000) 
        self.escrow_rate.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.escrow_rate.resizeColumnsToContents()
        self.escrow_rate.resizeRowsToContents()
        self.fill_escrow_rate()
        
        read_only_tables(self.escrow_rate)
        

        self.credit_is_got_fully_at_the_beginning = QtWidgets.QTableWidget(self.ui.centralwidget)
        self.credit_is_got_fully_at_the_beginning.setObjectName("credit_is_got_fully_atThe_beginning")  
        self.credit_is_got_fully_at_the_beginning.move(-3000,-3000) 
        self.credit_is_got_fully_at_the_beginning.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.credit_is_got_fully_at_the_beginning.resizeColumnsToContents()
        self.credit_is_got_fully_at_the_beginning.resizeRowsToContents()
    
        self.fill_credit_is_got_fully_at_the_beginning()
        read_only_tables(self.credit_is_got_fully_at_the_beginning)
      
        self.credit_line_chooses_evenly = QtWidgets.QTableWidget(self.ui.centralwidget)
        self.credit_line_chooses_evenly.setObjectName("credit_line_chooses_evenly")  
        self.credit_line_chooses_evenly.move(-3000,-3000) 
        self.credit_line_chooses_evenly.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.credit_line_chooses_evenly.resizeColumnsToContents()
        self.credit_line_chooses_evenly.resizeRowsToContents()
    
        self.fill_credit_line_chooses_evenly()
        read_only_tables(self.credit_line_chooses_evenly)

        self.mini_table_for_necessary_percents = QtWidgets.QTableWidget(self.ui.centralwidget)
        self.mini_table_for_necessary_percents.setObjectName("mini_table_for_necessary_percents")  
        self.mini_table_for_necessary_percents.move(-3000,-3000) 
        self.mini_table_for_necessary_percents.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.mini_table_for_necessary_percents.resizeColumnsToContents()
        self.mini_table_for_necessary_percents.resizeRowsToContents()
        self.mini_table_for_necessary_percents.setRowCount(1)
        self.mini_table_for_necessary_percents.setColumnCount(math.ceil(self.build_time / 3))
        self.mini_table_for_necessary_percents.setVerticalHeaderLabels(["процент потребности в деньгах от стоимости проекта"])

        self.main_table_necessary_percents = QtWidgets.QTableWidget(self.ui.centralwidget)
        self.main_table_necessary_percents.setObjectName("main_table_necessary_percents")  
        self.main_table_necessary_percents.move(-3000,-3000) 
        self.main_table_necessary_percents.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.main_table_necessary_percents.resizeColumnsToContents()
        self.main_table_necessary_percents.resizeRowsToContents()
        self.main_table_necessary_percents.setRowCount(7)
        self.main_table_necessary_percents.setColumnCount(math.ceil(self.build_time / 3) + 1)
        self.main_table_necessary_percents.setVerticalHeaderLabels(["потребность в денежныж средствах для реализации проекта", 
                                                                    "заемных средств, которые нужно взять у банка", 
                                                                    "количество заемных средств",
                                                                    "по 1 стратегии - в начале",
                                                                    "по 2 стратегии - в середине", 
                                                                    "по 3 стратегии - в конце", 
                                                                    "по 4 стратегии - равномерно"])

        self.show_main_table = QtWidgets.QPushButton(self.ui.centralwidget)
        self.show_main_table.setText("Заполнить таблицу")
        self.show_main_table.move(-3000, -3000)

        
        self.ui.pushButton.clicked.connect(self._exit)
        self.ui.show_tables.clicked.connect(self.choose_tables)
        self.ui.clear_tables.clicked.connect(self.clear_tables)
        self.show_main_table.clicked.connect(self.fill_main_table)
    

    #МНЕ КОРОЧЕ НАДОЕЛО НА СЕГОДНЯ ПИСАТЬ ЭТУ ФУНКЦИЮ, ПОЭТОМУ ОНА КРИВАЯ ЕЩЕ. НАДО СДЕЛАТЬ РЕПЛЕЙС ВСЕХ ЗАПЯТЫХ НА ТОЧКИ, ИНАЧЕ НЕ ПЕРЕВЕСТИ ВО ФЛОАТ
    def fill_main_table(self):
        percents_sum = 0
        for i in range(self.mini_table_for_necessary_percents.columnCount()):
            if(self.mini_table_for_necessary_percents.item(0, i) == None):
                message = 'Вы не заполнили все ячейки'
                QtWidgets.QMessageBox.warning(self, 'Уведомление', message,
                                                        QtWidgets.QMessageBox.Ok)
                return
            else:
                percents_sum += float(self.mini_table_for_necessary_percents.item(0, i).text())
        if(percents_sum != 100):
            message = f'Сумма процентов не равна 100 ({percents_sum})'
            QtWidgets.QMessageBox.warning(self, 'Уведомление', message,
                                                        QtWidgets.QMessageBox.Ok)
            return
        
        amount_of_credit_money = 0
        for i in range(self.mini_table_for_necessary_percents.columnCount()):
            self.main_table_necessary_percents.setItem(2, i, QTableWidgetItem(str(amount_of_credit_money)))
            cell_info = self.project_cost * float(self.mini_table_for_necessary_percents.item(0, i)) / 100
            amount_of_credit_money += cell_info
            self.main_table_necessary_percents.setItem(0, i, QTableWidgetItem(str(cell_info)))
            self.main_table_necessary_percents.setItem(1, i, QTableWidgetItem(str(cell_info)))

        self.main_table_necessary_percents.setItem(1, 0, QTableWidgetItem(str(0)))
        self.main_table_necessary_percents.setItem(1, 1, QTableWidgetItem(str(78859731,95)))

    def clear_tables(self):
        tables = self.ui.centralwidget.findChildren(QtWidgets.QTableWidget)
        for table in tables:
            table.move(-3000,-3000)

    def choose_tables(self):

        current_height = 100
        tables = self.ui.centralwidget.findChildren(QtWidgets.QTableWidget)
        self.show_main_table.move(-3000, -3000)
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
                if(check_height(current_height + self.mini_table_for_necessary_percents.height() + 10 + self.main_table_necessary_percents.height() + 10)):
                    self.mini_table_for_necessary_percents.move(0, current_height)
                    self.mini_table_for_necessary_percents.resize(1300, self.mini_table_for_necessary_percents.height())
                    self.show_main_table.move(self.mini_table_for_necessary_percents.width() + 10, current_height)
                    current_height += self.mini_table_for_necessary_percents.height() + 10
                    

                    self.main_table_necessary_percents.move(0, current_height)
                    self.main_table_necessary_percents.resize(1600, self.main_table_necessary_percents.height())
                    current_height += self.main_table_necessary_percents.height() + 10
                else:
                    break
                
    def _exit(self):
        self.parent().show()
        self.close()
        
    def fill_table(self):  
        decades = math.ceil(self.build_time/3)
        self.TableWidget.setRowCount(2)
        self.TableWidget.setColumnCount(decades + 1)
        labels_decades = []
        new_date = self.date_start.month()
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
            month = QDate.longMonthName(new_date)
            day = str(self.date_start.day())
            tempStr = F"{day} {month}"
            labels_decades.append(tempStr)
            new_date = new_date + 3

            if(new_date > 12):
                new_date -= 12
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
        labels_decades.append("Средняя цена") 
        Tlabels_decades = labels_decades
        self.TableWidget.setHorizontalHeaderLabels(Tlabels_decades)
        self.TableWidget.setVerticalHeaderLabels(tuple([F"цена 1 кв.м. - каждый квартал увеличивается на {self.z}%", "средняя цена 1 кв.м"]))

    def fill_table_with_flat_sell_plan(self): # план продаж в количестве квартир
        self.iterator = 0
        decades = math.ceil(self.build_time/3)
        self.Table_with_flat_sell_plan.setRowCount(14)
        self.Table_with_flat_sell_plan.setColumnCount(decades)
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

        
        
        def fill_cells(row, point):
            labels_names = []
            new_date = self.date_start.month()
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
                    month = QDate.longMonthName(new_date)
                    day = str(self.date_start.day())
                    tempStr = F"{day} {month}"
                    labels_names.append(tempStr)
                    new_date = new_date + 3
                    if(new_date > 12):
                        new_date -= 12
                
                flats.append(amount)
                flat_amount -= flats[i]
            self.Table_with_flat_sell_plan.setHorizontalHeaderLabels(labels_names)
            for i, flat in enumerate(flats):
                #perc = float(self.ui.TableWidget.item(0, self.iterator).text()) # пересчет стоимости квадратного метра каждый квартал
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
        fill_cells(3, decades) # хз, почема decades, мне это больно осознавать, но главное - работает правильно
    
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

    def fill_credit_is_got_fully_at_the_beginning(self):
        #Объявим несколько массивов
        self.first_strategy_payment = []
        self.second_strategy_payment = []
        self.third_strategy_payment = []
        self.fourth_strategy_payment = []

        decades = math.ceil(self.build_time / 3)
        new_date = self.date_start.month()
        self.credit_is_got_fully_at_the_beginning.setRowCount(4)
        self.credit_is_got_fully_at_the_beginning.setColumnCount(decades + 1)
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

        # self.credit_is_got_fully_at_the_beginning.setItem(0, decades + 1, QTableWidgetItem(str(round(sum(self.first_strategy_payment) / self.credit_money * 100, 2))))
        # self.credit_is_got_fully_at_the_beginning.setItem(1, decades + 1, QTableWidgetItem(str(round(sum(self.second_strategy_payment) / self.credit_money * 100, 2))))
        # self.credit_is_got_fully_at_the_beginning.setItem(2, decades + 1, QTableWidgetItem(str(round(sum(self.third_strategy_payment) / self.credit_money * 100, 2))))
        # self.credit_is_got_fully_at_the_beginning.setItem(3, decades + 1, QTableWidgetItem(str(round(sum(self.fourth_strategy_payment) / self.credit_money * 100, 2))))


        

        labels_names.append("Сумма платежей")
        # labels_names.append("Средневзвешенная процентная ставка")
        # labels_names.append("Эффект финансового рычага")
        # labels_names.append("Рентабильность собственного капиатала")
        # labels_names.append("Итого")
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
        self.credit_line_chooses_evenly.setColumnCount(decades + 1)
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

        # self.credit_is_got_fully_at_the_beginning.setItem(0, decades + 1, QTableWidgetItem(str(round(sum(self.first_strategy_payment) / self.credit_money * 100, 2))))
        # self.credit_is_got_fully_at_the_beginning.setItem(1, decades + 1, QTableWidgetItem(str(round(sum(self.second_strategy_payment) / self.credit_money * 100, 2))))
        # self.credit_is_got_fully_at_the_beginning.setItem(2, decades + 1, QTableWidgetItem(str(round(sum(self.third_strategy_payment) / self.credit_money * 100, 2))))
        # self.credit_is_got_fully_at_the_beginning.setItem(3, decades + 1, QTableWidgetItem(str(round(sum(self.fourth_strategy_payment) / self.credit_money * 100, 2))))


        

        labels_names.append("Сумма платежей")
        # labels_names.append("Средневзвешенная процентная ставка")
        # labels_names.append("Эффект финансового рычага")
        # labels_names.append("Рентабильность собственного капиатала")
        # labels_names.append("Итого")
        self.credit_line_chooses_evenly.setHorizontalHeaderLabels(labels_names)

app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())


