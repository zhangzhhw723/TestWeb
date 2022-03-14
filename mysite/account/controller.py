# -*- coding: utf-8 -*-
# @Time : 2022/3/12 9:00 下午
# @Author : zhw
# @File : controller.py
from account.models import User


# 这里主要写接口实现逻辑，从数据库存取数据等
class UserController(object):
    @classmethod
    def get_user_by_id(cls, user_id):
        pass

    @classmethod
    def get_user_name(cls, user_name):
        pass

    @classmethod
    def get_user_by_mobile(cls, mobile):
        pass

    @classmethod
    def get_user_by_email(cls, email):
        pass

    @classmethod
    def add_user(cls, name, password, mobile=None, email=None):
        # username和password不能为空
        user = User.objects.create(
            email=email,
            name=name,
            mobile=mobile,
            password=password
        )
        user.save()
        return user
