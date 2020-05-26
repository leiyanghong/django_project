from django.urls import path, include, reverse
from . import views

app_name = "app01"  # 子路由指定命名空间
urlpatterns = [

    path('hello/', views.hello, name="hello")  # name定义别名
]
