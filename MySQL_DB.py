from PyQt5.QtWidgets import QMessageBox
import os.path as path
import sys


def showError():
    msgBox = QMessageBox()
    msgBox.setFixedSize(400, 400)
    msgBox.setIcon(QMessageBox.Critical)
    msgBox.setText("No File Found 'MySQL_DB.txt'\nMake the file with the Database Name in it")
    msgBox.setWindowTitle("ERROR")
    
    returnValue = msgBox.exec_()
    if returnValue == QMessageBox.Ok:
        pass

def db():
    if path.exists("MySQL_DB.txt"):
        file = open("MySQL_DB.txt", "r")
        DB = file.read()
        file.close()

        return DB

    if not path.exists("MySQL_DB.txt"):
        showError()
        sys.exit()
