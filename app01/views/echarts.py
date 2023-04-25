from django.http import JsonResponse
from django.shortcuts import render


def echarts_list(request):
    return render(request, 'echarts_list.html')


def echarts_bar(request):
    legend_data = ['周世旭', '杨开林']
    x_axis_data = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']
    series_data = [
        {
            'name': '周世旭',
            'type': 'bar',
            'data': [5, 20, 49, 10, 10, 20, 5, 20, 36, 10, 10, 20]
        },
        {
            'name': '杨开林',
            'type': 'bar',
            'data': [15, 28, 36, 5, 18, 26, 12, 33, 24, 20, 45, 25]
        }
    ]
    result = {
        'legend_data': legend_data,
        'x_axis_data': x_axis_data,
        'series_data': series_data,
    }
    return JsonResponse({'status': True, 'data': result})


def echarts_pie(request):
    series_data = [
        {'value': 40, 'name': 'it部门'},
        {'value': 38, 'name': '运维部'},
        {'value': 32, 'name': '新媒体'},
        {'value': 30, 'name': '财务部'},
        {'value': 28, 'name': '仓储部'},
        {'value': 26, 'name': '人力资源'},
        {'value': 22, 'name': '生产部'},
        {'value': 18, 'name': '安全部'}
    ]
    result = {
        'status': True,
        'data': series_data,
    }
    return JsonResponse(result)

