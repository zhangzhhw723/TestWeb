# -*- coding: utf-8 -*-
# @Time : 2022/3/14 3:59 下午
# @Author : zhw
# @File : urls.py
from django.urls import path
from . import views


urlpatterns = [
    path("", views.ProjectList.as_view(), name="project_list"),
    path(r"<int:pk>/")
]
