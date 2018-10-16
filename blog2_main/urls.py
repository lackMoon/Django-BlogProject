from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^list/',views.blog_list),
    url(r'^details/(\d+)',views.blog_details)
]