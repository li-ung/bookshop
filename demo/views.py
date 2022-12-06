from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from . import send
from .models import *
import random
# Create your views here.


def toLogin_view(request):
    return render(request, 'login.html')


def Login_view(request):
    u = request.POST.get("user", '')
    p = request.POST.get("password", '')
    r = request.POST.get("role", '')

    if u and p:
        c = Users.objects.filter(name=u, psw=p, role=r).count()
        if c >= 1:
            if r == 'user':
                messages.success(request, '用户登录成功！')
                return render(request, 'index.html')
                # return HttpResponse("登录成功！")
            else:
                messages.success(request, '管理员登录成功！')
                return render(request, 'manager.html')
        else:
            if r:
                messages.error(request, '账号或密码错误！')
                return render(request, 'login.html')
                # return HttpResponse("账号或密码错误！")
            else:
                messages.error(request, '请选择角色！')
                return render(request, 'login.html')
    else:
        messages.error(request, '请输入正确的账号和密码！')
        return render(request, 'login.html')
        # return HttpResponse("请输入正确的账号和密码！")


def Send_view(request):
    n = "1"
    if n:
        send.sendone()
        return HttpResponse("发送成功")
    else:
        return HttpResponse("发送失败")


def toregister_view(request):
    return render(request, 'register.html')


# 点击注册后做的逻辑判断
def register_view(request):
    u = request.POST.get("user", '')
    p = request.POST.get("password", '')
    if u and p:
        user = Users(id=random.randrange(10001, 99999), name=u, psw=p, role='user')
        user.save()
        messages.success(request, '注册成功！')
        return render(request, 'login.html')
        # return HttpResponse("注册成功！")
    else:
        messages.success(request, '请输入完整的账号和密码！')
        return render(request, 'register.html')
        # return HttpResponse("请输入完整的账号和密码！")


def Index_view(request):
    return render(request, 'index.html')


def Shopcar_view(request):
    return render(request, 'shopcar.html')

def Manager_view(request):
    return render(request, 'manager.html')

def Shangjia_view(request):
    return render(request, 'shangjia.html')

def Xiajia_view(request):
    return render(request, 'xiajia.html')

def Bookdetail_view(request):
    return render(request, 'detail.html')