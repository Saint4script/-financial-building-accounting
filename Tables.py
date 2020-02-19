# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tables.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 1000)
        MainWindow.setMinimumSize(QtCore.QSize(1600, 1000))
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(990, 20, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 651, 91))
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
        self.show_tables = QtWidgets.QPushButton(self.centralwidget)
        self.show_tables.setGeometry(QtCore.QRect(670, 20, 131, 28))
        self.show_tables.setObjectName("show_tables")
        self.clear_tables = QtWidgets.QPushButton(self.centralwidget)
        self.clear_tables.setGeometry(QtCore.QRect(812, 20, 121, 28))
        self.clear_tables.setObjectName("clear_tables")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1600, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AdditionalWindow"))
        self.pushButton.setText(_translate("MainWindow", "Назад"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "Цена 1м^2"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "План продаж"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "Определение процентной ставки на эскроу"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "если кредит получен единовременно в начале, то платежи по процентам за пользование заемными средствами в конце периода"))
        item = self.listWidget.item(4)
        item.setText(_translate("MainWindow", "если кредитная линия выбирается равномерно в течении срока строительства, то платежи по процентам за пользование заемными средствами в конце периода"))
        item = self.listWidget.item(5)
        item.setText(_translate("MainWindow", "если кредитная линия выбирается по мере необходимости строительного процесса, то платежи по процентам за пользование заемными средствами в конце периода"))
        item = self.listWidget.item(6)
        item.setText(_translate("MainWindow", "Процентные выплаты, которые получит банк"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.show_tables.setText(_translate("MainWindow", "Показать выбранные"))
        self.clear_tables.setText(_translate("MainWindow", "Скрыть таблицы"))
