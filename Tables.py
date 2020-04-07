# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tables.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


import math
from PyQt5.QtCore import QDate
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QFrame

class Ui_NewWindow(object):
    def setupUi(self, MainWindow, percent):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 1000)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 800))
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(770, 10, 181, 31))
        self.pushButton.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 751, 161))
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.show_tables = QtWidgets.QPushButton(self.centralwidget)
        self.show_tables.setGeometry(QtCore.QRect(770, 130, 246, 31))
        self.show_tables.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.show_tables.setObjectName("show_tables")
        self.clear_tables = QtWidgets.QPushButton(self.centralwidget)
        self.clear_tables.setGeometry(QtCore.QRect(770, 70, 181, 31))
        self.clear_tables.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.clear_tables.setObjectName("clear_tables")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1600, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow, percent)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow, percent):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AdditionalWindow"))
        self.pushButton.setText(_translate("MainWindow", "Назад"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)

        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "Цена 1м²"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "План продаж"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "Определение процентной ставки на эскроу"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "Если кредит получен единовременно в начале, то платежи по процентам за пользование заемными средствами в конце периода"))
        item = self.listWidget.item(4)
        item.setText(_translate("MainWindow", "Если кредитная линия выбирается равномерно в течении срока строительства, то платежи по процентам за пользование заемными средствами в конце периода"))
        item = self.listWidget.item(5)
        item.setText(_translate("MainWindow", "Если кредитная линия выбирается по мере необходимости строительного процесса, то платежи по процентам за пользование заемными средствами в конце периода"))
        item = self.listWidget.item(6)
        item.setText(_translate("MainWindow", f'Прибыль с использованием заемных средств в объеме {percent} % от стоимости проекта'))
        item = self.listWidget.item(7)
        item.setText(_translate("MainWindow", "Финансовый рычаг при различных стратегиях продаж с использованием заемных средств"))
        item = self.listWidget.item(8)
        item.setText(_translate("MainWindow", "Рентабельность собственного капитала при различных стратегиях продаж с использованием заемных средств"))
        item = self.listWidget.item(9)
        item.setText(_translate("MainWindow", "Процентные выплаты, получаемые банком за предоставление кредита"))
        item = self.listWidget.item(10)
        item.setText(_translate("MainWindow", "Средневзвешенная процентная ставка по заемному капиталу строительной организации"))
        item = self.listWidget.item(11)
        item.setText(_translate("MainWindow", "Увеличение себестоимости 1м²  при кредитовании строительной организации"))
        item = self.listWidget.item(12)
        item.setText(_translate("MainWindow", "Увеличение себестоимости 1м²  при кредитовании строительной организации в %"))
        item = self.listWidget.item(13)
        item.setText(_translate("MainWindow", "Прикидка поступления денежных средств в бюджет за счет налоговых отчислений от строительной организации и банка"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.show_tables.setText(_translate("MainWindow", "Показать выбранные таблицы"))
        self.show_tables.setToolTip("Ctrl + click чтобы выбрать несколько таблиц")
        self.clear_tables.setText(_translate("MainWindow", "Скрыть таблицы"))

# no use for that
    def hide_tables(self):
        tables = self.centralwidget.findChildren(QtWidgets.QTableWidget)
        labels = self.centralwidget.findChildren(QtWidgets.QLabel)
        for table in tables:
            table.hide()
        for label in labels:
            label.hide()


    def create_tables(self, decades, percent):

        #Увелечение цены каждый квартал на какое-то кол-во процентов
        self.TableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.TableWidget.setObjectName("Table_decade")
        #self.TableWidget.move(-3000,-3000) 
        self.TableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.TableWidget.resizeColumnsToContents()
        self.TableWidget.resizeRowsToContents()
        self.TableWidget.setRowCount(2)
        self.TableWidget.setColumnCount(decades + 1)
        self.TableWidget.setHorizontalHeaderItem(decades, QTableWidgetItem("Средняя цена"))
        #self.TableWidget.setStyleSheet("background-color:rgb(207, 255, 245)")

        self.label_TableWidget = QtWidgets.QLabel(self.centralwidget)
        self.label_TableWidget.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_TableWidget.setText("Цена 1м²")

        #план продаж
        self.Table_with_flat_sell_plan = QtWidgets.QTableWidget(self.centralwidget)
        self.Table_with_flat_sell_plan.setObjectName("Table_with_flat_sell_plan")  
        #self.Table_with_flat_sell_plan.move(-3000,-3000) 
        self.Table_with_flat_sell_plan.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.Table_with_flat_sell_plan.resizeColumnsToContents()
        self.Table_with_flat_sell_plan.resizeRowsToContents()
        self.Table_with_flat_sell_plan.setRowCount(14)
        self.Table_with_flat_sell_plan.setColumnCount(decades + 1)#+2
        self.Table_with_flat_sell_plan.setHorizontalHeaderItem(decades, QTableWidgetItem("Итого"))
        #self.Table_with_flat_sell_plan.setHorizontalHeaderItem(decades + 1, QTableWidgetItem("Рентабильность активов"))
        self.Table_with_flat_sell_plan.setColumnWidth(decades + 1, 200)
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
        #self.Table_with_flat_sell_plan.setStyleSheet("background-color:rgb(207, 255, 245)")

        self.label_with_flat_sell_plan = QtWidgets.QLabel(self.centralwidget)
        self.label_with_flat_sell_plan.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_with_flat_sell_plan.setText("План продаж")

        #Эскроу счета
        self.escrow_rate = QtWidgets.QTableWidget(self.centralwidget)
        self.escrow_rate.setObjectName("escrow_rate")  
        #self.escrow_rate.move(-3000,-3000) 
        self.escrow_rate.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.escrow_rate.resizeColumnsToContents()
        self.escrow_rate.resizeRowsToContents()
        self.escrow_rate.setRowCount(4)
        self.escrow_rate.setColumnCount(decades)
        self.escrow_rate.setVerticalHeaderLabels([ "по стратегии 1 - в начале",
                                                            "по стратегии 2 - в середине",
                                                            "по стратегии 3 - в конце",
                                                            "по стратегии 4 - равномерно"])
        #self.escrow_rate.setStyleSheet("background-color:rgb(207, 255, 245)")

        self.label_escrow_rate = QtWidgets.QLabel(self.centralwidget)
        self.label_escrow_rate.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_escrow_rate.setText("Определение процентной ставки на эскроу")

        #Кредит получен целиком в начале
        self.credit_is_got_fully_at_the_beginning = QtWidgets.QTableWidget(self.centralwidget)
        self.credit_is_got_fully_at_the_beginning.setObjectName("credit_is_got_fully_atThe_beginning")  
        #self.credit_is_got_fully_at_the_beginning.move(-3000,-3000) 
        self.credit_is_got_fully_at_the_beginning.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.credit_is_got_fully_at_the_beginning.resizeColumnsToContents()
        self.credit_is_got_fully_at_the_beginning.resizeRowsToContents()
        self.credit_is_got_fully_at_the_beginning.setRowCount(4)
        self.credit_is_got_fully_at_the_beginning.setColumnCount(decades + 5)
        self.credit_is_got_fully_at_the_beginning.setVerticalHeaderLabels([ "по стратегии 1 - в начале",
                                                                            "по стратегии 2 - в середине",
                                                                            "по стратегии 3 - в конце",
                                                                            "по стратегии 4 - равномерно"])
        self.credit_is_got_fully_at_the_beginning.setColumnWidth(decades + 1, 230)
        self.credit_is_got_fully_at_the_beginning.setColumnWidth(decades + 2, 180)
        self.credit_is_got_fully_at_the_beginning.setColumnWidth(decades + 3, 230)
        #self.credit_is_got_fully_at_the_beginning.setStyleSheet("background-color:rgb(207, 255, 245)")

        self.label_credit_is_got_fully_at_the_beginning = QtWidgets.QLabel(self.centralwidget)
        self.label_credit_is_got_fully_at_the_beginning.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_credit_is_got_fully_at_the_beginning.setText("Платежи, если кредит получен единовременно в начале")

        #Кредит получен равномерно
        self.credit_line_chooses_evenly = QtWidgets.QTableWidget(self.centralwidget)
        self.credit_line_chooses_evenly.setObjectName("credit_line_chooses_evenly")  
        #self.credit_line_chooses_evenly.move(-3000,-3000) 
        self.credit_line_chooses_evenly.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.credit_line_chooses_evenly.resizeColumnsToContents()
        self.credit_line_chooses_evenly.resizeRowsToContents()
        self.credit_line_chooses_evenly.setRowCount(4)
        self.credit_line_chooses_evenly.setColumnCount(decades + 5)
        self.credit_line_chooses_evenly.setVerticalHeaderLabels([ "по стратегии 1 - в начале",
                                                            "по стратегии 2 - в середине",
                                                            "по стратегии 3 - в конце",
                                                            "по стратегии 4 - равномерно"])
       # self.credit_line_chooses_evenly.setStyleSheet("background-color:rgb(207, 255, 245)")

        self.label_credit_line_chooses_evenly = QtWidgets.QLabel(self.centralwidget)
        self.label_credit_line_chooses_evenly.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_credit_line_chooses_evenly.setText("Платежи, если кредит получен равномерно")

        #Кредит заполняется исходя из текущих нужд
        self.main_table_necessary_percents = QtWidgets.QTableWidget(self.centralwidget)
        self.main_table_necessary_percents.setObjectName("main_table_necessary_percents")  
        #self.main_table_necessary_percents.move(-3000,-3000) 
        self.main_table_necessary_percents.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.main_table_necessary_percents.resizeColumnsToContents()
        self.main_table_necessary_percents.resizeRowsToContents()
        self.main_table_necessary_percents.setRowCount(7)
        self.main_table_necessary_percents.setColumnCount(decades + 5)
        self.main_table_necessary_percents.setVerticalHeaderLabels(["потребность в денежныж средствах для реализации проекта", 
                                                                    "заемных средств, которые нужно взять у банка", 
                                                                    "количество заемных средств",
                                                                    "по 1 стратегии - в начале",
                                                                    "по 2 стратегии - в середине", 
                                                                    "по 3 стратегии - в конце", 
                                                                    "по 4 стратегии - равномерно"])
        
        self.main_table_necessary_percents.setHorizontalHeaderItem(decades, QTableWidgetItem("Сумма платежей"))
        self.main_table_necessary_percents.setHorizontalHeaderItem(decades + 1, QTableWidgetItem("Средневзвешенная процентная ставка"))
        self.main_table_necessary_percents.setHorizontalHeaderItem(decades + 2, QTableWidgetItem("Эффект финансового рычага"))
        self.main_table_necessary_percents.setHorizontalHeaderItem(decades + 3, QTableWidgetItem("Рентабильность собственного капиатала"))
        self.main_table_necessary_percents.setHorizontalHeaderItem(decades + 4, QTableWidgetItem("Итого"))
        self.main_table_necessary_percents.setColumnWidth(decades + 1, 230)
        self.main_table_necessary_percents.setColumnWidth(decades + 2, 180)
        self.main_table_necessary_percents.setColumnWidth(decades + 3, 240)
        #self.main_table_necessary_percents.setStyleSheet("background-color:rgb(207, 255, 245)")

        self.label_main_table_necessary_percents = QtWidgets.QLabel(self.centralwidget)
        self.label_main_table_necessary_percents.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_main_table_necessary_percents.setText("Платежи, если кредит получен из текущих нужд")

        #14. Прибыль до налогообложения строительной организации при различных стратегиях
        #продаж с использованием заемных средств в объеме 85 % от стоимости проекта.
        #таблица №2 из статьи, задание 14
        self.table_85_percent_debt_money = QtWidgets.QTableWidget(self.centralwidget)
        self.table_85_percent_debt_money.setObjectName('table_85_percent_debt_money')  
        #self.table_85_percent_debt_money.move(-3000,-3000) 
        self.table_85_percent_debt_money.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table_85_percent_debt_money.resizeColumnsToContents()
        self.table_85_percent_debt_money.resizeRowsToContents()
        self.table_85_percent_debt_money.setRowCount(3)
        self.table_85_percent_debt_money.setColumnCount(4)
        self.table_85_percent_debt_money.setVerticalHeaderLabels(["в начале строительства", "равномерно в течение строительства", "по мере производственной необходимости"])
        self.table_85_percent_debt_money.setHorizontalHeaderLabels(["в начале", "в середине", "в конце", "равномерно"])
        self.table_85_percent_debt_money.setAlternatingRowColors(True)
        self.table_85_percent_debt_money.setCornerButtonEnabled(True)
        #self.table_85_percent_debt_money.setStyleSheet("QTableCornerButton::section{border-width: 1px; border-color: #BABABA; border-style:solid; border-image: url(images/corner.png)0 0 0 0 stretch stretch}")

        self.label_85_percent_debt_money = QtWidgets.QLabel(self.centralwidget)
        self.label_85_percent_debt_money.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_85_percent_debt_money.setText(f"Прибыль с использованием заемных средств в объеме {percent}% от стоимости проекта")
        #self.label_85_percent_debt_money.setStyleSheet("background-color:rgb(207, 255, 245)")

        #15.	
        #Расчет эффект финансового рычага строительной организации при 
        #различных стратегиях продаж с использованием заемных средств
        self.table_financial_leverage_with_debt = QtWidgets.QTableWidget(self.centralwidget)
        self.table_financial_leverage_with_debt.setObjectName("table_financial_leverage_with_debt")  
        #self.table_financial_leverage_with_debt.move(-3000,-3000) 
        self.table_financial_leverage_with_debt.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table_financial_leverage_with_debt.resizeColumnsToContents()
        self.table_financial_leverage_with_debt.resizeRowsToContents()
        self.table_financial_leverage_with_debt.setRowCount(3)
        self.table_financial_leverage_with_debt.setColumnCount(4)
        self.table_financial_leverage_with_debt.setVerticalHeaderLabels(["в начале строительства", "равномерно в течение строительства", "по мере производственной необходимости"])
        self.table_financial_leverage_with_debt.setHorizontalHeaderLabels(["в начале", "в середине", "в конце", "равномерно"])
        #self.table_financial_leverage_with_debt.setStyleSheet("background-color:rgb(225, 255, 160)")
        self.table_financial_leverage_with_debt.setAlternatingRowColors(True)

        self.label_financial_leverage_with_debt = QtWidgets.QLabel(self.centralwidget)
        self.label_financial_leverage_with_debt.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_financial_leverage_with_debt.setText("Эффект финансового рычага строительной организации")
        #self.label_financial_leverage_with_debt.setStyleSheet("background-color:rgb(207, 255, 245)")

        #16.
        #Рентабельность собственного капитала строительной организации
        #при различных стратегиях продаж с использованием заемных средств
        #в объеме 85 % от стоимости проекта, в процентах.
        self.table_profitability_of_own_money = QtWidgets.QTableWidget(self.centralwidget)
        self.table_profitability_of_own_money.setObjectName("table_profitability_of_own_money")  
        #self.table_profitability_of_own_money.move(-3000,-3000) 
        self.table_profitability_of_own_money.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table_profitability_of_own_money.resizeColumnsToContents()
        self.table_profitability_of_own_money.resizeRowsToContents()
        self.table_profitability_of_own_money.setRowCount(3)
        self.table_profitability_of_own_money.setColumnCount(4)
        self.table_profitability_of_own_money.setVerticalHeaderLabels(["в начале строительства", "равномерно в течение строительства", "по мере производственной необходимости"])
        self.table_profitability_of_own_money.setHorizontalHeaderLabels(["в начале", "в середине", "в конце", "равномерно"])
        #self.table_profitability_of_own_money.setStyleSheet("background-color:rgb(225, 255, 160)")
        self.table_profitability_of_own_money.setAlternatingRowColors(True)

        self.label_profitability_of_own_money = QtWidgets.QLabel(self.centralwidget)
        self.label_profitability_of_own_money.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_profitability_of_own_money.setText("Рентабельность собственного капитала строительной организации")
        #self.label_profitability_of_own_money.setStyleSheet("background-color:rgb(207, 255, 245)")

        #17
        #Количество денежных средств, которые получит банк за предоставления кредита в размере 85%
        #от стоимости проекта за весь срок строительства
        self.table_bank_money_all_time = QtWidgets.QTableWidget(self.centralwidget)
        self.table_bank_money_all_time.setObjectName("table_bank_money_all_time")  
        #self.table_bank_money_all_time.move(-3000,-3000) 
        self.table_bank_money_all_time.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table_bank_money_all_time.resizeColumnsToContents()
        self.table_bank_money_all_time.resizeRowsToContents()
        self.table_bank_money_all_time.setRowCount(3)
        self.table_bank_money_all_time.setColumnCount(4)
        self.table_bank_money_all_time.setVerticalHeaderLabels(["в начале строительства", "равномерно в течение строительства", "по мере производственной необходимости"])
        self.table_bank_money_all_time.setHorizontalHeaderLabels(["в начале", "в середине", "в конце", "равномерно"])
        #self.table_bank_money_all_time.setStyleSheet("background-color:rgb(225, 255, 160)")
        self.table_bank_money_all_time.setAlternatingRowColors(True)

        self.label_bank_money_all_time = QtWidgets.QLabel(self.centralwidget)
        self.label_bank_money_all_time.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_bank_money_all_time.setText("Процентные выплаты, получаемые банком за предоставление кредита строительной организации")
        #self.label_bank_money_all_time.setStyleSheet("background-color:rgb(207, 255, 245)")

        #18
        #Расчет средневзвешенной процентной ставки по заемному капиталу строительной организации при кредитовании 
        self.table_average_weighted_rate = QtWidgets.QTableWidget(self.centralwidget)
        self.table_average_weighted_rate.setObjectName("table_average_weighted_rate")  
        #self.table_average_weighted_rate.move(-3000,-3000) 
        self.table_average_weighted_rate.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table_average_weighted_rate.resizeColumnsToContents()
        self.table_average_weighted_rate.resizeRowsToContents()
        self.table_average_weighted_rate.setRowCount(3)
        self.table_average_weighted_rate.setColumnCount(4)
        self.table_average_weighted_rate.setVerticalHeaderLabels(["в начале строительства", "равномерно в течение строительства", "по мере производственной необходимости"])
        self.table_average_weighted_rate.setHorizontalHeaderLabels(["в начале", "в середине", "в конце", "равномерно"])
        #self.table_average_weighted_rate.setStyleSheet("background-color:rgb(225, 255, 160)")
        self.table_average_weighted_rate.setAlternatingRowColors(True)

        self.label_average_weighted_rate = QtWidgets.QLabel(self.centralwidget)
        self.label_average_weighted_rate.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_average_weighted_rate.setText("Средневзвешенная процентная ставка по заемному капиталу за весь срок кредитования строительной организации")
        #self.label_average_weighted_rate.setStyleSheet("background-color:rgb(207, 255, 245)")

        #19.
        #Увеличение себестоимости 1м2 при различных видах кредитования и времени пополнения
        #счетов эскроу при кредитовании строительной организации
        self.table_encrease_owncost_area = QtWidgets.QTableWidget(self.centralwidget)
        self.table_encrease_owncost_area.setObjectName("table_encrease_owncost_area")  
        #self.table_encrease_owncost_area.move(-3000,-3000) 
        self.table_encrease_owncost_area.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table_encrease_owncost_area.resizeColumnsToContents()
        self.table_encrease_owncost_area.resizeRowsToContents()
        self.table_encrease_owncost_area.setRowCount(3)
        self.table_encrease_owncost_area.setColumnCount(4)
        self.table_encrease_owncost_area.setVerticalHeaderLabels(["в начале строительства", "равномерно в течение строительства", "по мере производственной необходимости"])
        self.table_encrease_owncost_area.setHorizontalHeaderLabels(["в начале", "в середине", "в конце", "равномерно"])
        #self.table_encrease_owncost_area.setStyleSheet("background-color:rgb(225, 255, 160)")
        self.table_encrease_owncost_area.setAlternatingRowColors(True)

        self.label_encrease_owncost_area = QtWidgets.QLabel(self.centralwidget)
        self.label_encrease_owncost_area.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_encrease_owncost_area.setText("Увеличение себестоимости 1м2 при различных видах кредитования и времени пополнения счетов эскроу при кредитовании строительной организации")
        #self.label_encrease_owncost_area.setStyleSheet("background-color:rgb(207, 255, 245)")

        #20
        #Увеличение себестоимости 1м2 при различных видах кредитования и времени пополнения
        #счетов эскроу при кредитовании строительной организации, %
        self.table_encrease_owncost_area_percentage = QtWidgets.QTableWidget(self.centralwidget)
        self.table_encrease_owncost_area_percentage.setObjectName("table_encrease_owncost_area_percentage")  
        #self.table_encrease_owncost_area_percentage.move(-3000,-3000) 
        self.table_encrease_owncost_area_percentage.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table_encrease_owncost_area_percentage.resizeColumnsToContents()
        self.table_encrease_owncost_area_percentage.resizeRowsToContents()
        self.table_encrease_owncost_area_percentage.setRowCount(3)
        self.table_encrease_owncost_area_percentage.setColumnCount(4)
        self.table_encrease_owncost_area_percentage.setVerticalHeaderLabels(["в начале строительства", "равномерно в течение строительства", "по мере производственной необходимости"])
        self.table_encrease_owncost_area_percentage.setHorizontalHeaderLabels(["в начале", "в середине", "в конце", "равномерно"])
        #self.table_encrease_owncost_area_percentage.setStyleSheet("background-color:rgb(225, 255, 160)")
        self.table_encrease_owncost_area_percentage.setAlternatingRowColors(True)

        self.label_encrease_owncost_area_percentage = QtWidgets.QLabel(self.centralwidget)
        self.label_encrease_owncost_area_percentage.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_encrease_owncost_area_percentage.setText("Увеличение себестоимости 1м2 при различных видах кредитования и времени пополнения счетов эскроу в процентах")
        #self.label_encrease_owncost_area_percentage.setStyleSheet("background-color:rgb(207, 255, 245)")

        #21
        #Прикидка поступления денежных средств в бюджет за счет налоговых отчислений
        #от строительной организации и банка при кредитовании строительной организации 
        self.table_budget_money_income = QtWidgets.QTableWidget(self.centralwidget)
        self.table_budget_money_income.setObjectName("table_budget_money_income")  
        #self.table_budget_money_income.move(-3000,-3000) 
        self.table_budget_money_income.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table_budget_money_income.resizeColumnsToContents()
        self.table_budget_money_income.resizeRowsToContents()
        self.table_budget_money_income.setRowCount(3)
        self.table_budget_money_income.setColumnCount(4)
        self.table_budget_money_income.setVerticalHeaderLabels(["в начале строительства", "равномерно в течение строительства", "по мере производственной необходимости"])
        self.table_budget_money_income.setHorizontalHeaderLabels(["в начале", "в середине", "в конце", "равномерно"])
        #self.table_budget_money_income.setStyleSheet("background-color:rgb(225, 255, 160)")
        self.table_budget_money_income.setAlternatingRowColors(True)
        #self.table_budget_money_income.horizontalHeader().setStretchLastSection(True)

        self.label_budget_money_income = QtWidgets.QLabel(self.centralwidget)
        self.label_budget_money_income.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_budget_money_income.setText("Прикидка поступления денежных средств в бюджет за счет налоговых отчислений от строительной организации и банка при кредитовании строительной организации")
        #self.label_budget_money_income.setStyleSheet("background-color:rgb(207, 255, 245)")
    
        self.hide_tables()