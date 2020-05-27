from django.db import models

from django.db.models import Model


class Student(models.Model):
    s_name = models.CharField(max_length=64,help_text="学生姓名")  # 字符串类型
    s_sex = models.IntegerField(choices=((0, '男'), (1, '女')), help_text="性别")  # 数字类型 限制数字只能有0或者1
    s_phone = models.CharField(max_length=11, help_text="手机号")  # 字符串类型 限制字段长度11位
    # auto_now_add=True 在每一次数据被添加进去的时候，记录当前时间
    create_time = models.DateTimeField(auto_now_add=True)
    # auto_now=True 在每一次数据被保存的时候，记录当前时间
    update_time = models.DateTimeField(auto_now=True)
    # models.ForeignKey # 设置外键约束
    # models.AutoField  # 自动设置数字自增类型
    # models.IntegerField  # 数字类型
    # models.DateField  # data 数据类型
    # models.DateTimeField  # 日期类型
    # models.TextField  # 文本类型