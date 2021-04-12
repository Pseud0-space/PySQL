from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton, QLabel

import sys

from InsertImage import ImageStore
from DisplayImage import ImageDisplay
from UpdateImage import ImageUpdate


class ImageConn(QMainWindow):
    def __init__(self):
        super(ImageConn, self).__init__()

        self.setWindowTitle("IMAGE INFORMATION")
        self.setFixedSize(758, 240)
        self.setStyleSheet("background-color : rgb(34, 34, 34);")

        self.MainLabel = QLabel(self)
        self.MainLabel.setText("Image Page Connector")
        self.MainLabel.setStyleSheet("background-color: rgb(34, 34, 34);\n"
                                     "font: 20pt \"Cambria\";\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "text-decoration: underline;\n")
        self.MainLabel.setGeometry(QtCore.QRect(255, 20, 320, 30))

        self.insertPush = QPushButton(self)
        self.insertPush.setStyleSheet("background-color: rgb(158, 0, 2);\n"
                                     "border-radius : 20%;\n"
                                     "font: 11pt \"Cambria\";"
                                     "color: rgb(255, 255, 255);")
        self.insertPush.setText("INSERT IMAGE")
        self.insertPush.setGeometry(QtCore.QRect(90, 120, 180, 60))
        self.insertPush.clicked.connect(self.redirect1)

        self.showPush = QPushButton(self)
        self.showPush.setStyleSheet("background-color: rgb(158, 0, 2);\n"
                                     "border-radius : 20%;\n"
                                     "font: 11pt \"Cambria\";"
                                     "color: rgb(255, 255, 255);")
        self.showPush.setText("SHOW IMAGE")
        self.showPush.setGeometry(QtCore.QRect(290, 120, 180, 60))
        self.showPush.clicked.connect(self.redirect2)

        self.updatePush = QPushButton(self)
        self.updatePush.setStyleSheet("background-color: rgb(158, 0, 2);\n"
                                     "border-radius : 20%;\n"
                                     "font: 11pt \"Cambria\";"
                                     "color: rgb(255, 255, 255);")
        self.updatePush.setText("IMAGE UPDATER")
        self.updatePush.setGeometry(QtCore.QRect(490, 120, 180, 60))
        self.updatePush.clicked.connect(self.redirect3)

        self.show()

    def redirect1(self):
            self.win = ImageStore()
            self.win.show()

    def redirect2(self):
            self.win = ImageDisplay()
            self.win.show()

    def redirect3(self):
            self.win = ImageUpdate()
            self.win.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ImageConn()
    sys.exit(app.exec_())