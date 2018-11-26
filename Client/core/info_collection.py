#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Project: CMDB 
# Software: PyCharm2018.3
# DateTime: 2018-11-26 15:10
# File: info_collection.py
# __author__: 天晴天朗
# Email: tqtl@tqtl.org


import sys
import platform


def linux_sys_info():
    from plugins.linux import sys_info
    return sys_info.collect()


def windows_sys_info():
    from plugins.windows import sys_info as win_sys_info
    return win_sys_info.collect()


class InfoCollection(object):

    def collect(self):
        # 收集平台信息
        # 首先判断当前平台，根据平台的不同，执行不同的方法
        try:
            func = getattr(self, platform.system())
            info_data = func()
            formatted_data = self.build_report_data(info_data)
            return formatted_data
        except AttributeError:
            sys.exit("不支持当前操作系统： [%s]! " % platform.system())

    def Linux(self):

        return linux_sys_info()

    def Windows(self):
        return windows_sys_info()

    def build_report_data(self, data):
        # 留下一个接口，方便以后增加功能或者过滤数据
        return data
