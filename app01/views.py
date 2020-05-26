from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.urls import reverse


def hello(request):
    print("我是app01")
    print(reverse("app02:bye"))  # 可以使用"命名空间:路由名"的方式来解析url
    return HttpResponse('我是app01中的bye')

def login(request):
    return HttpResponse('登录成功')