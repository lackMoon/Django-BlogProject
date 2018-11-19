from django.urls import path
from . import views
app_name='blog2_main'
urlpatterns=[
    path('list/',views.blog_list,name='list'),
    path('details/<int:id>/',views.blog_details,name='details'),
    path('',views.home,name='home'),
]