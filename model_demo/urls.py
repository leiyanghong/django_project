from django.urls import path ,re_path
from . import views

urlpatterns = [
    # reverse("v01:hello"),  # 根据命名空间去访问v01里面为hello的方法
    path('phone/', views.random_phone),  # 定义别名random_phone
    re_path("database/", views.DataBase.as_view()),
]

