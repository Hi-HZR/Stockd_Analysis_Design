import requests
import json
from django.http import HttpResponse
from django.shortcuts import render
from app_1.models import UserInfo


def emotion_text(string):
    # data参数
    content = json.dumps({"text": string})

    # headers参数
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    # 获取access_token后，完成URL拼接，获得URL参数
    host = (f"https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=MhsCMaKfJX9JyopuyviPbiK5"
            f"&client_secret=RGKHayxmxEfKAN2tqhrZsiCmoBLEQUs3")
    response = requests.get(host)
    my_token = response.json()['access_token']
    my_url = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify' + '?charset=UTF-8&access_token=' + my_token

    # request请求接口，通过for循环得到结果
    results = requests.post(url=my_url,
                            headers=headers,
                            data=content).json()

    # 获取数组结果
    # [{'confidence': 0.940806, 'negative_prob': 0.0266372, 'positive_prob': 0.973363, 'sentiment': 2}]
    value = results.get("items")

    # 输出value的第一组元素，再在第一组元素中输出关键字为positive_prob，negative_prob的元素
    # if value:
    positive_prob = value[0]["positive_prob"]
    negative_prob = value[0]["negative_prob"]
    return positive_prob, negative_prob
    # else:
    #     print("No sentiment analysis results found.")
    #     return None, None


def emotion_chart(request):
    queryset = UserInfo.objects.all()
    total_positive_prob = 0
    total_negative_prob = 0
    comment_count = 0

    for item in queryset:
        text = item.comment
        positive_prob, negative_prob = emotion_text(text)

        # Check if both probabilities are valid before adding
        if positive_prob is not None and negative_prob is not None:
            total_positive_prob += positive_prob
            total_negative_prob += negative_prob
            comment_count += 1

    # Calculate average only if there are analyzed comments
    if comment_count > 0:
        average_positive_prob = total_positive_prob / comment_count
        average_negative_prob = total_negative_prob / comment_count
        print("Average positive probability:", average_positive_prob)
        print("Average negative probability:", average_negative_prob)
    else:
        print("No valid sentiment scores found for comments.")

    # Rest of your function logic (e.g., rendering template)
    return render(request, 'emotion_chart.html',
                  {'average_positive_prob': average_positive_prob, 'average_negative_prob': average_negative_prob})
