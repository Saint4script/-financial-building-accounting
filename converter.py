import sys
import os
import math
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QTableWidgetItem, QDesktopWidget, QWidget
from PyQt5.QtCore import QDate

from zikkurat import Ui_MainWindow 
from Tables import Ui_NewWindow

#main window
class mywindow(QtWidgets.QMainWindow):
    k = S = n = s = p1 = z = c = build_time = own_money = Project_cost = 0 
    date_start = QDate.currentDate()
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Start datas window')
        self.setWindowIcon(QtGui.QIcon('images/icon.png'))
        self.ui.Build.clicked.connect(self.BuildFunc)
        self.ui.calendarWidget.hide()
        self.ui.Total_area.editingFinished.connect(lambda field = self.ui.Total_area: self.CheckerForFields(field))
        self.ui.Apartments_amount.editingFinished.connect(lambda field = self.ui.Apartments_amount: self.CheckerForFields(field))
        self.ui.Average_area_of_apartments.editingFinished.connect(lambda field = self.ui.Average_area_of_apartments: self.CheckerForFields(field))
        self.ui.Start_cost.editingFinished.connect(lambda field = self.ui.Start_cost: self.CheckerForFields(field))
        self.ui.Increasing_percentage.editingFinished.connect(lambda field = self.ui.Increasing_percentage: self.CheckerForFields(field))
        self.ui.Bulding_duration.editingFinished.connect(lambda field = self.ui.Bulding_duration: self.CheckerForFields(field))
        self.ui.Start_money.editingFinished.connect(lambda field = self.ui.Start_money: self.CheckerForFields(field))
        self.ui.Self_cost.editingFinished.connect(lambda field = self.ui.Self_cost: self.CheckerForFields(field))
        self.ui.Project_cost.editingFinished.connect(lambda field = self.ui.Project_cost: self.CheckerForFields(field))
        self.ui.calendarWidget.clicked[QDate].connect(self.show_date)
        
        

        self.mini_table_for_necessary_percents = QtWidgets.QTableWidget(self.ui.centralwidget)
        self.mini_table_for_necessary_percents.setObjectName("mini_table_for_necessary_percents")  
        self.mini_table_for_necessary_percents.hide() 
        #Комментировать вместе с автозаполнением
        self.mini_table_for_necessary_percents.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.mini_table_for_necessary_percents.resizeColumnsToContents()
        self.mini_table_for_necessary_percents.resizeRowsToContents()
        self.mini_table_for_necessary_percents.setRowCount(1)
        self.mini_table_for_necessary_percents.setColumnCount(10)
        self.mini_table_for_necessary_percents.setVerticalHeaderLabels(["Потребность в деньгах от стоимости проекта(%)"])
        #
        self.mini_table_for_necessary_percents.move(40, 420)

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
        self.mini_table_for_necessary_percents.setItem(0,9,QTableWidgetItem("5,75262499669948")) 

        self.ui.Apartments_amount.setText("368")#368
        self.ui.Average_area_of_apartments.setText("66")#66
        self.ui.Bulding_duration.setText("30")#30
        self.ui.Increasing_percentage.setText("2")#2
        self.ui.Start_money.setText("252109440")#189082080
        self.ui.Total_area.setText("24000")#24000
        self.ui.Start_cost.setText("54000")#54000
        self.ui.Self_cost.setText("51900")#51900

        #картинки на кнопки + code
        #self.TableWidget.setStyleSheet("QTableCornerButton::section{border-image:url(Corner.png)}")

        #path = os.path.dirname(os.path.abspath(__file__))
        #path1 = os.path.join(path, 'arrow.png')

        self.ui.show_calendar.clicked.connect(self.show_hide_calendar)
        self.ui.show_percents_table.clicked.connect(self.show_mini_percents_table)

        self.ui.show_calendar.setStyleSheet("border-image: url(images/calendar.png)0 0 0 0 stretch stretch")
        self.ui.show_percents_table.setStyleSheet("border-image: url(images/arrow.png)0 0 0 0 stretch stretch")



    #Заполнение таблицы процентов по выплатам
    def fill_mini_table_for_necessary_percents(self):
        percents_sum = 0
        for i in range(self.mini_table_for_necessary_percents.columnCount()):
            if(self.mini_table_for_necessary_percents.item(0, i) == None or 
                    self.mini_table_for_necessary_percents.item(0, i).text().replace(' ', '') == ''):
                message = 'Вы не заполнили все ячейки'
                QtWidgets.QMessageBox.warning(self, 'Уведомление', message, QtWidgets.QMessageBox.Ok)
                return False
            else:
                try:
                    percent = float(self.mini_table_for_necessary_percents.item(0, i).text().replace(',', '.'))
                    percents_sum += percent
                except(ValueError):
                    text = self.mini_table_for_necessary_percents.item(0, i).text()
                    message = f'Вы ввели некорректный символ: {text}'
                    QtWidgets.QMessageBox.warning(self, 'Уведомление', message,
                                                        QtWidgets.QMessageBox.Ok)
                    return False
        percents_sum = round(percents_sum, 4)
        if(percents_sum != float(100)):
            message = f'Сумма процентов не равна 100 ({percents_sum})'
            QtWidgets.QMessageBox.warning(self, 'Уведомление', message,
                                                        QtWidgets.QMessageBox.Ok)
            return False
        else:
            return True
    
    def show_date(self, date):
        self.date_start = date

    #Для дочернего класса
    def get_dimensions(self):
        l = (self.k,self.S,self.n,self.s,self.p1,self.z,self.build_time,self.own_money,self.c, self.date_start, self.Project_cost)
        return l

    #Переход к итоговым таблицам
    def BuildFunc(self):

        if(self.isnt_field_empty()):
            if(int(self.ui.Bulding_duration.text()) < 7):
                message = 'Срок строительства слишком мал'
                QtWidgets.QMessageBox.warning(self, 'Уведомление', message, QtWidgets.QMessageBox.Ok)
                return 
            #Автозаполнение стоимости проекта
            if(self.ui.Project_cost.text() == ""):
                tmp = int(self.ui.Self_cost.text())*int(self.ui.Apartments_amount.text()) * int(self.ui.Average_area_of_apartments.text())
                self.ui.Project_cost.setText(str(tmp))
            try:
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
            except(ValueError):
                message = 'Введите корректное значение!'
                QtWidgets.QMessageBox.warning(self, 'Уведомление', message, QtWidgets.QMessageBox.Ok)
                return 
            self.show_mini_percents_table()
            #Если собственных денег меньше, чем 1\10 себестоимости
            if(start_money < total_area * self_cost * 0.1):     
                message = 'Недостаточно собственных средств, строительство невозможно'
                QtWidgets.QMessageBox.warning(self, 'Уведомление', message, QtWidgets.QMessageBox.Ok)
                return
            elif(self.fill_mini_table_for_necessary_percents()):
                self.k = total_area * self_cost - start_money
                self.application = newwindow()
                self.application.show()
                self.hide()

    #Заполнение горизонтальных заголовков
    def fill_horizontal_headers(self, table):
        bt = int(self.ui.Bulding_duration.text())
        decades = math.ceil(bt / 3)
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

    #Проверка на пустые поля
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
            message = 'Заполните все поля!'
            QtWidgets.QMessageBox.warning(self, 'Уведомление', message, QtWidgets.QMessageBox.Ok)
            return  
        return checker

    #Проверка заполнения полей, чтобы не вводили что-то кроме чисел                  
    def CheckerForFields(self, field): 
        if(field.text() != ""): #Если не писать это условие, прога вообще не запускается _-_
            try:
                int(field.text())
            except ValueError:
                message = 'Некорректный ввод числовых значений.'
                QtWidgets.QMessageBox.warning(self, 'Уведомление', message, QtWidgets.QMessageBox.Ok)
                return 
    
    def show_hide_calendar(self):
        if(self.ui.calendarWidget.isHidden()):
            self.ui.calendarWidget.show()
        else:
            self.ui.calendarWidget.hide()
    
    #Показать таблицу с процентами
    def show_mini_percents_table(self):
        if(self.isnt_field_empty()):
            if(int(self.ui.Bulding_duration.text()) < 7):
                message = 'Срок строительства слишком мал'
                QtWidgets.QMessageBox.warning(self, 'Уведомление', message, QtWidgets.QMessageBox.Ok)
                return

            self.mini_table_for_necessary_percents.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
            self.mini_table_for_necessary_percents.horizontalHeader().setMinimumSectionSize(100)
            self.mini_table_for_necessary_percents.verticalHeader().setMinimumSectionSize(32)
            self.mini_table_for_necessary_percents.resizeColumnsToContents()
            self.mini_table_for_necessary_percents.resizeRowsToContents()
            self.mini_table_for_necessary_percents.setRowCount(1)
            self.mini_table_for_necessary_percents.setColumnCount(math.ceil(int(self.ui.Bulding_duration.text())/3))
            self.mini_table_for_necessary_percents.setVerticalHeaderLabels(["Потребность в деньгах от стоимости проекта(%)"])
            self.mini_table_for_necessary_percents.resize(1000, 80)
            self.fill_horizontal_headers(self.mini_table_for_necessary_percents)
            
            if(self.mini_table_for_necessary_percents.isHidden()):
                self.mini_table_for_necessary_percents.show()
                self.ui.label_11.setText("Скрыть/Обновить")
            else:
                self.mini_table_for_necessary_percents.hide()
                self.ui.label_11.setText("Ввод процентов потребности в денежных средствах по производственной необходимости")

