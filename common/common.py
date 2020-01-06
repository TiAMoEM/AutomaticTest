# -*- coding: UTF-8 -*-

import requests
import datetime
import time
import random


class CommonUtil:
    def __init__(self):
        pass

    def get_current_time(self):
        now = datetime.datetime.now()
        format = "%Y-%m-%d %H:%M:%S"
        return now.strftime(format)



