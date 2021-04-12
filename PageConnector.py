import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton, QLabel

from StudenInfo import StudentInfo
from FeeInfo import FeeInfo
from SubjectInfo import SubjectInfo
from PersonalInfo import PersonalInfo
from ImageConnector import ImageConn

class PageConnector(QMainWindow):
    def __init__(self):
        super(PageConnector, self).__init__()

        self.setWindowTitle("PAGE CONNECTOR")
        self.setFixedSize(900, 400)
        self.setStyleSheet("background-color : rgb(34, 34, 34);")

        self.MainLabel = QLabel(self)
        self.MainLabel.setText("PAGE CONNECTOR")
        self.MainLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                     "font: 20pt \"Cambria\";\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "text-decoration: underline;\n")
        self.MainLabel.setGeometry(QtCore.QRect(355, 20, 250, 30))

        self.stuPush = QPushButton(self)
        self.stuPush.setStyleSheet("background-color: rgb(158, 0, 2);\n"
                                     "border-radius : 20%;\n"
                                     "font: 11pt \"Cambria\";"
                                     "color: rgb(255, 255, 255);")
        self.stuPush.setText("STUDENT INFO")
        self.stuPush.setGeometry(QtCore.QRect(120, 110, 240, 70))
        self.stuPush.clicked.connect(self.redirect1)

        self.feePush = QPushButton(self)
        self.feePush.setStyleSheet("background-color: rgb(158, 0, 2);\n"
                                     "border-radius : 20%;\n"
                                     "font: 11pt \"Cambria\";"
                                     "color: rgb(255, 255, 255);")
        self.feePush.setText("FEE INFO")
        self.feePush.setGeometry(QtCore.QRect(550, 110, 240, 70))
        self.feePush.clicked.connect(self.redirect2)

        self.personalPush = QPushButton(self)
        self.personalPush.setStyleSheet("background-color: rgb(158, 0, 2);\n"
                                     "border-radius : 20%;\n"
                                     "font: 11pt \"Cambria\";"
                                     "color: rgb(255, 255, 255);")
        self.personalPush.setText("PERSONAL INFO")
        self.personalPush.setGeometry(QtCore.QRect(120, 280, 240, 70))
        self.personalPush.clicked.connect(self.redirect3)

        self.subjectPush = QPushButton(self)
        self.subjectPush.setStyleSheet("background-color: rgb(158, 0, 2);\n"
                                     "border-radius : 20%;\n"
                                     "font: 11pt \"Cambria\";"
                                     "color: rgb(255, 255, 255);")
        self.subjectPush.setText("SUBJECT INFO")
        self.subjectPush.setGeometry(QtCore.QRect(550, 280, 240, 70))
        self.subjectPush.clicked.connect(self.redirect4)

        self.imagePush = QPushButton(self)
        self.imagePush.setStyleSheet("background-color: rgb(158, 0, 2);\n"
                                     "border-radius : 20%;\n"
                                     "font: 11pt \"Cambria\";"
                                     "color: rgb(255, 255, 255);")
        self.imagePush.setText("IMAGE INFO")
        self.imagePush.setGeometry(QtCore.QRect(340, 195, 240, 70))
        self.imagePush.clicked.connect(self.redirect5)

        self.show()

    def redirect1(self):
            self.win = StudentInfo()
            self.win.show()

    def redirect2(self):
            self.win = FeeInfo()
            self.win.show()

    def redirect3(self):
            self.win = PersonalInfo()
            self.win.show()

    def redirect4(self):
            self.win = SubjectInfo()
            self.win.show()

    def redirect5(self):
            self.win = ImageConn()
            self.win.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = PageConnector()
    sys.exit(app.exec_())
