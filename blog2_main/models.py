from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.
class Category(models.Model):
	type_name=models.CharField(max_length=15,verbose_name="分类名")
	class Meta:
		verbose_name="分类"
		verbose_name_plural=verbose_name
	def __str__(self):
		return self.type_name
class Blog(models.Model):
	title=models.CharField(max_length=50,verbose_name="标题")
	blog_type=models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name="博客分类")
	author=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="作者")
	content = RichTextField(verbose_name="内容")
	created_time=models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
	last_updated_time=models.DateTimeField(auto_now=True,verbose_name="更新时间")
	class Meta:
		verbose_name="博客"
		verbose_name_plural = verbose_name
		ordering=["-created_time"]
	def __str__(self):
		return "<博客:%s>" %self.title
	def get_read_num(self):
		try:
			return self.readnum.read_num
		except Exception as e:
			return 0;
