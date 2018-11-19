from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
app_name='article'
urlpatterns=[
    path('article-column/',views.article_column,name="article_column"),
    path('rename-column/',views.rename_column,name="rename_column"),
    path('del-column/',views.del_column,name="del_column"),
    path('article-post/',views.article_post,name="article_post"),
]