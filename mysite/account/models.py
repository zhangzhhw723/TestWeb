from django.db import models


# Create your models here.
class User(models.Model):
    # 用户账号状态：1为可用，0为冻结
    USER_ACTIVE = 1
    USER_FROZEN = 0
    USER = ((USER_ACTIVE, "active"), (USER_FROZEN, "frozen"))

    user_id = models.AutoField(primary_key=True, default=1)
    name = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=10, null=False)
    email = models.CharField(max_length=64, unique=True)
    mobile = models.CharField(max_length=32, default=None)
    sex = models.CharField(default=0, max_length=10)
    status = models.SmallIntegerField(default=USER_ACTIVE, choices=USER)
    create_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("user_id", )
