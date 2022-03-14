# -*- coding: utf-8 -*-
# @Time : 2022/3/13 12:50 上午
# @Author : zhw
# @File : base_dao.py
class BaseDao(object):
    def get_user_by_name(self, _name: str):
        pass

    def get_user_by_id(self, _id: int):
        pass

    def get_user_by_mobile(self, _mobile):
        pass

    def get_user_by_email(self, _email):
        pass
