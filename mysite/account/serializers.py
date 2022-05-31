# -*- coding: utf-8 -*-
# @Time : 2022/3/14 5:16 下午
# @Author : zhw
# @File : serializers.py
from rest_framework import serializers
from account.models import User


class AccountSerializers(serializers.Serializer):
    user_id = serializers.IntegerField(read_only=True)
    name = serializers
    password = serializers
    email = serializers
    mobile = serializers
    sex = serializers
    status = serializers
    create_time = serializers
    modified_time = serializers
