# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_one (unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_1(self):
        success = True
        wd = self.wd
        wd.get("https://account.nice.chat/accounts/login/?next=/")
        wd.find_element_by_id("id_login").click()
        wd.find_element_by_id("id_login").clear()
        wd.find_element_by_id("id_login").send_keys("nicetest1@ex.ua")
        wd.find_element_by_id("id_password").click()
        wd.find_element_by_id("id_password").click()
        wd.find_element_by_id("id_password").clear()
        wd.find_element_by_id("id_password").send_keys("Freeman123")
        wd.find_element_by_css_selector("button.button").click()
        wd.find_element_by_xpath("//span[@class='MenuNavUserBlockComponent-modules__user-status___1wZ2d']/i").click()
        wd.find_element_by_css_selector("button.MenuNavUserBlockComponent-modules__log-out-button___1Bl7v").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
