import sys
import mysql.connector

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QShortcut
from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit, QTableWidget, QTextEdit

from InsertPersonalInfo import InsertPersonalInfo
from UpdatePersonalInfo import PersonalAlter

from MySQLPass import MySQLPassword
from MySQL_DB import db


class PersonalInfo(QMainWindow):
    def __init__(self):
        super(PersonalInfo, self).__init__()

        # USER INTERFACE
        self.setWindowTitle("PERSONAL DATA")
        self.setFixedSize(982, 880)
        self.setStyleSheet("background-color : rgb(34, 34, 34);")

        self.MainLabel = QLabel(self)
        self.MainLabel.setText("PERSONAL DATA")
        self.MainLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                     "font: 18pt \"Cambria\";\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "text-decoration: underline;\n")
        self.MainLabel.setGeometry(QtCore.QRect(420, 20, 190, 30))

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

        self.fnameLabel = QLabel(self)
        self.fnameLabel.setText("FATHER'S NAME :")
        self.fnameLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                      "font: 10pt \"Cambria\";\n"
                                      "color: rgb(255, 255, 255);")
        self.fnameLabel.setGeometry(QtCore.QRect(100, 150, 140, 30))

        self.fnameLine = QLineEdit(self)
        self.fnameLine.setStyleSheet("color: rgb(255, 255, 255);\n"
                                     "font: 11pt \"Cambria\";\n"
                                     "background-color: rgb(74, 74, 74);\n"
                                     "border-radius : 10%")
        self.fnameLine.setGeometry(QtCore.QRect(210, 150, 260, 30))

        self.mnameLabel = QLabel(self)
        self.mnameLabel.setText("MOTHER'S NAME :")
        self.mnameLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                    "font: 10pt \"Cambria\";\n"
                                    "color: rgb(255, 255, 255);")
        self.mnameLabel.setGeometry(QtCore.QRect(490, 150, 140, 30))

        self.mnameLine = QLineEdit(self)
        self.mnameLine.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 11pt \"Cambria\";\n"
                                   "background-color: rgb(74, 74, 74);\n"
                                   "border-radius : 10%")
        self.mnameLine.setGeometry(QtCore.QRect(600, 150, 280, 32))

        self.ageLabel = QLabel(self)
        self.ageLabel.setText("AGE :")
        self.ageLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                     "font: 12pt \"Cambria\";\n"
                                     "color: rgb(255, 255, 255);")
        self.ageLabel.setGeometry(QtCore.QRect(140, 200, 90, 30))

        self.ageLine = QLineEdit(self)
        self.ageLine.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 11pt \"Cambria\";\n"
                                    "background-color: rgb(74, 74, 74);\n"
                                    "border-radius : 10%")
        self.ageLine.setGeometry(QtCore.QRect(210, 200, 260, 30))

        self.pnumberLabel = QLabel(self)
        self.pnumberLabel.setText("PHONE NO. :")
        self.pnumberLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                    "font: 11pt \"Cambria\";\n"
                                    "color: rgb(255, 255, 255);")
        self.pnumberLabel.setGeometry(QtCore.QRect(500, 200, 140, 30))

        self.pnumberLine = QLineEdit(self)
        self.pnumberLine.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 11pt \"Cambria\";\n"
                                   "background-color: rgb(74, 74, 74);\n"
                                   "border-radius : 10%")
        self.pnumberLine.setGeometry(QtCore.QRect(600, 200, 280, 32))

        self.addrLabel = QLabel(self)
        self.addrLabel.setText("ADDRESS :")
        self.addrLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                     "font: 12pt \"Cambria\";\n"
                                     "color: rgb(255, 255, 255);")
        self.addrLabel.setGeometry(QtCore.QRect(100, 250, 90, 30))

        self.addrEdit = QTextEdit(self)
        self.addrEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 11pt \"Cambria\";\n"
                                    "background-color: rgb(74, 74, 74);\n"
                                    "border-radius : 10%")
        self.addrEdit.setGeometry(QtCore.QRect(210, 250, 670, 70))

        self.fetchPush = QPushButton(self)
        self.fetchPush.setStyleSheet("background-color: rgb(158, 0, 2);\n"
                                     "border-radius : 20%;\n"
                                     "font: 11pt \"Cambria\";"
                                     "color: rgb(255, 255, 255);")
        self.fetchPush.setText("SHOW DATA")
        self.fetchPush.setGeometry(QtCore.QRect(630, 350, 180, 60))
        self.fetchPush.clicked.connect(self.backend)

        self.alterPush = QPushButton(self)
        self.alterPush.setStyleSheet("background-color: rgb(158, 0, 2);\n"
                                     "border-radius : 20%;\n"
                                     "font: 11pt \"Cambria\";"
                                     "color: rgb(255, 255, 255);")
        self.alterPush.setText("UPDATE DATA")
        self.alterPush.setGeometry(QtCore.QRect(410, 350, 180, 60))
        self.alterPush.clicked.connect(self.redirect)

        self.insertPush = QPushButton(self)
        self.insertPush.setStyleSheet("background-color: rgb(158, 0, 2);\n"
                                     "border-radius : 20%;\n"
                                     "font: 11pt \"Cambria\";"
                                     "color: rgb(255, 255, 255);")
        self.insertPush.setText("INSERT DATA")
        self.insertPush.setGeometry(QtCore.QRect(190, 350, 180, 60))
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
        self.win = PersonalAlter()
        self.win.show()

    def redirect1(self):
        self.win = InsertPersonalInfo()
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

        qu = f"{ID} or {NAME} or {FNAME} or {MNAME} or {AGE} or {ADDR} or {PNUMBER}".replace(" or  ", "").lstrip("or ")
        execute = f"SELECT * FROM personalinfo WHERE {qu};"
        qu1 = f"select count(*) from personalinfo WHERE {qu};"

        if studentID == "" and name == "" and fname == "" and mname == "" and Age == "" and Addr == "":
            execute = "SELECT * FROM personalinfo ;"
            qu1 = "select count(*) from personalinfo ;"

        # BACKED STARTS
        database = mysql.connector.connect(host="localhost", user="root", passwd=MySQLPassword(), database=db())

        CountColumn = database.cursor()
        CountColumn.execute("select count(*) from information_schema.columns where table_name = 'personalinfo';")
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
        ColumnName.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'personalinfo';")
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
    ui = PersonalInfo()
    sys.exit(app.exec_())
