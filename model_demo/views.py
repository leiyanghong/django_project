import random
from django.core.paginator import Paginator
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
        # dict_list = []
        data = request.GET
        print(data["pagesize"])
        # for i in data:
        #     dict_list.append({i:data[i]})
        # print(dict_list)
        # student = Student.objects.filter(**dict_list[0])  # Paginator(Student.objects.filter(**dict_list[0]),per_page=10)

        # p = Paginator(Student.objects.all().values().order_by('id'), per_page=data["pagenum"]) # pagenum 设置每页展示多少条数据
        # data_list = []
        # for i in p.get_page(data["pagesize"]).object_list: # pagesize 查看第几页的数据
        #     data_list.append(i)

        p = Paginator(Student.objects.filter(s_name=data['name']).values().order_by("id"), per_page=data["pagenum"])
        data_list = []
        for i in p.get_page(data["pagesize"]).object_list:
            data_list.append(i)

        # data_list = []
        # for i in student:
        #     d={
        #         "name":i.s_name,
        #         "sex":i.s_sex,
        #         "phone":i.s_phone,
        #         "create_time":i.create_time,
        #         "update_time":i.update_time
        #     }
        #     data_list.append(d)
        return JsonResponse({"code":200,"msg":"查询成功","data":data_list},safe=False) #

    def post(self, request):
        student = json.loads(request.body)
        # student_list = []
        # for i in student:
        #     student_list.append(Student(s_name=i["name"],s_sex=i["sex"],s_phone=i["phone"]))
        student_list = [Student(s_name=i["s_name"],s_sex=i["s_sex"],s_phone=i["s_phone"]) for i in student]
        Student.objects.bulk_create(student_list)
        return JsonResponse({"code": 200, "masge": "新增成功","data":student},safe=False)

    def put(self, request):
        data = json.loads(request.body)
        students = Student.objects.filter(id=data["id"]).values()  # 筛选过滤满足传入的id值的数据
        data_list = []  # 获取修改的数据存进dict_list
        for i in students:
            data_list.append(i)
        # transaction.set_autocommit(False)
        students.update(**data)  # 根据传入的json数据,利用魔法传参的方式更新该条数据
        # s.save()  # 修改单个字段值,需要save
        # Student.objects.all().update(s_name="雷阳洪")
        # transaction.commit()  # 提交修改的操作
        # transaction.rollback()  # 如果报错就回滚
        return JsonResponse({"code": 200, "masge": "修改成功","data":data_list})

    def delete(self, request):
        data = json.loads(request.body)
        Student.objects.filter(id=data["id"]).delete()  # 根据传入的id值,删除指定数据的id数据
        return JsonResponse({"code": 200, "masge": "删除成功","data":data})

