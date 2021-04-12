import mysql.connector
import sys
import StudenInfo

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QLineEdit, QMessageBox
from PyQt5.QtGui import QPixmap

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64

from MySQLPass import MySQLPassword
from MySQL_DB import db


class Ui_RecvWindow(QMainWindow):
    def __init__(self):
        super(Ui_RecvWindow, self).__init__()

        self.setWindowTitle("PASSWORD RECOVERY")
        self.setFixedSize(670, 420)
        self.setStyleSheet("background-color: rgb(34, 34, 34);")
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 330, 181, 61))
        # self.pushButton.clicked.connect(self.backend_login)
        self.pushButton.setStyleSheet("background-color: rgb(172, 0, 2);\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "border-radius : 20%;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.backend)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 20, 220, 41))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 120, 130, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(240, 170, 360, 21))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(240, 270, 140, 21))
        self.label_4.setObjectName("label_4")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(390, 115, 231, 31))
        self.lineEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 11pt \"Cambria\";\n"
                                    "background-color: rgb(74, 74, 74);\n"
                                    "border-radius : 10%")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setEchoMode(QLineEdit.Password)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(240, 200, 380, 31))
        self.lineEdit_2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "font: 11pt \"Cambria\";\n"
                                      "background-color: rgb(74, 74, 74);\n"
                                      "border-radius : 10%")
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(390, 265, 231, 31))
        self.lineEdit_3.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "font: 11pt \"Cambria\";\n"
                                      "background-color: rgb(74, 74, 74);\n"
                                      "border-radius : 10%")
        self.lineEdit_3.setObjectName("lineEdit_2")

        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 590, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar()
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("LoginWindow", "RECOVER"))
        self.label.setText(_translate("LoginWindow",
                                      "<html><head/><body><p><span style=\" font-size:16pt; text-decoration: underline; color:#ffffff;\">PASSWORD RECOVERY</span></p></body></html>"))
        self.label_2.setText(_translate("LoginWindow",
                                        "<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">ADMIN Password</span></p></body></html>"))
        self.label_3.setText(_translate("LoginWindow",
                                        "<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Student ID of the student who's password is to be recovered </span></p></body></html>"))
        self.label_4.setText(_translate("LoginWindow",
                                        "<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">Recovered Password</span></p></body></html>"))
        self.pic = QPixmap('Images/PassRecv.png')

        self.LabelImg = QLabel(self)
        self.LabelImg.setPixmap(self.pic)
        self.LabelImg.setGeometry(QtCore.QRect(30, 80, 180, 185))

        self.show()

    def ShwError(self):
        msgBox = QMessageBox()
        msgBox.setFixedSize(400, 400)
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setText("Invalid Admin Password")
        msgBox.setWindowTitle("ERROR")
    
        returnValue = msgBox.exec_()
        if returnValue == QMessageBox.Ok:
            pass

    def ShwError1(self):
        msgBox = QMessageBox()
        msgBox.setFixedSize(400, 400)
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setText("Invalid Student ID")
        msgBox.setWindowTitle("ERROR")
    
        returnValue = msgBox.exec_()
        if returnValue == QMessageBox.Ok:
            pass

    def backend(self):
        def decrypt(inp):
            backend = default_backend()

            key = b"2\xb9(\x88\xd9gz\xdb\x9f};\x96\xf2\xfe\xf2\xa6Kb/V\xde\x00\xbd\xff\xe1\x9a\x1c\xb0\xb2d{M"
            iv = b'\xc62\xb3\x8d\x94z(\xb2\xbc\x13^\x18\r.\x92\xa7'

            paa = inp.encode()
            b64 = base64.b64decode(paa)
            cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
            decryptor = cipher.decryptor()
            dec = decryptor.update(b64) + decryptor.finalize()
            return dec.rstrip().decode()

        AdminPass = self.lineEdit.text()
        ID = int(self.lineEdit_2.text())
        RecvPass = self.lineEdit_3.text()

        database = mysql.connector.connect(host="localhost", user="root", passwd=MySQLPassword(), database=db())
        AdminCursor = database.cursor()

        AdminCursor.execute(f"SELECT * from login Where NAME = 'ADMIN';")
        fetchAdmin = AdminCursor.fetchall()[0][1]

        RecvCursor = database.cursor()
        RecvCursor.execute(f"SELECT * from login Where STUDENT_ID = {ID};")

        if AdminPass == decrypt(fetchAdmin):
            fetchPass = RecvCursor.fetchall()
            if fetchPass == []:
                self.ShwError1()
            else:
                recovered = decrypt(fetchPass[0][1])
                self.lineEdit_3.setText(recovered)

        else:
            self.ShwError()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_RecvWindow()
    sys.exit(app.exec_())
