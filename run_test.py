# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
import pytest
import allure
import os
import time
from common.settings import BASE_DIR
from util.command import Command


class RunTest:
    def __init__(self):
        self.cmd = Command()
        self.time_stamp = str(int(time.time()))
        pass

    def run_test(self):
        test_dir = os.path.join(BASE_DIR, 'test_cases/')
        html_report = os.path.join(BASE_DIR, 'report/html_report/')
        html_report += self.time_stamp+'.html'
        allure_report = os.path.join(BASE_DIR, 'report/allure_report')
        allure_reports = os.path.join(BASE_DIR, 'report/allure_reports/')
        pytest.main([test_dir,
                     '-v',
                     '-s',
                     '--html='+html_report,
                     '--alluredir='+allure_reports,
                     ])
        cmd = "allure generate " + allure_reports +" -o "+allure_report+" -c"
        self.cmd.execute_cmd(cmd)


if __name__ == '__main__':
    runner = RunTest()
    runner.run_test()