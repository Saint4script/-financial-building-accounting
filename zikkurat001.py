# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Zikkurat001.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Total_area = QtWidgets.QLineEdit(self.centralwidget)
        self.Total_area.setGeometry(QtCore.QRect(330, 30, 141, 22))
        self.Total_area.setObjectName("Total_area")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 30, 231, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 60, 241, 20))
        self.label_2.setObjectName("label_2")
        self.Apartments_amount = QtWidgets.QLineEdit(self.centralwidget)
        self.Apartments_amount.setGeometry(QtCore.QRect(330, 60, 141, 22))
        self.Apartments_amount.setObjectName("Apartments_amount")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 90, 241, 20))
        self.label_3.setObjectName("label_3")
        self.Average_area_of_apartments = QtWidgets.QLineEdit(self.centralwidget)
        self.Average_area_of_apartments.setGeometry(QtCore.QRect(330, 90, 141, 22))
        self.Average_area_of_apartments.setObjectName("Average_area_of_apartments")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 180, 241, 20))
        self.label_4.setObjectName("label_4")
        self.Bulding_duration = QtWidgets.QLineEdit(self.centralwidget)
        self.Bulding_duration.setGeometry(QtCore.QRect(330, 180, 141, 22))
        self.Bulding_duration.setObjectName("Bulding_duration")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 150, 241, 20))
        self.label_5.setObjectName("label_5")
        self.Increasing_percentage = QtWidgets.QLineEdit(self.centralwidget)
        self.Increasing_percentage.setGeometry(QtCore.QRect(330, 150, 141, 22))
        self.Increasing_percentage.setObjectName("Increasing_percentage")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 120, 241, 20))
        self.label_6.setObjectName("label_6")
        self.Start_cost = QtWidgets.QLineEdit(self.centralwidget)
        self.Start_cost.setGeometry(QtCore.QRect(330, 120, 141, 22))
        self.Start_cost.setObjectName("Start_cost")
        self.Start_money = QtWidgets.QLineEdit(self.centralwidget)
        self.Start_money.setGeometry(QtCore.QRect(330, 210, 141, 22))
        self.Start_money.setText("")
        self.Start_money.setObjectName("Start_money")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(50, 210, 241, 20))
        self.label_7.setObjectName("label_7")
        self.Self_cost = QtWidgets.QLineEdit(self.centralwidget)
        self.Self_cost.setGeometry(QtCore.QRect(330, 240, 141, 22))
        self.Self_cost.setObjectName("Self_cost")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(50, 240, 241, 20))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(50, 300, 241, 20))
        self.label_9.setObjectName("label_9")
        self.Project_cost = QtWidgets.QLineEdit(self.centralwidget)
        self.Project_cost.setGeometry(QtCore.QRect(330, 300, 141, 22))
        self.Project_cost.setObjectName("Project_cost")
        self.Build = QtWidgets.QPushButton(self.centralwidget)
        self.Build.setGeometry(QtCore.QRect(50, 350, 201, 71))
        self.Build.setObjectName("Build")
        self.Test = QtWidgets.QPushButton(self.centralwidget)
        self.Test.setGeometry(QtCore.QRect(400, 400, 211, 111))
        self.Test.setObjectName("Test")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(500, 150, 312, 183))
        self.calendarWidget.setObjectName("calendarWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>Общая площадь(м<span style=\" vertical-align:super;\">2</span>)</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Количество квартир(шт)"))
        self.label_3.setText(_translate("MainWindow", "Средняя площадь квартир - м2"))
        self.label_4.setText(_translate("MainWindow", "Срок строительства"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p>Процент увеличения цены 1м<span style=\" vertical-align:super;\">2 </span>в периоде </p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "Начальная цена 1 м2 – руб"))
        self.label_7.setText(_translate("MainWindow", "Собственный капитал "))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p>Себестоимость 1 м<span style=\" vertical-align:super;\">2</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p>*Стоимость проекта*</p></body></html>"))
        self.Build.setText(_translate("MainWindow", "Построить Зиккурат"))
        self.Test.setText(_translate("MainWindow", "PushButton"))
