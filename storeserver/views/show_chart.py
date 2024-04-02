from django.http import JsonResponse
from django.shortcuts import render


def show_chart(request):
    return render(request, "chart.html")


def chart_pie(request):
    data_list: [
        {"value": 1048, "name": '增加'},
        {"value": 735, "name": '删除'},
        {"value": 580, "name": '修改'},
        {"value": 484, "name": '情绪分析'},
        {"value": 484, "name": '其它'},
    ]
    result = {
        "status": True,
        "data": data_list
    }
    return JsonResponse(result)
