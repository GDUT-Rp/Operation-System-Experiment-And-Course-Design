# -*- coding: utf-8 -*-
# @File   : yibu.py
# @Author : Runpeng Zhang
# @Date   : 2020/1/5
# @Desc   : None

from threading import Thread
from time import sleep


def async(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()

    return wrapper


@async
def A():
    sleep(3)
    print("函数A睡了3秒钟。。。。。。")
    print("a function")


def B():
    print("b function")


A()
B()
