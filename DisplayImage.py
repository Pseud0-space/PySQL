import sys
import mysql.connector
from PIL import Image
import base64

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,  QShortcut, QMessageBox, QFileDialog
from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QPixmap

from MySQLPass import MySQLPassword
from MySQL_DB import db

class ImageDisplay(QMainWindow):
    def __init__(self):
        super(ImageDisplay, self).__init__()

        self.setWindowTitle("STUDENT IMAGE")
        self.setFixedSize(597, 720)
        self.setStyleSheet("background-color : rgb(34, 34, 34);")

        self.MainLabel = QLabel(self)
        self.MainLabel.setText("Display Student Image")
        self.MainLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                     "font: 20pt \"Cambria\";\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "text-decoration: underline;\n")
        self.MainLabel.setGeometry(QtCore.QRect(190, 20, 320, 30))

        self.stuLabel = QLabel(self)
        self.stuLabel.setText("STUDENT ID :")
        self.stuLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                    "font: 12pt \"Cambria\";\n"
                                    "color: rgb(255, 255, 255);")
        self.stuLabel.setGeometry(QtCore.QRect(110, 100, 120, 30))

        self.imgLabel = QLabel(self)
        self.imgLabel.setText("IMAGE")
        self.imgLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                    "font: 13pt \"Cambria\";\n"
                                    "color: rgb(255, 255, 255);")
        self.imgLabel.setGeometry(QtCore.QRect(280, 150, 120, 30))

        self.stuLine = QLineEdit(self)
        self.stuLine.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 11pt \"Cambria\";\n"
                                   "background-color: rgb(74, 74, 74);\n"
                                   "border-radius : 10%")
        self.stuLine.setGeometry(QtCore.QRect(220, 100, 265, 30))

        self.LabelImg = QLabel(self)
        self.LabelImg.setGeometry(QtCore.QRect(100, 190, 400, 400))

        self.shwPush = QPushButton(self)
        self.shwPush.setStyleSheet("background-color: rgb(158, 0, 2);\n"
                                     "border-radius : 15%;\n"
                                     "font: 11pt \"Cambria\";"
                                     "color: rgb(255, 255, 255);")
        self.shwPush.setText("SHOW IMAGE")
        self.shwPush.setGeometry(QtCore.QRect(210, 630, 180, 60))
        self.shwPush.clicked.connect(self.backend)

        self.show()

    def ShwError(self):
        msgBox = QMessageBox()
        msgBox.setFixedSize(400, 400)
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setText("Invalid Student ID!")
        msgBox.setWindowTitle("ERROR")

        returnValue = msgBox.exec_()
        if returnValue == QMessageBox.Ok:
            pass


    def backend(self):
        stuID = int(self.stuLine.text())
        database = mysql.connector.connect(host="localhost", user="root", passwd=MySQLPassword(), database=db())

        chkCursor = database.cursor()
        chkCursor.execute(f"Select STUDENT_ID from image where STUDENT_ID = {stuID}")
        chkfetch = chkCursor.fetchall()

        status = ""

        if chkfetch != []:
            status = True

        elif chkfetch == []:
            status = False

        if status == True:
            ImageCursor = database.cursor()
            qu = f"select IMAGE from image where Student_ID = {stuID}"
            ImageCursor.execute(qu)
            data = ImageCursor.fetchall()

            imgTmp = data[0][0]
            strImg = base64.b64decode(imgTmp)

            file = open("temp/temp.png", "wb")
            file.write(strImg)
            file.close()

            pic = QPixmap('temp/temp.png')
            self.LabelImg.setPixmap(pic)

        elif status == False:
            self.ShwError()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ImageDisplay()
    sys.exit(app.exec_())