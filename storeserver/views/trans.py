import os

from html2image import Html2Image
from django.http import HttpResponse


def tran(request):
    static_path = os.path.join('storeserver', 'static', 'images')
    hti = Html2Image(output_path=static_path, size=(1000, 440))
    hti.screenshot(other_file=os.path.join('png_origin.html'), save_as='origin.png')
    hti.screenshot(other_file=os.path.join('png_train.html'), save_as='train.png')
    hti.screenshot(other_file=os.path.join('png_test.html'), save_as='test.png')
    print('成功转换')
    return HttpResponse('成功转换')
