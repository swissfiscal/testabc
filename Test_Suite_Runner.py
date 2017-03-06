#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest

from pyunitttest import MyTestCase


class Test_Suite_Runner(unittest.TestCase):
    if __name__ == '__main__':
        # 手动构造测试集
        # suite = unittest.TestSuite()
        # suite.addTest(IOS_Log_Test("test_add_delete"))
        # # 执行测试
        # runner = unittest.TextTestRunner()
        # runner.run(suite)

        #testLoader方式构建测试机
        #此用法可以同时测试多个类
        suite1 = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
        suite = unittest.TestSuite([suite1,])
        unittest.TextTestRunner(verbosity=2).run(suite)