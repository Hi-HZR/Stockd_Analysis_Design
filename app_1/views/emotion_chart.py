from django.http import HttpResponse
from django.shortcuts import render
from openpyxl.reader.excel import load_workbook

from app_1.models import UserInfo
from app_1.views.emotion_sdk import emotion_sdk


def emotion_chart(request):
    workbook = load_workbook("D:/PythonProject/djangoProject/xueqiu.xlsx")
    # 选择活动的工作表
    sheet = workbook.active
    total_positive_prob = 0
    total_negative_prob = 0
    comment_count = 0
    for row in sheet.iter_rows(min_row=2):
        my_text = 'row[3].value'
        positive_prob, negative_prob = emotion_sdk(my_text)
        if positive_prob is not None and negative_prob is not None:
            print('正在分析第', comment_count + 1, '条数据，还剩',10*9-comment_count-1,'条数据。')
            total_positive_prob += positive_prob
            total_negative_prob += negative_prob
            comment_count += 1
    # Calculate average only if there are analyzed comments
    if comment_count > 0:
        # average_positive_prob = round(total_positive_prob / comment_count, 3)
        # average_negative_prob = round(total_negative_prob / comment_count, 3)
        average_positive_prob = total_positive_prob / comment_count
        average_negative_prob = total_negative_prob / comment_count
        print("评论积极评平均概率：", average_positive_prob)
        print("评论消极评平均概率：", average_negative_prob)
    else:
        print("No valid sentiment scores found for comments.")

    return render(request, 'emotion_chart.html',
                  {'average_positive_prob': average_positive_prob, 'average_negative_prob': average_negative_prob})
