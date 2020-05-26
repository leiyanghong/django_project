#!/usr/bin/env python
# -*- coding:utf-8 -*-
# leiyh
from django.http import HttpResponse


def hello_world(request):
    return HttpResponse("hello world")