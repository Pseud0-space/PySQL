import sys
import mysql.connector

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QShortcut
from PyQt5.QtWidgets import QRadioButton, QPushButton, QLabel, QLineEdit, QTableWidget

from MySQLPass import MySQLPassword
from MySQL_DB import db

from InsertSubjectInfo import InsertSubjectInfo
from UpdateSubjectInfo import UpdateSubject

class SubjectInfo(QMainWindow):
    def __init__(self):
        super(SubjectInfo, self).__init__()

        # USER INTERFACE
        self.setWindowTitle("STUDENT SUBJECT INFORMATION")
        self.setFixedSize(980, 900)
        self.setStyleSheet("background-color : rgb(34, 34, 34);")

        self.MainLabel = QLabel(self)
        self.MainLabel.setText("SUBJECT INFORMATION")
        self.MainLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                     "font: 20pt \"Cambria\";\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "text-decoration: underline;\n")
        self.MainLabel.setGeometry(QtCore.QRect(370, 20, 320, 30))

        self.crtLabel = QLabel(self)
        self.crtLabel.setText("Criterias availabel for search : ")
        self.crtLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                     "font: 13pt \"Cambria\";\n"
                                     "color: rgb(255, 255, 255);\n")
        self.crtLabel.setGeometry(QtCore.QRect(90, 70, 320, 30))

        self.stuLabel = QLabel(self)
        self.stuLabel.setText("STUDENT ID :")
        self.stuLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                    "font: 12pt \"Cambria\";\n"
                                    "color: rgb(255, 255, 255);")
        self.stuLabel.setGeometry(QtCore.QRect(100, 120, 120, 30))

        self.stuLine = QLineEdit(self)
        self.stuLine.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 11pt \"Cambria\";\n"
                                   "background-color: rgb(74, 74, 74);\n"
                                   "border-radius : 10%")
        self.stuLine.setGeometry(QtCore.QRect(210, 120, 260, 30))

        self.nameLabel = QLabel(self)
        self.nameLabel.setText("NAME :")
        self.nameLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                     "font: 12pt \"Cambria\";\n"
                                     "color: rgb(255, 255, 255);")
        self.nameLabel.setGeometry(QtCore.QRect(530, 120, 100, 30))

        self.nameLine = QLineEdit(self)
        self.nameLine.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 11pt \"Cambria\";\n"
                                    "background-color: rgb(74, 74, 74);\n"
                                    "border-radius : 10%")
        self.nameLine.setGeometry(QtCore.QRect(600, 120, 280, 32))

        self.chemistryRadio = QRadioButton(self)
        self.chemistryRadio.setText("CHEMISTRY")
        self.chemistryRadio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "background-color: rgb(34, 34, 34);\n")
        self.chemistryRadio.setGeometry(QtCore.QRect(100, 170, 100, 32))
        self.chemistryRadio.setAutoExclusive(False)

        self.englishRadio = QRadioButton(self)
        self.englishRadio.setText("ENGLISH")
        self.englishRadio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "background-color: rgb(34, 34, 34);\n")
        self.englishRadio.setGeometry(QtCore.QRect(240, 170, 100, 32))
        self.englishRadio.setAutoExclusive(False)

        self.biologyRadio = QRadioButton(self)
        self.biologyRadio.setText("BIOLOGY")
        self.biologyRadio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "background-color: rgb(34, 34, 34);\n")
        self.biologyRadio.setGeometry(QtCore.QRect(370, 170, 100, 32))
        self.biologyRadio.setAutoExclusive(False)

        self.historyRadio = QRadioButton(self)
        self.historyRadio.setText("HISTORY")
        self.historyRadio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "background-color: rgb(34, 34, 34);\n")
        self.historyRadio.setGeometry(QtCore.QRect(495, 170, 100, 32))
        self.historyRadio.setAutoExclusive(False)

        self.economicsRadio = QRadioButton(self)
        self.economicsRadio.setText("ECONOMICS")
        self.economicsRadio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "background-color: rgb(34, 34, 34);\n")
        self.economicsRadio.setGeometry(QtCore.QRect(615, 170, 110, 32))
        self.economicsRadio.setAutoExclusive(False)

        self.geoRadio = QRadioButton(self)
        self.geoRadio.setText("GEOGRAPHY")
        self.geoRadio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "background-color: rgb(34, 34, 34);\n")
        self.geoRadio.setGeometry(QtCore.QRect(760, 170, 110, 32))
        self.geoRadio.setAutoExclusive(False)

        self.socioRadio = QRadioButton(self)
        self.socioRadio.setText("SOCIOLOGY")
        self.socioRadio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "background-color: rgb(34, 34, 34);\n")
        self.socioRadio.setGeometry(QtCore.QRect(100, 210, 130, 32))
        self.socioRadio.setAutoExclusive(False)

        self.physicsRadio = QRadioButton(self)
        self.physicsRadio.setText("PHYSICS")
        self.physicsRadio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "background-color: rgb(34, 34, 34);\n")
        self.physicsRadio.setGeometry(QtCore.QRect(240, 210, 100, 32))
        self.physicsRadio.setAutoExclusive(False)

        self.paintRadio = QRadioButton(self)
        self.paintRadio.setText("PAINTING")
        self.paintRadio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "background-color: rgb(34, 34, 34);\n")
        self.paintRadio.setGeometry(QtCore.QRect(370, 210, 100, 32))
        self.paintRadio.setAutoExclusive(False)

        self.polscRadio = QRadioButton(self)
        self.polscRadio.setText("POLITICAL SCIENCE")
        self.polscRadio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "background-color: rgb(34, 34, 34);\n")
        self.polscRadio.setGeometry(QtCore.QRect(500, 210, 180, 32))
        self.polscRadio.setAutoExclusive(False)

        self.compRadio = QRadioButton(self)
        self.compRadio.setText("COMPUTER SCIENCE")
        self.compRadio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "background-color: rgb(34, 34, 34);\n")
        self.compRadio.setGeometry(QtCore.QRect(700, 210, 180, 32))
        self.compRadio.setAutoExclusive(False)

        self.busRadio = QRadioButton(self)
        self.busRadio.setText("BUSINESS STUDIES")
        self.busRadio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "background-color: rgb(34, 34, 34);\n")
        self.busRadio.setGeometry(QtCore.QRect(135, 250, 180, 32))
        self.busRadio.setAutoExclusive(False)

        self.peRadio = QRadioButton(self)
        self.peRadio.setText("PHYSICAL EDUCATION")
        self.peRadio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "background-color: rgb(34, 34, 34);\n")
        self.peRadio.setGeometry(QtCore.QRect(320, 250, 180, 32))
        self.peRadio.setAutoExclusive(False)

        self.mathRadio = QRadioButton(self)
        self.mathRadio.setText("MATHEMATICS")
        self.mathRadio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "background-color: rgb(34, 34, 34);\n")
        self.mathRadio.setGeometry(QtCore.QRect(530, 250, 180, 32))
        self.mathRadio.setAutoExclusive(False)

        self.homeRadio = QRadioButton(self)
        self.homeRadio.setText("HOME SCIENCE")
        self.homeRadio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "background-color: rgb(34, 34, 34);\n")
        self.homeRadio.setGeometry(QtCore.QRect(690, 250, 180, 32))
        self.homeRadio.setAutoExclusive(False)

        self.psyRadio = QRadioButton(self)
        self.psyRadio.setText("PSYCHOLOGY")
        self.psyRadio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "background-color: rgb(34, 34, 34);\n")
        self.psyRadio.setGeometry(QtCore.QRect(520, 290, 180, 32))
        self.psyRadio.setAutoExclusive(False)

        self.accRadio = QRadioButton(self)
        self.accRadio.setText("ACCOUNTANCY")
        self.accRadio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "background-color: rgb(34, 34, 34);\n")
        self.accRadio.setGeometry(QtCore.QRect(360, 290, 130, 32))
        self.accRadio.setAutoExclusive(False)

        self.fetchPush = QPushButton(self)
        self.fetchPush.setStyleSheet("background-color: rgb(158, 0, 2);\n"
                                     "border-radius : 20%;\n"
                                     "font: 11pt \"Cambria\";"
                                     "color: rgb(255, 255, 255);")
        self.fetchPush.setText("SHOW DATA")
        self.fetchPush.setGeometry(QtCore.QRect(637, 355, 180, 60))
        self.fetchPush.clicked.connect(self.backend)

        self.alterPush = QPushButton(self)
        self.alterPush.setStyleSheet("background-color: rgb(158, 0, 2);\n"
                                     "border-radius : 20%;\n"
                                     "font: 11pt \"Cambria\";"
                                     "color: rgb(255, 255, 255);")
        self.alterPush.setText("UPDATE DATA")
        self.alterPush.setGeometry(QtCore.QRect(410, 355, 180, 60))
        self.alterPush.clicked.connect(self.redirect2)

        self.insertPush = QPushButton(self)
        self.insertPush.setStyleSheet("background-color: rgb(158, 0, 2);\n"
                                     "border-radius : 20%;\n"
                                     "font: 11pt \"Cambria\";"
                                     "color: rgb(255, 255, 255);")
        self.insertPush.setText("INSERT DATA")
        self.insertPush.setGeometry(QtCore.QRect(180, 355, 180, 60))
        self.insertPush.clicked.connect(self.redirect1)

        self.tableLabel = QLabel(self)
        self.tableLabel.setText("DATA OUTPUT")
        self.tableLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "font: 16pt \"Cambria\";\n"
                                      "background-color: rgb(34, 34, 34);\n"
                                      "text-decoration: underline;\n")
        self.tableLabel.setGeometry(QtCore.QRect(430, 440, 150, 50))

        self.table = QTableWidget(self)
        self.table.setStyleSheet("color: rgb(0, 0, 0);\n"
                                 "border-radius : 15% ;\n"
                                 "background-color: rgb(255, 255, 255);\n")
        self.table.setGeometry(QtCore.QRect(40, 510, 900, 355))

        self.show()

    def redirect1(self):
        self.win = InsertSubjectInfo()
        self.win.show()

    def redirect2(self):
        self.win = UpdateSubject()
        self.win.show()

    def backend(self):
        studentID = self.stuLine.text()
        if studentID == "":
            ID = " "
        else:
            ID = f"STUDENT_ID = {int(studentID)}"

        name = self.nameLine.text()
        if name == "":
            NAME = " "
        else:
            NAME = f"NAME = '{name}'"

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

        qu = f"{ID} or {NAME} or {CHE} or {ENGL} or {BIO} or {HIS} or {ECO} or {GEO} or {SOCIO} or {PHY} or {PAINT} or {POLSC} or {COMP} or {BUS} or {PE} or {MATH} or {HOME} or {PSY} or {ACC}".replace(" or  ", "").lstrip("or ")
        execute = f"select * FROM subjectinfo where {qu};"
        qu1 = f"select count(*) from subjectinfo where {qu};"

        if studentID == "" and name == "" and not self.chemistryRadio.isChecked() and not self.englishRadio.isChecked() and not self.biologyRadio.isChecked() and not self.historyRadio.isChecked() and not self.economicsRadio.isChecked() and not self.geoRadio.isChecked() and not self.socioRadio.isChecked() and not self.physicsRadio.isChecked() and not self.paintRadio.isChecked() and not self.polscRadio.isChecked() and not self.compRadio.isChecked() and not self.busRadio.isChecked() and not self.peRadio.isChecked() and not self.mathRadio.isChecked() and not self.homeRadio.isChecked() and not self.psyRadio.isChecked() and not self.accRadio.isChecked():
            execute = "select * FROM subjectinfo ;"
            qu1 = "select count(*) from subjectinfo ;"

        # BACKED STARTS
        database = mysql.connector.connect(host="localhost", user="root", passwd=MySQLPassword(), database=db())

        CountColumn = database.cursor()
        CountColumn.execute("select count(*) from information_schema.columns where table_name = 'subjectinfo';")
        fetchColumn = CountColumn.fetchall()[0][0]

        realData = database.cursor()

        realData.execute(execute)
        realData = realData.fetchall()

        CountRows = database.cursor()
        CountRows.execute(qu1)
        fetchRows = CountRows.fetchall()[0]
        fetchRows = fetchRows[0]

        self.table.setRowCount(int(fetchRows + 1))
        self.table.setColumnCount(int(fetchColumn))

        ColumnName = database.cursor()
        ColumnName.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'subjectinfo';")
        ColumnName = ColumnName.fetchall()

        # SHOW DATA IN TABULAR FORM
        ColCount = 0
        for i in ColumnName:
            self.table.setItem(0, ColCount, QTableWidgetItem(i[0]))
            ColCount += 1

        column = 0
        for i in realData:
            for x in i:
                if str(type(x)) == "<class 'int'>":
                    self.table.setItem(1, column, QTableWidgetItem(str(x)))
                else:
                    self.table.setItem(1, column, QTableWidgetItem(x))
                column = column + 1
    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = SubjectInfo()
    sys.exit(app.exec_())