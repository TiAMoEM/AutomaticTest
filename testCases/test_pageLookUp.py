import unittest
from common.logger import Logger
from common.browserEngine import BrowserEngine
from common.common import CommonUtil
from config.read_config import ReadConfig
import os

class TestPageLook(unittest.TestCase):

    def setUp(self):
        Logger().build_start_line("PageLookUp")
        Logger().print_log().info("start test")
        self.url = ReadConfig().get_url("URL")
        self.driver = BrowserEngine().open_browser()

    # @classmethod
    # def setUpClass(cls):
    #     cls.case_name = os.path.basename(__file__)[:-3]


    def check(self, expected_code=200):
        url = self.url
        status = CommonUtil().get_status(url)
        self.assertEqual(expected_code, status, "This page isn't normal, URL:%s" % url)

    def test_pageLookup01_mainPage(self):
        self.driver.get(self.url)
        # self.driver.add_cookie()
        self.driver.refresh()
        self.check()

    def tearDown(self):
        Logger().build_end_line("PageLookUp")
        BrowserEngine().quit_browser(self.driver)

if __name__ == '__main__':
    unittest.main()
