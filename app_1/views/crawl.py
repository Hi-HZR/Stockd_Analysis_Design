# 爬取雪球用户的评论并且把数据存储到MYSQL的app_1_userinfo数据表
import re
import time

import pandas
import requests
from django.shortcuts import redirect
from openpyxl.reader.excel import load_workbook
from app_1.models import UserInfo


def crawl_file(request):
    last = None
    # 模拟浏览器请求头，字典数据类型
    headers = {
        'cookie': 'cookiesu=551709780632819; device_id=1a1695b4205a2730eb03a1a0c1bbd71a; xq_is_login=1; u=3094906363; '
                  's=br16wjxj42; bid=82de4c8815f512ca2448f432e1f97c93_ltiywjgg; '
                  'xq_a_token=e88842db3485b0fbb41d3c6e4386807d5c5a3e87; xqat=e88842db3485b0fbb41d3c6e4386807d5c5a3e87; '
                  'xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9'
                  '.eyJ1aWQiOjMwOTQ5MDYzNjMsImlzcyI6InVjIiwiZXhwIjoxNzEyODM4MzU1LCJjdG0iOjE3MTAyNDYzNTUyMTIsImNpZCI6ImQ5ZDBuNEFadXAifQ.HdFrwRmpE-gAff387LAGmAsU7u-S-mqLJb09K3pk6thxK1_JkJSnWr-IpKuNw5ilkjEhPQfA0B8Be8uBjCcNEYT-zoBykuDnvwx8eFQRZc6cpGCz9gO4nHe6CIonyvhwqRTPTJDgu0xtBJVoEnqgnhcLa-q7lqnYvrlahSxgrnn1ihaQkKXb8IGy4LhadjT6pUHZaq69WxKsW9skDPG3KknlDnKhG-u76H-UntkIIqgfFJj4mDxao0SxYFP-DuPXBGM9xAGRNdrxQOqsShM0OYmK7QEz7Ck0-0JGfeRTe5TahCPA3p0K0-2kt0RLYLb5dnVR4KHGwWG1YQzdtauvdA; xq_r_token=6dff90b03184ab23dc30734e44fa57919de8bcd2; Hm_lvt_1db88642e346389874251b5a1eded6e3=1709921145,1709952991,1710246356,1710492106; acw_tc=2760826217107506676084278e353f0273dfb6b3999a0959a9e20a4a127da5',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 '
                      'Safari/537.36'
    }
    content_list = []
    # 正则表达式
    obj = re.compile(r'<[^>]+>', re.S)

    for page in range(1, 11):
        if page % 10 == 0:
            time.sleep(5)
        print("正在爬取第", page, "页的内容")
        # 请求网站
        if page == 1:
            url = (
                'https://xueqiu.com/query/v1/symbol/search/status.json?count=10&comment=0&symbol=SH000300&hl=0&source'
                '=all&sort=time&page={page}&q=&type=12')
        else:
            url = (
                'https://xueqiu.com/query/v1/symbol/search/status.json?count=10&comment=0&symbol=SH000300&hl=0&source'
                f'=all&sort=time&page={page}&q=&type=12&last_id={last}')

        # 发生get请求，<Response [200]>表示请求的结果成功
        response = requests.get(url, headers=headers)
        data = response.json()
        # 字典数据使用键值对取值,for循环取值
        try:
            for item in data['list'][1:]:
                # 提取数据，保存到自己的字典当中
                dit = {

                    'uid': item['user']['id'],
                    'name': item['user']['screen_name'],
                    'comment': obj.sub('', item['text']),
                }
                content_list.append(dit)
                last = item['id']
        except UnicodeEncodeError as e:
            # 如果出现UnicodeEncodeError，则不添加到content_list
            print(f"Error encoding string: {e}")

    # 获取的用户数据
    print('success')
    # return redirect('http://127.0.0.1:8000/info')
    return content_list
