# 爬取雪球用户的评论并且把数据存储到MYSQL的app_1_userinfo数据表
import datetime
import time

import pandas
import requests
from django.shortcuts import render
from requests import request


def crawl_price(request):
    # 模拟浏览器请求头，字典数据类型
    headers = {
        'cookie': 'cookiesu=551709780632819; device_id=1a1695b4205a2730eb03a1a0c1bbd71a; s=br16wjxj42; bid=82de4c8815f512ca2448f432e1f97c93_ltiywjgg; Hm_lvt_1db88642e346389874251b5a1eded6e3=1711365027,1711444827,1711464274,1711615693; Hm_lvt_d67baafd318097a18e70ee8d8d1de57a=1711443502,1711464275,1711615694; xq_a_token=2d49585dadb6162d8f06bae1922afeb618f52c58; xqat=2d49585dadb6162d8f06bae1922afeb618f52c58; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjMwOTQ5MDYzNjMsImlzcyI6InVjIiwiZXhwIjoxNzE0MjA3NjkwLCJjdG0iOjE3MTE2MTU3MTc3NDcsImNpZCI6ImQ5ZDBuNEFadXAifQ.jct-3tRtUrd08An3VYa5ouCetBAekk8PZfuS2Ux0rPV2sJFKn5R0ZFSW65UlzoZld2cQk7kJu2euOp7xRxfaInJVOMnCkp8OgD5f7RJVmsOfsME3c4FcMh0nRycZg3fHgTo5whaL-zSfkciDeHrgkTDhxQmZnJvp-A_gEEZaGckB4biI8Zr_tYhscvJ4Czlb7fiJMJHr04QESIoXWwInCx5CyQI8yh5vpEdEt2s89BfmmNfTTQGcShAHdA4ObmsDsHqq-G2tR9hAqKsxKlxHTQyvJ0i0Go_tMLqeKGgM7WraN926etd58v7l0I18qIPuhlbFxfZJ-XndbqVdSOs3iQ; xq_r_token=08169bc3db0aa0fb416748e282d90f766d8e7925; xq_is_login=1; u=3094906363; snbim_minify=true; is_overseas=0; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1711618942; Hm_lpvt_d67baafd318097a18e70ee8d8d1de57a=1711618943',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
    }
    content_list_point = []
    # 2004-12-31 00:00:00开始
    # 请求网站
    url = 'https://stock.xueqiu.com/v5/stock/chart/kline.json?symbol=SH000300&begin=1104422400000&end=1712086063880&period=day&type=before&indicator=kline'

    # 发生get请求，<Response [200]>表示请求的结果成功
    response = requests.get(url, headers=headers)
    # print(response)
    data = response.json()
    # 字典数据使用键值对取值,for循环取值
    # try:
    for item in data['data']['item']:
        # 将13位时间戳转换为秒级时间戳
        timestamp = item[0] / 1000

        # 将时间戳转换为datetime对象
        dt = datetime.datetime.fromtimestamp(timestamp)

        # 将datetime对象转换为指定格式的字符串
        formatted_date = dt.strftime('%Y-%m-%d')

        # 提取数据，保存到自己的字典当中
        dit = {

            'point': item[5],
            'time': formatted_date,

        }
        content_list_point.append(dit)
    # except UnicodeEncodeError as e:
    #     # 如果出现UnicodeEncodeError，则不添加到content_list
    #     print(f"Error encoding string: {e}")

    # 获取的用户数据
    d = pandas.DataFrame(content_list_point)
    d.to_excel('point.xlsx')

    print('成功获取股市价格')
    return content_list_point
