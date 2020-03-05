"""
Definition of models.
"""

from django.db import models
# Create your models here.


class user(models.Model):
    objects = models.Manager()
    #账号 用户名 密码 注册时间 性别 简况 qq 电话 头像
    user_email = models.EmailField(primary_key = True)
    user_name = models.CharField(max_length = 32)
    password = models.CharField(max_length = 16)
    logon_time = models.DateField(auto_now_add = True)
    last_login = models.DateTimeField()
    user_sex = models.NullBooleanField()
    user_profile = models.CharField(max_length = 100)
    user_phonenum = models.IntegerField(null = True)
    user_head = models.ImageField(upload_to = "head",default="head/defaulthead.jpg")
    def __str__(self):
        return self.user_email
    class Meta:
        db_table = "user"

class attachment(models.Model):
    file = models.FileField(upload_to = 'upload')
    def __str__(self):
        return self.file.name

    class Meta:
        db_table = "attachment"

class Mymail(models.Model):
    objects = models.Manager()
    #生成唯一id
    mid = models.CharField(max_length = 32,default = '')
    #主题 内容 时间 接受者 发送者 是否删除 状态(成功与否) 阅读与否
    theme = models.CharField(max_length=20)
    content = models.CharField(max_length=1000)
    time = models.DateTimeField(auto_now_add = True)
    receiver = models.EmailField()
    sender = models.EmailField()
    isdelete = models.BooleanField(default = False)
    sendstatus = models.BooleanField(default = True)
    readstatus = models.BooleanField(default = False)
    files = models.ManyToManyField(attachment,related_name='files')
    def __str__(self):
        return self.theme
    class Meta:
        db_table = "mail"
        ordering = ["time"]

class friendlist(models.Model):
    objects = models.Manager()
    user_email = models.EmailField(primary_key = True)
    friendemail = models.CharField(max_length = 2000)
    def __str__(self):
        return self.user_email + "_friendlist"

    class Meta:
        db_table = "friendlist"