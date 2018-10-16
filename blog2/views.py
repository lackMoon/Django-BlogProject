from django.shortcuts import render
def home(request):
    return render(request,'blog_menu.html',{'title':'博客首页','home_active':'active'})