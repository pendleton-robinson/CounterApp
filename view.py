# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'view.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_root(object):
    def setupUi(self, root):
        if not root.objectName():
            root.setObjectName(u"root")
        root.resize(500, 300)
        self.centralwidget = QWidget(root)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lblFrame = QGroupBox(self.centralwidget)
        self.lblFrame.setObjectName(u"lblFrame")
        self.lblFrame.setGeometry(QRect(0, 10, 471, 101))
        self.gridLayout = QGridLayout(self.lblFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.entEdit = QLineEdit(self.lblFrame)
        self.entEdit.setObjectName(u"entEdit")

        self.gridLayout.addWidget(self.entEdit, 2, 0, 1, 1)

        self.lblAmount = QLabel(self.lblFrame)
        self.lblAmount.setObjectName(u"lblAmount")
        self.lblAmount.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lblAmount.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lblAmount, 1, 0, 1, 1)

        self.btnFrame = QFrame(self.centralwidget)
        self.btnFrame.setObjectName(u"btnFrame")
        self.btnFrame.setGeometry(QRect(160, 120, 176, 44))
        self.btnFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.btnFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.btnFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnDecrement = QPushButton(self.btnFrame)
        self.btnDecrement.setObjectName(u"btnDecrement")

        self.horizontalLayout.addWidget(self.btnDecrement)

        self.btnIncrement = QPushButton(self.btnFrame)
        self.btnIncrement.setObjectName(u"btnIncrement")

        self.horizontalLayout.addWidget(self.btnIncrement)

        root.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(root)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 500, 22))
        root.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(root)
        self.statusbar.setObjectName(u"statusbar")
        root.setStatusBar(self.statusbar)

        self.retranslateUi(root)

        QMetaObject.connectSlotsByName(root)
    # setupUi

    def retranslateUi(self, root):
        root.setWindowTitle(QCoreApplication.translate("root", u"Counter", None))
        self.lblFrame.setTitle(QCoreApplication.translate("root", u"Counter", None))
        self.lblAmount.setText(QCoreApplication.translate("root", u"0", None))
        self.btnDecrement.setText(QCoreApplication.translate("root", u"-", None))
        self.btnIncrement.setText(QCoreApplication.translate("root", u"+", None))
    # retranslateUi

