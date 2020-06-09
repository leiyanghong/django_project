import json

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from utils.token import *
from django.http import HttpResponse, JsonResponse
from django.urls import reverse

#
# def bye(request):
#     print("我是app02")
#     return HttpResponse("我是app02")
from django.views import View


def bye(request):
    print(reverse("app01:hello")) # 可以使用"命名空间:路由名"的方式来解析url
    return HttpResponse('我是app02中的hello')

class Login(View):
    def post(self,request):
        data = json.loads(request.body)
        username = data.get("username", None)
        password = data.get("password", None)
        # 验证用户名密码需要用到Django自带的函数,如果校验成功,会返回一个user对象,校验失败会返回一个None
        user = authenticate(username=username,password=password)  # 校验用户名和密码,成功返回user对象,失败返回None
        # 不为空 登录成功
        if user:
            token = create_token(user.username)
            # 返回jsonresponse
            return JsonResponse({"code": "0000", "message": "登录成功", "data": token})
        # 为空 登录失败
        else:
            return JsonResponse({"code": "9999", "message": "登录失败,用户名或密码不正确", "data": None})




class Signup(View):
    def post(self,request):
        data = json.loads(request.body)
        print(data)
        username = data.get("username",None)
        print(username)
        password = data.get("password",None)
        email =  data.get("email",None)
        # 判断用户名是否存在,存在添加失败,不存在添加成功
        try:
            # 利用Django自带的User模块create_user()方法去创建用户 并且返回一个user对象
            user= User.objects.create_user(username=username,password=password,email=email)
            # 创建token  user.username获取user对象的username
            token = create_token(user.username)
            # 返回jsonresponse
            return JsonResponse({"code":"0000","message":"注册成功","data":token})
        except:
            return JsonResponse({"code": "9999", "message": "注册失败,用户已存在或者信息头缺失", "data": None})

