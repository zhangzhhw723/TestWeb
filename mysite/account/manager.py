# -*- coding: utf-8 -*-
# @Time : 2022/3/13 10:04 上午
# @Author : zhw
# @File : manager.py
from typing import List
from account.dao import UserDao
from account.models import User


class UserManager(object):
    @classmethod
    def query_user_by_name(cls, user_name: List[str]) -> List[User]:
        return UserDao.get_by_name(user_name)

    @classmethod
    def query_user_by_id(cls):
        pass

    @classmethod
    def query_user_by_mobile(cls):
        pass

    @classmethod
    def query_user_by_email(cls):
        pass

    @classmethod
    def create_user(cls):
        pass
