# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'converter.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_Converter(object):
    def setupUi(self, Converter):
        if not Converter.objectName():
            Converter.setObjectName(u"Converter")
        Converter.resize(800, 600)
        self.centralwidget = QWidget(Converter)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(240, 110, 321, 261))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.line = QFrame(self.verticalLayoutWidget_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.label = QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_2.addWidget(self.label, 0, Qt.AlignVCenter)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pb_browse = QPushButton(self.verticalLayoutWidget_2)
        self.pb_browse.setObjectName(u"pb_browse")
        self.pb_browse.setMinimumSize(QSize(100, 25))
        self.pb_browse.setMaximumSize(QSize(100, 25))

        self.horizontalLayout.addWidget(self.pb_browse)

        self.pb_convert = QPushButton(self.verticalLayoutWidget_2)
        self.pb_convert.setObjectName(u"pb_convert")
        self.pb_convert.setMinimumSize(QSize(100, 25))
        self.pb_convert.setMaximumSize(QSize(100, 25))

        self.horizontalLayout.addWidget(self.pb_convert)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.plainTextEdit = QPlainTextEdit(self.verticalLayoutWidget_2)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMaximumSize(QSize(200, 25))
        self.plainTextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.plainTextEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_2.addWidget(self.plainTextEdit, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.lb_work_done = QLabel(self.verticalLayoutWidget_2)
        self.lb_work_done.setObjectName(u"lb_work_done")

        self.verticalLayout_2.addWidget(self.lb_work_done, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        Converter.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Converter)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        Converter.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Converter)
        self.statusbar.setObjectName(u"statusbar")
        Converter.setStatusBar(self.statusbar)

        self.retranslateUi(Converter)

        QMetaObject.connectSlotsByName(Converter)
    # setupUi

    def retranslateUi(self, Converter):
        Converter.setWindowTitle(QCoreApplication.translate("Converter", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("Converter", u"Split PDF", None))
        self.pb_browse.setText(QCoreApplication.translate("Converter", u"Browse", None))
        self.pb_convert.setText(QCoreApplication.translate("Converter", u"Convert", None))
        self.plainTextEdit.setPlaceholderText(QCoreApplication.translate("Converter", u"Enter output filename", None))
        self.lb_work_done.setText(QCoreApplication.translate("Converter", u"TextLabel", None))
    # retranslateUi

