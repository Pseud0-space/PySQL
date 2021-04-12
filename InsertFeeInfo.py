import sys
import mysql.connector

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,  QShortcut, QMessageBox
from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64

from MySQLPass import MySQLPassword
from MySQL_DB import db


class InsertFee(QMainWindow):
    def __init__(self):
        super(InsertFee, self).__init__()

        # USER INTERFACE
        self.setWindowTitle("INSERT FEE DATA")
        self.setFixedSize(982, 535)
        self.setStyleSheet("background-color : rgb(34, 34, 34);")

        self.MainLabel = QLabel(self)
        self.MainLabel.setText("INSERT FEE DATA")
        self.MainLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                     "font: 20pt \"Cambria\";\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "text-decoration: underline;\n")
        self.MainLabel.setGeometry(QtCore.QRect(405, 20, 320, 30))

        self.inLabel = QLabel(self)
        self.inLabel.setText("Enter the ADMIN PASSWORD for inserting new data :")
        self.inLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "color: rgb(255, 255, 255);")
        self.inLabel.setGeometry(QtCore.QRect(100, 100, 480, 30))

        self.passLabel = QLabel(self)
        self.passLabel.setText("ADMIN PASSWORD :")
        self.passLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                    "font: 12pt \"Cambria\";\n"
                                    "color: rgb(255, 255, 255);")
        self.passLabel.setGeometry(QtCore.QRect(100, 140, 160, 30))

        self.passLine = QLineEdit(self)
        self.passLine.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 11pt \"Cambria\";\n"
                                   "background-color: rgb(74, 74, 74);\n"
                                   "border-radius : 10%")
        self.passLine.setGeometry(QtCore.QRect(250, 140, 260, 30))
        self.passLine.setEchoMode(QLineEdit.Password)

        self.outLabel = QLabel(self)
        self.outLabel.setText("Give the required information :")
        self.outLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                    "font: 12pt \"Cambria\";\n"
                                    "color: rgb(255, 255, 255);")
        self.outLabel.setGeometry(QtCore.QRect(100, 220, 350, 30))

        self.nameLabel = QLabel(self)
        self.nameLabel.setText("NAME :")
        self.nameLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                     "font: 12pt \"Cambria\";\n"
                                     "color: rgb(255, 255, 255);")
        self.nameLabel.setGeometry(QtCore.QRect(530, 260, 100, 30))

        self.nameLine = QLineEdit(self)
        self.nameLine.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 11pt \"Cambria\";\n"
                                    "background-color: rgb(74, 74, 74);\n"
                                    "border-radius : 10%")
        self.nameLine.setGeometry(QtCore.QRect(600, 260, 280, 32))

        self.stuLabel = QLabel(self)
        self.stuLabel.setText("STUDENT ID :")
        self.stuLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                      "font: 12pt \"Cambria\";\n"
                                      "color: rgb(255, 255, 255);")
        self.stuLabel.setGeometry(QtCore.QRect(100, 310, 100, 30))

        self.stuLine = QLineEdit(self)
        self.stuLine.setStyleSheet("color: rgb(255, 255, 255);\n"
                                     "font: 11pt \"Cambria\";\n"
                                     "background-color: rgb(74, 74, 74);\n"
                                     "border-radius : 10%")
        self.stuLine.setGeometry(QtCore.QRect(210, 310, 260, 30))

        self.totalLabel = QLabel(self)
        self.totalLabel.setText("TOTAL FEE :")
        self.totalLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                    "font: 12pt \"Cambria\";\n"
                                    "color: rgb(255, 255, 255);")
        self.totalLabel.setGeometry(QtCore.QRect(500, 310, 90, 30))

        self.totalLine = QLineEdit(self)
        self.totalLine.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 11pt \"Cambria\";\n"
                                   "background-color: rgb(74, 74, 74);\n"
                                   "border-radius : 10%")
        self.totalLine.setGeometry(QtCore.QRect(600, 310, 280, 32))

        self.paidLabel = QLabel(self)
        self.paidLabel.setText("FEE PAID :")
        self.paidLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                     "font: 12pt \"Cambria\";\n"
                                     "color: rgb(255, 255, 255);")
        self.paidLabel.setGeometry(QtCore.QRect(110, 360, 120, 30))

        self.paidLine = QLineEdit(self)
        self.paidLine.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 11pt \"Cambria\";\n"
                                    "background-color: rgb(74, 74, 74);\n"
                                    "border-radius : 10%")
        self.paidLine.setGeometry(QtCore.QRect(210, 360, 260, 30))

        self.classLabel = QLabel(self)
        self.classLabel.setText("CLASS :")
        self.classLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                    "font: 11pt \"Cambria\";\n"
                                    "color: rgb(255, 255, 255);")
        self.classLabel.setGeometry(QtCore.QRect(530, 360, 120, 30))

        self.classLine = QLineEdit(self)
        self.classLine.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 11pt \"Cambria\";\n"
                                   "background-color: rgb(74, 74, 74);\n"
                                   "border-radius : 10%")
        self.classLine.setGeometry(QtCore.QRect(600, 360, 280, 32))

        self.feeLabel = QLabel(self)
        self.feeLabel.setText("FEE ID : ")
        self.feeLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                       "font: 12pt \"Cambria\";\n"
                                       "color: rgb(255, 255, 255);")
        self.feeLabel.setGeometry(QtCore.QRect(115, 260, 220, 30))

        self.feeLine = QLineEdit(self)
        self.feeLine.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 11pt \"Cambria\";\n"
                                   "background-color: rgb(74, 74, 74);\n"
                                   "border-radius : 10%")
        self.feeLine.setGeometry(QtCore.QRect(210, 260, 260, 32))

        self.insertPush = QPushButton(self)
        self.insertPush.setStyleSheet("background-color: rgb(158, 0, 2);\n"
                                     "border-radius : 20%;\n"
                                     "font: 11pt \"Cambria\";"
                                     "color: rgb(255, 255, 255);")
        self.insertPush.setText("INSERT DATA")
        self.insertPush.setGeometry(QtCore.QRect(410, 440, 180, 60))
        self.insertPush.clicked.connect(self.backend)

        self.shortcut = QShortcut(QtGui.QKeySequence("Ctrl+e"), self)
        self.shortcut.activated.connect(self.backend)
        
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
        msgBox.setText("FEE ID Already Present in Data")
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
        feeID = int(self.feeLine.text())
        
        chkCursor = database.cursor()
        chkCursor.execute(f"Select STUDENT_ID from feeinfo where FEE_ID = {feeID}")
        chkfetch = chkCursor.fetchall()

        status = ""

        if chkfetch != []:
            status = False

        elif chkfetch == []:
            status = True

        if status == True:
            if pa == self.admin:
                stuID = int(self.stuLine.text())
                name = self.nameLine.text()
                total = float(self.totalLine.text())
                paid = float(self.paidLine.text())
                Class =  self.classLine.text()
                feeDue = total - paid

                qu = f"insert into feeinfo VALUES({stuID}, {feeID}, '{name}', {total}, {paid}, {feeDue}, '{Class}');"
                cursor = database.cursor()
                cursor.execute(qu)
                database.commit()

                self.ShwSuc()
            
            elif pa != self.admin:
                self.ShwError()
        
        elif status == False:
            self.ShwError1()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = InsertFee()
    sys.exit(app.exec_())