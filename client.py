# coding:utf-8
from __future__ import print_function
import socket
import hashlib
from Crypto.Cipher import AES
from code import DES, DES2, desdecode, desencode, encode
import base64

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
    c = desencode(line, '0f1571c947')
    return c


def communication(client):
    while True:
        a = raw_input("请输入要发送的内容")
        a = jiami_des(a)
        client.write(a + str("\r\n"))
        if a == str("1"):
            break


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


def client_process():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PROT))

    is_first = raw_input("是否为第一次登陆？")
    print(type(is_first))
    if is_first.lower() == "y":
        client_name = raw_input("请输入用户名!")
        # 绑定socket与fd
        fd = s.makefile("rw", 0)
        fd.write("f_" + client_name + "\r\n")
        while True:
            buf = fd.readline()
            if not len(buf):
                break
            print("收到了 " + buf)
            if buf.split(" ")[0] == "S/Key":
                seed = buf.split(" ")[1]
                m = buf.split(" ")[2].split('\n')[0]
                print("my seed " + seed)
                print(m)
                private_key = raw_input("请输入要创建的私钥，牢记！")
                private_kai = pre_treat(private_key, seed)
                first_hashed_result = hash_private_kai_of_m(private_kai, m)
                # 发送第一次hash之后的值
                fd.write(first_hashed_result + "\r\n")
                # 结束标志
                fd.write("\r\n")
            else:
                # 如果没收到S/Key开头的则断言错误
                assert NameError

        fd.close()

    elif is_first.lower() == "n":
        client_name = raw_input("请输入用户名!")
        # 绑定socket与fd
        fd = s.makefile("rw", 0)
        fd.write(client_name + "\r\n")
        while True:
            buf = fd.readline()
            if not len(buf):
                break
            print("收到了 " + buf)
            if buf.split(" ")[0] == "S/Key":
                seed = buf.split(" ")[1]
                m = buf.split(" ")[2].split('\n')[0]
                print("my seed " + seed)
                print(m)
                private_key = raw_input("请输入之前记住的私钥！")
                private_kai = pre_treat(private_key, seed)
                now_hashed_result = hash_private_kai_of_m(private_kai, m)
                # 发送输入的密钥预处理hash之后的值
                fd.write(now_hashed_result + "\r\n")
                test_success = fd.readline()
                if test_success[0] == "s":
                    print("恭喜老铁 ，登陆成功")
                    communication(fd)
                elif test_success[0] == "f":
                    print("输错密钥了老铁，耻辱下播！")
                else:
                    print("非法响应！")
                # 结束标志
                fd.write("\r\n")
                break
            else:
                # 如果没收到S/Key开头的则断言错误
                assert NameError
        fd.close()
    else:
        print("输入非法")
    s.close()


if __name__ == '__main__':
    client_process()
    # jiami("二十多")
