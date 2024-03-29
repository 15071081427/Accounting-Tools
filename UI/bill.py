# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bill.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(498, 438)
        self.centralLayout = QtWidgets.QVBoxLayout(Dialog)
        self.centralLayout.setObjectName("centralLayout")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_expense = QtWidgets.QWidget()
        self.tab_expense.setObjectName("tab_expense")
        self.expenseLayout = QtWidgets.QVBoxLayout(self.tab_expense)
        self.expenseLayout.setObjectName("expenseLayout")
        self.expenseTitleLayout = QtWidgets.QHBoxLayout()
        self.expenseTitleLayout.setObjectName("expenseTitleLayout")
        self.label_expenseType = QtWidgets.QLabel(self.tab_expense)
        self.label_expenseType.setObjectName("label_expenseType")
        self.expenseTitleLayout.addWidget(self.label_expenseType)
        spacerItem = QtWidgets.QSpacerItem(451, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.expenseTitleLayout.addItem(spacerItem)
        self.lineEdit_expenseVal = QtWidgets.QLineEdit(self.tab_expense)
        self.lineEdit_expenseVal.setObjectName("lineEdit_expenseVal")
        self.expenseTitleLayout.addWidget(self.lineEdit_expenseVal)
        self.expenseTitleLayout.setStretch(0, 1)
        self.expenseTitleLayout.setStretch(1, 4)
        self.expenseTitleLayout.setStretch(2, 1)
        self.expenseLayout.addLayout(self.expenseTitleLayout)
        self.expenseTypeLayout = QtWidgets.QGridLayout()
        self.expenseTypeLayout.setObjectName("expenseTypeLayout")
        self.expenseLayout.addLayout(self.expenseTypeLayout)
        self.expenseLayout.setStretch(0, 1)
        self.expenseLayout.setStretch(1, 6)
        self.tabWidget.addTab(self.tab_expense, "")
        self.tab_income = QtWidgets.QWidget()
        self.tab_income.setObjectName("tab_income")
        self.incomeLayout = QtWidgets.QVBoxLayout(self.tab_income)
        self.incomeLayout.setObjectName("incomeLayout")
        self.incomeTitleLayout = QtWidgets.QHBoxLayout()
        self.incomeTitleLayout.setObjectName("incomeTitleLayout")
        self.label_incomeType = QtWidgets.QLabel(self.tab_income)
        self.label_incomeType.setObjectName("label_incomeType")
        self.incomeTitleLayout.addWidget(self.label_incomeType)
        spacerItem1 = QtWidgets.QSpacerItem(453, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.incomeTitleLayout.addItem(spacerItem1)
        self.lineEdit_incomeVal = QtWidgets.QLineEdit(self.tab_income)
        self.lineEdit_incomeVal.setObjectName("lineEdit_incomeVal")
        self.incomeTitleLayout.addWidget(self.lineEdit_incomeVal)
        self.incomeTitleLayout.setStretch(0, 1)
        self.incomeTitleLayout.setStretch(1, 4)
        self.incomeTitleLayout.setStretch(2, 1)
        self.incomeLayout.addLayout(self.incomeTitleLayout)
        self.incomeTypeLayout = QtWidgets.QGridLayout()
        self.incomeTypeLayout.setObjectName("incomeTypeLayout")
        self.incomeLayout.addLayout(self.incomeTypeLayout)
        self.incomeLayout.setStretch(0, 1)
        self.incomeLayout.setStretch(1, 6)
        self.tabWidget.addTab(self.tab_income, "")
        self.centralLayout.addWidget(self.tabWidget)
        self.closeLayout = QtWidgets.QHBoxLayout()
        self.closeLayout.setObjectName("closeLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.closeLayout.addItem(spacerItem2)
        self.pushButton_confirm = QtWidgets.QPushButton(Dialog)
        self.pushButton_confirm.setObjectName("pushButton_confirm")
        self.closeLayout.addWidget(self.pushButton_confirm)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.closeLayout.addItem(spacerItem3)
        self.centralLayout.addLayout(self.closeLayout)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_expenseType.setText(_translate("Dialog", "其他"))
        self.lineEdit_expenseVal.setText(_translate("Dialog", "0.00"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_expense), _translate("Dialog", "支出"))
        self.label_incomeType.setText(_translate("Dialog", "其他"))
        self.lineEdit_incomeVal.setText(_translate("Dialog", "0.00"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_income), _translate("Dialog", "收入"))
        self.pushButton_confirm.setText(_translate("Dialog", "确认"))
