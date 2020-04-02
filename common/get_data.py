# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
from util.excel_util import ExcelUtil


class GetData:
    def __init__(self):
        self.excel = ExcelUtil("/Users/qing.li/Desktop/thrid_case.xlsx")

    def get_excel_data(self):
        # 去掉表头
        result = self.excel.get_data()[1:]
        return result


