from django.http import HttpResponse

from app_1.models import UserInfo


def index(request):
    queryset = UserInfo.objects.all()
    for item in queryset:
        print(item.id, item.name, item.comment)
        return HttpResponse("success")
