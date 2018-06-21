# -*- coding: utf-8 -*-
"""
保存可跨文件修改的真·全局变量的文件，而不是普通的不可被多个文件修改的全局变量
"""
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def set_username(user):
    global username
    username = user
    return username

def get_username():
    global username
    return username

def set_password(passwd):
    global password
    password = passwd
    return password

def get_password():
    global password
    return password


def set_network_client2(client):
    global networkclient2
    networkclient2 = client
    return networkclient2

def get_network_client2():
    global networkclient2
    return networkclient2

def set_queue(qw):
    global queue_word
    queue_word = qw
    return qw

def get_queue(qw):
    global queue_word
    return queue_word

