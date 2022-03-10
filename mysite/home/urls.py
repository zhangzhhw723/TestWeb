# -*- coding: utf-8 -*-
# @Time : 2022/2/28 4:23 下午
# @Author : zhw
# @File : urls.py.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
