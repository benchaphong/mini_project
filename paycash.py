# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\ProPy\UI\paycash.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from thankyou import Ui_Thank
import thankyou

class Ui_Form(object):

    def changeThank(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Thank()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(793, 585)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(160, 140, 401, 181))
        self.label.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"font: 87 20pt \"Segoe UI Black\";")
        self.label.setObjectName("label")
        self.pushPay = QtWidgets.QPushButton(Form)
        self.pushPay.setGeometry(QtCore.QRect(270, 400, 201, 81))
        self.pushPay.setStyleSheet("font: 81 16pt \"Rockwell Extra Bold\";\n"
"background-color: rgb(255, 170, 127);")
        self.pushPay.setObjectName("pushPay")

        self.pushPay.clicked.connect(self.changeThank)

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(-120, -50, 1011, 671))
        self.label_2.setStyleSheet("background-image: url(C:/ProPy/JPEG/c.jpg);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.label.raise_()
        self.pushPay.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\">Wait for the merchant </p><p align=\"center\">and make the payment</p></body></html>"))
        self.pushPay.setText(_translate("Form", "confirm"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
