from django.db import models


# Create your models here.
class Stu(models.Model):
    '''
    max_length:限制字段最大长度
    null:False 不能为空
    help_text:备注的文本信息
    '''
    s_name = models.CharField('学生姓名', max_length=64, null=False, help_text='学生姓名')
    # choices:限制字段数据只能为0或者1
    s_sex = models.CharField("性别", max_length=1, choices=(
        (0, '男'),
        (1, '女')
    ), help_text='性别：0-男；1-女')
    # PositiveIntegerField:设置正整数的字段类型 0 ～ 2147483647
    # default:设置字段的默认值为0
    s_age = models.PositiveIntegerField('年龄', null=False, default=0, help_text='年龄')
    s_dept = models.CharField("专业", max_length=64, null=False, help_text="专业")
    '''
    ManyToManyField():多对多关联 
    to:设置要关联的表
    db_table:默认创建第三张表时，数据库中表的名称。
    related_name:同ForeignKey字段
    '''
    course = models.ManyToManyField(to="Course", db_table="stu_course", related_name="course_student")

    class Meta:
        db_table = 'stu'


class StudentInfo(models.Model):
    s_card = models.CharField("身份证号", max_length=18, null=False, unique=True)
    s_phone = models.CharField(max_length=11, null=False, unique=True, help_text="手机号")
    s_addr = models.CharField("家庭住址", max_length=128, help_text="家庭住址")
    # 一对一 to:表名 to_field:关联的表的字段  on_delete:同ForeignKey字段级联删除（默认） models.CASCADE:删除关联数据，与之关联也删除 related_name:反向查询字段
    s_id = models.OneToOneField(to='Stu', to_field="id", on_delete=models.CASCADE, db_column='s_id',
                                related_name="stu_info_stu")

    class Meta:
        db_table = "student_info"


class Course(models.Model):
    c_name = models.CharField('课程名', max_length=64, null=False, help_text="课程名")
    # 多对一
    t_id = models.ForeignKey(to="Teacher", to_field="id", on_delete=models.CASCADE, related_name='teacher_course',
                             db_column='t_id', help_text="老师编号")

    class Meta:
        db_table = "course"


class Score(models.Model):
    # 多对一
    s_id = models.ForeignKey(to="Stu", to_field="id", on_delete=models.CASCADE, related_name='stu_score',
                             db_column='s_id', help_text="学生编号")
    # 多对一
    c_id = models.ForeignKey(to="Course", to_field="id", on_delete=models.CASCADE, related_name='course_score',
                             db_column='c_id', help_text="学生编号")
    #
    score = models.PositiveIntegerField("成绩", null=False, default=0, help_text="成绩")

    class Meta:
        db_table = "score"


class Teacher(models.Model):
    t_name = models.CharField("老师姓名", max_length=64, null=False, help_text="老师姓名")

    class Meta:
        db_table = "teacher"
