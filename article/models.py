from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ArticleColumn(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="用户")
    column=models.CharField(max_length=200,verbose_name="栏目")
    created_time=models.DateField(auto_now_add=True,verbose_name="创建时间")
    def __str__(self):
        return self.column
class Article(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="作者")
    title=models.CharField(max_length=200)
    column=models.ForeignKey(ArticleColumn,on_delete=models.CASCADE,verbose_name="所属栏目")
    body=models.TextField()
    created_time=models.DateTimeField(default=timezone.now,verbose_name="创建时间")
    updated_time=models.DateTimeField(auto_now_add=True,verbose_name="更新时间")
    class Meta:
        ordering=["-created_time"]
    def __str__(self):
        return self.title
