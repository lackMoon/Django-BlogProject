from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.
@login_required(login_url="/account/login/")
@csrf_exempt
def article_column(request):
    if request.method=='GET':
        columns=ArticleColumn.objects.filter(user=request.user)
        column_form=ArticleColumnForm()
        return render(request,'article/article_column.html',{"columns":columns,"column_form":column_form,"column_active":"active"})
    if request.method=="POST":
        column_name=request.POST["column"]
        columns=ArticleColumn.objects.filter(user_id=request.user.id,column=column_name)
        if columns:
            return HttpResponse("0")
        else:
            ArticleColumn.objects.create(user=request.user,column=column_name)
            return HttpResponse("1")

@login_required(login_url="/account/login/")
@require_POST
@csrf_exempt
def rename_column(request):
    column_name=request.POST["column_name"]
    column_id=request.POST["column_id"]
    try:
        line=ArticleColumn.objects.get(id=column_id)
        line.column=column_name
        line.save()
        return HttpResponse("1")
    except:
        return HttpResponse("0")

@login_required(login_url="/account/login/")
@require_POST
@csrf_exempt
def del_column(request):
    column_id=request.POST["column_id"]
    try:
        line=ArticleColumn.objects.get(id=column_id)
        line.delete()
        return HttpResponse("1")
    except:
        return HttpResponse("0")
@login_required(login_url="/account/login/")
@csrf_exempt
def article_post(request):
    if request.method=="POST":
        article_form=ArticleForm(request.POST)
        if article_form.is_valid():
            cd=article_form.cleaned_data
            try:
                new_article=article_form.save(commit=False)
                new_article.author=request.user
                new_article.column=ArticleColumn.objects.get(id=request.POST["column_id"])
                new_article.save()
                return HttpResponse("1")
            except:
                return HttpResponse("0")
        else:
            return HttpResponse("-1")
    else:
        article_form=ArticleForm()
        article_columns=ArticleColumn.objects.filter(user=request.user)
        return render(request,"article/article_post.html",{"article_form":article_form,"article_columns":article_columns,"article_active":"active"})