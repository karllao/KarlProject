from django import forms
from django.forms import widgets
from django.core.exceptions import ValidationError
from ShuaBu import models

class ShuabuForm(forms.Form):
    # number = forms.CharField(min_length=11, max_length=11, label="手机号", error_messages={"min_length": "号码过短", "max_length": "号码过长", "required": "号码不能为空!"})
    # password = forms.PasswordInput(render_value=True, label="密码", error_messages={"required": "密码不能为空!"})
    # step = forms.DecimalField(max_value=5000, label="步数", error_messages={"required": "步数不能为空!"})
    number = forms.CharField(label='账号',
                           # 自定义错误信息
                           error_messages={
                               'required': '账号输入不能为空!',
                           },
                           # 添加一个form-control类
                           widget=widgets.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='密码',
                               error_messages={
                                   'required': '密码不能为空!',
                               },
                               widget=widgets.PasswordInput(attrs={'class':'form-control'}))
    step = forms.CharField(max_length=5, min_length=3, label='步数',
                           # 自定义错误信息
                           error_messages={
                               'min_length': '步数最少3位!',
                               'max_length': '步数最大5位',
                               'required': '步数不能为空!',
                           },
                           # 添加一个form-control类
                           widget=widgets.TextInput(attrs={'class':'form-control'}))