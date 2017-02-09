#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from sauceclient import SauceClient

desired_cap = {
    'platform': "Mac OS X 10.9",
    'browserName': "chrome",
    'version': "50",
}
driver = webdriver.Remote(
    command_executor='http://qazp:7a182ce9-a60c-4e08-b1c4-88123f2511fd@ondemand.saucelabs.com:80/wd/hub',
    desired_capabilities=desired_cap)
# driver.implicitly_wait(30)
# driver.get('http://testadmin.yumimobi.com/index.php/user/login?t=dff78159f3417ea40c2466b8917ad317ff')
# driver.quit()
class TestTravis():
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        # driver = webdriver.Chrome()
        driver.implicitly_wait(30)
        driver.get('http://testadmin.yumimobi.com/index.php/user/login?t=dff78159f3417ea40c2466b8917ad317ff')
        driver.quit()
		sauce_client = SauceClient("qazp", "7a182ce9-a60c-4e08-b1c4-88123f2511fd")
		assert 'a'=='b'