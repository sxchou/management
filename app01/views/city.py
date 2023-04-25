from django.shortcuts import render, redirect

from app01 import models
from app01.utils.forms import CityModerForm


def city_list(request):
    queryset = models.City.objects.all()
    return render(request, 'city_list.html', {'queryset': queryset})


def city_add(request):
    title = '新建城市'
    if request.method == 'GET':
        form = CityModerForm()
        return render(request, 'city_add.html', {'form': form, 'title': title})
    form = CityModerForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        form.save()
        return redirect('/city/list/')
    return render(request, 'city_add.html', {'form': form, 'title': title})
