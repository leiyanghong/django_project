import json
import re  # 导入正则模块

# 设置白名单,设置登录接口和注册接口
from django.http import HttpResponse
from requests import Response
from utils.token import *

white_list = ["v02/login/","v02/signup/"]
# 设置黑名单 设置的接口不会通过
black_list = ["v02/black/"]

class LoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # 配置和初始化

    def __call__(self, request):
        # 在这里编写视图和后面的中间件被调用之前需要执行的代码
        # 这里其实就是旧的process_request()方法的代码
        request_url = request.path_info  # 获取请求接口的url地址(获取的是地址不带ip和端口)
        # 使用正则匹配白名单是否相等
        for p in white_list:  # 遍历拿到白名单里面所有的数据
            r = re.compile(p)  # 利用compile编译每个数据,compile()与match()一起使用，可返回一个class、str、tuple。但是一定需要注意match()
            if r.match(request_url):  # 如果数据能跟接口的url地址能匹配到
                response = self.get_response(request)  # 获取响应结果
                return response  # 最后返回响应结果
        # 判断黑名单
        # 遍历拿到黑名单里面所有的数据
        for p in black_list:
            # 利用compile编译每个数据,compile()与match()一起使用，可返回一个class、str、tuple。但是一定需要注意match()
            r = re.compile(p)
            # 如果数据能跟接口的url地址能匹配到
            if r.match(request_url):
                # 实例化一个http响应对象,用来自定义响应数据
                response = HttpResponse()
                # 自定义response.content的内容,只能接受字符串类型的数据,所以要把json数据转换成字符串类型的数据
                response.content = json.dumps({"code":"9999","message":"请求内容非法","data":None})
                # 设置添加响应头,response是一个类字典数据,所以支持字典赋值操作,指定传入的参数必须为json格式,否则会报错
                response["Content-Type"] = "application/json;charset=utf-8"
                return response  # 最后返回响应结果
        # 获取本次请求里面所有的请求头信息 是一个Python字典
        # 因为META获取的key全部都是以"HTTP_后缀名(比如获取token)"大写,所以要获取请求头中token的数据要写成"HTTP_TOKEN"
        token = request.META.get("HTTP_TOKEN")  # 获取请求头中token的值
        # 校验token是否有效,为true就返回响应结果
        if check_token(token):
            response = self.get_response(request)  # 获取响应结果
            return response  # 最后返回响应结果
        # 反之 提示暂未登录或者token已过期
        else:
            response = HttpResponse()
            response.content = json.dumps({"code": "9999", "message": "暂未登录或token已过期", "data": None})
            response["Content-Type"] = "application/json;charset=utf-8"
            return response

        # 在这里编写视图调用后需要执行的代码
        # 这里其实就是旧的process_response()方法的代码



