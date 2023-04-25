from django.shortcuts import render, redirect

from app01 import models
from app01.utils import forms
from app01.utils.pagination import Pagination


def pretty_list(request):
    """靓号列表"""
    data_dict = {}
    query = request.GET.get('query', '')
    if query:
        data_dict['mobile__contains'] = query
    queryset = models.PrettyNum.objects.filter(**data_dict).order_by('-level')
    page_object = Pagination(request, queryset)
    context = {
        "query": query,
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # html页码
    }
    return render(request, 'pretty_list.html', context)


def pretty_add(request):
    """添加靓号"""
    if request.method == 'GET':
        form = forms.PrettyModerForm()
        return render(request, 'pretty_add.html', {'form': form})
    form = forms.PrettyModerForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/pretty/list/')
    return render(request, 'pretty_add.html', {'form': form})


def pretty_edit(request, index_id):
    """编辑靓号"""
    row_obj = models.PrettyNum.objects.filter(id=index_id).first()
    if request.method == 'GET':
        form = forms.PrettyModerForm(instance=row_obj)
        return render(request, 'pretty_edit.html', {'form': form})
    form = forms.PrettyModerForm(request.POST, instance=row_obj)
    if form.is_valid():
        form.save()
        return redirect('/pretty/list/')
    return render(request, 'pretty_edit.html', {'form': form})


def pretty_delete(request, index_id):
    """删除靓号"""
    models.PrettyNum.objects.filter(id=index_id).delete()
    return redirect('/pretty/list/')
