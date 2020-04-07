# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
import pytest
from util.db_util import DB
import allure
import requests


class TestDbCase:

    test_data = DB().get_case_data()

    @pytest.mark.parametrize(
        "name, describe, url, request_data, method, except_desc, except_content",
        test_data,
    )
    def test_db_interface(self, name, describe, url, request_data, method, except_desc, except_content):
        allure.description(name + " " + describe)
        if method == 'get':
            response = requests.get(url).text
            # print(response)
        elif method == 'post':
            # 格式化请求数据， 发送post请求
            params = request_data
            response = requests.post(url, data=params).text
        else:
            raise TypeError("暂不支持此类型请求")
        print(except_desc)
        if except_desc == 'contains':
            assert except_content in response
        elif except_desc == 'equal':
            assert except_content == response
        else:
            assert False is True
        # print(name, describe, url, request_data, method, except_desc, except_content)