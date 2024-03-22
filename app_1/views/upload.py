import pandas
from django.shortcuts import redirect
from openpyxl.reader.excel import load_workbook
from app_1.models import UserInfo
from app_1.views.crawl import crawl_file


def upload_file(request):
    result = crawl_file(request)
    d = pandas.DataFrame(result)
    d.to_excel('xueqiu.xlsx')
    # 上传excel文件,并获取
    file_object = request.FILES.get("excel")
    print(type(file_object))

    # 通过openpyxl打开文件
    exc = load_workbook("D:/PythonProject/djangoProject/xueqiu.xlsx")
    sheet = exc.worksheets[0]
    my_id = 0
    # 循环输入数据
    for row in sheet.iter_rows(min_row=2):
        text_uid = row[1].value
        text_name = row[2].value
        text_comment = row[3].value
        my_id += 1
        try:
            UserInfo.objects.create(id=my_id, name=text_name, uid=text_uid, comment=text_comment)
        except UnicodeEncodeError as e:
            # 如果出现UnicodeEncodeError，则不添加到content_list
            print(f"Error encoding string: {e}")

    return redirect('http://127.0.0.1:8000/info')
