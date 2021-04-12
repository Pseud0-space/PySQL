import sys
import mysql.connector

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,  QMessageBox
from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit, QTextEdit

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64

from MySQLPass import MySQLPassword
from MySQL_DB import db


class InsertPersonalInfo(QMainWindow):
    def __init__(self):
        super(InsertPersonalInfo, self).__init__()

        # USER INTERFACE
        self.setWindowTitle("ADD PERSONAL INFORMATION")
        self.setFixedSize(980, 560)
        self.setStyleSheet("background-color : rgb(34, 34, 34);")

        self.MainLabel = QLabel(self)
        self.MainLabel.setText("INSERT PERSONAL INFORMATION")
        self.MainLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                     "font: 18pt \"Cambria\";\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "text-decoration: underline;\n")
        self.MainLabel.setGeometry(QtCore.QRect(330, 20, 380, 30))

        self.inLabel = QLabel(self)
        self.inLabel.setText("Enter the ADMIN PASSWORD for inserting new data :")
        self.inLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "color: rgb(255, 255, 255);")
        self.inLabel.setGeometry(QtCore.QRect(100, 80, 480, 30))

        self.passLabel = QLabel(self)
        self.passLabel.setText("ADMIN PASSWORD :")
        self.passLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                    "font: 12pt \"Cambria\";\n"
                                    "color: rgb(255, 255, 255);")
        self.passLabel.setGeometry(QtCore.QRect(100, 120, 160, 30))

        self.passLine = QLineEdit(self)
        self.passLine.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 11pt \"Cambria\";\n"
                                   "background-color: rgb(74, 74, 74);\n"
                                   "border-radius : 10%")
        self.passLine.setGeometry(QtCore.QRect(250, 120, 260, 30))
        self.passLine.setEchoMode(QLineEdit.Password)

        self.outLabel = QLabel(self)
        self.outLabel.setText("Give the following information :")
        self.outLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                    "font: 12pt \"Cambria\";\n"
                                    "color: rgb(255, 255, 255);")
        self.outLabel.setGeometry(QtCore.QRect(100, 180, 350, 30))

        self.stuLabel = QLabel(self)
        self.stuLabel.setText("STUDENT ID :")
        self.stuLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                    "font: 12pt \"Cambria\";\n"
                                    "color: rgb(255, 255, 255);")
        self.stuLabel.setGeometry(QtCore.QRect(100, 220, 120, 30))

        self.stuLine = QLineEdit(self)
        self.stuLine.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 11pt \"Cambria\";\n"
                                   "background-color: rgb(74, 74, 74);\n"
                                   "border-radius : 10%")
        self.stuLine.setGeometry(QtCore.QRect(210, 220, 260, 30))
        self.nameLabel = QLabel(self)
        self.nameLabel.setText("NAME :")
        self.nameLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                     "font: 12pt \"Cambria\";\n"
                                     "color: rgb(255, 255, 255);")
        self.nameLabel.setGeometry(QtCore.QRect(530, 220, 100, 30))

        self.nameLine = QLineEdit(self)
        self.nameLine.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 11pt \"Cambria\";\n"
                                    "background-color: rgb(74, 74, 74);\n"
                                    "border-radius : 10%")
        self.nameLine.setGeometry(QtCore.QRect(600, 220, 280, 32))

        self.fnameLabel = QLabel(self)
        self.fnameLabel.setText("FATHER'S NAME :")
        self.fnameLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                      "font: 10pt \"Cambria\";\n"
                                      "color: rgb(255, 255, 255);")
        self.fnameLabel.setGeometry(QtCore.QRect(100, 270, 140, 30))

        self.fnameLine = QLineEdit(self)
        self.fnameLine.setStyleSheet("color: rgb(255, 255, 255);\n"
                                     "font: 11pt \"Cambria\";\n"
                                     "background-color: rgb(74, 74, 74);\n"
                                     "border-radius : 10%")
        self.fnameLine.setGeometry(QtCore.QRect(210, 270, 260, 30))

        self.mnameLabel = QLabel(self)
        self.mnameLabel.setText("MOTHER'S NAME :")
        self.mnameLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                    "font: 10pt \"Cambria\";\n"
                                    "color: rgb(255, 255, 255);")
        self.mnameLabel.setGeometry(QtCore.QRect(490, 270, 140, 30))

        self.mnameLine = QLineEdit(self)
        self.mnameLine.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 11pt \"Cambria\";\n"
                                   "background-color: rgb(74, 74, 74);\n"
                                   "border-radius : 10%")
        self.mnameLine.setGeometry(QtCore.QRect(600, 270, 280, 32))

        self.ageLabel = QLabel(self)
        self.ageLabel.setText("AGE :")
        self.ageLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                     "font: 12pt \"Cambria\";\n"
                                     "color: rgb(255, 255, 255);")
        self.ageLabel.setGeometry(QtCore.QRect(140, 320, 90, 30))

        self.ageLine = QLineEdit(self)
        self.ageLine.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 11pt \"Cambria\";\n"
                                    "background-color: rgb(74, 74, 74);\n"
                                    "border-radius : 10%")
        self.ageLine.setGeometry(QtCore.QRect(210, 320, 260, 30))

        self.pnumberLabel = QLabel(self)
        self.pnumberLabel.setText("PHONE NO. :")
        self.pnumberLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                    "font: 11pt \"Cambria\";\n"
                                    "color: rgb(255, 255, 255);")
        self.pnumberLabel.setGeometry(QtCore.QRect(500, 320, 140, 30))

        self.pnumberLine = QLineEdit(self)
        self.pnumberLine.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 11pt \"Cambria\";\n"
                                   "background-color: rgb(74, 74, 74);\n"
                                   "border-radius : 10%")
        self.pnumberLine.setGeometry(QtCore.QRect(600, 320, 280, 32))

        self.addrLabel = QLabel(self)
        self.addrLabel.setText("ADDRESS :")
        self.addrLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                     "font: 12pt \"Cambria\";\n"
                                     "color: rgb(255, 255, 255);")
        self.addrLabel.setGeometry(QtCore.QRect(100, 370, 90, 30))

        self.addrEdit = QTextEdit(self)
        self.addrEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 11pt \"Cambria\";\n"
                                    "background-color: rgb(74, 74, 74);\n"
                                    "border-radius : 10%")
        self.addrEdit.setGeometry(QtCore.QRect(210, 370, 670, 70))

        self.insertPush = QPushButton(self)
        self.insertPush.setStyleSheet("background-color: rgb(158, 0, 2);\n"
                                     "border-radius : 20%;\n"
                                     "font: 11pt \"Cambria\";"
                                     "color: rgb(255, 255, 255);")
        self.insertPush.setText("INSERT DATA")
        self.insertPush.setGeometry(QtCore.QRect(420, 470, 180, 60))
        self.insertPush.clicked.connect(self.backend)

        self.show()

    def ShwSuc(self):
        msgBox = QMessageBox()
        msgBox.setFixedSize(400, 400)
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Data Inserted Successfully")
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
    
    def ShwAddr(self):
        msgBox = QMessageBox()
        msgBox.setFixedSize(400, 400)
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setText("ADDRESS word max limit 255")
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
        
        self.admin = self.passLine.text()

        database = mysql.connector.connect(host="localhost", user="root", passwd=MySQLPassword(), database=db())
        AdminCursor = database.cursor()

        AdminCursor.execute(f"SELECT * from login Where NAME = 'ADMIN';")
        fetchAdmin = AdminCursor.fetchall()[0][1]

        pa = decrypt(fetchAdmin)
        StuID = int(self.stuLine.text())

        lenchk = len(self.addrEdit.toPlainText())
        
        chkCursor = database.cursor()
        chkCursor.execute(f"Select STUDENT_ID from personalinfo where STUDENT_ID = {StuID}")
        chkfetch = chkCursor.fetchall()

        status = ""

        if chkfetch != []:
            status = False

        elif chkfetch == []:
            status = True

        if status == True:
            if pa == self.admin:
                if lenchk <= 255:
                    stuID = int(self.stuLine.text())
                    name = self.nameLine.text()
                    fname = self.fnameLine.text()
                    mname = self.mnameLine.text()
                    age = int(self.ageLine.text())
                    addr = self.addrEdit.toPlainText()
                    pnumber  = self.pnumberLine.text()

                    qu = f"insert into personalinfo VALUES({stuID}, '{name}', '{fname}', '{mname}', {age}, '{addr}', '{pnumber}');"
                    cursor = database.cursor()
                    cursor.execute(qu)
                    database.commit()

                    self.ShwSuc()
                
                elif lenchk > 255:
                    self.ShwAddr()
            
            elif pa != self.admin:
                self.ShwError()
        
        elif status == False:
            self.ShwError1()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = InsertPersonalInfo()
    sys.exit(app.exec_())