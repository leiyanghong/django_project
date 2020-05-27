import json

from django import http
from django.shortcuts import render
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views import View


def hello_world(request):
    print("访问文件路径:", request.path)
    print("请求的方法:", request.method)
    print("请求的参数", request.body.decode('utf-8'))
    print(request.POST)
    return HttpResponse('{"code":2000,"msg":"请求成功"}')


def render_demo(request):
    # 响应一个html页面
    return render(request, "test.html", {"name": "hello!测开大佬们!!"})


class Project(View):
    def get(self, request,page,size):
        return HttpResponse("查询了一个项目{}{}".format(page,size))

    def post(self, request):
        # body_json_data = request.body.decode('utf-8')
        # user = json.loads(body_json_data)
        data = request.POST
        print(data)
        # username = user['username']
        # password = user['password']
        # with open("./user_file.txt", "r", encoding='utf-8')as file:
        #     s = [x.strip() for x in file.readlines()]
        #     data = [i.split(",") for i in s]
        #     for i in range(len(data)):
        #         if (username == data[i][0] and password == data[i][1]):
        #             return JsonResponse({"code": 200, "masge": "登录成功", "data": user})
        #         else:
        #             return JsonResponse({"code": 999, "masge": "登录失败", "data": user})
        return JsonResponse({"code": 200, "masge": "登录成功", "data": "null"})

    def put(self, request,page,size):
        return HttpResponse("修改了一个项目")

    def delete(self, request,page,size):
        return HttpResponse("删除了一个项目")

