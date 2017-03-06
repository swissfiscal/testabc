#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)
        print  'test1'
    def test_something1(self):
        self.assertEqual(True, True)
        print  'test12'
    def test_something2(self):
        self.assertEqual(True, True)
        print  'test13'
    def test_something3(self):
        self.assertEqual(True, True)
        print  'test14'
    def test_something4(self):
        self.assertEqual(True, True)
        print  "测试".decode("utf8")
    def test_something5(self):
        self.assertAlmostEqual('你好', '你好1')
        # print  "测试".decode("utf8")


if __name__ == '__main__':
    unittest.main()
