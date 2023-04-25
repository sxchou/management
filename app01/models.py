from django.db import models


# Create your models here.
class Admin(models.Model):
    """管理员"""
    username = models.CharField(verbose_name='用户名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=64)

    def __str__(self):
        return self.username


class Department(models.Model):
    """ 部门表 """
    department_name = models.CharField(verbose_name='部门名称', max_length=32)

    def __str__(self):
        return self.department_name


class UserInfo(models.Model):
    """ 员工表 """
    name = models.CharField(verbose_name='姓名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=64)
    age = models.SmallIntegerField(verbose_name='年龄')
    account = models.DecimalField(verbose_name='账户余额', max_digits=8, decimal_places=2, default=0.00)
    create_date = models.DateField(verbose_name='入职日期')
    depart = models.ForeignKey(verbose_name='所属部门', to='Department', to_field='id', on_delete=models.CASCADE)
    gender_choices = (
        (1, '男'),
        (2, '女'),
    )
    gender = models.SmallIntegerField(verbose_name='性别', choices=gender_choices)


class PrettyNum(models.Model):
    """靓号管理"""
    mobile = models.CharField(verbose_name='手机号', max_length=11, unique=True)
    price = models.DecimalField(verbose_name='价格', max_digits=8, decimal_places=2, default=0.00)
    level_choices = (
        (1, '一级'),
        (2, '二级'),
        (3, '三级'),
        (4, '四级'),
        (5, '五级'),
    )

    level = models.SmallIntegerField(verbose_name='级别', choices=level_choices, default=1)
    status_choices = (
        (1, '已占用'),
        (2, '未使用'),
    )
    status = models.SmallIntegerField(verbose_name='状态', choices=status_choices, default=2)


class Order(models.Model):
    """ 订单 """
    oid = models.CharField(verbose_name="订单号", max_length=64)
    title = models.CharField(verbose_name="商品名称", max_length=32)
    price = models.DecimalField(verbose_name="价格", max_digits=8, decimal_places=2)

    status_choices = (
        (1, "待支付"),
        (2, "已支付"),
    )
    status = models.SmallIntegerField(verbose_name="状态", choices=status_choices, default=1)
    # admin_id
    admin = models.ForeignKey(verbose_name="创建人", to="Admin", on_delete=models.CASCADE)
    create_time = models.DateTimeField(verbose_name='创建时间', null=True)
    modification_time = models.DateTimeField(verbose_name='最后修改时间', null=True)
    modification_people = models.CharField(verbose_name="修改人", max_length=16, null=True)


class City(models.Model):
    """ 城市 """
    name = models.CharField(verbose_name="名称", max_length=32)
    count = models.IntegerField(verbose_name="人口")

    # 本质上数据库也是CharField，自动保存数据。
    img = models.FileField(verbose_name="Logo", max_length=128, upload_to='city/')
