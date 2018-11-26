#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Project: CMDB 
# Software: PyCharm2018.3
# DateTime: 2018-11-26 15:16
# File: urls.py
# __author__: 天晴天朗
# Email: tqtl@tqtl.org
from assets import views
from django.urls import path, re_path

# 配合实例命名空间
app_name = 'assets'

urlpatterns = [
    path('report/', views.report, name='report')
]
