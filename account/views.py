from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from .forms import *
from .models import *
# Create your views here.
def register(request):
    if request.method=="GET":
        user_form=RegisterForm()
        userprofile_form=UserProfileForm()
        userinfo_form=UserInfoForm()
        return render(request,'account/register.html',{"form":user_form,"profile":userprofile_form,"info":userinfo_form})
    if request.method=="POST":
        user_form=RegisterForm(request.POST)
        userprofile_form=UserProfileForm(request.POST)
        userinfo_form=UserInfoForm(request.POST)
        if user_form.is_valid() and userprofile_form.is_valid() and userinfo_form.is_valid():
            new_user=user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()
            new_profile=userprofile_form.save(commit=False)
            new_profile.user=new_user
            new_profile.save()
            new_info=userinfo_form.save(commit=False)
            new_info.user=new_user
            new_info.save()
            return HttpResponseRedirect("/account/login/")
        else:
            return HttpResponse("信息填写不完整，请重新填写")
@login_required(login_url="/account/login/")
def user_center(request):
    user=User.objects.get(username=request.user.username)
    userprofile=UserProfile.objects.get(user=user)
    userinfo = UserInfo.objects.get(user=user)
    return render(request,"account/user_center.html",{"title":"用户中心","user":user,"userprofile":userprofile,"userinfo":userinfo})

@login_required(login_url="/account/login/")
def userinfo_edit(request):
    user = User.objects.get(username=request.user.username)
    userprofile = UserProfile.objects.get(user=request.user)
    userinfo = UserInfo.objects.get(user=request.user)
    if request.method=="POST":
        user_form=UserForm(request.POST)
        userprofile_form=UserProfileForm(request.POST)
        userinfo_form=UserInfoForm(request.POST)
        if user_form.is_valid() and userprofile_form.is_valid() and userinfo_form.is_valid():
            user_cd=user_form.cleaned_data
            userprofile_cd=userprofile_form.cleaned_data
            userinfo_cd=userinfo_form.cleaned_data
            user.email=user_cd["email"]
            userprofile.birth=userprofile_cd["birth"]
            userprofile.phone = userprofile_cd["phone"]
            userinfo.school=userinfo_cd["school"]
            userinfo.company = userinfo_cd["company"]
            userinfo.profession = userinfo_cd["profession"]
            userinfo.address = userinfo_cd["address"]
            userinfo.aboutme = userinfo_cd["aboutme"]
            user.save()
            userprofile.save()
            userinfo.save()
            return HttpResponseRedirect("/account/user-center/")
        else:
            return HttpResponse("信息填写不完整，请重新填写")
    else:
        user_form=UserForm(instance=request.user)
        userprofile_form=UserProfileForm(initial={"birth":userprofile.birth,"phone":userprofile.phone})
        userinfo_form=UserInfoForm(initial={"school":userinfo.school,"company":userinfo.company,"profession":userinfo.profession,"address":userinfo.address,"aboutme":userinfo.aboutme})
        return render(request,"account/userinfo_edit.html",{"title":"信息编辑","user_form":user_form,"userprofile_form":userprofile_form,"userinfo_form":userinfo_form})
@login_required(login_url="/account/login/")
def profile_photo(request):
    if request.method=="POST":
        img=request.POST["img"]
        userinfo=UserInfo.objects.get(user=request.user)
        userinfo.photo=img
        userinfo.save()
        return HttpResponse("1")
    else:
        return render(request,"account/imagecrop.html")