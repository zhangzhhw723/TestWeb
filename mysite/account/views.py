# from django.shortcuts import render
# from api.base_api import ProjectList
# from account.controller import UserController
from django.views import View
from django.http.response import JsonResponse
from .models import User
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from account.serializers import UserSerializer, GroupSerializer


# Create your views here.
# class AccountHandle(ProjectList):
#     def do_create_user(self, request, ):
#         user = UserController.add_user()
#         return
#     pass
"""
POST /user/创建用户
GET /user/获取所有用户信息

GET /user/<pk>获取一个用户信息
PUT /user/<pk>更新一个用户信息

DELETE 不提供

一个路由对应一个视图类，所以我们可以把5个API分为两个类来完成
"""
# class UserView(View):
#     def post(self, request):
#         """
#         添加一个用户信息
#         """
#         # 1. 接收客户端提交的数据
#         name = request.POST.get("name")
#         password = request.POST.get("password")
#         email = request.POST.get("email")
#         mobile = request.POST.get("mobile")
#         sex = request.POST.get("sex")
#         # status = request.POST.get("status")
#         create_time = request.POST.get("create_time")
#         modified_time = request.POST.get("modified_time")
#
#         # 1.1 验证客户端的数据
#
#         # 2. 操作数据库，保存数据
#         instance = User.objects.create(
#            name=name,
#            password=password,
#            email=email,
#            mobile=mobile,
#            sex=sex,
#            # status=status,
#            create_time=create_time,
#            modified_time=modified_time
#         )
#         # 3. 返回结果
#         return JsonResponse(
#             data={
#                 "id": instance.pk,
#                 "name": instance.name,
#                 "sex": instance.sex,
#                 "status": instance.status
#             },
#             status=201
#         )


class UserViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径。
    """
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    允许组查看或编辑的API路径。
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer