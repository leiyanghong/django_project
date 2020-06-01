"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include

from django_project.view import hello_world
from . import view

urlpatterns = [
    path('login/', view.hello_world),
    path('test/', include("views_demo.urls")), # 指定子路由路径为test/
    # 使用include分发路由的时候，给每个子路由指定一个命名空间，这样就可以区分出每个子路由中的同名路由了
    path('v01/',include("app01.urls",namespace='app01')),  # 主路由分发子路由路径为v01/  ,namespace='v01'
    path('v02/',include("app02.urls",namespace='app02')),  # 主路由分发子路由路径为v02/  ,namespace='v02'
    path('model/',include('model_demo.urls')),
]
