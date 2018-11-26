#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Project: CMDB 
# Software: PyCharm2018.3
# DateTime: 2018-11-26 15:09
# File: settings.py
# __author__: 天晴天朗
# Email: tqtl@tqtl.org


import os

# 远端服务器配置
Params = {
    "server": "127.0.0.1",
    "port": 8000,
    'url': '/assets/report/',
    'request_timeout': 30,
}

# 日志文件配置

PATH = os.path.join(os.path.dirname(os.getcwd()), 'log', 'cmdb.log')