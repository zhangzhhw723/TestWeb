# -*- coding: utf-8 -*-
# @Time : 2022/3/12 8:59 下午
# @Author : zhw
# @File : dao.py
from typing import List
from utils.base_dao import BaseDao
from account.models import User


class UserDao(BaseDao):
    # 数据库表取出
    @classmethod
    def get_by_name(cls, user_name: List[str]) -> List[User]:
        return User.objects.filter(name__in=user_name)
