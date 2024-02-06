import sys
import copy
import os

from PyPDF2 import PdfWriter, PdfReader
from ui_form import Ui_MainWindow
from PySide6.QtWidgets import QTableWidgetItem
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtUiTools import QUiLoader

#TODO load data
#metadata new window
#PDF splitter new window
#Help page, first time starting



def mainwindow_setup(window):
    table_widget = window.tw_books
    table_widget.setColumnCount(7)

    data = [
                ['Item 1-1', 'Item 1-2', 'Item 1-3'],
                ['Item 2-1', 'Item 2-2', 'Item 2-3'],
                ['Item 3-1', 'Item 3-2', 'Item 3-3']
            ]

    table_widget.setHorizontalHeaderLabels(["On PC", "On device", "Author", "Title", "Year", "Size", "Publisher"])

    for row_data in data:
        row_position = table_widget.rowCount()
        table_widget.insertRow(row_position)
        for col, value in enumerate(row_data):
            item = QTableWidgetItem(value)
            table_widget.setItem(row_position, col, item)



if __name__ == "__main__":
    loader = QUiLoader()
    app = QtWidgets.QApplication(sys.argv)

    window = loader.load("form.ui", None)
    mainwindow_setup(window)
    window.show()

    app.exec()


