from django.shortcuts import render, redirect

from app01 import models
from app01.utils import forms
from app01.utils.pagination import Pagination


def user_list(request):
    data_dict = {}
    query = request.GET.get('query', '')
    if query:
        data_dict['name__contains'] = query
    user_info = models.UserInfo.objects.filter(**data_dict)
    page_obj = Pagination(request, user_info, page_size=5)
    context = {
        "query": query,
        'user_info': page_obj.page_queryset,
        'page_string': page_obj.html()
    }
    return render(request, 'user_list.html', context)


# def user_add(request):
#     gender = {
#         'gender_choices': models.UserInfo.gender_choices,
#         'department_list': models.Department.objects.all()
#     }
#     return render(request, 'user_add.html', gender)


def user_model_form_add(request):
    if request.method == 'GET':
        form = forms.UserModerForm
        return render(request, 'user_model_form_add.html', {'form': form})
    form = forms.UserModerForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/user/list/')
    return render(request, 'user_model_form_add.html', {'form': form})


def user_edit(request, index_id):
    row_obj = models.UserInfo.objects.filter(id=index_id).first()
    if request.method == 'GET':
        form = forms.UserModerForm(instance=row_obj)
        return render(request, 'user_edit.html', {'form': form})
    form = forms.UserModerForm(data=request.POST, instance=row_obj)
    if form.is_valid():
        form.save()
        return redirect('/user/list/')
    return render(request, 'user_edit.html', {'form': form})


def user_delete(request, index_id):
    models.UserInfo.objects.filter(id=index_id).delete()
    return redirect('/user/list/')
