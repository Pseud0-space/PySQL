from PyQt5 import QtCore, QtWidgets
import sys
import register
import Login
import ChangePass
import RecvPass


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(797, 200)
        MainWindow.setStyleSheet("background-color: rgb(34, 34, 34);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 20, 231, 51))
        self.label.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
                                 "text-decoration: underline;")

        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 110, 161, 51))
        self.pushButton.clicked.connect(self.logn)
        self.pushButton.setStyleSheet("background-color: rgb(172, 0, 2);\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "border-radius : 20%;")

        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 110, 151, 51))
        self.pushButton_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton_2.setStyleSheet("background-color: rgb(172, 0, 2);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "border-radius : 20%;")

        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.reg)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(410, 110, 151, 51))
        self.pushButton_3.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton_3.setStyleSheet("background-color: rgb(172, 0, 2);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "border-radius : 20%;")

        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.ChangePass)

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(570, 110, 151, 51))
        self.pushButton_4.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton_4.setStyleSheet("background-color: rgb(172, 0, 2);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "border-radius : 20%;")

        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.RecvPass)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LOGIN & REGISTER"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">LOGIN &amp; REGISTER</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "LOGIN"))
        self.pushButton_2.setText(_translate("MainWindow", "REGISTER"))
        self.pushButton_3.setText(_translate("MainWindow", "CHANGE PASSWORD"))
        self.pushButton_4.setText(_translate("MainWindow", "RECOVER PASSWORD"))

        MainWindow.show()

    def reg(self):
        self.win = register.Ui_RegisterWindow()
        self.win.show()

    def logn(self):
        self.win2 = Login.Ui_LoginWindow()
        self.win2.show()

    def ChangePass(self):
        self.win3 = ChangePass.ChangePass()
        self.win3.show()

    def RecvPass(self):
        self.win4 = RecvPass.Ui_RecvWindow()
        self.win4.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    sys.exit(app.exec_())
