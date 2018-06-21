# -*- coding: utf-8 -*-

"""
Module implementing IndexDialog.
"""
from PyQt4 import QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QDialog

from Ui_index import Ui_Dialog
from sign_up import SighUpWindow



class IndexDialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
    
    @pyqtSignature("")
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.sign_up_window = SighUpWindow()
        self.sign_up_window.show()
    
    @pyqtSignature("")
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    dlg = IndexDialog()
    dlg.show()
    sys.exit(app.exec_())