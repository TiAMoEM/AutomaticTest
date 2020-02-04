# -*- coding: UTF-8 -*-

import configparser
import codecs
import os

class ReadConfig:
    def __init__(self):
        self.config = configparser.ConfigParser()
        # self.config.read(os.path.join(os.getcwd(), "config.ini"))
        self.config_path = os.path.split(os.path.abspath(__file__))[0] + '/' + "config.ini"
        # 去除BOM，Windows下编码问题
        self.config.readfp(codecs.open(self.config_path, "r", "utf-8-sig"))

    def get_browser_type(self, name):
        return self.config.get("browserType", name)

    def get_url(self, name):
        return self.config.get("testServer", name)

    def get_account(self, name):
        return self.config.get("account", name)

if __name__ == "__main__":
    config = ReadConfig()
    print(config.get_url("URL"))
    print(config.get_account("login_cookie"))



