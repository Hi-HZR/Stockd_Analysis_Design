from django.http import HttpResponse
from django.shortcuts import render
from app_1.views.emotion import emotion_text
from app_1.models import UserInfo


def emotion_chart(request):
    queryset = UserInfo.objects.all()
    for item in queryset:
        text = item.comment
        result = emotion_text(text)
        positive_prob = result[0]
        negative_prob = result[1]
        print(positive_prob, negative_prob)
    # return HttpResponse("success")
    #     return render(request, 'emotion_chart.html', {'positive_prob': positive_prob, 'negative_prob': negative_prob})
    # print("积极概率：", positive_prob, "消极概率：", negative_prob)
    # print(positive_prob, negative_prob)