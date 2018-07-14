# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.t1 = QtWidgets.QLineEdit(Form)
        self.t1.setObjectName("t1")
        self.horizontalLayout.addWidget(self.t1)
        self.b1 = QtWidgets.QPushButton(Form)
        self.b1.setObjectName("b1")
        self.horizontalLayout.addWidget(self.b1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.t2 = QtWidgets.QLineEdit(Form)
        self.t2.setObjectName("t2")
        self.horizontalLayout_2.addWidget(self.t2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.t3 = QtWidgets.QLineEdit(Form)
        self.t3.setObjectName("t3")
        self.horizontalLayout_3.addWidget(self.t3)
        self.b2 = QtWidgets.QPushButton(Form)
        self.b2.setObjectName("b2")
        self.horizontalLayout_3.addWidget(self.b2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.t4 = QtWidgets.QLineEdit(Form)
        self.t4.setObjectName("t4")
        self.horizontalLayout_4.addWidget(self.t4)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.b1.clicked.connect(self.bookprice)
        self.b2.clicked.connect(self.totalprice)
        self.t3.setValidator(QtGui.QIntValidator())

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Book Title: "))
        self.b1.setText(_translate("Form", "Find Price"))
        self.label_2.setText(_translate("Form", "Price: "))
        self.label_3.setText(_translate("Form", "Quantity"))
        self.b2.setText(_translate("Form", "Find Total"))
        self.label_4.setText(_translate("Form", "Total"))
        
    def bookprice(self):
        import sqlite3 
        db=sqlite3.connect("listofbooks.db")
        cur=db.cursor()
        nm=self.t1.text()
        cur.execute("select * from books where Title = '"+nm+"';")
        record=cur.fetchone()
        if record==None:
            self.t2.setText("No Book found")
        else:
            prc=float(record[3])
            self.t2.setText(str(prc))
    def totalprice(self):
        prc=float(self.t2.text())       
        prc=prc*float(self.t3.text())
        self.t4.setText(str(prc))
               

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