#Это теперь дочерний класс класса mywindow
class newwindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(newwindow, self).__init__()
        self.ui = Ui_NewWindow()
        self.setWindowTitle('Result tables')
        self.setWindowIcon(QtGui.QIcon('images/icon.png'))
        #self.mainWindow = mywindow()
        self.k, self.S, self.n, self.s, self.p1,self.z, self.build_time, self.own_money, self.c, self.date_start, self.project_cost = application.get_dimensions()
        self.decades = math.ceil(self.build_time / 3)
        self.tmp_percent = round((1 - self.own_money / self.project_cost) * 100, 2) # для динамического отображения процентов в лейбле и листе
        self.credit_money = self.project_cost - self.own_money #заемные средства
        self.rentable_array = []

        self.ui.setupUi(self, self.tmp_percent)
        self.ui.create_tables(self.decades, self.tmp_percent)

        #Центрируем окно
        cp = QDesktopWidget().availableGeometry().center()
        self.move(int(round(cp.x() - self.width() / 2)), int(round(cp.y() - self.height() / 2 - 20)))
    
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
                    bruh = QtGui.QBrush(QtGui.QColor(0, 251, 255))
                    bruh.setStyle(QtCore.Qt.SolidPattern)
                    if(i % 2 == 0):
                        table.item(i, j).setBackground(bruh)
                        
            headerH = table.horizontalHeader()
            headerH.setStyleSheet(
            "QHeaderView::section{"
                "border-top:0px solid #D8D8D8;"
                "border-left:0px solid #D8D8D8;"
                "border-right:1px solid #D8D8D8;"
                "border-bottom: 1px solid black;"
                "background-color:white;"
                "padding:4px;"
            "}")
            headerV = table.verticalHeader()
            headerV.setStyleSheet(
            "QHeaderView::section{"
                "border-top:0px solid #D8D8D8;"
                "border-left:0px solid #D8D8D8;"
                "border-right:1px solid black;"
                "border-bottom: 0px solid black;"
                "background-color:white;"
                "padding:4px;"
            "}")
            table.setHorizontalHeader(headerH)
            table.setVerticalHeader(headerV)
            table.setStyleSheet("QTableCornerButton::section{"
                "border-top:0px solid #D8D8D8;"
                "border-left:0px solid #D8D8D8;"
                "border-right:1px solid black;"
                "border-bottom: 1px solid black;"
                "background-color:white;"
                "padding:4px;"
            "}")

        #Выравнивание контента в ячейках таблиц по центру
        def align_items(table):
                for i in range(table.rowCount()):
                    for j in range(table.columnCount()):
                        if(table.item(i, j) != None): # Если не сделать проверку на None(NULL), то когда он пытается обратиться к пустой ячейке, он падает, 
                                                    #т.к она NoneType -_-
                            table.item(i, j).setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                        else:
                            table.setItem(i, j, QTableWidgetItem(""))  #Поэтому надо положить в нее хотя бы пустую строку
                            table.item(i, j).setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)

        #Разбиение длинных чисел по разрядам
        def decorate_numbers(table):
            for i in range(table.rowCount()):
                for j in range(table.columnCount()):
                    x = float(table.item(i, j).text())
                    table.item(i,j).setText('{0:,}'.format(x).replace(',', ' '))
                    

        # Выделение лучшего элемента в таблице 
        def find_best(table):
            maxim = float(table.item(0, 0).text().replace(" ", ""))
            for i in range(table.rowCount()):
                for j in range(table.columnCount()):
                    if (maxim < float(table.item(i, j).text().replace(" ", ""))):
                        maxim = float(table.item(i, j).text().replace(" ", ""))
            for i in range(table.rowCount()):
                for j in range(table.columnCount()):
                    if(float(table.item(i, j).text().replace(" ", "")) == maxim):
                        font = QtGui.QFont()
                        font.setBold(True)
                        font.setWeight(75)
                        table.item(i, j).setFont(font)
                    bruh = QtGui.QBrush(QtGui.QColor(233, 145, 255))
                    bruh.setStyle(QtCore.Qt.SolidPattern)
                    if(i % 2 == 0):
                        table.item(i, j).setBackground(bruh) 


        #Увелечение цены каждый квартал на какое-то кол-во процентов
        self.fill_table()
        self.fill_horizontal_headers(self.ui.TableWidget)
        
        
        #план продаж
        self.fill_Table_with_flat_sell_plan()
        self.fill_horizontal_headers(self.ui.Table_with_flat_sell_plan)

        #Эскроу счета
        self.fill_escrow_rate()
        self.fill_horizontal_headers(self.ui.escrow_rate)
        
        #Кредит получен целиком в начале
        self.fill_credit_is_got_fully_at_the_beginning()

        #Кредит получен равномерно
        self.fill_credit_line_chooses_evenly()

        #Кредидб получается исходя из текущих нужд
        self.fill_horizontal_headers(self.ui.main_table_necessary_percents)
        self.fill_main_table_necessary_percents()

        #14. Прибыль до налогообложения строительной организации при различных стратегиях
        #продаж с использованием заемных средств в объеме 85 % от стоимости проекта.
        #таблица №2 из статьи, задание 14
        self.fill_table_85_percent_debt_money()
        

        #15.	
        #Расчет эффект финансового рычага строительной организации при 
        #различных стратегиях продаж с использованием заемных средств
        self.fill_table_financial_leverage_with_debt()
        

        #16.
        #Рентабельность собственного капитала строительной организации
        #при различных стратегиях продаж с использованием заемных средств
        #в объеме 85 % от стоимости проекта, в процентах.
        self.fill_table_profitability_of_own_money()
        

        #17
        #Количество денежных средств, которые получит банк за предоставления кредита в размере 85%
        #от стоимости проекта за весь срок строительства
        self.fill_table_bank_money_all_time()
        

        #18
        #Расчет средневзвешенной процентной ставки по заемному капиталу строительной организации при кредитовании 
        self.fill_table_average_weighted_rate()
        
        
        #19.
        #Увеличение себестоимости 1м2 при различных видах кредитования и времени пополнения
        #счетов эскроу при кредитовании строительной организации
        self.fill_table_encrease_owncost_area()
        
        

        #20
        #Увеличение себестоимости 1м2 при различных видах кредитования и времени пополнения
        #счетов эскроу при кредитовании строительной организации, %
        self.fill_table_encrease_owncost_area_percentage()
        

        #21
        #Прикидка поступления денежных средств в бюджет за счет налоговых отчислений
        #от строительной организации и банка при кредитовании строительной организации 
        self.fill_table_budget_money_income()

        


        #Выравнивание и запрет на редактирование эл-в таблиц
        tables = self.ui.centralwidget.findChildren(QtWidgets.QTableWidget)
        for table in tables:
            read_only_tables(table)
            align_items(table)


        tables_for_users = [
            self.ui.table_85_percent_debt_money,
            self.ui.table_financial_leverage_with_debt,
            self.ui.table_profitability_of_own_money,
            self.ui.table_bank_money_all_time,
            self.ui.table_average_weighted_rate,
            self.ui.table_encrease_owncost_area,
            self.ui.table_encrease_owncost_area_percentage,
            self.ui.table_budget_money_income
        ]
        for table in tables_for_users:
            decorate_numbers(table)
            find_best(table)
            

        self.ui.pushButton.clicked.connect(self._exit)
        self.ui.show_tables.clicked.connect(self.choose_tables)
        self.ui.clear_tables.clicked.connect(self.clear_tables)
        

    #Это мы уже видели
    def fill_horizontal_headers(self, table):
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

    #Кредидб получается исходя из текущих нужд
    def fill_main_table_necessary_percents(self):
        current_own_money = self.project_cost - self.credit_money
        item = 0
        cell_info_sum = 0
        
        for i in range(application.mini_table_for_necessary_percents.columnCount()):
            TableItem = application.mini_table_for_necessary_percents.item(0, i).text().replace(',', '.') #это надо из-за того,
            # что дробные числа в питоне пишутся через точку, а ввести могут с запятыми 
            cell_info = self.project_cost * float(TableItem) / 100
           
            if(current_own_money - cell_info >= 0):
                item = 0
                current_own_money -= cell_info
            else:
                if(current_own_money > 0):
                   item = cell_info - current_own_money
                   current_own_money = 0
                else:
                    item = cell_info
            cell_info_sum += item

            self.ui.main_table_necessary_percents.setItem(0, i, QTableWidgetItem(str(cell_info)))
            self.ui.main_table_necessary_percents.setItem(1, i, QTableWidgetItem(str(item)))
            self.ui.main_table_necessary_percents.setItem(2, i, QTableWidgetItem(str(cell_info_sum)))

        for i in range(4):
            row_sum = 0
            for j in range(self.decades):
                tmp = float(self.ui.main_table_necessary_percents.item(2, j).text())          
                percent = float(self.ui.escrow_rate.item(i,j).text())
                row_sum += tmp * percent / 4
                self.ui.main_table_necessary_percents.setItem(i + 3, j, QTableWidgetItem(str(tmp *percent / 4 )))
            self.ui.main_table_necessary_percents.setItem(i + 3, self.decades, QTableWidgetItem(str(row_sum)))
            self.ui.main_table_necessary_percents.setItem(i + 3, self.decades + 1, QTableWidgetItem(str(round(row_sum / self.credit_money * 100 , 2))))
        
        for i in range(4):
            rent = self.rentable_array[i]
            rate = float(self.ui.main_table_necessary_percents.item(i + 3, self.decades + 1).text())
            effect = 0.8 * (rent - rate / 100) * self.credit_money / self.own_money
            self.ui.main_table_necessary_percents.setItem(i + 3, self.decades + 2, QTableWidgetItem(str(effect))) # Эффект финансового рычага
            self.ui.main_table_necessary_percents.setItem(i + 3, self.decades + 3, QTableWidgetItem(str(0.8 * rent + effect))) # Рентабильность собственного капитала
            
        for i in range(4):
            total_sum = 0
            for j in range(2,self.decades):
                total_sum += float(self.ui.main_table_necessary_percents.item(i + 3, j).text())
            
            total_sum += self.credit_money + self.own_money
            self.ui.main_table_necessary_percents.setItem(i + 3, self.decades + 4, QTableWidgetItem(str(round(total_sum, 2)))) #Итого
        
        

    #Спрятать таблицы
    def clear_tables(self):
        tables = self.ui.centralwidget.findChildren(QtWidgets.QTableWidget)
        for table in tables:
            table.hide()
        labels = self.ui.centralwidget.findChildren(QtWidgets.QLabel)
        for label in labels:
            label.hide()

        

    #Отображение ВЫБРАННЫХ таблиц
    def choose_tables(self):
        self.ui.labels_for_corner()
        current_height = 200
        tables = self.ui.centralwidget.findChildren(QtWidgets.QTableWidget)
        labels = self.ui.centralwidget.findChildren(QtWidgets.QLabel)
        for table in tables:
            table.hide()
        
        for label in labels:
            label.hide()
        
        
        selected_items = self.ui.listWidget.selectedItems()

        def check_height(height):
            if(height > self.height() - 10):
                message = 'Слишком много таблиц'
                QtWidgets.QMessageBox.warning(self, 'Уведомление', message,
                                                        QtWidgets.QMessageBox.Ok)
                
                return False
            return True

        for elem in selected_items:
            if(elem.text() == 'Цена 1м²'): #9 img
                if(check_height(current_height + self.ui.TableWidget.height() + 10 + self.ui.label_TableWidget.height() + 5)):
                    self.ui.label_TableWidget.show()
                    self.ui.label_TableWidget.move(10, current_height)
                    current_height += self.ui.label_85_percent_debt_money.height() + 5
                    self.ui.img9.move(11, current_height + 2)
                    self.ui.img9.show()
                    self.ui.TableWidget.show()
                    self.ui.TableWidget.move(10,current_height)
                    current_height += self.ui.TableWidget.height() + 10
                    self.ui.TableWidget.resize(1200, self.ui.TableWidget.height())
                else:
                    break
            elif(elem.text() == 'План продаж'): #10 img
                if(check_height(current_height + self.ui.Table_with_flat_sell_plan.height() + 10 + self.ui.label_with_flat_sell_plan.height() + 5)):
                    self.ui.label_with_flat_sell_plan.show()
                    self.ui.label_with_flat_sell_plan.move(10, current_height)
                    current_height += self.ui.label_85_percent_debt_money.height() + 5
                    self.ui.img10.move(11, current_height + 2)
                    self.ui.img10.show()
                    self.ui.Table_with_flat_sell_plan.show()
                    self.ui.Table_with_flat_sell_plan.move(10,current_height)
                    current_height += self.ui.Table_with_flat_sell_plan.height() + 10
                    self.ui.Table_with_flat_sell_plan.resize(1200, self.ui.Table_with_flat_sell_plan.height())
                else:
                    break
            elif(elem.text() == 'Определение процентной ставки на эскроу'):
                if(check_height(current_height + self.ui.escrow_rate.height() + 10 + self.ui.label_escrow_rate.height() + 5)):
                    self.ui.label_escrow_rate.show()
                    self.ui.label_escrow_rate.move(10, current_height)
                    current_height += self.ui.label_85_percent_debt_money.height() + 5 #12img
                    self.ui.img12.move(11, current_height + 2)
                    self.ui.img12.show()
                    self.ui.escrow_rate.show()
                    self.ui.escrow_rate.move(10,current_height)
                    current_height += self.ui.escrow_rate.height() + 10
                    self.ui.escrow_rate.resize(1200, self.ui.escrow_rate.height())
                else:
                    break
            elif(elem.text() == "Если кредит получен единовременно в начале, то платежи по процентам за пользование заемными средствами в конце периода"):
                if(check_height(current_height + self.ui.credit_is_got_fully_at_the_beginning.height() + 10 + self.ui.label_credit_is_got_fully_at_the_beginning.height() + 5)):
                    self.ui.label_credit_is_got_fully_at_the_beginning.show()
                    self.ui.label_credit_is_got_fully_at_the_beginning.move(10, current_height)
                    current_height += self.ui.label_85_percent_debt_money.height() + 5 #13 img
                    self.ui.img13.move(11, current_height + 2)
                    self.ui.img13.show()
                    self.ui.credit_is_got_fully_at_the_beginning.show()
                    self.ui.credit_is_got_fully_at_the_beginning.move(10, current_height)
                    current_height += self.ui.credit_is_got_fully_at_the_beginning.height() + 10
                    self.ui.credit_is_got_fully_at_the_beginning.resize(1200, self.ui.credit_is_got_fully_at_the_beginning.height())
                else:
                    break
            elif(elem.text() == "Если кредитная линия выбирается равномерно в течении срока строительства, то платежи по процентам за пользование заемными средствами в конце периода"):
                if(check_height(current_height + self.ui.credit_line_chooses_evenly.height() + 10 + self.ui.label_credit_line_chooses_evenly.height() + 5)):
                    self.ui.label_credit_line_chooses_evenly.show()
                    self.ui.label_credit_line_chooses_evenly.move(10, current_height)
                    current_height += self.ui.label_85_percent_debt_money.height() + 5
                    self.ui.img14.move(11, current_height + 2)                # 14 img
                    self.ui.img14.show()
                    self.ui.credit_line_chooses_evenly.show()
                    self.ui.credit_line_chooses_evenly.move(10, current_height)
                    current_height += self.ui.credit_line_chooses_evenly.height() + 10
                    self.ui.credit_line_chooses_evenly.resize(1200, self.ui.credit_line_chooses_evenly.height())
                else:
                    break
            elif(elem.text() == "Если кредитная линия выбирается по мере необходимости строительного процесса, то платежи по процентам за пользование заемными средствами в конце периода"):
                if(check_height(current_height + self.ui.main_table_necessary_percents.height() + 10 + self.ui.label_main_table_necessary_percents.height() + 5)):
                    self.ui.label_main_table_necessary_percents.show()
                    self.ui.label_main_table_necessary_percents.move(10, current_height)
                    current_height += self.ui.label_85_percent_debt_money.height() + 5
                    self.ui.img11.move(11, current_height + 2)
                    self.ui.img11.show()
                    self.ui.main_table_necessary_percents.show()
                    self.ui.main_table_necessary_percents.move(10, current_height)
                    self.ui.main_table_necessary_percents.resize(1200, self.ui.main_table_necessary_percents.height())
                    current_height += self.ui.main_table_necessary_percents.height() + 10
                else:
                    break
            elif(elem.text() == f'Прибыль с использованием заемных средств в объеме {self.tmp_percent} % от стоимости проекта'):#1
                if(check_height(current_height + self.ui.table_85_percent_debt_money.height() + 10 + self.ui.label_85_percent_debt_money.height() + 5)):
                    self.ui.label_85_percent_debt_money.show()
                    self.ui.label_85_percent_debt_money.move(10, current_height)
                    current_height += self.ui.label_85_percent_debt_money.height() + 5
                    self.ui.img1.move(11, current_height + 2)
                    self.ui.img1.show()
                    self.ui.table_85_percent_debt_money.show()
                    self.ui.table_85_percent_debt_money.move(10, current_height)
                    self.ui.table_85_percent_debt_money.resize(900, self.ui.table_85_percent_debt_money.height())
                    self.ui.table_85_percent_debt_money.adjustSize()
                    current_height += self.ui.table_85_percent_debt_money.height() + 10
                else:
                    break
            elif(elem.text() == "Финансовый рычаг при различных стратегиях продаж с использованием заемных средств"):#2
                if(check_height(current_height + self.ui.table_financial_leverage_with_debt.height() + 10 + self.ui.label_financial_leverage_with_debt.height() + 5)):
                    self.ui.label_financial_leverage_with_debt.show()
                    self.ui.label_financial_leverage_with_debt.move(10, current_height)
                    current_height += self.ui.label_financial_leverage_with_debt.height() + 5
                    self.ui.img2.move(11, current_height + 2)
                    self.ui.img2.show()
                    self.ui.table_financial_leverage_with_debt.show()
                    self.ui.table_financial_leverage_with_debt.move(10, current_height)
                    self.ui.table_financial_leverage_with_debt.resize(900, self.ui.table_financial_leverage_with_debt.height())
                    self.ui.table_financial_leverage_with_debt.adjustSize()
                    current_height += self.ui.table_financial_leverage_with_debt.height() + 10
                else:
                    break
            elif(elem.text() == "Рентабельность собственного капитала при различных стратегиях продаж с использованием заемных средств"):#3
                if(check_height(current_height + self.ui.table_profitability_of_own_money.height() + 10 + self.ui.label_profitability_of_own_money.height() + 5)):
                    self.ui.label_profitability_of_own_money.show()
                    self.ui.label_profitability_of_own_money.move(10, current_height)
                    current_height += self.ui.label_profitability_of_own_money.height() + 5
                    self.ui.img3.move(11, current_height + 2)
                    self.ui.img3.show()
                    self.ui.table_profitability_of_own_money.show()
                    self.ui.table_profitability_of_own_money.move(10, current_height)
                    self.ui.table_profitability_of_own_money.resize(900, self.ui.table_profitability_of_own_money.height())
                    self.ui.table_profitability_of_own_money.adjustSize()
                    current_height += self.ui.table_profitability_of_own_money.height() + 10
                else:
                    break
            elif(elem.text() == "Процентные выплаты, получаемые банком за предоставление кредита"):#4
                if(check_height(current_height + self.ui.table_bank_money_all_time.height() + 10 + self.ui.label_bank_money_all_time.height() + 5)):
                    self.ui.label_bank_money_all_time.show()
                    self.ui.label_bank_money_all_time.move(10, current_height)
                    current_height += self.ui.label_bank_money_all_time.height() + 5
                    self.ui.img4.move(11, current_height + 2)
                    self.ui.img4.show()
                    self.ui.table_bank_money_all_time.show()
                    self.ui.table_bank_money_all_time.move(10, current_height)
                    self.ui.table_bank_money_all_time.resize(900, self.ui.table_bank_money_all_time.height())
                    self.ui.table_bank_money_all_time.adjustSize()
                    current_height += self.ui.table_bank_money_all_time.height() + 10
                else:
                    break
            elif(elem.text() == "Средневзвешенная процентная ставка по заемному капиталу строительной организации"):#5
                if(check_height(current_height + self.ui.table_average_weighted_rate.height() + 10 + self.ui.label_average_weighted_rate.height() + 5)):
                    self.ui.label_average_weighted_rate.show()
                    self.ui.label_average_weighted_rate.move(10, current_height)
                    current_height += self.ui.label_average_weighted_rate.height() + 5
                    self.ui.img5.move(11, current_height + 2)
                    self.ui.img5.show()
                    self.ui.table_average_weighted_rate.show()
                    self.ui.table_average_weighted_rate.move(10, current_height)
                    self.ui.table_average_weighted_rate.resize(900, self.ui.table_average_weighted_rate.height())
                    self.ui.table_average_weighted_rate.adjustSize()
                    current_height += self.ui.table_average_weighted_rate.height() + 10
                else:
                    break
            elif(elem.text() == "Увеличение себестоимости 1м²  при кредитовании строительной организации"):#6
                if(check_height(current_height + self.ui.table_encrease_owncost_area.height() + 10 + self.ui.label_encrease_owncost_area.height() + 5)):
                    self.ui.label_encrease_owncost_area.show()
                    self.ui.label_encrease_owncost_area.move(10, current_height)
                    current_height += self.ui.label_encrease_owncost_area.height() + 5
                    self.ui.img6.move(11, current_height + 2)
                    self.ui.img6.show()
                    self.ui.table_encrease_owncost_area.show()
                    self.ui.table_encrease_owncost_area.move(10, current_height)
                    self.ui.table_encrease_owncost_area.resize(900, self.ui.table_encrease_owncost_area.height())
                    self.ui.table_encrease_owncost_area.adjustSize()
                    current_height += self.ui.table_encrease_owncost_area.height() + 10
                else:
                    break
            elif(elem.text() == "Увеличение себестоимости 1м²  при кредитовании строительной организации в %"):#7
                if(check_height(current_height + self.ui.table_encrease_owncost_area_percentage.height() + 10 + self.ui.label_encrease_owncost_area_percentage.height() + 5)):
                    self.ui.label_encrease_owncost_area_percentage.show()
                    self.ui.label_encrease_owncost_area_percentage.move(10, current_height)
                    current_height += self.ui.label_encrease_owncost_area_percentage.height() + 5
                    self.ui.img7.move(11, current_height + 2)
                    self.ui.img7.show()
                    self.ui.table_encrease_owncost_area_percentage.show()
                    self.ui.table_encrease_owncost_area_percentage.move(10, current_height)
                    self.ui.table_encrease_owncost_area_percentage.resize(900, self.ui.table_encrease_owncost_area_percentage.height())
                    self.ui.table_encrease_owncost_area_percentage.adjustSize()
                    current_height += self.ui.table_encrease_owncost_area_percentage.height() + 10
                else:
                    break
            elif(elem.text() == "Прикидка поступления денежных средств в бюджет за счет налоговых отчислений от строительной организации и банка"): #8
                if(check_height(current_height + self.ui.table_budget_money_income.height() + 10 + self.ui.label_budget_money_income.height() + 5)):
                    self.ui.label_budget_money_income.show()
                    self.ui.label_budget_money_income.move(10, current_height)
                    current_height += self.ui.label_budget_money_income.height() + 5
                    self.ui.img8.move(11, current_height + 2)
                    self.ui.img8.show()
                    self.ui.table_budget_money_income.show()
                    btn = self.ui.table_budget_money_income.findChildren(QtWidgets.QAbstractButton)
                    self.ui.table_budget_money_income.move(10, current_height)
                    self.ui.table_budget_money_income.resize(900, self.ui.table_budget_money_income.height())
                    self.ui.table_budget_money_income.adjustSize()
                    current_height += self.ui.table_budget_money_income.height() + 10
                else:
                    break

    #Выход      
    def _exit(self):
        application.show()
        self.close()

    #Увелечение цены каждый квартал на какое-то кол-во процентов    
    def fill_table(self):  
        decades = math.ceil(self.build_time/3)
        # self.TableWidget.setRowCount(2)
        # self.TableWidget.setColumnCount(decades + 1)
        price  = self.p1
        avg_sum1 = avg_sum2 = avg_sum3 = total_avg = 0
        self.pointer = [math.floor(decades/3),decades - math.floor(decades/3)*2]
        
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
            self.ui.TableWidget.setItem(0 , i, cell_info)
            price = price * (1 + self.z/100)
        
        avg_sum1 = avg_sum1 / self.pointer[0]
        avg_sum2 = avg_sum2 / self.pointer[1]
        avg_sum3 = avg_sum3 / self.pointer[0]
        self.ui.TableWidget.setItem(1 , 0, QTableWidgetItem(str(round(avg_sum1,2))))
        self.ui.TableWidget.setItem(1 , self.pointer[0], QTableWidgetItem(str(round(avg_sum2,2))))
        self.ui.TableWidget.setItem(1 , self.pointer[0] + self.pointer[1], QTableWidgetItem(str(round(avg_sum3,2))))

        total_avg = total_avg / decades   
        self.Array_of_avg_flat_prices = [avg_sum1, avg_sum2 , avg_sum3, total_avg]   #Да, я переопределил тут массив, но мне пофиг, там хотя бы видно, зачем он создан
          
        self.ui.TableWidget.setItem(1, decades, QTableWidgetItem(str(round(total_avg,2))))    

        
        self.ui.TableWidget.setVerticalHeaderLabels([F"цена 1 кв.м. - каждый квартал увеличивается на {self.z}%", "средняя цена 1 кв.м"])

    # план продаж в количестве квартир
    def fill_Table_with_flat_sell_plan(self): 
        self.iterator = 0
        decades = math.ceil(self.build_time/3)

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
                    self.ui.Table_with_flat_sell_plan.setItem(row, i + self.pointer[0], QTableWidgetItem(str(flat)))
                    self.ui.Table_with_flat_sell_plan.setItem(row+5, i + self.pointer[0], QTableWidgetItem(str(round(tmp,1))))
                    self.ui.Table_with_flat_sell_plan.setItem(row+10, i + self.pointer[0], QTableWidgetItem(str(round(sum1,1))))
                elif(row == 2):
                    self.ui.Table_with_flat_sell_plan.setItem(row, i + self.pointer[0] + self.pointer[1], QTableWidgetItem(str(flat)))
                    self.ui.Table_with_flat_sell_plan.setItem(row+5, i + self.pointer[0] + self.pointer[1], QTableWidgetItem(str(round(tmp,1))))
                    self.ui.Table_with_flat_sell_plan.setItem(row+10, i + self.pointer[0] + self.pointer[1], QTableWidgetItem(str(round(sum1,1))))
                else:
                    self.ui.Table_with_flat_sell_plan.setItem(row, i, QTableWidgetItem(str(flat)))
                    self.ui.Table_with_flat_sell_plan.setItem(row+5, i, QTableWidgetItem(str((round(tmp,1)))))
                    self.ui.Table_with_flat_sell_plan.setItem(row+10, i, QTableWidgetItem(str(round(sum1,1))))
        
        
        fill_cells(0, self.pointer[0])
        fill_cells(1, self.pointer[1])
        fill_cells(2, self.pointer[0])
        self.iterator = 0
        fill_cells(3, decades)
        #Заполняем сумму по квартирам в каждой стратегии 
        self.ui.Table_with_flat_sell_plan.setItem(0, decades, QTableWidgetItem(str(sum(self.flats_amount_first_three_strategies[: self.pointer[0]]))))
        self.ui.Table_with_flat_sell_plan.setItem(1, decades, QTableWidgetItem(str(sum(self.flats_amount_first_three_strategies[self.pointer[0]: decades - self.pointer[0]]))))
        self.ui.Table_with_flat_sell_plan.setItem(2, decades, QTableWidgetItem(str(sum(self.flats_amount_first_three_strategies[-self.pointer[0] : ]))))
        self.ui.Table_with_flat_sell_plan.setItem(3, decades, QTableWidgetItem(str(sum(self.flats_amount_fourth_strategy))))
        #Заполняем сумму по плану продаж 
        self.sell_plan_sum_of_each_str[0] = sum(self.sell_plan_in_rub_first_three_strategies[: self.pointer[0]])
        self.ui.Table_with_flat_sell_plan.setItem(5, decades, QTableWidgetItem(str(round( self.sell_plan_sum_of_each_str[0], 2))))

        self.sell_plan_sum_of_each_str[1] = sum(self.sell_plan_in_rub_first_three_strategies[self.pointer[0]: decades - self.pointer[0]])
        self.ui.Table_with_flat_sell_plan.setItem(6, decades, QTableWidgetItem(str(round(self.sell_plan_sum_of_each_str[1], 2))))

        self.sell_plan_sum_of_each_str[2] = sum(self.sell_plan_in_rub_first_three_strategies[-self.pointer[0] : ])
        self.ui.Table_with_flat_sell_plan.setItem(7, decades, QTableWidgetItem(str(round(self.sell_plan_sum_of_each_str[2], 2))))

        self.sell_plan_sum_of_each_str[3] = sum(self.sell_plan_in_rub_fourth_strategy)
        self.ui.Table_with_flat_sell_plan.setItem(8, decades, QTableWidgetItem(str(round(self.sell_plan_sum_of_each_str[3], 2))))

        #Заполним рентабилность активов 
        for i in range(4):
            value = (self.sell_plan_sum_of_each_str[i] - self.S * self.c) / (self.own_money + self.credit_money)
            self.rentable_array.append(value)
            #self.ui.Table_with_flat_sell_plan.setItem(i + 5, decades + 1, QTableWidgetItem(str(value)))

    #Эскроу счета
    def fill_escrow_rate(self):
        decades = math.ceil(self.build_time / 3)
        #ЗАПОЛНЯЕМ ПЕРВУЮ СТРОЧКУ
        for i in range(decades):
            if(self.escrow_amount_of_money_first_three_strategies[i] < self.credit_money / 2 and i < self.pointer[0]):
                cell_info = QTableWidgetItem("0.12")
                self.ui.escrow_rate.setItem(0, i, cell_info)

            elif(self.escrow_amount_of_money_first_three_strategies[i] < self.credit_money * 0.75 and i < self.pointer[0]):
                cell_info = QTableWidgetItem("0.09")
                self.ui.escrow_rate.setItem(0, i, cell_info)

            elif(self.escrow_amount_of_money_first_three_strategies[i] < self.credit_money  and i < self.pointer[0]):
                cell_info = QTableWidgetItem("0.06")
                self.ui.escrow_rate.setItem(0, i, cell_info)

            #elif(self.escrow_amount_of_money_first_three_strategies[i] < self.credit_money * 1.5 or i >= self.pointer[0]):
            else:
                cell_info = QTableWidgetItem("0.03")
                self.ui.escrow_rate.setItem(0, i, cell_info)     
        #ЗАПОЛНЯЕМ ВТОРУЮ СТРОЧКУ
        for i in range(self.pointer[0]):
            cell_info = QTableWidgetItem("0.12")
            self.ui.escrow_rate.setItem(1, i, cell_info)

        for i in range(self.pointer[0], decades - self.pointer[0]):
            if(self.escrow_amount_of_money_first_three_strategies[i] < self.credit_money / 2 ):
                cell_info = QTableWidgetItem("0.12")
                self.ui.escrow_rate.setItem(1, i, cell_info) 
            elif(self.escrow_amount_of_money_first_three_strategies[i] < self.credit_money * 0.75):
                cell_info = QTableWidgetItem("0.09")
                self.ui.escrow_rate.setItem(1, i, cell_info)
            elif(self.escrow_amount_of_money_first_three_strategies[i] < self.credit_money):
                cell_info = QTableWidgetItem("0.06")
                self.ui.escrow_rate.setItem(1, i, cell_info)
            #elif(self.escrow_amount_of_money_first_three_strategies[i] < self.credit_money * 1.5):
            else:
                cell_info = QTableWidgetItem("0.03")
                self.ui.escrow_rate.setItem(1, i, cell_info)  
        
        for i in range(decades - self.pointer[0], decades):
            cell_info = QTableWidgetItem("0.03")
            self.ui.escrow_rate.setItem(1, i, cell_info)

        #ЗАПОЛНЯЕМ ТРЕТЬЮ СТРОЧКУ

        for i in range(decades - self.pointer[0]):
            cell_info = QTableWidgetItem("0.12")
            self.ui.escrow_rate.setItem(2, i, cell_info)
        
        for i in range(decades - self.pointer[0], decades):
            if(self.escrow_amount_of_money_first_three_strategies[i] < self.credit_money / 2 ):
                cell_info = QTableWidgetItem("0.12")
                self.ui.escrow_rate.setItem(2, i, cell_info) 
            elif(self.escrow_amount_of_money_first_three_strategies[i] < self.credit_money * 0.75):
                cell_info = QTableWidgetItem("0.09")
                self.ui.escrow_rate.setItem(2, i, cell_info)
            elif(self.escrow_amount_of_money_first_three_strategies[i] < self.credit_money):
                cell_info = QTableWidgetItem("0.06")
                self.ui.escrow_rate.setItem(2, i, cell_info)
            #elif(self.escrow_amount_of_money_first_three_strategies[i] < self.credit_money * 1.5):
            else:
                cell_info = QTableWidgetItem("0.03")
                self.ui.escrow_rate.setItem(2, i, cell_info) 
             
        #ЗАПОЛНЯЕМ ЧЕТВЕРТУЮ СТРОЧКУ
        for i in range(decades):
            if(self.escrow_amount_of_money_fourth_strategy[i] < self.credit_money / 2 ):
                cell_info = QTableWidgetItem("0.12")
                self.ui.escrow_rate.setItem(3, i, cell_info) 
            elif(self.escrow_amount_of_money_fourth_strategy[i] < self.credit_money * 0.75):
                cell_info = QTableWidgetItem("0.09")
                self.ui.escrow_rate.setItem(3, i, cell_info)
            elif(self.escrow_amount_of_money_fourth_strategy[i] < self.credit_money):
                cell_info = QTableWidgetItem("0.06")
                self.ui.escrow_rate.setItem(3, i, cell_info)
            #elif(self.escrow_amount_of_money_fourth_strategy[i] < self.credit_money * 1.5):
            else:
                cell_info = QTableWidgetItem("0.03")
                self.ui.escrow_rate.setItem(3, i, cell_info)     

    #Кредит получен в начале
    def fill_credit_is_got_fully_at_the_beginning(self):
        #Объявим несколько массивов
        self.first_strategy_payment = []
        self.second_strategy_payment = []
        self.third_strategy_payment = []
        self.fourth_strategy_payment = []

        decades = math.ceil(self.build_time / 3)
        new_date = self.date_start.month()
        

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
                
                cell_info = self.credit_money  / 4 * float(self.ui.escrow_rate.item(i, j).text())
                self.ui.credit_is_got_fully_at_the_beginning.setItem(i, j, QTableWidgetItem(str(round(cell_info, 2))))
                if(i == 0):
                    self.first_strategy_payment.append(cell_info)
                elif(i == 1):
                    self.second_strategy_payment.append(cell_info)
                elif(i == 2):
                    self.third_strategy_payment.append(cell_info)
                elif(i == 3):
                    self.fourth_strategy_payment.append(cell_info)
        
        self.ui.credit_is_got_fully_at_the_beginning.setItem(0, decades, QTableWidgetItem(str(round(sum(self.first_strategy_payment), 2))))
        self.ui.credit_is_got_fully_at_the_beginning.setItem(1, decades, QTableWidgetItem(str(round(sum(self.second_strategy_payment), 2))))
        self.ui.credit_is_got_fully_at_the_beginning.setItem(2, decades, QTableWidgetItem(str(round(sum(self.third_strategy_payment), 2))))
        self.ui.credit_is_got_fully_at_the_beginning.setItem(3, decades, QTableWidgetItem(str(round(sum(self.fourth_strategy_payment), 2))))

        self.ui.credit_is_got_fully_at_the_beginning.setItem(0, decades + 1, QTableWidgetItem(str(round(sum(self.first_strategy_payment) / self.credit_money * 100, 2))))
        self.ui.credit_is_got_fully_at_the_beginning.setItem(1, decades + 1, QTableWidgetItem(str(round(sum(self.second_strategy_payment) / self.credit_money * 100, 2))))
        self.ui.credit_is_got_fully_at_the_beginning.setItem(2, decades + 1, QTableWidgetItem(str(round(sum(self.third_strategy_payment) / self.credit_money * 100, 2))))
        self.ui.credit_is_got_fully_at_the_beginning.setItem(3, decades + 1, QTableWidgetItem(str(round(sum(self.fourth_strategy_payment) / self.credit_money * 100, 2))))


        for i in range(4):
            rent = self.rentable_array[i]
            rate = float(self.ui.credit_is_got_fully_at_the_beginning.item(i, decades + 1).text())
            effect = 0.8 * (rent - rate / 100) * self.credit_money / self.own_money
            self.ui.credit_is_got_fully_at_the_beginning.setItem(i, decades + 2, QTableWidgetItem(str(effect))) # Эффект финансового рычага
            self.ui.credit_is_got_fully_at_the_beginning.setItem(i, decades + 3, QTableWidgetItem(str(0.8 * rent + effect))) # Рентабильность собственного капитала
            
        for i in range(4):
            total_sum = 0
            #говно-цикл, презираю, осуждаю
            for j in range(decades):
                total_sum += float(self.ui.credit_is_got_fully_at_the_beginning.item(i, j).text())
            total_sum += self.credit_money + self.own_money
            self.ui.credit_is_got_fully_at_the_beginning.setItem(i, decades + 4, QTableWidgetItem(str(round(total_sum, 2)))) #Итого

        labels_names.append("Сумма платежей")
        labels_names.append("средневзвешенная процентная ставка")
        labels_names.append("Эффект финансового рычага")
        labels_names.append("Рентабильность собственного капитала")
        labels_names.append("Итого")
        self.ui.credit_is_got_fully_at_the_beginning.setHorizontalHeaderLabels(labels_names)

    #Кредит получен равномерно
    def fill_credit_line_chooses_evenly(self):
        #Объявим несколько массивов
        self.first_strategy_credit_line = []
        self.second_strategy_credit_line = []
        self.third_strategy_credit_line = []
        self.fourth_strategy_credit_line = []

        decades = math.ceil(self.build_time / 3)
        new_date = self.date_start.month()
        

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
                
                cell_info = self.credit_money  / (2.5 * 4) * float(self.ui.escrow_rate.item(i, j).text()) 
                self.ui.credit_line_chooses_evenly.setItem(i, j, QTableWidgetItem(str(round(cell_info, 2))))
                if(i == 0):
                    self.first_strategy_credit_line.append(cell_info)
                elif(i == 1):
                    self.second_strategy_credit_line.append(cell_info)
                elif(i == 2):
                    self.third_strategy_credit_line.append(cell_info)
                elif(i == 3):
                    self.fourth_strategy_credit_line.append(cell_info)
        
        self.ui.credit_line_chooses_evenly.setItem(0, decades, QTableWidgetItem(str(round(sum(self.first_strategy_credit_line), 2))))
        self.ui.credit_line_chooses_evenly.setItem(1, decades, QTableWidgetItem(str(round(sum(self.second_strategy_credit_line), 2))))
        self.ui.credit_line_chooses_evenly.setItem(2, decades, QTableWidgetItem(str(round(sum(self.third_strategy_credit_line), 2))))
        self.ui.credit_line_chooses_evenly.setItem(3, decades, QTableWidgetItem(str(round(sum(self.fourth_strategy_credit_line), 2))))

        self.ui.credit_line_chooses_evenly.setItem(0, decades + 1, QTableWidgetItem(str(round(sum(self.first_strategy_credit_line) / self.credit_money * 100, 2))))
        self.ui.credit_line_chooses_evenly.setItem(1, decades + 1, QTableWidgetItem(str(round(sum(self.second_strategy_credit_line) / self.credit_money * 100, 2))))
        self.ui.credit_line_chooses_evenly.setItem(2, decades + 1, QTableWidgetItem(str(round(sum(self.third_strategy_credit_line) / self.credit_money * 100, 2))))
        self.ui.credit_line_chooses_evenly.setItem(3, decades + 1, QTableWidgetItem(str(round(sum(self.fourth_strategy_credit_line) / self.credit_money * 100, 2))))

        for i in range(4):
            rent = self.rentable_array[i]
            rate = float(self.ui.credit_line_chooses_evenly.item(i, decades + 1).text())
            effect = 0.8 * (rent - rate / 100) * self.credit_money / self.own_money
            self.ui.credit_line_chooses_evenly.setItem(i, decades + 2, QTableWidgetItem(str(effect))) # Эффект финансового рычага
            self.ui.credit_line_chooses_evenly.setItem(i, decades + 3, QTableWidgetItem(str(0.8 * rent + effect))) # Рентабильность собственного капитала
            
        for i in range(4):
            total_sum = 0
            for j in range(decades):
                total_sum += float(self.ui.credit_line_chooses_evenly.item(i, j).text())
            total_sum += self.credit_money + self.own_money
            self.ui.credit_line_chooses_evenly.setItem(i, decades + 4, QTableWidgetItem(str(round(total_sum, 2)))) #Итого




        self.ui.credit_line_chooses_evenly.setColumnWidth(decades + 1, 230)
        self.ui.credit_line_chooses_evenly.setColumnWidth(decades + 2, 180)
        self.ui.credit_line_chooses_evenly.setColumnWidth(decades + 3, 240)

        labels_names.append("Сумма платежей")
        labels_names.append("Средневзвешенная процентная ставка")
        labels_names.append("Эффект финансового рычага")
        labels_names.append("Рентабильность собственного капиатала")
        labels_names.append("Итого")
        self.ui.credit_line_chooses_evenly.setHorizontalHeaderLabels(labels_names)


    def fill_general_table_bank_position(self):
        self.general_table_bank_position.setItem(0, 0, QTableWidgetItem(str(round(sum(self.first_strategy_payment),2))))
        self.general_table_bank_position.setItem(0, 1, QTableWidgetItem(str(round(sum(self.second_strategy_payment),2))))
        self.general_table_bank_position.setItem(0, 2, QTableWidgetItem(str(round(sum(self.third_strategy_payment),2))))
        self.general_table_bank_position.setItem(0, 3, QTableWidgetItem(str(round(sum(self.fourth_strategy_payment),2))))

        self.general_table_bank_position.setItem(1, 0, QTableWidgetItem(str(round(sum(self.first_strategy_credit_line),2))))
        self.general_table_bank_position.setItem(1, 1, QTableWidgetItem(str(round(sum(self.second_strategy_credit_line),2))))
        self.general_table_bank_position.setItem(1, 2, QTableWidgetItem(str(round(sum(self.third_strategy_credit_line),2))))
        self.general_table_bank_position.setItem(1, 3, QTableWidgetItem(str(round(sum(self.fourth_strategy_credit_line),2))))

        self.general_table_bank_position.setItem(2, 0, QTableWidgetItem(self.ui.main_table_necessary_percents.item(3, self.decades).text()))
        self.general_table_bank_position.setItem(2, 1, QTableWidgetItem(self.ui.main_table_necessary_percents.item(4, self.decades).text()))
        self.general_table_bank_position.setItem(2, 2, QTableWidgetItem(self.ui.main_table_necessary_percents.item(5, self.decades).text()))
        self.general_table_bank_position.setItem(2, 3, QTableWidgetItem(self.ui.main_table_necessary_percents.item(6, self.decades).text()))

    #14. Прибыль до налогообложения строительной организации при различных стратегиях
    #продаж с использованием заемных средств в объеме 85 % от стоимости проекта.
    #таблица №2 из статьи, задание 14
    def fill_table_financial_leverage_with_debt(self):

        #заполняем первую строку
        for i in range(4):
            item = QTableWidgetItem(str(round(float(self.ui.credit_is_got_fully_at_the_beginning.item(i, self.decades+2).text())*100, 2)))
            self.ui.table_financial_leverage_with_debt.setItem(0, i, item)
        #заполняем вторую строку
        for i in range(4):
           item = QTableWidgetItem(str(round(float(self.ui.credit_line_chooses_evenly.item(i, self.decades+2).text())*100, 2)))
           self.ui.table_financial_leverage_with_debt.setItem(1, i, item)
        #заполняем третью строку
        for i in range(4):
            item = QTableWidgetItem(str(round(float(self.ui.main_table_necessary_percents.item(i+3, self.decades+2).text())*100, 2)))
            self.ui.table_financial_leverage_with_debt.setItem(2, i, item)

    #15.	
    #Расчет эффект финансового рычага строительной организации при 
    #различных стратегиях продаж с использованием заемных средств    
    def fill_table_85_percent_debt_money(self):
        #заполняем первую строку
        for i in range(4):
            item1 = float(self.ui.Table_with_flat_sell_plan.item(i+5, self.decades).text())
            item2 = float(self.ui.credit_is_got_fully_at_the_beginning.item(i, self.decades + 4).text())
            res = QTableWidgetItem(str(round(item1 - item2, 2)))
            self.ui.table_85_percent_debt_money.setItem(0, i, res)
        #заполняем вторую строку
        for i in range(4):
            item1 = float(self.ui.Table_with_flat_sell_plan.item(i+5, self.decades).text())
            item2 = float(self.ui.credit_line_chooses_evenly.item(i, self.decades + 4).text())
            res = QTableWidgetItem(str(round(item1 - item2, 2)))
            self.ui.table_85_percent_debt_money.setItem(1, i, res)
        #заполняем третью строку
        for i in range(4):
            item1 = float(self.ui.Table_with_flat_sell_plan.item(i+5, self.decades).text())
            item2 = float(self.ui.main_table_necessary_percents.item(i+3, self.decades + 4).text())
            res = QTableWidgetItem(str(round(item1 - item2, 2)))
            self.ui.table_85_percent_debt_money.setItem(2, i, res)

    #16.
    #Рентабельность собственного капитала строительной организации
    #при различных стратегиях продаж с использованием заемных средств
    #в объеме 85 % от стоимости проекта, в процентах.
    def fill_table_profitability_of_own_money(self):
        #заполняем первую строку
        for i in range(4):
            item = QTableWidgetItem(str(round(float(self.ui.credit_is_got_fully_at_the_beginning.item(i, self.decades+3).text())*100, 2)))
            self.ui.table_profitability_of_own_money.setItem(0, i, item)
        #заполняем вторую строку
        for i in range(4):
           item = QTableWidgetItem(str(round(float(self.ui.credit_line_chooses_evenly.item(i, self.decades+3).text())*100, 2)))
           self.ui.table_profitability_of_own_money.setItem(1, i, item)
        #заполняем третью строку
        for i in range(4):
            item = QTableWidgetItem(str(round(float(self.ui.main_table_necessary_percents.item(i+3, self.decades+3).text())*100, 2)))
            self.ui.table_profitability_of_own_money.setItem(2, i, item)

    #17
    #Количество денежных средств, которые получит банк за предоставления кредита в размере 85%
    #от стоимости проекта за весь срок строительства
    def fill_table_bank_money_all_time(self):
        #заполняем первую строку
        for i in range(4):
            item = QTableWidgetItem(str(round(float(self.ui.credit_is_got_fully_at_the_beginning.item(i, self.decades).text()), 2)))
            self.ui.table_bank_money_all_time.setItem(0, i, item)
        #заполняем вторую строку
        for i in range(4):
           item = QTableWidgetItem(str(round(float(self.ui.credit_line_chooses_evenly.item(i, self.decades).text()), 2)))
           self.ui.table_bank_money_all_time.setItem(1, i, item)
        #заполняем третью строку
        for i in range(4):
            item = QTableWidgetItem(str(round(float(self.ui.main_table_necessary_percents.item(i+3, self.decades).text()), 2)))
            self.ui.table_bank_money_all_time.setItem(2, i, item)

    #18
    #Расчет средневзвешенной процентной ставки по заемному капиталу строительной организации при кредитовании 
    def fill_table_average_weighted_rate(self):
        #заполняем первую строку
        for i in range(4):
            item = QTableWidgetItem(str(round(float(self.ui.credit_is_got_fully_at_the_beginning.item(i, self.decades+1).text()), 2)))
            self.ui.table_average_weighted_rate.setItem(0, i, item)
        #заполняем вторую строку
        for i in range(4):
           item = QTableWidgetItem(str(round(float(self.ui.credit_line_chooses_evenly.item(i, self.decades+1).text()), 2)))
           self.ui.table_average_weighted_rate.setItem(1, i, item)
        #заполняем третью строку
        for i in range(4):
            item = QTableWidgetItem(str(round(float(self.ui.main_table_necessary_percents.item(i+3, self.decades+1).text()), 2)))
            self.ui.table_average_weighted_rate.setItem(2, i, item)

    #19.
    #Увеличение себестоимости 1м2 при различных видах кредитования и времени пополнения
    #счетов эскроу при кредитовании строительной организации
    def fill_table_encrease_owncost_area(self):
        tmp = self.s*self.n
        for i in range(3):
            for j in range(4):
                item = float(self.ui.table_bank_money_all_time.item(i,j).text())
                self.ui.table_encrease_owncost_area.setItem(i, j, QTableWidgetItem(str(round(float(item/tmp)))))

    #20
    #Увеличение себестоимости 1м2 при различных видах кредитования и времени пополнения
    #счетов эскроу при кредитовании строительной организации, %
    def fill_table_encrease_owncost_area_percentage(self):
        for i in range(3):
            for j in range(4):
                item = float(self.ui.table_encrease_owncost_area.item(i,j).text())
                self.ui.table_encrease_owncost_area_percentage.setItem(i, j,
                 QTableWidgetItem(str(round(float(item / self.c * 100), 1))))

    #21
    #Прикидка поступления денежных средств в бюджет за счет налоговых отчислений
    #от строительной организации и банка при кредитовании строительной организации 
    def fill_table_budget_money_income(self):
        for j in range(3):
            for i in range(4):
                if(j == 0):
                    q5 = float(self.ui.credit_is_got_fully_at_the_beginning.item(i, self.decades+4).text())
                elif(j == 1):
                    q5 = float(self.ui.credit_line_chooses_evenly.item(i, self.decades+4).text())
                else:
                    q5 = float(self.ui.main_table_necessary_percents.item(i + 3, self.decades+4).text())
                q2 = float(self.ui.Table_with_flat_sell_plan.item(i + 5, self.decades).text())
                item1 = (float(self.ui.table_bank_money_all_time.item(j, i).text()) - self.credit_money*0.05) * 0.24
                item2 = (q2 - q5)*0.2
                
                if(item1 > 0.0 and item2 > 0.0):
                    elem = QTableWidgetItem(str(round(item1 + item2)))
                elif(item1 < 0.0 and item2 > 0.0):
                    elem = QTableWidgetItem(str(round(item2)))
                elif(item1 > 0.0 and item2 < 0.0):
                    elem = QTableWidgetItem(str(round(item1)))
                else:
                    elem = QTableWidgetItem('0')
                self.ui.table_budget_money_income.setItem(j, i, elem)

    
        


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()
    sys.exit(app.exec())
