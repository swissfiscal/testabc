#!/usr/bin/python
# -*- coding: utf-8 -*-
# import  logging
# #默认情况下，logging将日志打印到屏幕，日志级别为WARNING；
# # 日志级别大小关系为：CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET
# import sys
#
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(filename)s [line:%(lineno)d] [%(levelname)s]  %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S',
#                     filename='myapp.log',
#                     filemode='w')
# #定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
# console = logging.StreamHandler()
# console.setLevel(logging.DEBUG)
# formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# console.setFormatter(formatter)
# logging.getLogger('').addHandler(console)
#
#
# logging.debug('This is debug message')
# logging.info('This is info message')
# logging.warning('This is warning message')

import logging.config
import os,stat
import unittest
import sys
class BaseClass(unittest.TestCase):
    # os.chdir(os.path.dirname(os.path.dirname(os.getcwd())))
    # print  os.getcwd()
    # logging.config.fileConfig("conf/logger.conf")
    # logger = logging.getLogger("example01")
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    # print BASE_DIR
    LOG_DIR = os.path.join(BASE_DIR, "logs")
    # print LOG_DIR

    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)  # 创建路径
    os.chmod(LOG_DIR,stat.S_IWGRP)
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)s %(funcName)s [line:%(lineno)d]  [%(levelname)s] %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        filename=LOG_DIR+'/myapp.log',
                        filemode='a+')
    #定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    # formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    formatter = logging.Formatter('%(asctime)s %(filename)s %(funcName)s [line:%(lineno)d]  [%(levelname)s] %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
    # logging.debug('This is debug message')
        # logger.info('This is info message')
        # logger.warning('This is warning message')

        # logger = logging.getLogger("example02")
        # logger.debug('This is debug message')
        # logger.info('This is info message')
        # logger.warning('This is warning message')
# class cde(abc):
#     def test_abc(self):
#         logging.debug("def")
if __name__ == '__main__':
   unittest.main()