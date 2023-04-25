import random
from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from app01.models import Order
from app01.utils.forms import OrderModerForm
from app01.utils.pagination import Pagination


def order_list(request):
    """订单列表 js模态框"""
    queryset = Order.objects.all().order_by("-id")
    form = OrderModerForm()
    page_object = Pagination(request, queryset)
    context = {
        "form": form,
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成页码
    }
    return render(request, 'order_list.html', context)


@csrf_exempt
def order_add(request):
    """新建订单 ajax请求"""
    form = OrderModerForm(data=request.POST)
    if form.is_valid():
        form.instance.admin_id = request.session['info']['id']
        form.instance.oid = datetime.now().strftime('%Y%m%d%H%M%S') + str(random.randint(1000, 9999))
        form.instance.create_time = datetime.now()
        form.save()

        return JsonResponse({'status': True})
    return JsonResponse({'status': False, 'errors': form.errors})


def order_delete(request):
    """ 删除订单 """
    uid = request.GET.get('uid')
    exists = Order.objects.filter(id=uid).exists()
    if exists:
        Order.objects.filter(id=uid).delete()
        return JsonResponse({'status': True})
    return JsonResponse({'status': False, 'error': '数据不存在或已被删除,请刷新后重试'})


def order_edit(request):
    e_id = request.GET.get('e_id')
    row_dict = Order.objects.filter(id=e_id).values('oid', 'title', 'price', 'status').first()
    if not row_dict:
        return JsonResponse({'status': False, 'error': '数据不存在或已被删除,请刷新后重试'})
    return JsonResponse({'status': True, "data": row_dict})


@csrf_exempt
def edit_save(request):
    edit_id = request.GET.get('edit_id')
    row_obj = Order.objects.filter(id=edit_id).first()
    if row_obj:
        form = OrderModerForm(data=request.POST, instance=row_obj)
        form.instance.modification_time = datetime.now()
        form.instance.modification_people = request.session['info']['name']
        if form.is_valid():
            form.save()
            return JsonResponse({'status': True})
        return JsonResponse({'status': False, 'errors': form.errors})
    return JsonResponse({'status': False, 'tips': '数据不存在或已被删除,请刷新后重试'})
