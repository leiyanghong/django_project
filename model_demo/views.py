import random

from django.db import transaction
from django.http import HttpResponse, JsonResponse
from django.views import View
import json
from model_demo.models import Student


def random_phone(request):
    # 第二位数字
    second = [3, 4, 5, 7, 8][random.randint(0, 4)]
    # 第三位数字
    third = {
        3: random.randint(0, 9),
        4: [5, 7, 9][random.randint(0, 2)],
        5: [i for i in range(10) if i != 4][random.randint(0, 8)],
        7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
        8: random.randint(0, 9),
    }[second]
    # 最后八位数字
    suffix = random.randint(9999999, 100000000)
    # 拼接手机号
    return HttpResponse("1{}{}{}".format(second, third, suffix))


class DataBase(View):
    def get(self, request):
        student = Student.objects.all()
        data_list = []
        for i in student:
            d={
                "id":i.id,
                "name":i.s_name,
                "sex":i.s_sex,
                "phone":i.s_phone,
            }
            data_list.append(d)
        return JsonResponse({"code":200,"msg":"查询成功","data":data_list},safe=False)

    def post(self, request):
        student = json.loads(request.body)
        # student_list = []
        # for i in student:
        #     student_list.append(Student(s_name=i["name"],s_sex=["sex"],s_phone=["phone"]))
        student_list = [Student(s_name=i["name"],s_sex=i["sex"],s_phone=i["phone"]) for i in student]
        Student.objects.bulk_create(student_list)
        return JsonResponse({"code": 200, "masge": "新增成功"})

    def put(self, request):
        students = Student.objects.all()
        data = json.loads(request.body)
        # transaction.set_autocommit(False)
        students.update(**data)
        # s.save()  # 修改单个字段值,需要save
        # Student.objects.all().update(s_name="雷阳洪")
        # transaction.commit()  # 提交修改的操作
        # transaction.rollback()  # 如果报错就回滚
        return JsonResponse({"code": 200, "masge": "修改成功"})

    def delete(self, request):
        Student.objects.all().delete()
        return JsonResponse({"code": 200, "masge": "删除成功"})

