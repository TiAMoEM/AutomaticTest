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

    def get_status(self, url):
        r = requests.get(url=url, allow_redirects=False, verify=False)
        return r.status_code

    def window_scroll(self, driver, scroll_type=0):
        if scroll_type == 0:
            # 随机滑动
            num = random.randint(2, 5)  # 随机滚动次数
            for i in range(num):
                driver.execute_script("var q=document.documentElement.scrollTop=%d" % random.randint(50, 1000))
                time.sleep(2)
        elif scroll_type == 1:  # 匀速滚动
            # 向下滑动
            num = random.randint(100, 300)  # 随机滚动次数
            high = driver.get_window_size()['height']
            distance = high / num
            for i in range(num):
                driver.execute_script("var q=document.documentElement.scrollTop=%d" % distance)
                distance = distance + 10
                time.sleep(0.03)
        else:
            print("please select a scroll type.")

        # 最后滑动回到顶部
        js = "var q=document.documentElement.scrollTop=0"
        driver.execute_script(js)
        time.sleep(2)

