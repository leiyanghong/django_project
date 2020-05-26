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
from django.urls import path
from django.urls import path ,re_path
from views_demo.views import hello_world, render_demo
from . import views
urlpatterns = [
    # path(‘admin/’, admin.site.urls),
    # re_path(r"^request[/]?$]",views.Project.as_view()),
    path('aaa/login/', hello_world),
    # path('bbb/', render_demo),
    # path('request/',views.Project.as_view()),
    # path("projects/<int:page>/<int:size>/",views.Project.as_view(),{"page":1,"size":5}),
    # re_path(r"^projects/(?P<page>[a-zA-Z1-9]+)/(?P<size>[a-zA-Z1-9]+).?$", views.Project.as_view()),  # 正则表达式的写法,
    re_path("projects/login/", views.Project.as_view()),  # 正则表达式的写法,

]



