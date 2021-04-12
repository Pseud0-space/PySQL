from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication

import sys
import mysql.connector

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64

from MySQLPass import MySQLPassword
from MySQL_DB import db


class ChangePass(QMainWindow):
    def __init__(self):
        super(ChangePass, self).__init__()

        self.setWindowTitle("CHANGE PASSWORD")
        self.setFixedSize(750, 340)
        self.setStyleSheet("background-color: rgb(34, 34, 34);")

        self.title = QLabel(self)
        self.title.setText(
            "<html><body><p><span style = \" font-size:16pt; color:#ffffff;\"><u> CHANGE PASSWORD </span></p></body></html>")
        self.title.setGeometry(QtCore.QRect(290, 15, 200, 60))

        self.OldTitle = QLabel(self)
        self.OldTitle.setText(
            "<html><body><p><span style = \" font-size:11pt; color:#ffffff;\">Enter Old Password</span></p></body></html>")
        self.OldTitle.setGeometry(QtCore.QRect(250, 100, 200, 60))

        self.OldPass = QLineEdit(self)
        self.OldPass.setEchoMode(QLineEdit.Password)
        self.OldPass.setStyleSheet("color : rgb(255, 255, 255); \n"
                                   "font: 11pt \"Cambria\";\n"
                                   "background-color : rgb(74, 74, 74); \n"
                                   "border-radius : 10%;")
        self.OldPass.setGeometry(QtCore.QRect(400, 115, 280, 30))

        self.NewTitle = QLabel(self)
        self.NewTitle.setText(
            "<html><body><p><span style = \" font-size:11pt; color:#ffffff;\">Enter New Password</span></p></body></html>")
        self.NewTitle.setGeometry(QtCore.QRect(250, 160, 200, 60))

        self.NewPass = QLineEdit(self)
        self.NewPass.setStyleSheet("color : rgb(255, 255, 255); \n"
                                   "font: 12pt \"Cambria\";\n"
                                   "background-color : rgb(74, 74, 74); \n"
                                   "border-radius : 10%;")
        self.NewPass.setGeometry(QtCore.QRect(400, 175, 280, 30))

        self.ButtonChange = QPushButton(self)
        self.ButtonChange.setStyleSheet("background-color: rgb(158, 0, 2);\n"
                                        "border-radius : 20%;\n"
                                        "font: 10pt \"Cambria\";"
                                        "color : rgb(255, 255, 255)")
        self.ButtonChange.setText("CHANGE")
        self.ButtonChange.setGeometry(QtCore.QRect(380, 240, 180, 60))
        self.ButtonChange.clicked.connect(self.backend)

        self.pic = QPixmap('Images/ChangePassword.png')

        self.LabelImg = QLabel(self)
        self.LabelImg.setPixmap(self.pic)
        self.LabelImg.setGeometry(QtCore.QRect(50, 80, 170, 170))

        self.show()

    def ShwError(self):
        msgBox = QMessageBox()
        msgBox.setFixedSize(400, 400)
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setText("Invalid User Password")
        msgBox.setWindowTitle("ERROR")
    
        returnValue = msgBox.exec_()
        if returnValue == QMessageBox.Ok:
            pass

    def ShwAccept(self):
        msgBox = QMessageBox()
        msgBox.setFixedSize(400, 400)
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Password changed successfully")
        msgBox.setWindowTitle("SUCCESS")
    
        returnValue = msgBox.exec_()
        if returnValue == QMessageBox.Ok:
            pass
    def backend(self):
        backend = default_backend()

        key = b"2\xb9(\x88\xd9gz\xdb\x9f};\x96\xf2\xfe\xf2\xa6Kb/V\xde\x00\xbd\xff\xe1\x9a\x1c\xb0\xb2d{M"
        iv = b'\xc62\xb3\x8d\x94z(\xb2\xbc\x13^\x18\r.\x92\xa7'

        def padding(data):
            while len(data) % 16 != 0:
                data = data + " "
            return data

        def decrypt(inp):
            paa = inp.encode()
            b64 = base64.b64decode(paa)
            cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
            decryptor = cipher.decryptor()
            dec = decryptor.update(b64) + decryptor.finalize()
            return dec.rstrip().decode()

        def encrypt(inp):
            padded_msg = padding(inp).encode()
            cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
            encryptor = cipher.encryptor()
            ct = encryptor.update(padded_msg) + encryptor.finalize()
            b64 = base64.b64encode(ct).decode()
            return b64

        database = mysql.connector.connect(host="localhost", user="root", passwd=MySQLPassword(), database=db())
        CountCursor = database.cursor()

        old = self.OldPass.text()

        AllCursor = database.cursor()
        AllCursor.execute(f"SELECT PASSWORD from login;")

        dat = AllCursor.fetchall()

        cnt = 0

        for data in dat:
            decPass = decrypt(data[0])
            if decPass != old:
                cnt += 0
                    
            elif decPass == old:
                cnt += 1

        if cnt == 1:
            for data in dat:
                decPass = decrypt(data[0])
                
                if decPass == old:
                    newEnc = encrypt(self.NewPass.text())  # new encrypted pass
                    oldPass = encrypt(decPass)  # old encrypted pass

                    c = database.cursor()
                    c.execute(f"update login set PASSWORD = '{newEnc}' WHERE PASSWORD = '{oldPass}';")

                    database.commit()
                    self.ShwAccept()
        
        elif cnt == 0:
            self.ShwError()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = ChangePass()
    sys.exit(app.exec_())