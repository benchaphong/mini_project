# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\ProPy\UI\addsmoothie.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(792, 589)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(210, 60, 381, 91))
        self.label.setStyleSheet("font: 50pt \"Playbill\";\n"
"background-color: rgb(231, 210, 255);\n"
"color: rgb(255, 0, 0);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 220, 241, 41))
        self.label_2.setStyleSheet("font: 20pt \"Tw Cen MT Condensed Extra Bold\";\n"
"background-color: rgb(207, 255, 246);\n"
"")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(80, 300, 241, 41))
        self.label_3.setStyleSheet("font: 20pt \"Tw Cen MT Condensed Extra Bold\";\n"
"background-color: rgb(207, 255, 246);\n"
"")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(390, 220, 301, 41))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(390, 310, 301, 41))
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.pushAddcon = QtWidgets.QPushButton(Form)
        self.pushAddcon.setGeometry(QtCore.QRect(280, 440, 211, 91))
        self.pushAddcon.setStyleSheet("font: 24pt \"Tw Cen MT Condensed Extra Bold\";\n"
"color:rgb(255, 116, 17);\n"
"background-color: rgb(255, 245, 184);")
        self.pushAddcon.setObjectName("pushAddcon")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(-220, -110, 1091, 741))
        self.label_6.setStyleSheet("background-image: url(:/newPrefix/d.jpg);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_6.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.pushAddcon.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\">Add Smoothie </p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\">Name Smoothie :</p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p align=\"center\">Cost :</p></body></html>"))
        self.pushAddcon.setText(_translate("Form", "Add Confirm"))
import 1_rc
