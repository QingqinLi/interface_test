# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
import requests
from common.get_data import GetData
import pytest
import allure


class TestCommon:

    data = GetData().get_excel_data()
    print(data)

    @pytest.mark.parametrize(
        "mokuai, case_name, url, data_method, data, result_method, result",
        data
    )
    def test_excel_case(self, mokuai, case_name, url, data_method, data, result_method, result):
        # print(mokuai, case_name, url, data_method, data, result_method, result)
        # 应该再封装一个base, case层调用base的方法即可
        allure.description(mokuai+" "+case_name)
        if data_method == 'get':
            response = requests.get(url).json()
        elif data_method == 'post':
            # 格式化请求数据， 发送post请求
            params = data
            response = requests.post(url, data=params)
        else:
            raise TypeError("暂不支持此类型请求")
        if result_method == '包含':
            assert result in response
        elif result_method == '等于':
            assert result == response



