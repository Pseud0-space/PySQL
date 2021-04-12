import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QMessageBox, QLineEdit
import mysql.connector

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64

from MySQLPass import MySQLPassword
from MySQL_DB import db


class Ui_RegisterWindow(QMainWindow):
    def __init__(self):
        super(Ui_RegisterWindow, self).__init__()

        self.setWindowTitle("REGISTER")
        self.setFixedSize(691, 830)
        self.setStyleSheet("background-color: rgb(27, 27, 27);")
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 730, 201, 71))
        self.pushButton.clicked.connect(self.backend_register)
        self.pushButton.setStyleSheet("background-color: rgb(158, 0, 2);\n"
                                      "border-radius : 20%;\n"
                                      "font: 11pt \"Cambria\";"
                                      "color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(257, 20, 211, 41))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.Mlabel = QtWidgets.QLabel(self.centralwidget)
        self.Mlabel.setGeometry(QtCore.QRect(120, 258, 320, 41))
        self.Mlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.Mlabel.setObjectName("Mlabel")

        self.Alabel = QtWidgets.QLabel(self.centralwidget)
        self.Alabel.setGeometry(QtCore.QRect(140, 320, 160, 41))
        self.Alabel.setAlignment(QtCore.Qt.AlignCenter)
        self.Alabel.setObjectName("Alabel")

        self.Adminline = QtWidgets.QLineEdit(self.centralwidget)
        self.Adminline.setGeometry(QtCore.QRect(310, 325, 281, 31))
        self.Adminline.setStyleSheet("background-color: rgb(74, 74, 74);\n"
                                    "font: 10pt \"Cambria\";\n"
                                    "border-radius : 10%;\n"
                                    "color: rgb(255, 255, 255);")
        self.Adminline.setObjectName("Adminline")
        self.Adminline.setEchoMode(QLineEdit.Password)

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(310, 385, 281, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(74, 74, 74);\n"
                                    "font: 10pt \"Cambria\";\n"
                                    "border-radius : 10%;\n"
                                    "color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit2.setGeometry(QtCore.QRect(310, 440, 281, 31))
        self.lineEdit2.setStyleSheet("background-color: rgb(74, 74, 75);\n"
                                     "font: 10pt \"Cambria\";\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "border-radius : 10%")
        self.lineEdit2.setObjectName("lineEdit2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 390, 61, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 445, 140, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(150, 665, 131, 21))
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(310, 660, 281, 31))
        self.lineEdit_2.setStyleSheet("background-color: rgb(74, 74, 74);\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "font: 11pt \"Cambria\";\n"
                                      "border-radius : 10%;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(310, 495, 281, 31))
        self.lineEdit_3.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(74, 74, 74);\n"
                                      "font: 11pt \"Cambria\";\n"
                                      "border-radius : 10%")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(310, 550, 281, 31))
        self.lineEdit_4.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "font: 11pt \"Cambria\";\n"
                                      "background-color: rgb(74, 74, 74);\n"
                                      "border-radius : 10%")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(310, 605, 281, 31))
        self.lineEdit_5.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(74, 74, 74);\n"
                                      "font: 11pt \"Cambria\";\n"
                                      "border-radius : 10%")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(195, 500, 90, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(190, 555, 61, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(170, 610, 111, 21))
        self.label_7.setObjectName("label_7")

        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 691, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar()
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("RegisterWindow", "REGISTER"))
        self.label.setText(_translate("RegisterWindow",
                                      "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\"><u>REGISTRATION FORM</span></p></body></html>"))
        self.label_2.setText(_translate("RegisterWindow",
                                        "<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">Name </span></p></body></html>"))
        self.label_3.setText(_translate("RegisterWindow",
                                        "<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">Register Password</span></p></body></html>"))
        self.label_4.setText(_translate("RegisterWindow",
                                        "<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">Enter Student ID</span></p></body></html>"))
        self.label_5.setText(_translate("RegisterWindow",
                                        "<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">Class</span></p></body></html>"))
        self.label_6.setText(_translate("RegisterWindow",
                                        "<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">Section</span></p></body></html>"))
        self.label_7.setText(_translate("RegisterWindow",
                                        "<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">Roll Number</span></p></body></html>"))
        self.Mlabel.setText(_translate("RegisterWindow",
                                        "<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Enter Admin Password and Data for Registration  :</span></p></body></html>"))
        self.Alabel.setText(_translate("RegisterWindow",
                                        "<html><head/><body><p><span style=\" font-size:11pt; color:#ffffff;\">Admin Password :</span></p></body></html>"))

        self.pic = QPixmap('Images/Register.png')

        self.LabelImg = QLabel(self)
        self.LabelImg.setPixmap(self.pic)
        self.LabelImg.setGeometry(QtCore.QRect(275, 70, 180, 180))

        self.show()

    def ShwSuc(self):
        msgBox = QMessageBox()
        msgBox.setFixedSize(400, 400)
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("User Successfully Registered")
        msgBox.setWindowTitle("SUCCESS")
    
        returnValue = msgBox.exec_()
        if returnValue == QMessageBox.Ok:
            pass

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
        msgBox.setText("Student ID already present in Data")
        msgBox.setWindowTitle("ERROR")
    
        returnValue = msgBox.exec_()
        if returnValue == QMessageBox.Ok:
            pass

    def backend_register(self):
        backend = default_backend()

        key = b"2\xb9(\x88\xd9gz\xdb\x9f};\x96\xf2\xfe\xf2\xa6Kb/V\xde\x00\xbd\xff\xe1\x9a\x1c\xb0\xb2d{M"
        iv = b'\xc62\xb3\x8d\x94z(\xb2\xbc\x13^\x18\r.\x92\xa7'

        def padding(data):
            while len(data) % 16 != 0:
                data = data + " "
            return data

        def encrypt(inp):
            padded_msg = padding(inp).encode()
            cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
            encryptor = cipher.encryptor()
            ct = encryptor.update(padded_msg) + encryptor.finalize()
            b64 = base64.b64encode(ct).decode()
            return b64

        def decrypt(inp):
            backend = default_backend()

            ke = b"2\xb9(\x88\xd9gz\xdb\x9f};\x96\xf2\xfe\xf2\xa6Kb/V\xde\x00\xbd\xff\xe1\x9a\x1c\xb0\xb2d{M"
            i = b'\xc62\xb3\x8d\x94z(\xb2\xbc\x13^\x18\r.\x92\xa7'

            paa = inp.encode()
            b64 = base64.b64decode(paa)
            cipher = Cipher(algorithms.AES(ke), modes.CBC(i), backend=backend)
            decryptor = cipher.decryptor()
            dec = decryptor.update(b64) + decryptor.finalize()
            return dec.rstrip().decode()

        database = mysql.connector.connect(host="localhost", user="root", passwd=MySQLPassword(), database=db())
        cursor = database.cursor()
        AdminCursor = database.cursor()

        AdminCursor.execute(f"SELECT * from login Where NAME = 'ADMIN';")
        fetchAdmin = AdminCursor.fetchall()[0][1]

        STUID = int(self.lineEdit_2.text())

        chkCursor = database.cursor()
        chkCursor.execute(f"Select STUDENT_ID from login where STUDENT_ID = {STUID}")
        chkfetch = chkCursor.fetchall()

        status = ""

        if chkfetch != []:
            status = False

        elif chkfetch == []:
            status = True

        admin = self.Adminline.text()

        pa = decrypt(fetchAdmin)

        if admin == pa:
            if status == True:
                NAME = self.lineEdit.text()
                PASSWORD = encrypt(self.lineEdit2.text())
                CLASS = int(self.lineEdit_3.text())
                SECTION = self.lineEdit_4.text()
                ROLL = int(self.lineEdit_5.text())
                ID = int(self.lineEdit_2.text())

                cursor.execute(f"insert into login VALUES('{NAME}', '{PASSWORD}', {CLASS}, '{SECTION}', {ROLL}, {ID});")

                database.commit()

                self.ShwSuc()

            elif status == False:
                self.ShwError1()
        
        elif admin != pa:
            self.ShwError()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_RegisterWindow()
    sys.exit(app.exec_())