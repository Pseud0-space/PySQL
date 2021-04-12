import sys
import mysql.connector

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QShortcut, QTextEdit, QMessageBox
from PyQt5.QtWidgets import QRadioButton, QPushButton, QLabel, QLineEdit, QTableWidget

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64

from MySQLPass import MySQLPassword
from MySQL_DB import db


class PersonalAlter(QMainWindow):
    def __init__(self):
        super(PersonalAlter, self).__init__()

        # USER INTERFACE
        self.setWindowTitle("PERSONAL AlTER")
        self.setFixedSize(982, 600)
        self.setStyleSheet("background-color : rgb(34, 34, 34);")

        self.MainLabel = QLabel(self)
        self.MainLabel.setText("UPDATE PERSONAL DATA")
        self.MainLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                     "font: 20pt \"Cambria\";\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "text-decoration: underline;\n")
        self.MainLabel.setGeometry(QtCore.QRect(370, 20, 320, 30))

        self.inLabel = QLabel(self)
        self.inLabel.setText("Enter the following for updating data :")
        self.inLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "color: rgb(255, 255, 255);")
        self.inLabel.setGeometry(QtCore.QRect(100, 80, 480, 30))

        self.passLabel = QLabel(self)
        self.passLabel.setText("ADMIN PASSWORD :")
        self.passLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                    "font: 12pt \"Cambria\";\n"
                                    "color: rgb(255, 255, 255);")
        self.passLabel.setGeometry(QtCore.QRect(100, 125, 160, 30))

        self.passLine = QLineEdit(self)
        self.passLine.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 11pt \"Cambria\";\n"
                                   "background-color: rgb(74, 74, 74);\n"
                                   "border-radius : 10%")
        self.passLine.setGeometry(QtCore.QRect(250, 125, 260, 30))
        self.passLine.setEchoMode(QLineEdit.Password)

        self.stuLabel = QLabel(self)
        self.stuLabel.setText("STUDENT ID :")
        self.stuLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                    "font: 12pt \"Cambria\";\n"
                                    "color: rgb(255, 255, 255);")
        self.stuLabel.setGeometry(QtCore.QRect(120, 165, 120, 30))

        self.stuLine = QLineEdit(self)
        self.stuLine.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 11pt \"Cambria\";\n"
                                   "background-color: rgb(74, 74, 74);\n"
                                   "border-radius : 10%")
        self.stuLine.setGeometry(QtCore.QRect(250, 165, 260, 30))

        self.outLabel = QLabel(self)
        self.outLabel.setText("Criteria available for update :")
        self.outLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                    "font: 12pt \"Cambria\";\n"
                                    "color: rgb(255, 255, 255);")
        self.outLabel.setGeometry(QtCore.QRect(100, 220, 350, 30))

        self.nameLabel = QLabel(self)
        self.nameLabel.setText("NAME :")
        self.nameLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                     "font: 12pt \"Cambria\";\n"
                                     "color: rgb(255, 255, 255);")
        self.nameLabel.setGeometry(QtCore.QRect(520, 310, 100, 30))

        self.nameLine = QLineEdit(self)
        self.nameLine.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 11pt \"Cambria\";\n"
                                    "background-color: rgb(74, 74, 74);\n"
                                    "border-radius : 10%")
        self.nameLine.setGeometry(QtCore.QRect(600, 310, 280, 32))

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
        self.ageLabel.setGeometry(QtCore.QRect(130, 310, 90, 30))

        self.ageLine = QLineEdit(self)
        self.ageLine.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 11pt \"Cambria\";\n"
                                    "background-color: rgb(74, 74, 74);\n"
                                    "border-radius : 10%")
        self.ageLine.setGeometry(QtCore.QRect(210, 310, 260, 30))

        self.pnumberLabel = QLabel(self)
        self.pnumberLabel.setText("PHONE NO. :")
        self.pnumberLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                    "font: 11pt \"Cambria\";\n"
                                    "color: rgb(255, 255, 255);")
        self.pnumberLabel.setGeometry(QtCore.QRect(300, 360, 140, 30))

        self.pnumberLine = QLineEdit(self)
        self.pnumberLine.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 11pt \"Cambria\";\n"
                                   "background-color: rgb(74, 74, 74);\n"
                                   "border-radius : 10%")
        self.pnumberLine.setGeometry(QtCore.QRect(400, 360, 280, 32))

        self.addrLabel = QLabel(self)
        self.addrLabel.setText("ADDRESS :")
        self.addrLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                     "font: 12pt \"Cambria\";\n"
                                     "color: rgb(255, 255, 255);")
        self.addrLabel.setGeometry(QtCore.QRect(100, 420, 90, 30))

        self.addrEdit = QTextEdit(self)
        self.addrEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 11pt \"Cambria\";\n"
                                    "background-color: rgb(74, 74, 74);\n"
                                    "border-radius : 10%")
        self.addrEdit.setGeometry(QtCore.QRect(210, 420, 670, 70))

        self.alterPush = QPushButton(self)
        self.alterPush.setStyleSheet("background-color: rgb(158, 0, 2);\n"
                                     "border-radius : 20%;\n"
                                     "font: 11pt \"Cambria\";"
                                     "color: rgb(255, 255, 255);")
        self.alterPush.setText("UPDATE DATA")
        self.alterPush.setGeometry(QtCore.QRect(410, 520, 180, 60))
        self.alterPush.clicked.connect(self.backend)

        self.show()

    def ShwSuc(self):
        msgBox = QMessageBox()
        msgBox.setFixedSize(400, 400)
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Data Updated Successfully")
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

    def ShwAddr(self):
        msgBox = QMessageBox()
        msgBox.setFixedSize(400, 400)
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setText("ADDRESS word max limit 255")
        msgBox.setWindowTitle("ERROR")
    
        returnValue = msgBox.exec_()
        if returnValue == QMessageBox.Ok:
            pass
    
    def ShwERROR(self):
        msgBox = QMessageBox()
        msgBox.setFixedSize(400, 400)
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setText("STUDENT ID not found")
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

        ID  = int(self.stuLine.text())

        chkCursor = database.cursor()
        chkCursor.execute(f"Select STUDENT_ID from personalinfo where STUDENT_ID = {ID}")
        chkfetch = chkCursor.fetchall()

        status = ""

        if chkfetch != []:
            status = True

        elif chkfetch == []:
            status = False

        pa = decrypt(fetchAdmin)

        lenchk = len(self.addrEdit.toPlainText())

        if pa == self.admin:
            if status ==  True:
                if lenchk <= 255:
                    name = self.nameLine.text()
                    if name == "":
                        NAME = " "
                    else:
                        NAME = f"NAME = '{name}'"

                    fname = self.fnameLine.text()
                    if fname == "":
                        FNAME = " "
                    else:
                        FNAME = f"FATHER_NAME = '{fname}'"

                    mname = self.mnameLine.text()
                    if mname == "":
                        MNAME = " "
                    else:
                        MNAME = f"MOTHER_NAME = '{mname}'"

                    Age = self.ageLine.text()
                    if Age == "":
                        AGE = " "
                    else:
                        AGE = f"AGE = {int(Age)}"

                    Addr = self.addrEdit.toPlainText()
                    if Addr == "":
                        ADDR = " "
                    else:
                        ADDR = f"ADDRESS = '{Addr}'"

                    PNumber = self.pnumberLine.text()
                    if PNumber == "":
                        PNUMBER = " "
                    else:
                        PNUMBER = f"PHONE_NUMBER = '{PNumber}'"

                    qu = f"{NAME} , {FNAME} , {MNAME} , {AGE} , {ADDR} , {PNUMBER}".replace(" ,  ", "").lstrip(", ")
                    execute = f"update personalInfo set {qu} WHERE {ID};"

                    realData = database.cursor()
                    realData.execute(execute)

                    database.commit()
                    self.ShwSuc()

                elif lenchk > 255:
                    self.ShwAddr()
            
            elif status == False:
                self.ShwERROR()

        elif pa != self.admin:
            self.ShwError()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = PersonalAlter()
    sys.exit(app.exec_())