import sys
import mysql.connector

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QShortcut, QMessageBox
from PyQt5.QtWidgets import QRadioButton, QPushButton, QLabel, QLineEdit, QTableWidget

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64

from MySQLPass import MySQLPassword
from MySQL_DB import db


class StudentAlter(QMainWindow):
    def __init__(self):
        super(StudentAlter, self).__init__()

        # USER INTERFACE
        self.setWindowTitle("STUDENT AlTER")
        self.setFixedSize(982, 535)
        self.setStyleSheet("background-color : rgb(34, 34, 34);")

        self.MainLabel = QLabel(self)
        self.MainLabel.setText("UPDATE STUDENT DATA")
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
        self.nameLabel.setGeometry(QtCore.QRect(530, 260, 100, 30))

        self.nameLine = QLineEdit(self)
        self.nameLine.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 11pt \"Cambria\";\n"
                                    "background-color: rgb(74, 74, 74);\n"
                                    "border-radius : 10%")
        self.nameLine.setGeometry(QtCore.QRect(600, 260, 280, 32))

        self.classLabel = QLabel(self)
        self.classLabel.setText("CLASS :")
        self.classLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                      "font: 12pt \"Cambria\";\n"
                                      "color: rgb(255, 255, 255);")
        self.classLabel.setGeometry(QtCore.QRect(120, 310, 90, 30))

        self.classLine = QLineEdit(self)
        self.classLine.setStyleSheet("color: rgb(255, 255, 255);\n"
                                     "font: 11pt \"Cambria\";\n"
                                     "background-color: rgb(74, 74, 74);\n"
                                     "border-radius : 10%")
        self.classLine.setGeometry(QtCore.QRect(210, 310, 260, 30))

        self.secLabel = QLabel(self)
        self.secLabel.setText("SEC :")
        self.secLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                    "font: 12pt \"Cambria\";\n"
                                    "color: rgb(255, 255, 255);")
        self.secLabel.setGeometry(QtCore.QRect(535, 310, 90, 30))

        self.secLine = QLineEdit(self)
        self.secLine.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 11pt \"Cambria\";\n"
                                   "background-color: rgb(74, 74, 74);\n"
                                   "border-radius : 10%")
        self.secLine.setGeometry(QtCore.QRect(600, 310, 280, 32))

        self.rollLabel = QLabel(self)
        self.rollLabel.setText("ROLL NUMBER :")
        self.rollLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                     "font: 12pt \"Cambria\";\n"
                                     "color: rgb(255, 255, 255);")
        self.rollLabel.setGeometry(QtCore.QRect(90, 360, 120, 30))

        self.rollLine = QLineEdit(self)
        self.rollLine.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 11pt \"Cambria\";\n"
                                    "background-color: rgb(74, 74, 74);\n"
                                    "border-radius : 10%")
        self.rollLine.setGeometry(QtCore.QRect(210, 360, 260, 30))

        self.bldLabel = QLabel(self)
        self.bldLabel.setText("BLOOD GROUP :")
        self.bldLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                    "font: 11pt \"Cambria\";\n"
                                    "color: rgb(255, 255, 255);")
        self.bldLabel.setGeometry(QtCore.QRect(490, 360, 120, 30))

        self.bldLine = QLineEdit(self)
        self.bldLine.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 11pt \"Cambria\";\n"
                                   "background-color: rgb(74, 74, 74);\n"
                                   "border-radius : 10%")
        self.bldLine.setGeometry(QtCore.QRect(600, 360, 280, 32))

        self.genderLabel = QLabel(self)
        self.genderLabel.setText("GENDER : ")
        self.genderLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                       "font: 12pt \"Cambria\";\n"
                                       "color: rgb(255, 255, 255);")
        self.genderLabel.setGeometry(QtCore.QRect(115, 260, 220, 30))

        self.mlRadio = QRadioButton(self)
        self.mlRadio.setText("MALE")
        self.mlRadio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "background-color: rgb(34, 34, 34);\n")
        self.mlRadio.setGeometry(QtCore.QRect(240, 260, 60, 32))
        self.mlRadio.setAutoExclusive(False)

        self.fmlRadio = QRadioButton(self)
        self.fmlRadio.setText("FEMALE")
        self.fmlRadio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 12pt \"Cambria\";\n"
                                    "background-color: rgb(34, 34, 34);\n")
        self.fmlRadio.setGeometry(QtCore.QRect(360, 260, 80, 32))
        self.fmlRadio.setAutoExclusive(False)

        self.altPush = QPushButton(self)
        self.altPush.setStyleSheet("background-color: rgb(158, 0, 2);\n"
                                     "border-radius : 20%;\n"
                                     "font: 11pt \"Cambria\";"
                                     "color: rgb(255, 255, 255);")
        self.altPush.setText("UPDATE DATA")
        self.altPush.setGeometry(QtCore.QRect(410, 440, 180, 60))
        self.altPush.clicked.connect(self.backend)

        self.shortcut = QShortcut(QtGui.QKeySequence("Ctrl+e"), self)
        self.shortcut.activated.connect(self.backend)
        
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

        pa = decrypt(fetchAdmin)
        studentID = self.stuLine.text()

        chkCursor = database.cursor()
        chkCursor.execute(f"Select STUDENT_ID from studentinfo where STUDENT_ID = {int(studentID)}")
        chkfetch = chkCursor.fetchall()

        status = ""

        if chkfetch != []:
            status = True

        elif chkfetch == []:
            status = False

        if pa == self.admin:
            if status == True:
                # QUERY MAKING
            
                if studentID == "":
                    ID = " "
                else:
                    ID = f"STUDENT_ID = {int(studentID)}"

                name = self.nameLine.text()
                if name == "":
                    NAME = " "
                else:
                    NAME = f"_NAME_ = '{name}'"

                Class = self.classLine.text()
                if Class == "":
                    CLASS = " "
                else:
                    CLASS = f"CLASS = {int(Class)}"

                Sec = self.secLine.text()
                if Sec == "":
                    SEC = " "
                else:
                    SEC = f"SEC = '{Sec}'"

                Roll = self.rollLine.text()
                if Roll == "":
                    ROLL = " "
                else:
                    ROLL = f"ROLL_NUMBER = {int(Roll)}"
                Blood = self.bldLine.text()
                if Blood == "":
                    BLOOD = " "
                else:
                    BLOOD = f"BLOOD_GROUP = '{Blood}'"

                GENDER = " "

                if self.mlRadio.isChecked():
                    GENDER = "GENDER = 'M'"

                elif self.fmlRadio.isChecked():
                    GENDER = "GENDER = 'F'"

                qu = f"{NAME} , {CLASS} , {SEC} , {ROLL} , {BLOOD} , {GENDER}".replace(" ,  ", "").lstrip(", ")
                execute = f"update studentinfo set {qu} WHERE {ID};"

                if studentID == "" and name == "" and Class == "" and Sec == "" and Roll == "" and Blood == "" and not self.mlRadio.isChecked() and not self.fmlRadio.isChecked():
                    execute = "SELECT * FROM studentinfo ;"

                realData = database.cursor()
                realData.execute(execute)

                database.commit()
                self.ShwSuc()
            
            elif status == False:
                self.ShwERROR()
        
        elif pa != self.admin:
            self.ShwError()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = StudentAlter()
    sys.exit(app.exec_())
