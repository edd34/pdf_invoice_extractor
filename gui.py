# -*- coding: utf-8 -*-    
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from main import main

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("SMAE Invoice Data Extractir")
        MainWindow.resize(514, 381)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.text_output = QtWidgets.QTextEdit(self.centralwidget)
        self.text_output.setGeometry(QtCore.QRect(80, 10, 351, 271))
        self.text_output.setObjectName("text_output")
        self.btn_Action = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Action.setGeometry(QtCore.QRect(220, 300, 75, 23))
        self.btn_Action.setObjectName("btn_Action")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 514, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_File = QtWidgets.QAction(MainWindow)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.actionOpen_File.setShortcut('Ctrl+O')
        self.actionOpen_File.triggered.connect(self.file_open)
        self.menuFile.addAction(self.actionOpen_File)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_Action.setText(_translate("MainWindow", "Action"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_File.setText(_translate("MainWindow", "Open File"))


    def file_open(self):
        name, _ = QtWidgets.QFileDialog.getOpenFileName(None, 'Open File', options=QtWidgets.QFileDialog.DontUseNativeDialog)
        file = open(name, 'rb')
        print(name, file.name)
        self.text_output.append(name)
        self.filename = file
        # with file:
        #     print(name)
        #     # text = file.read()
        #     # self.text_output.setText(text)

    def run_extraction(self): 
        print(self.filename.name)
        pass
        # f = self.text_output
        # print(self.text_output)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btn_Action.clicked.connect(lambda: ui.text_output.append(str(ui.run_extraction())))
    MainWindow.show()
    sys.exit(app.exec_())
