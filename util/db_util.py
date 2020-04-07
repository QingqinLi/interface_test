# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
import pymysql


class DB:
    def __init__(self):
        self.host = 'localhost'
        self.port = 3306
        self.db = pymysql.connect(host=self.host, port=self.port, user="root", password="liqing", database='tool_platform')

    def get_case_data(self):
        # 使用cursor()方法获取操作游标
        cursor = self.db.cursor()

        sql = 'select `name`, `describe`, url, `request_data`, method, except_desc, except_content from interface_data where is_delete=True'
        # 使用execute方法执行SQL语句
        cursor.execute(sql)

        # 使用 fetchone() 方法获取一条数据
        data = cursor.fetchall()
        result_list = []
        # 关闭数据库连接
        if data:
            for i in data:
                result_list.append(i)
            self.db.close()
            return result_list
        else:
            self.db.close()
            return None


if __name__ == '__main__':
    db = DB()
    print(db.get_case_data())