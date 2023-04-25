import re

from django import forms
from django.core.exceptions import ValidationError

from app01 import models
from app01.utils.bootstrap import BootstrapModerForm, BootstrapForm
from app01.utils.encrypt import md5


class UserModerForm(BootstrapModerForm):
    name = forms.CharField(min_length=2, label='姓名')
    password = forms.CharField(min_length=10, label='密码')

    class Meta:
        model = models.UserInfo
        fields = "__all__"
        # fields = ['name', 'password', 'age', 'create_date', 'account', 'gender', 'depart']
        # widgets = {
        #     'password': forms.TextInput(attrs={'class': 'form-control'})
        # }  # 单独添加部件


class PrettyModerForm(BootstrapModerForm):
    """
    mobile = forms.CharField(
        label='手机号',
        validators=[RegexValidator(r'^1[3-9]\\d{9}$', '手机号格式错误')]
    )
    mobile = forms.CharField(disabled=True)  # 设置字段不允许修改
    """

    class Meta:
        model = models.PrettyNum
        # fields = ['id', 'mobile', 'price', 'level', 'status'] # 添加要显示的字段
        # exclude = ['mobile']  # 排除不显示的字段
        fields = '__all__'  # 显示所有字段

    def clean_mobile(self):
        # self.instance.pk 获取主键id
        mobile_text = self.cleaned_data['mobile']
        pattern = re.compile('^1[3-9]\\d{9}$')
        if pattern.match(mobile_text):
            return mobile_text  # 返回什么,数据库就保存此字段是什么
        raise ValidationError('请输入合法的手机号')


class AdminModerForm(BootstrapModerForm):
    confirm_password = forms.CharField(
        label='确认密码',
        widget=forms.PasswordInput(render_value=True)
    )

    class Meta:
        model = models.Admin
        fields = ['username', 'password', 'confirm_password']
        widgets = {
            'password': forms.PasswordInput(render_value=True)
        }

    def clean_password(self):
        password = self.cleaned_data['password']
        return md5(password)

    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = md5(self.cleaned_data['confirm_password'])
        if password != confirm_password:
            raise ValidationError('密码不一致,请重新输入')
        return confirm_password  # 返回什么,数据库就保存此字段是什么


class LoginForm(BootstrapForm):
    username = forms.CharField(
        label='用户名',
        widget=forms.TextInput
    )
    password = forms.CharField(
        label='密码',
        widget=forms.PasswordInput(render_value=True)
    )
    code = forms.CharField(
        label='验证码',
        widget=forms.TextInput
    )

    def clean_password(self):
        password = self.cleaned_data['password']
        return md5(password)


class OrderModerForm(BootstrapModerForm):
    oid = forms.CharField(
        label='订单号',
        disabled=True,
        empty_value='占位',
        widget=forms.TextInput(
            attrs={'placeholder': '订单号自动生成'})
    )

    class Meta:
        model = models.Order
        exclude = ['admin', 'create_time', 'modification_time', 'modification_people']


class CityModerForm(BootstrapModerForm):
    bootstrap_exclude_fields = ['img']

    class Meta:
        model = models.City
        fields = "__all__"
