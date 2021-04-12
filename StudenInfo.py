import sys
import mysql.connector

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QShortcut
from PyQt5.QtWidgets import QRadioButton, QPushButton, QLabel, QLineEdit, QTableWidget

from UpdateStudentInfo import StudentAlter
from InsertStudentInfo import InsertStudentInfo

from MySQLPass import MySQLPassword
from MySQL_DB import db


# command to find number of columns - select count(*) from information_schema.columns where table_name = '{TABLE NAME}';
# command to find column name - SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{TABLE NAME}';
# command to find number of rows - select count(*) from {TABLE NAME};


class StudentInfo(QMainWindow):
    def __init__(self):
        super(StudentInfo, self).__init__()

        # USER INTERFACE
        self.setWindowTitle("STUDENT DATA")
        self.setFixedSize(982, 880)
        self.setStyleSheet("background-color : rgb(34, 34, 34);")

        self.MainLabel = QLabel(self)
        self.MainLabel.setText("STUDENT DATA")
        self.MainLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                     "font: 20pt \"Cambria\";\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "text-decoration: underline;\n")
        self.MainLabel.setGeometry(QtCore.QRect(410, 20, 190, 30))

        self.stuLabel = QLabel(self)
        self.stuLabel.setText("STUDENT ID :")
        self.stuLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                    "font: 12pt \"Cambria\";\n"
                                    "color: rgb(255, 255, 255);")
        self.stuLabel.setGeometry(QtCore.QRect(100, 100, 120, 30))

        self.stuLine = QLineEdit(self)
        self.stuLine.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 11pt \"Cambria\";\n"
                                   "background-color: rgb(74, 74, 74);\n"
                                   "border-radius : 10%")
        self.stuLine.setGeometry(QtCore.QRect(210, 100, 260, 30))

        self.nameLabel = QLabel(self)
        self.nameLabel.setText("NAME :")
        self.nameLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                     "font: 12pt \"Cambria\";\n"
                                     "color: rgb(255, 255, 255);")
        self.nameLabel.setGeometry(QtCore.QRect(530, 100, 100, 30))

        self.nameLine = QLineEdit(self)
        self.nameLine.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 11pt \"Cambria\";\n"
                                    "background-color: rgb(74, 74, 74);\n"
                                    "border-radius : 10%")
        self.nameLine.setGeometry(QtCore.QRect(600, 100, 280, 32))

        self.classLabel = QLabel(self)
        self.classLabel.setText("CLASS :")
        self.classLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                      "font: 12pt \"Cambria\";\n"
                                      "color: rgb(255, 255, 255);")
        self.classLabel.setGeometry(QtCore.QRect(120, 150, 90, 30))

        self.classLine = QLineEdit(self)
        self.classLine.setStyleSheet("color: rgb(255, 255, 255);\n"
                                     "font: 11pt \"Cambria\";\n"
                                     "background-color: rgb(74, 74, 74);\n"
                                     "border-radius : 10%")
        self.classLine.setGeometry(QtCore.QRect(210, 150, 260, 30))

        self.secLabel = QLabel(self)
        self.secLabel.setText("SEC :")
        self.secLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                    "font: 12pt \"Cambria\";\n"
                                    "color: rgb(255, 255, 255);")
        self.secLabel.setGeometry(QtCore.QRect(535, 150, 90, 30))

        self.secLine = QLineEdit(self)
        self.secLine.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 11pt \"Cambria\";\n"
                                   "background-color: rgb(74, 74, 74);\n"
                                   "border-radius : 10%")
        self.secLine.setGeometry(QtCore.QRect(600, 150, 280, 32))

        self.rollLabel = QLabel(self)
        self.rollLabel.setText("ROLL NUMBER :")
        self.rollLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                     "font: 12pt \"Cambria\";\n"
                                     "color: rgb(255, 255, 255);")
        self.rollLabel.setGeometry(QtCore.QRect(90, 200, 120, 30))

        self.rollLine = QLineEdit(self)
        self.rollLine.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 11pt \"Cambria\";\n"
                                    "background-color: rgb(74, 74, 74);\n"
                                    "border-radius : 10%")
        self.rollLine.setGeometry(QtCore.QRect(210, 200, 260, 30))

        self.bldLabel = QLabel(self)
        self.bldLabel.setText("BLOOD GROUP :")
        self.bldLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                    "font: 11pt \"Cambria\";\n"
                                    "color: rgb(255, 255, 255);")
        self.bldLabel.setGeometry(QtCore.QRect(490, 200, 120, 30))

        self.bldLine = QLineEdit(self)
        self.bldLine.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 11pt \"Cambria\";\n"
                                   "background-color: rgb(74, 74, 74);\n"
                                   "border-radius : 10%")
        self.bldLine.setGeometry(QtCore.QRect(600, 200, 280, 32))

        self.genderLabel = QLabel(self)
        self.genderLabel.setText("GENDER : ")
        self.genderLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                       "font: 12pt \"Cambria\";\n"
                                       "color: rgb(255, 255, 255);")
        self.genderLabel.setGeometry(QtCore.QRect(380, 270, 220, 30))

        self.mlRadio = QRadioButton(self)
        self.mlRadio.setText("MALE")
        self.mlRadio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"Cambria\";\n"
                                   "background-color: rgb(34, 34, 34);\n")
        self.mlRadio.setGeometry(QtCore.QRect(470, 270, 60, 32))
        self.mlRadio.setAutoExclusive(False)

        self.fmlRadio = QRadioButton(self)
        self.fmlRadio.setText("FEMALE")
        self.fmlRadio.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 12pt \"Cambria\";\n"
                                    "background-color: rgb(34, 34, 34);\n")
        self.fmlRadio.setGeometry(QtCore.QRect(550, 270, 80, 32))
        self.fmlRadio.setAutoExclusive(False)

        self.fetchPush = QPushButton(self)
        self.fetchPush.setStyleSheet("background-color: rgb(158, 0, 2);\n"
                                     "border-radius : 20%;\n"
                                     "font: 11pt \"Cambria\";"
                                     "color: rgb(255, 255, 255);")
        self.fetchPush.setText("SHOW DATA")
        self.fetchPush.setGeometry(QtCore.QRect(640, 340, 180, 60))
        self.fetchPush.clicked.connect(self.backend)

        self.alterPush = QPushButton(self)
        self.alterPush.setStyleSheet("background-color: rgb(158, 0, 2);\n"
                                     "border-radius : 20%;\n"
                                     "font: 11pt \"Cambria\";"
                                     "color: rgb(255, 255, 255);")
        self.alterPush.setText("UPDATE DATA")
        self.alterPush.setGeometry(QtCore.QRect(420, 340, 180, 60))
        self.alterPush.clicked.connect(self.redirect)

        self.insertPush = QPushButton(self)
        self.insertPush.setStyleSheet("background-color: rgb(158, 0, 2);\n"
                                     "border-radius : 20%;\n"
                                     "font: 11pt \"Cambria\";"
                                     "color: rgb(255, 255, 255);")
        self.insertPush.setText("INSERT DATA")
        self.insertPush.setGeometry(QtCore.QRect(200, 340, 180, 60))
        self.insertPush.clicked.connect(self.redirect1)

        self.tableLabel = QLabel(self)
        self.tableLabel.setText("DATA OUTPUT")
        self.tableLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "font: 16pt \"Cambria\";\n"
                                      "background-color: rgb(34, 34, 34);\n"
                                      "text-decoration: underline;\n")
        self.tableLabel.setGeometry(QtCore.QRect(430, 430, 150, 50))

        self.table = QTableWidget(self)
        self.table.setStyleSheet("color: rgb(0, 0, 0);\n"
                                 "border-radius : 15% ;\n"
                                 "background-color: rgb(255, 255, 255);\n")
        self.table.setGeometry(QtCore.QRect(40, 490, 900, 355))

        self.shortcut = QShortcut(QtGui.QKeySequence("Ctrl+e"), self)
        self.shortcut.activated.connect(self.backend)

        self.show()

    def redirect(self):
        self.win = StudentAlter()
        self.win.show()

    def redirect1(self):
        self.win = InsertStudentInfo()
        self.win.show()

    def backend(self):
        def StrToInt(string):
            integer = int(string)
            return integer

        # QUERY MAKING
        
        studentID = self.stuLine.text()
        if studentID == "":
            ID = " "
        else:
            ID = f"STUDENT_ID = {StrToInt(studentID)}"

        name = self.nameLine.text()
        if name == "":
            NAME = " "
        else:
            NAME = f"_NAME_ = '{name}'"

        Class = self.classLine.text()
        if Class == "":
            CLASS = " "
        else:
            CLASS = f"CLASS = {StrToInt(Class)}"

        Sec = self.secLine.text()
        if Sec == "":
            SEC = " "
        else:
            SEC = f"SEC = '{Sec}'"

        Roll = self.rollLine.text()
        if Roll == "":
            ROLL = " "
        else:
            ROLL = f"ROLL_NUMBER = {StrToInt(Roll)}"
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

        if self.mlRadio.isChecked() and self.fmlRadio.isChecked():
            GENDER = "GENDER = 'M' or GENDER = 'F'"

        qu = f"{ID} or {NAME} or {CLASS} or {SEC} or {ROLL} or {BLOOD} or {GENDER}".replace(" or  ", "").lstrip("or ")
        execute = f"SELECT * FROM studentinfo WHERE {qu};"
        qu1 = f"select count(*) from studentinfo WHERE {qu};"

        if studentID == "" and name == "" and Class == "" and Sec == "" and Roll == "" and Blood == "" and not self.mlRadio.isChecked() and not self.fmlRadio.isChecked():
            execute = "SELECT * FROM studentinfo ;"
            qu1 = "select count(*) from studentinfo ;"

        # BACKED STARTS
        database = mysql.connector.connect(host="localhost", user="root", passwd=MySQLPassword(), database=db())

        CountColumn = database.cursor()
        CountColumn.execute("select count(*) from information_schema.columns where table_name = 'studentinfo';")
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
        ColumnName.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'studentinfo';")
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
    ui = StudentInfo()
    sys.exit(app.exec_())
