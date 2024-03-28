import requests


def spider_list_ver(project):
    # 获取项目下已发布的爬虫版本列表
    url = "http://127.0.0.1:6800/listversions.json?project={}".format(project)
    res = requests.get(url)
    return res.json()
