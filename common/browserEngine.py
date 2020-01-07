# coding=utf-8

from selenium import webdriver
from config.read_config import ReadConfig
from common import logger

class BrowserEngine(object):
    read_config = ReadConfig()
    browser_type = read_config.get_browser_type('chrome')

    def __init__(self, driver):
        self.driver = driver
        self.logger = logger.Logger().print_log()

    def open_browser(self):
        self.logger.info("使用%s浏览器", self.browser_type)
        self.logger.info("打开浏览器")

        if self.browser_type == "FireFox":
            driver = webdriver.Firefox()
        elif self.browser_type == "IE":
            driver = webdriver.Ie()
        else:
            driver = webdriver.Chrome()

        self.logger.info(u"最大化浏览器")
        driver.maximize_window()
        self.logger.info(u"设置隐式时间等待")
        driver.implicitly_wait(10)
        return driver

