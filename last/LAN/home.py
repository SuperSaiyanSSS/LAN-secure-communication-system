# -*- coding: utf-8 -*-

"""
Module implementing HomeDialog.
"""
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QDialog
import global_var


from Ui_home import Ui_Dialog
from main import NetWorkLoginIn, NetWorkSignUp


class HomeDialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    UserAndPasswordSignal = QtCore.pyqtSignal(list)

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


    @pyqtSignature("")
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # 实例化注册的线程
        self.network = NetWorkSignUp(self)
        self.network.start()

        username = unicode(self.lineEdit.text()).encode("utf-8")
        password = unicode(self.lineEdit_2.text()).encode("utf-8")

        self.UserAndPasswordSignal.emit([username, password])
        QtGui.QMessageBox.information(self, 'Message', u"注册成功！", QtGui.QMessageBox.Yes)

    @pyqtSignature("")
    def on_pushButton_2_clicked(self):
        """
        登录事件
        """
        # 实例化登录的线程
        self.network2 = NetWorkLoginIn(self)
        self.network2.start()
        global_var.set_network_client2(self.network2)

        username = unicode(self.lineEdit.text()).encode("utf-8")
        password = unicode(self.lineEdit_2.text()).encode("utf-8")
        # print username.encode("utf-8")
        # print password
        # print type(username.encode("utf-8"))


        from login_in import LoginInWindow
        self.logininwindow = LoginInWindow(username = unicode(self.lineEdit.text()))
        self.logininwindow.show()
        global_var.set_loginin_client(self.logininwindow)


        # 先出来页面再关。。
        self.UserAndPasswordSignal.emit([username, password])


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    dlg = HomeDialog()
    dlg.show()
    sys.exit(app.exec_())