from io import BytesIO

from django.shortcuts import render, redirect, HttpResponse

from app01 import models
from app01.utils.code import check_code
from app01.utils.forms import LoginForm


def login(request):
    """ 登录 """
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    form = LoginForm(data=request.POST)
    if form.is_valid():
        user_input_code = form.cleaned_data.pop('code')
        code = request.session.get('code', '')
        if user_input_code.upper() != code.upper():
            form.add_error('code', '验证码错误')
            return render(request, 'login.html', {'form': form})
        row_obj = models.Admin.objects.filter(**form.cleaned_data).first()
        if not row_obj:
            form.add_error('password', '用户名或密码错误')
            return render(request, 'login.html', {'form': form})
        request.session['info'] = {'id': row_obj.id, 'name': row_obj.username}
        request.session.set_expiry(60*60*24)
        return redirect('/admin/list/')
    return render(request, 'login.html', {'form': form})


def image_code(request):
    """ 图片验证码 """
    img, code_string = check_code()
    request.session['code'] = code_string
    request.session.set_expiry(60)
    stream = BytesIO()
    img.save(stream, 'png')
    return HttpResponse(stream.getvalue())


def logout(request):
    """ 注销 """
    request.session.clear()
    return redirect('/login/')
