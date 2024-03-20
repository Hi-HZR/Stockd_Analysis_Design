from django.shortcuts import render


def show_function(request):
    return render(request, "show_function.html")
