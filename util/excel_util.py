# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
import xlrd
from xlutils import copy


class ExcelUtil:
    def __init__(self, path=None, index=None):
        if path:
            self.path = path
        else:
            self.path = '/Users/qing.li/PycharmProjects/hm/selenium_/imooc/common/data_case.xlsx'
        # 表单
        if not index:
            self.index = 0
        else:
            self.index = index
        self.data = xlrd.open_workbook(self.path)
        self.table = self.data.sheets()[self.index]

    def get_data(self):
        result = []
        lines = self.get_lines()
        if lines:
            for i in range(lines):
                line = self.table.row_values(i)
                result.append(tuple(line))
            return result
        else:
            return None

    def get_col_value(self, row, col):
        """
        获取单元格的数据
        :param row:
        :param col:
        :return:
        """
        if self.get_lines() > row:
            data = self.table.cell(row, col).value
            return data
        return None

    def get_lines(self):
        row = self.table.nrows
        if row >= 1:
            return row
        else:
            return 0

    def write_data(self, row, col, data):
        """
        在单元格写入数据
        :param col:
        :param row:
        :param data:
        :return:
        """
        read_value = xlrd.open_workbook(self.path)
        write_data = copy(read_value)
        write_data.get_sheet(self.index).write(row, col, data)
        write_data.save(self.path)


if __name__ == '__main__':
    excel = ExcelUtil("/Users/qing.li/Desktop/thrid_case.xlsx")
    print(excel.get_data())




