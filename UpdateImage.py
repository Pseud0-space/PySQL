import sys
import mysql.connector
from PIL import Image
import base64

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,  QShortcut, QMessageBox, QFileDialog
from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit

from MySQLPass import MySQLPassword
from MySQL_DB import db

class ImageUpdate(QMainWindow):
    def __init__(self):
        super(ImageUpdate, self).__init__()

        self.setWindowTitle("STUDENT IMAGE")
        self.setFixedSize(600, 320)
        self.setStyleSheet("background-color : rgb(34, 34, 34);")

        self.MainLabel = QLabel(self)
        self.MainLabel.setText("Update Student Image")
        self.MainLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                     "font: 20pt \"Cambria\";\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "text-decoration: underline;\n")
        self.MainLabel.setGeometry(QtCore.QRect(185, 20, 320, 30))

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

        self.imgLine = QLineEdit(self)
        self.imgLine.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 11pt \"Cambria\";\n"
                                   "background-color: rgb(74, 74, 74);\n"
                                   "border-radius : 10%")
        self.imgLine.setGeometry(QtCore.QRect(80, 160, 310, 30))

        self.selectPush = QPushButton(self)
        self.selectPush.setStyleSheet("background-color: rgb(158, 0, 2);\n"
                                     "border-radius : 15%;\n"
                                     "font: 10pt \"Cambria\";"
                                     "color: rgb(255, 255, 255);")
        self.selectPush.setText("SELECT IMAGE")
        self.selectPush.setGeometry(QtCore.QRect(400, 155, 120, 40))
        self.selectPush.clicked.connect(self.find)

        self.insertPush = QPushButton(self)
        self.insertPush.setStyleSheet("background-color: rgb(158, 0, 2);\n"
                                     "border-radius : 15%;\n"
                                     "font: 11pt \"Cambria\";"
                                     "color: rgb(255, 255, 255);")
        self.insertPush.setText("UPDATE IMAGE")
        self.insertPush.setGeometry(QtCore.QRect(210, 230, 180, 60))
        self.insertPush.clicked.connect(self.backend)

        self.show()

    def find(self):
        dialog = QFileDialog(self)
        fname = dialog.getOpenFileName(self, "Select Image File", "/", "Image files (*.png *.jpg *.jpeg)")[0]
        self.imgLine.setText(fname)

    def ShwSuc(self):
        msgBox = QMessageBox()
        msgBox.setFixedSize(400, 400)
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Image Updated Successfully")
        msgBox.setWindowTitle("SUCCESS")
    
        returnValue = msgBox.exec_()
        if returnValue == QMessageBox.Ok:
            pass
    
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
        def convertToBinaryData(filename):
            with open(filename, 'rb') as file:
                binaryData = base64.b64encode(file.read())
            return binaryData.decode()

        stuID = int(self.stuLine.text())
        size = (400, 400)
        img = Image.open(self.imgLine.text())
        if img.size != size:
            out = img.resize(size)
            out.save(self.imgLine.text())

        imgStr = convertToBinaryData(self.imgLine.text())

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
            qu = f"update image set IMAGE = '{imgStr}' where Student_ID = {stuID}"
            ImageCursor.execute(qu)
            database.commit()
            
            self.ShwSuc()
        
        elif status == False:
            self.ShwError()

        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ImageUpdate()
    sys.exit(app.exec_())