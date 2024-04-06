"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.views.generic import TemplateView

from storeserver.views import (views, info, show_chart, crawl_comment, upload, emotion_chart, emotion_sdk, lstm,
                               crawl_price, trans, summary, test, snownlp, analyze_sentiment)
from django.contrib import admin

urlpatterns = [
    # 测试路由
    path('test/', test.test),

    # 服务端路由
    path('admin/', admin.site.urls),

    # 前端爬取数据系列路由
    path('crawl/comment/', crawl_comment.crawl_comment),
    path('crawl/price/', crawl_price.crawl_price),
    path('upload/', upload.upload_file),
    path('upload/all/', upload.upload_all),

    # 前端展示信息相关路由
    path('info/', info.info),
    path('delete/', views.delete),
    path('web/', views.web),
    path('<int:uid>/edit/', views.edit),
    path('add/', views.user_model_form_add),
    path('search/', views.search),
    path('chart/', show_chart.show_chart),

    # nlp分析
    path('snownlp/', snownlp.snownlp),
    path('analyze_sentiment/', analyze_sentiment.analyze_sentiment),

    # 前端显示情绪分析图表相关路由
    path('emotion/chart/', emotion_chart.emotion_chart),
    path('emotion/sdk/', emotion_sdk.emotion_sdk),

    # 前端LSTM相关路由
    path('lstm/', lstm.lstm),
    path('trans/', trans.tran),

    # 前端分析总结相关路由
    path('summary/', summary.summary),

    # # vue路由
    # path(r'^admin/', admin.site.urls),
    # path(r'^$', TemplateView.as_view(template_name="index.html")),
    # path(r'^api/', include('storeweb.urls', namespace='api')),
]
