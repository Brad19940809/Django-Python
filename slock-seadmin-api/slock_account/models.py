from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
import random


# from uuidfield import UUIDField
# import uuid
# from hashlib import md5
# import datetime;
# import random;
# nowTime=datetime.datetime.now().strftime("%Y%m%d%H%M%S");#生成当前时间
# randomNum=random.randint(0,100);#生成的随机整数n，其中0<=n<=100
# if randomNum<=10:
#     randomNum=str(0)+str(randomNum);
# uniqueNum=str(nowTime)+str(randomNum);
# print uniqueNum;


def make_id():
    now = timezone.now().strftime("%Y%m%d%H%M%S")
    num = random.randint(10, 100)
    id = now + str(num)
    return int(id)


class Account(models.Model):
    user = models.OneToOneField(User)
    update = models.DateTimeField(null=True)
    misc = models.TextField(null=True)


class AccessLog(models.Model):
    account = models.ForeignKey(Account)
    t = models.DateTimeField(default=timezone.now)
    ip = models.GenericIPAddressField(null=True)
    token = models.CharField(max_length=40)


class PasswordHistory(models.Model):
    account = models.ForeignKey(Account)
    t = models.DateTimeField(default=timezone.now)
    ip = models.GenericIPAddressField(null=True)
    password = models.CharField(max_length=32)


class Brad(models.Model):
    # id = models.BigAutoField(primary_key=True)
    # uid = UUIDField(auto=True,primary_key=True)
    uid = models.IntegerField(primary_key=True, default=make_id)
    name = models.CharField(max_length=128)
