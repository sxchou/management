"""usermanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.urls import path, re_path
from django.views.static import serve
from django.contrib import admin

from app01.views import department, users, pretty, account, order, echarts, city,admin

urlpatterns = [
    # path('admin/', admin.site.urls),

    # 基于modelform上传文件的配置（还需在setting中加入以下两句）
    # MEDIA_ROOT = os.path.join(BASE_DIR, "media")
    # MEDIA_URL = "/media/"
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),


    # 部门管理
    path('department/list/', department.department_list),
    path('department/add/', department.department_add),
    path('department/<int:index_id>/delete/', department.department_delete),
    path('department/<int:index_id>/edit/', department.department_edit),
    path('depart/multi/', department.department_multi),

    # 用户管理
    path('user/list/', users.user_list),
    # path('user/add/', users.user_add),
    path('user/model/form/add/', users.user_model_form_add),
    path('user/<int:index_id>/edit/', users.user_edit),
    path('user/<int:index_id>/delete/', users.user_delete),

    # 靓号管理
    path('pretty/list/', pretty.pretty_list),
    path('pretty/add/', pretty.pretty_add),
    path('pretty/<int:index_id>/edit/', pretty.pretty_edit),
    path('pretty/<int:index_id>/delete/', pretty.pretty_delete),

    # 管理员
    path('admin/list/', admin.admin_list),
    path('admin/add/', admin.admin_add),
    path('admin/<int:index_id>/edit/', admin.admin_edit),
    path('admin/<int:index_id>/delete/', admin.admin_delete),
    path('admin/<int:index_id>/reset/', admin.admin_reset),

    # 登录和注销
    path('login/', account.login),
    path('image/code/', account.image_code),
    path('logout/', account.logout),

    # 订单管理
    path('order/list/', order.order_list),
    path('order/add/', order.order_add),
    path('order/delete/', order.order_delete),
    path('order/edit/', order.order_edit),
    path('order/edit/save/', order.edit_save),

    # 数据可视化图表
    path('echarts/list/', echarts.echarts_list),
    path('echarts/bar/', echarts.echarts_bar),
    path('echarts/pie/', echarts.echarts_pie),

    # 图片上传
    path('city/list/', city.city_list),
    path('city/add/', city.city_add),
]
