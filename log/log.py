# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
import logging
import os
from common.settings import BASE_DIR


class Logger:
    def __init__(self):
        self.path = os.path.join(BASE_DIR, 'log/logs/interface.log')
        self.logger = logging.getLogger()
        fh = logging.FileHandler(self.path, 'a+', encoding='utf-8')
        sh = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s - %(lineno)t -%(filename)s -%(msg)s")
        fh.setFormatter(formatter)
        sh.setFormatter(formatter)
        self.logger.addHandler(fh)
        self.logger.addHandler(sh)

        fh.close()
        sh.close()

    def get_logger(self):
        return self.logger
