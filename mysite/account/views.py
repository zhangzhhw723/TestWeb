from django.shortcuts import render
from api.base_api import ProjectList
from account.controller import UserController

# Create your views here.
class AccountHandle(ProjectList):
    def do_create_user(self, request, ):
        user = UserController.add_user(

        )
        return
    pass
