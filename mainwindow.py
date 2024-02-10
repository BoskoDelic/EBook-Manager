import sys
import copy
import os
from PyPDF2 import PdfWriter, PdfReader
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QMainWindow
from PySide6.QtUiTools import QUiLoader
from ui_mainwindow import Ui_MainWindow

#GET UI FILE
#pyside6-uic mainwindow.ui -o ui_mainwindow.py

#TODO
#change to OOP
#design UI files
#load data
#metadata new window
#PDF splitter new window
#Help page, first time starting

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


def mainwindow_setup(window):
    window.setWindowTitle("EBook Manager")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


