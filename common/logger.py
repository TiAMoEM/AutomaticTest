# -*- coding: UTF-8 -*-

import logging
import os
import time

class Logger:
    def __init__(self):
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        log_time = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
        formatter = logging.Formatter('%(asctime)s-[%(filename)s][line:%(lineno)d][%(levelname)s] %(message)s')
        log_path = os.path.abspath('') + '/' + 'logs' + '/' + log_time + '/'
        if not os.path.exists(log_path):
            os.makedirs(log_path)
        log_file = log_path + log_time + '.log'

        fh = logging.FileHandler(log_file)
        fh.setLevel(logging.INFO)
        fh.setFormatter(formatter)
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(formatter)

        logger.addHandler(fh)
        logger.addHandler(ch)

        self.logger = logger
        self.log_path = log_path

    def build_start_line(self, case_name):
        """
        :param case_name:
        :return:
        """
        start_line = "***************************Begin to test testcase: %s ***************************" % case_name
        self.logger.info(start_line)

    def build_end_line(self, case_name):
        """
        :param case_name:
        :return:
        """
        end_line = "***************************End to test testcase: %s ***************************" % case_name
        self.logger.info(end_line)

    def print_log(self):
        return self.logger

    def get_log_path(self):
        return self.log_path

