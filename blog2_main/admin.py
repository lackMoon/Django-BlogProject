from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
	list_display=['title','blog_type','author','created_time','last_updated_time','content']
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display=['id','type_name']