# -*- coding: utf-8 -*-

"""
Module implementing LoginInWindow.
"""

from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QMainWindow
import global_var
from PyQt4 import QtCore
from Ui_login_in import Ui_MainWindow


class LoginInWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    SendWordSignal = QtCore.pyqtSignal(str)

    def __init__(self, parent=None, username=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.network2 = global_var.get_network_client2()
        self.network2.printfSignal.connect(self.printEvent)
        self.lineEdit.setText(username)
    
    @pyqtSignature("")
    def on_pushButton_word_clicked(self):
        """
        Slot documentation goes here.
        """
        word =unicode(self.textEdit_word.toPlainText())
        self.SendWordSignal.emit(word)
        self.printEvent(u"发送："+word)

    def printEvent(self, line):
        self.textEdit_log.setText( unicode(self.textEdit_log.toPlainText()) + u'\n' + unicode(line))
