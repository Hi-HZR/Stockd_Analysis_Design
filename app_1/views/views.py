from django import forms
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from app_1.models import UserInfo
from app_1.utils.pagination import Pagination
from django.utils.safestring import mark_safe
import requests
import re
import json
import csv
import time
import datetime


# Create your views here.
def web(request):
    return render(request, "web.html")


class LoginForm(forms.Form):
    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput,
        required=True
    )
    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput,
        required=True
    )


def login(request):
    if request.method == "GET":
        fm = LoginForm()
        return render(request, "login.html", {"form": fm})
    else:
        fm = LoginForm(data=request.POST)
        if fm.is_valid():
            print(fm.cleaned_data)
            return HttpResponse("成功")
        else:
            return render(request, "login.html", {"form": fm})


def info(request):
    queryset = UserInfo.objects.all().order_by("id")

    page_object = Pagination(request, queryset)
    context = {
        "queryset": page_object.page_queryset,  # 分页的数据
        "page_string": page_object.html(),  # 页码
    }

    return render(request, "info.html", context)


def delete(request):
    # 删除数据
    uid = request.GET.get("nid")
    UserInfo.objects.filter(id=uid).delete()
    return redirect("http://127.0.0.1:8000/info/")


class UserModelForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ["name", "comment", "uid"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "comment": forms.TextInput(attrs={"class": "form-control"}),
            "uid": forms.TextInput(attrs={"class": "form-control"})
        }


def user_model_form_add(request):
    if request.method == "GET":
        fm = UserModelForm()  # 实例化MyForm这个类，对象为fm
        return render(request, "add.html", {"form": fm})
    else:
        fm = UserModelForm(data=request.POST)
        if fm.is_valid():
            fm.save()
            return redirect("http://127.0.0.1:8000/info/")
        else:
            print(fm.errors)


def edit(request, uid):
    row_object = UserInfo.objects.filter(id=uid).first()
    if request.method == "GET":
        fm = UserModelForm(instance=row_object)
        return render(request, "edit.html", {"form": fm})
        print(row_object.id, row_object.name, row_object.comment)
    else:
        fm = UserModelForm(data=request.POST, instance=row_object)
        if fm.is_valid():
            fm.save()
            return redirect("http://127.0.0.1:8000/info/")
        else:
            return render(request, "edit.html", {"form": fm})


def search(request):
    search_info = request.GET.get('search_info')
    if not search_info:
        return HttpResponse("错误")
    else:
        msg = UserInfo.objects.filter(
            Q(name__icontains=search_info) | Q(uid__icontains=search_info) | Q(uid__icontains=search_info))
        return render(request, 'result.html', {'msg': msg})


def function(request):
    return render(request, 'show_function.html')


def test(request):
    text = UserInfo.objects.filter(id="2")
    print(text)
