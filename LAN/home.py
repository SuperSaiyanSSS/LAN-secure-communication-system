# -*- coding: utf-8 -*-

"""
Module implementing HomeDialog.
"""
from PyQt4 import QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QDialog
import global_var


from Ui_home import Ui_Dialog
from main import NetWorkLoginIn


class HomeDialog(QDialog, Ui_Dialog):
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
        # 设置密码模式
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.network2 = NetWorkLoginIn()
        global_var.set_network_client2(self.network2)

    @pyqtSignature("")
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError


    @pyqtSignature("")
    def on_pushButton_2_clicked(self):
        """
        登录事件
        """
        username = unicode(self.lineEdit.text()).encode("utf-8")
        password = unicode(self.lineEdit_2.text()).encode("utf-8")
        # print username.encode("utf-8")
        # print password
        # print type(username.encode("utf-8"))
        from main import NetWorkLoginIn
        from login_in import LoginInWindow
        self.logininwindow = LoginInWindow()
        self.logininwindow.show()

        self.network2.set_user_and_pwd(username, password)
      #  global_var.set_network_client2(self.network2)







if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    dlg = HomeDialog()
    dlg.show()
    sys.exit(app.exec_())