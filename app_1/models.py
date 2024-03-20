from django.db import models


# Create your models here.
class UserInfo(models.Model):
    objects = None
    name = models.CharField(max_length=20, verbose_name="名称")
    comment = models.TextField(verbose_name="评论")
    uid = models.IntegerField(verbose_name="UID")


class Task(models.Model):
    title = models.TextField(verbose_name="标题")
    detail = models.TextField(verbose_name="详细信息")
