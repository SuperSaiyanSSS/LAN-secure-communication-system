# -*- coding: utf-8 -*-

"""
Module implementing SighUpWindow.
"""
from PyQt4 import QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QMainWindow

from Ui_sign_up import Ui_MainWindow


class SighUpWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
    
    @pyqtSignature("")
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        username = unicode(self.lineEdit.text())
        password = unicode(self.lineEdit_2.text())
        print username.encode("utf-8")
        print password
        print type(username.encode("utf-8"))