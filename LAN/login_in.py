# -*- coding: utf-8 -*-

"""
Module implementing LoginInWindow.
"""

from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QMainWindow
import global_var
from Ui_login_in import Ui_MainWindow


class LoginInWindow(QMainWindow, Ui_MainWindow):
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
        self.network2 = global_var.get_network_client2()
        self.network2.printfSignal.connect(self.printEvent)

    
    @pyqtSignature("")
    def on_pushButton_key_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSignature("")
    def on_pushButton_word_clicked(self):
        """
        Slot documentation goes here.
        """
        word =unicode(self.textEdit_word.toPlainText()).encode('utf-8')

    def printEvent(self, line):
        self.textEdit_log.setText( unicode(self.textEdit_log.toPlainText()) + u'\n' + unicode(line))
