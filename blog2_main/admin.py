from django.contrib import admin
from .models import *
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
	list_display=['title','blog_type','author','created_time','last_updated_time','content']
class CategoryAdmin(admin.ModelAdmin):
	list_display=['id','type_name']
admin.site.register(Blog,BlogAdmin)
admin.site.register(Category,CategoryAdmin)