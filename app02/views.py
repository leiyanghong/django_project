from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.urls import reverse

#
# def bye(request):
#     print("我是app02")
#     return HttpResponse("我是app02")

def bye(request):
    print(reverse("app01:hello")) # 可以使用"命名空间:路由名"的方式来解析url
    return HttpResponse('我是app02中的hello')