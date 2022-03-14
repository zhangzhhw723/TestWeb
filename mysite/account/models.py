from django.db import models


# Create your models here.
class User(models.Model):
    # def __str__(self):
    #     return self.user_text

    # 用户账号状态：1为可用，0为冻结
    USER_ACTIVE = 1
    USER_FROZEN = 0
    USER = ((USER_ACTIVE, "active"), (USER_FROZEN, "frozen"))

    name = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=10, null=False)
    email = models.CharField(max_length=64, unique=True)
    mobile = models.CharField(max_length=32, default=None)
    status = models.SmallIntegerField(default=USER_ACTIVE, choices=USER)
    create_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
