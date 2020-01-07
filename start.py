# -*- coding: UTF-8 -*-

import os
import unittest
import HTMLTestReportCN
import time
import logging
import common.logger

class Run:
    def __init__(self):
        self.case_path = os.path.join(os.getcwd(), "testcase")
        self.date = time.strftime("%Y%m%d")
        self.time = time.strftime("%Y%m%d%H%M%S")
        self.logger = common.logger.Logger()


    def run(self):
        try:
            print(self.logger.build_start_line("11111111111"))
        except Exception as e:
            self.logger.print_log().error(str(e))










if __name__ == "__main__":
    start = Run()
    start.run()






