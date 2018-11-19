from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
app_name='account'
urlpatterns=[
    path('login/',auth_views.login,{"template_name":"account/login.html"},name="user_login"),
    path('logout/',auth_views.logout,{"template_name":"account/logout.html"},name="user_logout"),
    path('register/',views.register,name="user_register"),
    path('user-center/',views.user_center,name="user_center"),
    path('user-edit/',views.userinfo_edit,name="userinfo_edit"),
    path('user-image/',views.profile_photo,name="user_image"),
    path('pwd-change/',auth_views.password_change,{"template_name":"account/password_change.html","post_change_redirect":"/account/password_change_done"},name="pwd_change"),
    path('pwd-change-done/',auth_views.password_change_done,{"template_name":"account/password_change_done.html"},name="pwd_change_done"),
    path('pwd-reset/',include("password_reset.urls",namespace="pwd_reset")),
]