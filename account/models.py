from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user=models.OneToOneField(User,unique=True,on_delete=models.CASCADE,verbose_name="用户")
    birth=models.DateField(blank=True,null=True,verbose_name="生日")
    phone=models.CharField(max_length=20,null=True,verbose_name="手机号码")
    def __str__(self):
        return "<用户名:%s>" %self.user.username
class UserInfo(models.Model):
    user=models.OneToOneField(User,unique=True,on_delete=models.CASCADE,verbose_name="用户")
    school=models.CharField(max_length=100,null=True,blank=True,verbose_name="学校")
    company=models.CharField(max_length=100,null=True,blank=True,verbose_name="公司")
    profession=models.CharField(max_length=100,null=True,blank=True,verbose_name="职业")
    address = models.CharField(max_length=100,null=True, blank=True, verbose_name="住址")
    aboutme=models.TextField(blank=True,null=True,verbose_name="自我介绍",default="无")
    photo=models.ImageField(blank=True,verbose_name="头像")
    def __str__(self):
        return "<用户名:%s>" %self.user.username