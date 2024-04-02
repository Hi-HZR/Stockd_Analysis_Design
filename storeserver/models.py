from django.db import models


# Create your models here.
class UserInfo(models.Model):
    uid = models.BigIntegerField(verbose_name="UID")
    name = models.CharField(max_length=20, verbose_name="名称")
    comment = models.TextField(verbose_name="评论")
    class Meta:
        verbose_name = '股票评论表'
        verbose_name_plural = verbose_name

class StorePoint(models.Model):
    point = models.FloatField(verbose_name="股票点数")
    time = models.DateField(verbose_name="时间")

    class Meta:
        verbose_name = '股票价格表'
        verbose_name_plural = verbose_name
