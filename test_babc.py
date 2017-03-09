#!/usr/bin/python
# -*- coding: utf-8 -*-
from BaseClass import *
from test_aabc import *
from test_abc import *
class test_babc(BaseClass):
    def test_aaa(self):
        logging.info('aaaa')
    def test_cccc(self):
        logging.info('cccc')
    def test_abbb(self):
        logging.info('bbbbb')
    def test_dddd(self):
        logging.info('dddd')

if __name__ == '__main__':
    # suite = unittest.TestSuite()
    # suite.addTest(testbabc("test_aaa"))
    # suite.addTest(testbabc("test_cccc"))
    # suite.addTest(testbabc("test_abbb"))
    # suite.addTest(testbabc("test_dddd"))
    # suite.addTest(testaabc("test_dddd"))
    # suite.addTest(testaabc("test_aaa"))
    # suite.addTest(testabc("test_abbb"))
    # suite.addTest(testabc("test_aaa"))
    # # 执行测试
    # runner = unittest.TextTestRunner()
    # runner.run(suite)

    #testLoader方式构建测试机
    #此用法可以同时测试多个类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(test_aabc)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(test_abc)
    suite3 = unittest.TestLoader().loadTestsFromTestCase(test_babc)
    suite = unittest.TestSuite([suite3,suite2,suite1])
    unittest.TextTestRunner(verbosity=2).run(suite)