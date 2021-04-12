import sys
import mysql.connector

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,  QShortcut, QMessageBox
from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit, QRadioButton

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64

from MySQLPass import MySQLPassword
from MySQL_DB import db


class UpdateSubject(QMainWindow):
    def __init__(self):
        super(UpdateSubject, self).__init__()
        self.setWindowTitle("UPDATE SUBJECT DATA")
        self.setFixedSize(982, 630)
        self.setStyleSheet("background-color : rgb(34, 34, 34);")

        self.MainLabel = QLabel(self)
        self.MainLabel.setText("UPDATE SUBJECT DATA")
        self.MainLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                     "font: 18pt \"Cambria\";\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "text-decoration: underline;\n")
        self.MainLabel.setGeometry(QtCore.QRect(390, 20, 320, 30))

        self.inLabel = QLabel(self)
        self.inLabel.setText("Enter the Following for Updating data :")
        self.inLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "color: rgb(255, 255, 255);")
        self.inLabel.setGeometry(QtCore.QRect(100, 90, 480, 30))

        self.passLabel = QLabel(self)
        self.passLabel.setText("ADMIN PASSWORD :")
        self.passLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                    "font: 12pt \"Cambria\";\n"
                                    "color: rgb(255, 255, 255);")
        self.passLabel.setGeometry(QtCore.QRect(100, 130, 160, 30))

        self.passLine = QLineEdit(self)
        self.passLine.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 11pt \"Cambria\";\n"
                                   "background-color: rgb(74, 74, 74);\n"
                                   "border-radius : 10%")
        self.passLine.setGeometry(QtCore.QRect(250, 130, 260, 30))
        self.passLine.setEchoMode(QLineEdit.Password)

        self.stuLabel = QLabel(self)
        self.stuLabel.setText("STUDENT ID :")
        self.stuLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                    "font: 12pt \"Cambria\";\n"
                                    "color: rgb(255, 255, 255);")
        self.stuLabel.setGeometry(QtCore.QRect(120, 170, 120, 30))

        self.stuLine = QLineEdit(self)
        self.stuLine.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 11pt \"Cambria\";\n"
                                   "background-color: rgb(74, 74, 74);\n"
                                   "border-radius : 10%")
        self.stuLine.setGeometry(QtCore.QRect(250, 170, 260, 30))

        self.outLabel = QLabel(self)
        self.outLabel.setText("Criterias available for update :")
        self.outLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                    "font: 13pt \"Cambria\";\n"
                                    "color: rgb(255, 255, 255);")
        self.outLabel.setGeometry(QtCore.QRect(100, 230, 350, 30))

        self.optRadio = QRadioButton(self)
        self.optRadio.setText("OPTED")
        self.optRadio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "background-color: rgb(34, 34, 34);\n")
        self.optRadio.setGeometry(QtCore.QRect(160, 260, 180, 32))

        self.notoptRadio = QRadioButton(self)
        self.notoptRadio.setText("DID NOT OPT")
        self.notoptRadio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "background-color: rgb(34, 34, 34);\n")
        self.notoptRadio.setGeometry(QtCore.QRect(320, 260, 180, 32))

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

        self.subLabel = QLabel(self)
        self.subLabel.setText("Subjects available for update :")
        self.subLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                    "font: 13pt \"Cambria\";\n"
                                    "color: rgb(255, 255, 255);")
        self.subLabel.setGeometry(QtCore.QRect(100, 310, 350, 30))

        self.chemistryRadio = QRadioButton(self)
        self.chemistryRadio.setText("CHEMISTRY")
        self.chemistryRadio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "background-color: rgb(34, 34, 34);\n")
        self.chemistryRadio.setGeometry(QtCore.QRect(100, 355, 100, 32))
        self.chemistryRadio.setAutoExclusive(False)

        self.englishRadio = QRadioButton(self)
        self.englishRadio.setText("ENGLISH")
        self.englishRadio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "background-color: rgb(34, 34, 34);\n")
        self.englishRadio.setGeometry(QtCore.QRect(240, 355, 100, 32))
        self.englishRadio.setAutoExclusive(False)

        self.biologyRadio = QRadioButton(self)
        self.biologyRadio.setText("BIOLOGY")
        self.biologyRadio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "background-color: rgb(34, 34, 34);\n")
        self.biologyRadio.setGeometry(QtCore.QRect(370, 355, 100, 32))
        self.biologyRadio.setAutoExclusive(False)

        self.historyRadio = QRadioButton(self)
        self.historyRadio.setText("HISTORY")
        self.historyRadio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "background-color: rgb(34, 34, 34);\n")
        self.historyRadio.setGeometry(QtCore.QRect(495, 355, 100, 32))
        self.historyRadio.setAutoExclusive(False)

        self.economicsRadio = QRadioButton(self)
        self.economicsRadio.setText("ECONOMICS")
        self.economicsRadio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "background-color: rgb(34, 34, 34);\n")
        self.economicsRadio.setGeometry(QtCore.QRect(615, 355, 110, 32))
        self.economicsRadio.setAutoExclusive(False)

        self.geoRadio = QRadioButton(self)
        self.geoRadio.setText("GEOGRAPHY")
        self.geoRadio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "background-color: rgb(34, 34, 34);\n")
        self.geoRadio.setGeometry(QtCore.QRect(760, 355, 110, 32))
        self.geoRadio.setAutoExclusive(False)

        self.socioRadio = QRadioButton(self)
        self.socioRadio.setText("SOCIOLOGY")
        self.socioRadio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "background-color: rgb(34, 34, 34);\n")
        self.socioRadio.setGeometry(QtCore.QRect(100, 395, 130, 32))
        self.socioRadio.setAutoExclusive(False)

        self.physicsRadio = QRadioButton(self)
        self.physicsRadio.setText("PHYSICS")
        self.physicsRadio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "background-color: rgb(34, 34, 34);\n")
        self.physicsRadio.setGeometry(QtCore.QRect(240, 395, 100, 32))
        self.physicsRadio.setAutoExclusive(False)

        self.paintRadio = QRadioButton(self)
        self.paintRadio.setText("PAINTING")
        self.paintRadio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "background-color: rgb(34, 34, 34);\n")
        self.paintRadio.setGeometry(QtCore.QRect(370, 395, 100, 32))
        self.paintRadio.setAutoExclusive(False)

        self.polscRadio = QRadioButton(self)
        self.polscRadio.setText("POLITICAL SCIENCE")
        self.polscRadio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "background-color: rgb(34, 34, 34);\n")
        self.polscRadio.setGeometry(QtCore.QRect(500, 395, 180, 32))
        self.polscRadio.setAutoExclusive(False)

        self.compRadio = QRadioButton(self)
        self.compRadio.setText("COMPUTER SCIENCE")
        self.compRadio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "background-color: rgb(34, 34, 34);\n")
        self.compRadio.setGeometry(QtCore.QRect(700, 395, 180, 32))
        self.compRadio.setAutoExclusive(False)

        self.busRadio = QRadioButton(self)
        self.busRadio.setText("BUSINESS STUDIES")
        self.busRadio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "background-color: rgb(34, 34, 34);\n")
        self.busRadio.setGeometry(QtCore.QRect(135, 435, 180, 32))
        self.busRadio.setAutoExclusive(False)

        self.peRadio = QRadioButton(self)
        self.peRadio.setText("PHYSICAL EDUCATION")
        self.peRadio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "background-color: rgb(34, 34, 34);\n")
        self.peRadio.setGeometry(QtCore.QRect(320, 435, 180, 32))
        self.peRadio.setAutoExclusive(False)

        self.mathRadio = QRadioButton(self)
        self.mathRadio.setText("MATHEMATICS")
        self.mathRadio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "background-color: rgb(34, 34, 34);\n")
        self.mathRadio.setGeometry(QtCore.QRect(530, 435, 180, 32))
        self.mathRadio.setAutoExclusive(False)

        self.homeRadio = QRadioButton(self)
        self.homeRadio.setText("HOME SCIENCE")
        self.homeRadio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "background-color: rgb(34, 34, 34);\n")
        self.homeRadio.setGeometry(QtCore.QRect(690, 435, 180, 32))
        self.homeRadio.setAutoExclusive(False)

        self.psyRadio = QRadioButton(self)
        self.psyRadio.setText("PSYCHOLOGY")
        self.psyRadio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "background-color: rgb(34, 34, 34);\n")
        self.psyRadio.setGeometry(QtCore.QRect(520, 475, 180, 32))
        self.psyRadio.setAutoExclusive(False)

        self.accRadio = QRadioButton(self)
        self.accRadio.setText("ACCOUNTANCY")
        self.accRadio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "background-color: rgb(34, 34, 34);\n")
        self.accRadio.setGeometry(QtCore.QRect(360, 475, 130, 32))
        self.accRadio.setAutoExclusive(False)

        self.alterPush = QPushButton(self)
        self.alterPush.setStyleSheet("background-color: rgb(158, 0, 2);\n"
                                     "border-radius : 20%;\n"
                                     "font: 11pt \"Cambria\";"
                                     "color: rgb(255, 255, 255);")
        self.alterPush.setText("UPDATE DATA")
        self.alterPush.setGeometry(QtCore.QRect(400, 535, 180, 60))
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
        id = int(self.stuLine.text())

        chkCursor = database.cursor()
        chkCursor.execute(f"Select STUDENT_ID from subjectinfo where STUDENT_ID = {id}")
        chkfetch = chkCursor.fetchall()

        status = ""

        if chkfetch != []:
            status = True

        elif chkfetch == []:
            status = False

        if pa == self.admin:
            if status == True:
                StuID = f"STUDENT_ID = '{int(self.stuLine.text())}'"
                name = self.nameLine.text()
                if name == "":
                    NAME = " "
                else:
                    NAME = f"NAME = '{name}'"
                
                qu = ""

                if self.optRadio.isChecked():
                    if self.chemistryRadio.isChecked():
                        CHE = "CHEMISTRY = 'OPTED'"
                    else:
                        CHE = " "
                    
                    if self.englishRadio.isChecked():
                        ENGL = "ENGLISH = 'OPTED'"
                    else:
                        ENGL = " "

                    if self.biologyRadio.isChecked():
                        BIO = "BIOLOGY = 'OPTED'"
                    else:
                        BIO = " "

                    if self.historyRadio.isChecked():
                        HIS = "HISTORY = 'OPTED'"
                    else:
                        HIS = " "

                    if self.economicsRadio.isChecked():
                        ECO = "ECONOMICS = 'OPTED'"
                    else:
                        ECO = " "

                    if self.geoRadio.isChecked():
                        GEO = "GEOGRAPHY = 'OPTED'"
                    else:
                        GEO = " "

                    if self.socioRadio.isChecked():
                        SOCIO = "SOCIOLOGY = 'OPTED'"
                    else:
                        SOCIO = " "

                    if self.physicsRadio.isChecked():
                        PHY = "PHYSICS = 'OPTED'"
                    else:
                        PHY = " "

                    if self.paintRadio.isChecked():
                        PAINT = "PAINTING = 'OPTED'"
                    else:
                        PAINT = " "

                    if self.polscRadio.isChecked():
                        POLSC = "POLITICAL_SCIENCE = 'OPTED'"
                    else:
                        POLSC = " "

                    if self.compRadio.isChecked():
                        COMP = "COMPUTER_SCIENCE = 'OPTED'"
                    else:
                        COMP = " "

                    if self.busRadio.isChecked():
                        BUS = "BUSINESS_STUDIES = 'OPTED'"
                    else:
                        BUS = " "

                    if self.peRadio.isChecked():
                        PE = "PHYSICAL_EDUCATION = 'OPTED'"
                    else:
                        PE = " "

                    if self.mathRadio.isChecked():
                        MATH = "MATHEMATICS = 'OPTED'"
                    else:
                        MATH = " "

                    if self.homeRadio.isChecked():
                        HOME = "HOME_SCIENCE = 'OPTED'"
                    else:
                        HOME = " "

                    if self.psyRadio.isChecked():
                        PSY = "PSYCHOLOGY = 'OPTED'"
                    else:
                        PSY = " "

                    if self.accRadio.isChecked():
                        ACC = "ACCOUNTANCY = 'OPTED'"
                    else:
                        ACC = " "

                    qu = f"{NAME} , {CHE} , {ENGL} , {BIO} , {HIS} , {ECO} , {GEO} , {SOCIO} , {PHY} , {PAINT} , {POLSC} , {COMP} , {BUS} , {PE} , {MATH} , {HOME} , {PSY} , {ACC}".replace(" ,  ", "").lstrip(", ")

                elif self.notoptRadio.isChecked():
                    if self.chemistryRadio.isChecked():
                        CHE = "CHEMISTRY = '--'"
                    else:
                        CHE = " "
                    
                    if self.englishRadio.isChecked():
                        ENGL = "ENGLISH = '--'"
                    else:
                        ENGL = " "

                    if self.biologyRadio.isChecked():
                        BIO = "BIOLOGY = '--'"
                    else:
                        BIO = " "

                    if self.historyRadio.isChecked():
                        HIS = "HISTORY = '--'"
                    else:
                        HIS = " "

                    if self.economicsRadio.isChecked():
                        ECO = "ECONOMICS = '--'"
                    else:
                        ECO = " "

                    if self.geoRadio.isChecked():
                        GEO = "GEOGRAPHY = '--'"
                    else:
                        GEO = " "

                    if self.socioRadio.isChecked():
                        SOCIO = "SOCIOLOGY = '--'"
                    else:
                        SOCIO = " "

                    if self.physicsRadio.isChecked():
                        PHY = "PHYSICS = '--'"
                    else:
                        PHY = " "

                    if self.paintRadio.isChecked():
                        PAINT = "PAINTING = '--'"
                    else:
                        PAINT = " "

                    if self.polscRadio.isChecked():
                        POLSC = "POLITICAL_SCIENCE = '--'"
                    else:
                        POLSC = " "

                    if self.compRadio.isChecked():
                        COMP = "COMPUTER_SCIENCE = '--'"
                    else:
                        COMP = " "

                    if self.busRadio.isChecked():
                        BUS = "BUSINESS_STUDIES = '--'"
                    else:
                        BUS = " "

                    if self.peRadio.isChecked():
                        PE = "PHYSICAL_EDUCATION = '--'"
                    else:
                        PE = " "

                    if self.mathRadio.isChecked():
                        MATH = "MATHEMATICS = '--'"
                    else:
                        MATH = " "

                    if self.homeRadio.isChecked():
                        HOME = "HOME_SCIENCE = '--'"
                    else:
                        HOME = " "

                    if self.psyRadio.isChecked():
                        PSY = "PSYCHOLOGY = '--'"
                    else:
                        PSY = " "

                    if self.accRadio.isChecked():
                        ACC = "ACCOUNTANCY = '--'"
                    else:
                        ACC = " "

                    qu = f"{NAME} , {CHE} , {ENGL} , {BIO} , {HIS} , {ECO} , {GEO} , {SOCIO} , {PHY} , {PAINT} , {POLSC} , {COMP} , {BUS} , {PE} , {MATH} , {HOME} , {PSY} , {ACC}".replace(" ,  ", "").lstrip(", ")

                execute = f"update subjectinfo set {qu} WHERE {StuID};"

                database = mysql.connector.connect(host="localhost", user="root", passwd="root", database="backend")

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
    ui = UpdateSubject()
    sys.exit(app.exec_())