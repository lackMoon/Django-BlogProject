from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(ArticleColumn)
class ArticleColumnAdmin(admin.ModelAdmin):
    list_display = ['user','column','created_time']
    list_filter = ["column",]