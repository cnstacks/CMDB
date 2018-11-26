#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Project: CMDB 
# Software: PyCharm2018.3
# DateTime: 2018-11-26 11:31
# File: main.py
# __author__: 天晴天朗
# Email: tqtl@tqtl.org
import os
import sys

BASE_DIR = os.path.dirname(os.getcwd())
sys.path.append(BASE_DIR)
from Client.core import handler

if __name__ == '__main__':
    handler.ArgvHandler(sys.argv)
