# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rapp.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(538, 461)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(170, 400, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.ti = QtWidgets.QLabel(Dialog)
        self.ti.setGeometry(QtCore.QRect(60, 90, 61, 41))
        self.ti.setObjectName("ti")
        self.ty = QtWidgets.QLabel(Dialog)
        self.ty.setGeometry(QtCore.QRect(60, 140, 71, 41))
        self.ty.setObjectName("ty")
        self.dh = QtWidgets.QLabel(Dialog)
        self.dh.setGeometry(QtCore.QRect(50, 310, 71, 31))
        self.dh.setObjectName("dh")
        self.des = QtWidgets.QLabel(Dialog)
        self.des.setGeometry(QtCore.QRect(10, 220, 121, 41))
        self.des.setObjectName("des")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(160, 90, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(Dialog)
        self.dateTimeEdit.setGeometry(QtCore.QRect(140, 310, 194, 22))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(170, 140, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(140, 10, 261, 71))
        self.label_5.setObjectName("label_5")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(140, 220, 141, 71))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.aj = QtWidgets.QPushButton(Dialog)
        self.aj.setGeometry(QtCore.QRect(130, 400, 75, 23))
        self.aj.setObjectName("aj")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.ti.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#ff007f;\">Titre :</span></p><p><br/></p></body></html>"))
        self.ty.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#ff007f;\">Type :</span></p><p><br/></p></body></html>"))
        self.dh.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#ff007f;\">Date :</span></p></body></html>"))
        self.des.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#ff007f;\">Description :</span></p><p><br/></p><p><br/></p></body></html>"))
        self.comboBox.setItemText(0, _translate("Dialog", "Sortie"))
        self.comboBox.setItemText(1, _translate("Dialog", "Loisir"))
        self.comboBox.setItemText(2, _translate("Dialog", "Sante"))
        self.comboBox.setItemText(3, _translate("Dialog", "Travail"))
        self.comboBox.setItemText(4, _translate("Dialog", "Education"))
        self.comboBox.setItemText(5, _translate("Dialog", "Autre"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; font-style:italic; text-decoration: underline; color:#5500ff;\">Gestion de Rapelles</span></p></body></html>"))
        self.aj.setText(_translate("Dialog", "Ajouter "))
