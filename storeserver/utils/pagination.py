from django.utils.safestring import mark_safe


class Pagination(object):
    def __init__(self, request, queryset, page_size=3, page_param="page", page_show=5, plus=3):
        page = request.GET.get(page_param, "1")
        # 如果不是整数,强制让页码为1
        if page.isdecimal():
            page = int(page)
        else:
            page = 1

        self.page = page
        self.page_size = 3
        self.start = (page - 1) * page_size
        self.end = page * page_size

        # 每页展示的数据行数
        self.page_queryset = queryset[self.start:self.end]

        page_count = queryset.count()
        page_number, remainder = divmod(page_count, page_size)
        if remainder:
            page_number += 1
        self.page_number = page_number  # 总页码数量
        self.page_show = page_show  # 当前页前后展示的页码数量
        self.request = request
        self.plus = plus

    def html(self):
        # 显示页面的数量
        if self.page_number < 2 * self.plus + 1:
            start_page = 1
            end_page = self.page_number + 1
        else:
            # 小于3页以上时的情况
            if self.page <= self.plus:
                start_page = 1
                end_page = 2 * self.plus + 1
            else:
                if (self.page + self.plus) > self.page_number:
                    start_page = self.page_number - 2 * self.plus
                    end_page = self.page_number + 1
                else:
                    start_page = self.page - self.plus
                    end_page = self.page + self.plus + 1

        # 计算页面
        page_list = []

        # 首页
        page_list.append('<li><a class="page-link" href="?page={}">首页</a></li>'.format(1))

        # 上一页
        if self.page >= 1:
            pre = '<li><a class="page-link" href="?page={}">上一页</a></li>'.format(self.page - 1)
        else:
            pre = '<li><a class="page-link" href="?page={}">上一页</a></li>'.format(1)
        page_list.append(pre)

        # 页面
        for i in range(start_page, end_page):
            if i == self.page:
                ele = '<li class="active"><a class="page-link" href="?page={}">{}</a></li>'.format(i, i)
            else:
                ele = '<li><a class="page-link" href="?page={}">{}</a></li>'.format(i, i)
            page_list.append(ele)

        # 下一页
        if self.page < self.page_number:
            pre = '<li><a class="page-link" href="?page={}">下一页</a></li>'.format(self.page + 1)
        else:
            pre = '<li><a class="page-link" href="?page={}">下一页</a></li>'.format(self.page_number)
        page_list.append(pre)
        # 尾页
        page_list.append('<li><a class="page-link" href="?page={}">尾页</a></li>'.format(self.page_number))
        page_string = mark_safe(''.join(page_list))
        return page_string