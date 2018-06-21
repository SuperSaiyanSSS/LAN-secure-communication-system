# coding: utf-8
from __future__ import print_function
import socket
import hashlib
from Crypto.Cipher import AES
from code import encode
from DES import desencode
import base64

from PyQt4 import QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore
import global_var

PROT = 5555
HOST = "localhost"

key = 0xff


def jiami_des(line):

    line = encode(line)
    # 如果长度不等于16的倍数，那么在前面填充0，使其到达16的倍数
    if len(line) % 16 != 0:
        print(len(line))
        line = line.zfill(16 * (len(line) / 16 + 1))
        print(">>")
        print(len(line))
    c = desencode(line, '11111111')
    return c


# 预处理
def pre_treat(private_key, seed):
    result = private_key + seed
    return result


def hash_private_kai_of_m(private_kai, m):
    m = int(m)
    while m != 0:
        # 创建的md5加密对象
        hash_object = hashlib.md5()
        hash_object.update(private_kai.encode(encoding='utf-8'))
        private_kai = hash_object.hexdigest()
        m -= 1
        print("aaa", private_kai)
    return private_kai


class NetWorkSignUp(QtCore.QThread):
    def __init__(self, parent=None):
        super(NetWorkSignUp, self).__init__(parent)
        self.parent = parent
        self.parent.UserAndPasswordSignal.connect(self.set_user_and_pwd)
        self.init_network()

    def run(self):
        pass

    def init_network(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((HOST, PROT))

    def set_user_and_pwd(self, username_password_list):
        username = username_password_list[0]
        password = username_password_list[1]
        # 绑定socket与fd
        self.fd = self.s.makefile("rw", 0)
        self.fd.write("f_" + username + "\r\n")
        buf = self.fd.readline()

        if not len(buf):
            assert KeyError

        print("收到了 " + buf)
        if buf.split(" ")[0] == "S/Key":
            seed = buf.split(" ")[1]
            m = buf.split(" ")[2].split('\n')[0]
            print("my seed " + seed)
            print(m)
            private_key = password
            private_kai = pre_treat(private_key, seed)
            first_hashed_result = hash_private_kai_of_m(private_kai, m)
            # 发送第一次hash之后的值
            self.fd.write(first_hashed_result + "\r\n")
            # 结束标志
            self.fd.write("\r\n")

        self.fd.close()


class NetWorkLoginIn(QtCore.QThread):
    # 不能放在__init__中 具体原因不明
    # 需指定返回的类型
    finishSignal = QtCore.pyqtSignal(str)
    printfSignal = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(NetWorkLoginIn, self).__init__(parent)
        self.parent = parent
        self.parent.UserAndPasswordSignal.connect(self.set_user_and_pwd)
        # 登陆成功/失败标志
        self.flag = False

    def run(self):
        self.init_network()

        pass

    def init_network(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((HOST, PROT))

    def set_user_and_pwd(self, username_password_list):
        username = username_password_list[0]
        password = username_password_list[1]
        # 绑定socket与fd
        self.fd = self.s.makefile("rw", 0)
        self.fd.write(username + "\r\n")
        buf = self.fd.readline()

        print("收到了 " + buf)
        if buf.split(" ")[0] == "S/Key":
            seed = buf.split(" ")[1]
            m = buf.split(" ")[2].split('\n')[0]
            self.printfSignal.emit("my seed " + seed)
            self.printfSignal.emit("the m is " + m)
           # print("my seed " + seed)
           # print(m)
            private_key = password
            private_kai = pre_treat(private_key, seed)
            now_hashed_result = hash_private_kai_of_m(private_kai, m)
            # 发送输入的密钥预处理hash之后的值
            self.fd.write(now_hashed_result + "\r\n")
            test_success = self.fd.readline()
            if test_success[0] == "s":
                self.printfSignal.emit(u"登录成功`")
                self.flag = True
                # self.communication(self.fd)
                self.logininclient = global_var.get_loginin_client()
                self.logininclient.SendWordSignal.connect(self.communication)
            elif test_success[0] == "f":
                self.printfSignal.emit(u"输错密钥了，请重新登录！！！")
                self.flag = False
            else:
                self.printfSignal.emit(u"非法相应")
                self.flag = False
            # 结束标志
                self.fd.write("\r\n")
        else:
            # 如果没收到S/Key开头的则断言错误
            assert NameError
      #  self.fd.close()

    def communication(self, word):
        print(word)
          #  a = raw_input("请输入要发送的内容")
        a = jiami_des(str(word))
        self.fd.write(a + str("\r\n"))
        # if a == str("1"):
        #     break


if __name__ == '__main__':
    pass