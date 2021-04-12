from PyQt5.QtWidgets import QMessageBox
import os.path as path
import sys


def showError():
    msgBox = QMessageBox()
    msgBox.setFixedSize(400, 400)
    msgBox.setIcon(QMessageBox.Critical)
    msgBox.setText("No File Found 'MySQL_Password.txt'\nMake the file with the MySQL Password in it")
    msgBox.setWindowTitle("ERROR")
    
    returnValue = msgBox.exec_()
    if returnValue == QMessageBox.Ok:
        pass

def MySQLPassword():
    if path.exists("MySQL_Password.txt"):
        file = open("MySQL_Password.txt", "r")
        pa = file.read()
        file.close()

        return pa

    if not path.exists("MySQL_Password.txt"):
        showError()
        sys.exit()