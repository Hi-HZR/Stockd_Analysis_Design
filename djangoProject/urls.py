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
from django.urls import path
from app_1.views import views, show_chart, emotion, test, crawl, upload

urlpatterns = [
    # views
    path('login/', views.login),
    path('info/', views.info),
    path('delete/', views.delete),
    path('web/', views.web),
    path('<int:uid>/edit/', views.edit),
    path('add/', views.user_model_form_add),
    path('search/', views.search),
    path('emotion/chart', emotion.emotion_chart),
    path('chart/', show_chart.show_chart),
    path('crawl/file', crawl.crawl_file),
    path('upload', upload.upload_file),
]
