from django.urls import path, include, reverse
from . import views

app_name = "app02"  # 子路由指定命名空间
urlpatterns = [
    # reverse("v01:hello"),  # 根据命名空间去访问v01里面为hello的方法
    path('bye/', views.bye, name="bye"),  # 定义别名bye
]
