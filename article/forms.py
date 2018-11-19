from django import forms
from django.contrib.auth.models import User
from .models import *
class ArticleColumnForm(forms.ModelForm):
    class Meta:
        model=ArticleColumn
        fields=("column",)
class ArticleForm(forms.ModelForm):
    class Meta:
        model=Article
        fields=("title","body")