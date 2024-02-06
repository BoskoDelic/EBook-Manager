import sys
import copy
import os
from PyPDF2 import PdfWriter, PdfReader
from ui_form import Ui_MainWindow
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtUiTools import QUiLoader

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py


def mainwindow_setup(window):
    window.setWindowTitle("EBook Manager")


if __name__ == "__main__":
    loader = QUiLoader()
    app = QtWidgets.QApplication(sys.argv)

    window = loader.load("form.ui", None)
    mainwindow_setup(window)
    window.show()

    app.exec()


