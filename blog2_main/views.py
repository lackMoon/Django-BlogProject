from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from .models import *
# Create your views here.
def home(request):
    return render(request,'blog_menu.html',{'title':'博客首页','home_active':'active'})

def blog_list(request):
    blogs=Blog.objects.all()
    types = Category.objects.all()
    paginator=Paginator(blogs,10)
    page_num=request.GET.get("page",1)
    page_blogs=paginator.get_page(page_num) #当前页的博客总数
    #设置分页页码范围
    current_page=page_blogs.number
    page_range=[x for x in range(int(current_page)-3,int(current_page)+2) if 0<x<=page_blogs.paginator.num_pages]
    if page_range[0]-3>1:
        page_range.insert(0,"...")
    if page_range[0]!=1:
        page_range.insert(0,1)
    return render(request,"blog_main/blog_list.html",{'page_blogs':page_blogs,'types':types,'title':'博客列表','blog_active':'active',"page_range":page_range})

def blog_details(request,id):
    blog=get_object_or_404(Blog,pk=id)
    previous_blog=Blog.objects.filter(created_time__gt=blog.created_time).last()
    next_blog=Blog.objects.filter(created_time__lt=blog.created_time).first()
    response=render(request,"blog_main/blog_detail.html",{'blog':blog,'previous_blog':previous_blog,'next_blog':next_blog,'title':'博客内容','blog_active':'active'})
    return response