from django.contrib import admin
from .models import UserInfo

admin.site.site_header = '管理后台'  # 设置header
admin.site.site_title = '管理后台'  # 设置title
admin.site.index_title = '管理后台'


class users_Manager(admin.ModelAdmin):
    list_display = ['uid', 'name', 'comment']


admin.site.register(UserInfo, users_Manager)
