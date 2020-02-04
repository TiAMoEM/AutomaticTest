# -*- coding: UTF-8 -*-

import os
import config.read_config
import unittest
import time
import common.logger
import common.common
import HTMLTestReportCN

class Run:
    def __init__(self):
        self.case_path = os.path.join(os.getcwd(), "testcase")
        self.date = time.strftime("%Y%m%d")
        self.time = time.strftime("%Y%m%d%H%M%S")
        self.logger = common.logger.Logger()
        self.config = config.read_config.ReadConfig()
        self.report_path = os.path.abspath('') + r'/reports/'


    def run(self):
        try:
            self.logger.print_log().info("=======================================Begin Test=======================================")
            self.logger.print_log().info("测试URL: %s" % self.config.get_url("URL"))
            report_time = self.time
            report_file = self.report_path + "report_" + report_time + ".html"
            case_path = os.path.abspath('') + '/testCases'

            test_suit = unittest.TestSuite()
            discover = unittest.defaultTestLoader.discover(case_path, pattern='test_*.py')
            test_suit.addTest(discover)


            with open(report_file, "wb") as fp:
                runner = HTMLTestReportCN.HTMLTestRunner(stream=fp, title="kanzhun测试报告", description="用例测试情况")
                runner.run(test_suit)


        except Exception as e:
            self.logger.print_log().error(str(e))


if __name__ == "__main__":
    start = Run()
    start.run()






