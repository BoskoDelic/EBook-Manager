import sys
import copy
import os
from PyPDF2 import PdfWriter, PdfReader
from ui_form import Ui_MainWindow
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtUiTools import QUiLoader
import time


def mainwindow_setup(window):
    pass


if __name__ == "__main__":
    loader = QUiLoader()
    app = QtWidgets.QApplication(sys.argv)

    window = loader.load("form.ui", None)
    mainwindow_setup(window)
    window.show()

    app.exec()


