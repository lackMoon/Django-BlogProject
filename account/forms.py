from django import forms
from django.contrib.auth.models import User
from .models import *
class RegisterForm(forms.ModelForm):
    password=forms.CharField(label="密码",widget=forms.PasswordInput)
    password2=forms.CharField(label="确认密码",widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=('username','email')
    def confirm_password(self):
        cd=self.cleaned_data
        if cd["password"]!=cd["password2"]:
            raise forms.ValidationError("两次输入的密码不一致")
        return cd["password2"]
class UserProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=('phone','birth')
class UserInfoForm(forms.ModelForm):
    class Meta:
        model=UserInfo
        fields=('school','company','profession','address','aboutme','photo')
#修改用户信息表单类
class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('email',)
