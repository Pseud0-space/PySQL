import sys
import mysql.connector

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QShortcut
from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit, QTableWidget

from InsertFeeInfo import InsertFee
from UpdateFeeInfo import UpdateFee

from MySQLPass import MySQLPassword
from MySQL_DB import db

class FeeInfo(QMainWindow):
    def __init__(self):
        super(FeeInfo, self).__init__()

        # USER INTERFACE
        self.setWindowTitle("STUDENT FEE DATA")
        self.setFixedSize(982, 800)
        self.setStyleSheet("background-color : rgb(34, 34, 34);")

        self.MainLabel = QLabel(self)
        self.MainLabel.setText("STUDENT FEE DATA")
        self.MainLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                     "font: 20pt \"Cambria\";\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "text-decoration: underline;\n")
        self.MainLabel.setGeometry(QtCore.QRect(390, 20, 250, 30))

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

        self.feeIdLabel = QLabel(self)
        self.feeIdLabel.setText("FEE ID :")
        self.feeIdLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                      "font: 12pt \"Cambria\";\n"
                                      "color: rgb(255, 255, 255);")
        self.feeIdLabel.setGeometry(QtCore.QRect(120, 150, 90, 30))

        self.feeIdLine = QLineEdit(self)
        self.feeIdLine.setStyleSheet("color: rgb(255, 255, 255);\n"
                                     "font: 11pt \"Cambria\";\n"
                                     "background-color: rgb(74, 74, 74);\n"
                                     "border-radius : 10%")
        self.feeIdLine.setGeometry(QtCore.QRect(210, 150, 260, 30))

        self.classLabel = QLabel(self)
        self.classLabel.setText("CLASS :")
        self.classLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                    "font: 12pt \"Cambria\";\n"
                                    "color: rgb(255, 255, 255);")
        self.classLabel.setGeometry(QtCore.QRect(535, 150, 90, 30))

        self.classLine = QLineEdit(self)
        self.classLine.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 11pt \"Cambria\";\n"
                                   "background-color: rgb(74, 74, 74);\n"
                                   "border-radius : 10%")
        self.classLine.setGeometry(QtCore.QRect(600, 150, 280, 32))

        self.fetchPush = QPushButton(self)
        self.fetchPush.setStyleSheet("background-color: rgb(158, 0, 2);\n"
                                     "border-radius : 20%;\n"
                                     "font: 11pt \"Cambria\";"
                                     "color: rgb(255, 255, 255);")
        self.fetchPush.setText("SHOW DATA")
        self.fetchPush.setGeometry(QtCore.QRect(637, 260, 180, 60))
        self.fetchPush.clicked.connect(self.showBackend)

        self.alterPush = QPushButton(self)
        self.alterPush.setStyleSheet("background-color: rgb(158, 0, 2);\n"
                                     "border-radius : 20%;\n"
                                     "font: 11pt \"Cambria\";"
                                     "color: rgb(255, 255, 255);")
        self.alterPush.setText("UPDATE DATA")
        self.alterPush.setGeometry(QtCore.QRect(410, 260, 180, 60))
        self.alterPush.clicked.connect(self.redirect2)

        self.insertPush = QPushButton(self)
        self.insertPush.setStyleSheet("background-color: rgb(158, 0, 2);\n"
                                     "border-radius : 20%;\n"
                                     "font: 11pt \"Cambria\";"
                                     "color: rgb(255, 255, 255);")
        self.insertPush.setText("INSERT DATA")
        self.insertPush.setGeometry(QtCore.QRect(180, 260, 180, 60))
        self.insertPush.clicked.connect(self.redirect1)

        self.tableLabel = QLabel(self)
        self.tableLabel.setText("DATA OUTPUT")
        self.tableLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "font: 16pt \"Cambria\";\n"
                                      "background-color: rgb(34, 34, 34);\n"
                                      "text-decoration: underline;\n")
        self.tableLabel.setGeometry(QtCore.QRect(430, 350, 150, 50))

        self.table = QTableWidget(self)
        self.table.setStyleSheet("color: rgb(0, 0, 0);\n"
                                 "border-radius : 15% ;\n"
                                 "background-color: rgb(255, 255, 255);\n")
        self.table.setGeometry(QtCore.QRect(40, 410, 900, 355))

        self.shortcut = QShortcut(QtGui.QKeySequence("Ctrl+e"), self)
        self.shortcut.activated.connect(self.showBackend)

        self.show()

    def redirect1(self):
        self.win = InsertFee()
        self.win.show()

    def redirect2(self):
        self.win = UpdateFee()
        self.win.show()


    def showBackend(self):
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
            NAME = f"NAME = '{name}'"

        feeID = self.feeIdLine.text()
        if feeID == "":
            FeeID = " "
        else:
            FeeID = f"FEE_ID = {StrToInt(feeID)}"
        
        Class = self.classLine.text()
        if Class == "":
            CLASS = " "
        else:
            CLASS = f"CLASS = '{Class}'"
        
        qu = f"{ID} or {NAME} or {FeeID} or {CLASS}".replace(" or  ", "").lstrip("or ")
        execute = f"select * FROM feeinfo where {qu};"
        qu1 = f"select count(*) from feeinfo where {qu};"

        if studentID == "" and name == "" and Class == "" and feeID == "":
            execute = "select * FROM feeinfo ;"
            qu1 = "select count(*) from feeinfo ;"

        # BACKED STARTS
        database = mysql.connector.connect(host="localhost", user="root", passwd=MySQLPassword(), database=db())

        CountColumn = database.cursor()
        CountColumn.execute("select count(*) from information_schema.columns where table_name = 'feeinfo';")
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
        ColumnName.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'feeinfo';")
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
                elif str(type(x)) == "<class 'float'>":
                    self.table.setItem(1, column, QTableWidgetItem(str(x)))
                else:
                    self.table.setItem(1, column, QTableWidgetItem(x))
                column = column + 1

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = FeeInfo()
    sys.exit(app.exec_())