from django.shortcuts import render, redirect

from app01 import models
from app01.utils.forms import AdminModerForm
from app01.utils.pagination import Pagination


def admin_list(request):
    data_dict = {}
    query = request.GET.get('query', '')
    if query:
        data_dict['username__contains'] = query
    queryset = models.Admin.objects.filter(**data_dict)
    page_obj = Pagination(request, queryset)
    context = {
        'query': query,
        'queryset': page_obj.page_queryset,
        'page_string': page_obj.html(),
    }
    return render(request, 'admin_list.html', context)


def admin_add(request):
    title = '新建管理员'
    if request.method == 'GET':
        form = AdminModerForm()
        return render(request, 'change.html', {"title": title, 'form': form})
    form = AdminModerForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')
    return render(request, 'change.html', {"title": title, 'form': form})


def admin_edit(request, index_id):
    """编辑管理员"""
    title = '编辑管理员'
    row_obj = models.Admin.objects.filter(id=index_id).first()
    if not row_obj:
        return render(request, 'error.html', {'msg': '数据不存在或已被删除!!!'})
    if request.method == 'GET':
        form = AdminModerForm(instance=row_obj)
        return render(request, 'change.html', {'form': form, 'title': title})
    form = AdminModerForm(request.POST, instance=row_obj)
    if form.is_valid():
        form.save()
        return redirect('/admin/list')
    return render(request, 'change.html', {'form': form, 'title': title})


def admin_delete(request, index_id):
    models.Admin.objects.filter(id=index_id).delete()
    return redirect("/admin/list/")


def admin_reset(request, index_id):
    row_obj = models.Admin.objects.filter(id=index_id).first()
    if not row_obj:
        return render(request, 'error.html', {'msg': '数据不存在或已被删除!!!'})
    title = f'重置密码-{row_obj.username}'
    if request.method == 'GET':
        form = AdminModerForm(instance=row_obj)
        return render(request, 'change.html', {'title': title, 'form': form})
    form = AdminModerForm(data=request.POST, instance=row_obj)
    if form.is_valid():
        form.save()
        return redirect("/admin/list/")
    return render(request, 'change.html', {'title': title, 'form': form})
