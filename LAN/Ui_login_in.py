# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'H:\py\newworkplace\LAN\login_in.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1138, 745)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.textEdit_log = QtGui.QTextEdit(self.centralWidget)
        self.textEdit_log.setGeometry(QtCore.QRect(670, 100, 381, 541))
        self.textEdit_log.setObjectName(_fromUtf8("textEdit_log"))
        self.textEdit_key = QtGui.QTextEdit(self.centralWidget)
        self.textEdit_key.setGeometry(QtCore.QRect(180, 100, 291, 61))
        self.textEdit_key.setObjectName(_fromUtf8("textEdit_key"))
        self.pushButton_key = QtGui.QPushButton(self.centralWidget)
        self.pushButton_key.setGeometry(QtCore.QRect(180, 210, 291, 71))
        self.pushButton_key.setObjectName(_fromUtf8("pushButton_key"))
        self.pushButton_word = QtGui.QPushButton(self.centralWidget)
        self.pushButton_word.setGeometry(QtCore.QRect(180, 560, 291, 71))
        self.pushButton_word.setObjectName(_fromUtf8("pushButton_word"))
        self.textEdit_word = QtGui.QTextEdit(self.centralWidget)
        self.textEdit_word.setGeometry(QtCore.QRect(180, 370, 291, 151))
        self.textEdit_word.setObjectName(_fromUtf8("textEdit_word"))
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton_key.setText(_translate("MainWindow", "PushButton", None))
        self.pushButton_word.setText(_translate("MainWindow", "PushButton", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

