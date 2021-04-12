import sys
import mysql.connector

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtWidgets import QRadioButton, QPushButton, QLabel, QLineEdit

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64

from MySQLPass import MySQLPassword
from MySQL_DB import db


class InsertSubjectInfo(QMainWindow):
    def __init__(self):
        super(InsertSubjectInfo, self).__init__()

        # USER INTERFACE
        self.setWindowTitle("ADD SUBJECT INFORMATION")
        self.setFixedSize(980, 550)
        self.setStyleSheet("background-color : rgb(34, 34, 34);")

        self.MainLabel = QLabel(self)
        self.MainLabel.setText("INSERT SUBJECT INFORMATION")
        self.MainLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                     "font: 18pt \"Cambria\";\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "text-decoration: underline;\n")
        self.MainLabel.setGeometry(QtCore.QRect(350, 20, 380, 30))

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

        self.crtLabel = QLabel(self)
        self.crtLabel.setText("Enter Name, Student ID and select the opted subjects : ")
        self.crtLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                     "font: 13pt \"Cambria\";\n"
                                     "color: rgb(255, 255, 255);\n")
        self.crtLabel.setGeometry(QtCore.QRect(90, 175, 420, 30))

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

        self.chemistryRadio = QRadioButton(self)
        self.chemistryRadio.setText("CHEMISTRY")
        self.chemistryRadio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "background-color: rgb(34, 34, 34);\n")
        self.chemistryRadio.setGeometry(QtCore.QRect(100, 260, 100, 32))
        self.chemistryRadio.setAutoExclusive(False)

        self.englishRadio = QRadioButton(self)
        self.englishRadio.setText("ENGLISH")
        self.englishRadio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "background-color: rgb(34, 34, 34);\n")
        self.englishRadio.setGeometry(QtCore.QRect(240, 260, 100, 32))
        self.englishRadio.setAutoExclusive(False)

        self.biologyRadio = QRadioButton(self)
        self.biologyRadio.setText("BIOLOGY")
        self.biologyRadio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "background-color: rgb(34, 34, 34);\n")
        self.biologyRadio.setGeometry(QtCore.QRect(370, 260, 100, 32))
        self.biologyRadio.setAutoExclusive(False)

        self.historyRadio = QRadioButton(self)
        self.historyRadio.setText("HISTORY")
        self.historyRadio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "background-color: rgb(34, 34, 34);\n")
        self.historyRadio.setGeometry(QtCore.QRect(495, 260, 100, 32))
        self.historyRadio.setAutoExclusive(False)

        self.economicsRadio = QRadioButton(self)
        self.economicsRadio.setText("ECONOMICS")
        self.economicsRadio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "background-color: rgb(34, 34, 34);\n")
        self.economicsRadio.setGeometry(QtCore.QRect(615, 260, 110, 32))
        self.economicsRadio.setAutoExclusive(False)

        self.geoRadio = QRadioButton(self)
        self.geoRadio.setText("GEOGRAPHY")
        self.geoRadio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "background-color: rgb(34, 34, 34);\n")
        self.geoRadio.setGeometry(QtCore.QRect(760, 260, 110, 32))
        self.geoRadio.setAutoExclusive(False)

        self.socioRadio = QRadioButton(self)
        self.socioRadio.setText("SOCIOLOGY")
        self.socioRadio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "background-color: rgb(34, 34, 34);\n")
        self.socioRadio.setGeometry(QtCore.QRect(100, 300, 130, 32))
        self.socioRadio.setAutoExclusive(False)

        self.physicsRadio = QRadioButton(self)
        self.physicsRadio.setText("PHYSICS")
        self.physicsRadio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "background-color: rgb(34, 34, 34);\n")
        self.physicsRadio.setGeometry(QtCore.QRect(240, 300, 100, 32))
        self.physicsRadio.setAutoExclusive(False)

        self.paintRadio = QRadioButton(self)
        self.paintRadio.setText("PAINTING")
        self.paintRadio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "background-color: rgb(34, 34, 34);\n")
        self.paintRadio.setGeometry(QtCore.QRect(370, 300, 100, 32))
        self.paintRadio.setAutoExclusive(False)

        self.polscRadio = QRadioButton(self)
        self.polscRadio.setText("POLITICAL SCIENCE")
        self.polscRadio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "background-color: rgb(34, 34, 34);\n")
        self.polscRadio.setGeometry(QtCore.QRect(500, 300, 180, 32))
        self.polscRadio.setAutoExclusive(False)

        self.compRadio = QRadioButton(self)
        self.compRadio.setText("COMPUTER SCIENCE")
        self.compRadio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "background-color: rgb(34, 34, 34);\n")
        self.compRadio.setGeometry(QtCore.QRect(700, 300, 180, 32))
        self.compRadio.setAutoExclusive(False)

        self.busRadio = QRadioButton(self)
        self.busRadio.setText("BUSINESS STUDIES")
        self.busRadio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "background-color: rgb(34, 34, 34);\n")
        self.busRadio.setGeometry(QtCore.QRect(135, 340, 180, 32))
        self.busRadio.setAutoExclusive(False)

        self.peRadio = QRadioButton(self)
        self.peRadio.setText("PHYSICAL EDUCATION")
        self.peRadio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "background-color: rgb(34, 34, 34);\n")
        self.peRadio.setGeometry(QtCore.QRect(320, 340, 180, 32))
        self.peRadio.setAutoExclusive(False)

        self.mathRadio = QRadioButton(self)
        self.mathRadio.setText("MATHEMATICS")
        self.mathRadio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "background-color: rgb(34, 34, 34);\n")
        self.mathRadio.setGeometry(QtCore.QRect(530, 340, 180, 32))
        self.mathRadio.setAutoExclusive(False)

        self.homeRadio = QRadioButton(self)
        self.homeRadio.setText("HOME SCIENCE")
        self.homeRadio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "background-color: rgb(34, 34, 34);\n")
        self.homeRadio.setGeometry(QtCore.QRect(690, 340, 180, 32))
        self.homeRadio.setAutoExclusive(False)

        self.psyRadio = QRadioButton(self)
        self.psyRadio.setText("PSYCHOLOGY")
        self.psyRadio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "background-color: rgb(34, 34, 34);\n")
        self.psyRadio.setGeometry(QtCore.QRect(520, 380, 180, 32))
        self.psyRadio.setAutoExclusive(False)

        self.accRadio = QRadioButton(self)
        self.accRadio.setText("ACCOUNTANCY")
        self.accRadio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "background-color: rgb(34, 34, 34);\n")
        self.accRadio.setGeometry(QtCore.QRect(360, 380, 130, 32))
        self.accRadio.setAutoExclusive(False)

        self.insertPush = QPushButton(self)
        self.insertPush.setStyleSheet("background-color: rgb(158, 0, 2);\n"
                                     "border-radius : 20%;\n"
                                     "font: 11pt \"Cambria\";"
                                     "color: rgb(255, 255, 255);")
        self.insertPush.setText("INSERT DATA")
        self.insertPush.setGeometry(QtCore.QRect(400, 450, 180, 60))
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
        
        chkCursor = database.cursor()
        chkCursor.execute(f"Select STUDENT_ID from subjectinfo where STUDENT_ID = {StuID}")
        chkfetch = chkCursor.fetchall()

        status = ""

        if chkfetch != []:
            status = False

        elif chkfetch == []:
            status = True
        
        if status == True:
            if pa == self.admin:
                studentID = self.stuLine.text()
                ID = int(studentID)

                name = self.nameLine.text()
                NAME = name

                if self.chemistryRadio.isChecked():
                    CHE = "OPTED"
                else:
                    CHE = "--"
                
                if self.englishRadio.isChecked():
                    ENGL = "OPTED"
                else:
                    ENGL = "--"

                if self.biologyRadio.isChecked():
                    BIO = "OPTED"
                else:
                    BIO = "--"

                if self.historyRadio.isChecked():
                    HIS = "OPTED"
                else:
                    HIS = "--"

                if self.economicsRadio.isChecked():
                    ECO = "OPTED"
                else:
                    ECO = "--"

                if self.geoRadio.isChecked():
                    GEO = "OPTED"
                else:
                    GEO = "--"

                if self.socioRadio.isChecked():
                    SOCIO = "OPTED"
                else:
                    SOCIO = "--"

                if self.physicsRadio.isChecked():
                    PHY = "OPTED"
                else:
                    PHY = "--"

                if self.paintRadio.isChecked():
                    PAINT = "OPTED"
                else:
                    PAINT = "--"

                if self.polscRadio.isChecked():
                    POLSC = "OPTED"
                else:
                    POLSC = "--"

                if self.compRadio.isChecked():
                    COMP = "OPTED"
                else:
                    COMP = "--"

                if self.busRadio.isChecked():
                    BUS = "OPTED"
                else:
                    BUS = "--"

                if self.peRadio.isChecked():
                    PE = "OPTED"
                else:
                    PE = "--"

                if self.mathRadio.isChecked():
                    MATH = "OPTED"
                else:
                    MATH = "--"

                if self.homeRadio.isChecked():
                    HOME = "OPTED"
                else:
                    HOME = "--"

                if self.psyRadio.isChecked():
                    PSY = "OPTED"
                else:
                    PSY = "--"

                if self.accRadio.isChecked():
                    ACC = "OPTED"
                else:
                    ACC = "--"

                qu = f"insert into subjectinfo VALUES({ID}, '{NAME}', '{CHE}', '{ENGL}', '{BIO}', '{HIS}', '{ECO}', '{GEO}', '{SOCIO}', '{PHY}', '{PAINT}', '{POLSC}', '{COMP}', '{BUS}', '{PE}', '{MATH}', '{HOME}', '{PSY}', '{ACC}');"
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
    ui = InsertSubjectInfo()
    sys.exit(app.exec_())