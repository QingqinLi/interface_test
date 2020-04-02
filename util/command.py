# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
import os
import subprocess
from common.settings import BASE_DIR


class Command:
    def __init__(self):
        pass

    def execute_cmd(self, cmd):
        log_file = os.path.join(BASE_DIR, 'log/logs/cmd.log')
        subprocess.Popen(cmd, shell=True, stdout=open(log_file, 'a+'), stderr=subprocess.STDOUT)

    def execute_cmd_result(self, cmd):
        result_list = []
        result = os.popen(cmd).readlines()
        for i in result:
            if i == '\n':
                pass
            else:
                result_list.append(i.strip("\n"))
        return result_list


if __name__ == '__main__':
    cmd = Command()
    print(cmd.execute_cmd_result("ls"))

